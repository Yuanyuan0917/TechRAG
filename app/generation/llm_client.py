"""Small OpenAI-compatible language model client for TechRAG."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Sequence

from dotenv import load_dotenv

from app.config import GENERATION_TEMPERATURE, LLM_BASE_URL, LLM_MODEL

_TRAILING_SPECIAL_TOKENS = (
    "<|im_end|>",
    "<|endoftext|>",
    "<|end_of_text|>",
)


class LLMConfigurationError(ValueError):
    """Raised when required LLM configuration is missing."""


class LLMRequestError(RuntimeError):
    """Raised when an LLM request fails or returns an invalid response."""


def remove_trailing_special_tokens(text: str) -> str:
    """Remove only recognized model control tokens at the end of a response."""
    cleaned = text.rstrip()
    while True:
        for token in _TRAILING_SPECIAL_TOKENS:
            if cleaned.endswith(token):
                cleaned = cleaned[: -len(token)].rstrip()
                break
        else:
            return cleaned


class OpenAICompatibleLLMClient:
    """Generate text through an OpenAI-compatible chat completions endpoint."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        temperature: float = GENERATION_TEMPERATURE,
        timeout: float = 60.0,
    ) -> None:
        load_dotenv()
        self.api_key = api_key or os.getenv("LLM_API_KEY", "")
        self.base_url = (base_url or os.getenv("LLM_BASE_URL") or LLM_BASE_URL).rstrip(
            "/"
        )
        self.model = model or os.getenv("LLM_MODEL") or LLM_MODEL
        self.temperature = temperature
        self.timeout = timeout
        if not self.api_key:
            raise LLMConfigurationError(
                "LLM_API_KEY is required for answer generation; configure it in the "
                "environment or a local .env file"
            )
        if not self.base_url:
            raise LLMConfigurationError("LLM_BASE_URL must not be empty")
        if not self.model:
            raise LLMConfigurationError("LLM_MODEL must not be empty")

    def generate(self, messages: Sequence[dict[str, str]]) -> str:
        """Return generated text for chat-style messages."""
        if not messages:
            raise ValueError("messages must not be empty")
        payload = json.dumps(
            {
                "model": self.model,
                "messages": list(messages),
                "temperature": self.temperature,
            }
        ).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            raise LLMRequestError(
                f"LLM request failed with HTTP status {error.code}"
            ) from error
        except urllib.error.URLError as error:
            raise LLMRequestError(f"LLM request failed: {error.reason}") from error
        except TimeoutError as error:
            raise LLMRequestError("LLM request timed out") from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise LLMRequestError("LLM response was not valid JSON") from error

        try:
            content = response_data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as error:
            raise LLMRequestError("LLM response did not contain generated text") from error
        if not isinstance(content, str):
            raise LLMRequestError("LLM response contained empty generated text")
        content = remove_trailing_special_tokens(content)
        if not content:
            raise LLMRequestError("LLM response contained empty generated text")
        return content.strip()
