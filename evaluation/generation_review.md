# Generation Evaluation Review

Scores use the manually reviewed 0–2 rubric. Context excerpts are truncated; raw JSON preserves full text.

# q001

## Question

What does dependency injection mean in FastAPI?

## Reference Answer

A path operation declares what it needs, and FastAPI provides or injects those dependencies, enabling shared logic, database connections, and security requirements with less repetition.

---

## Dense

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …

### Answer

Dependency injection in FastAPI means that your code (such as *path operation functions*) can declare dependencies that it requires to work, and **FastAPI** will take care of providing those dependencies ("injecting" them) [C2]. This system allows for shared logic, database connections, security enforcement, and more to be integrated seamlessly with your API functions [C2].

### Citations

[C2] -> `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Matches the dependency-injection reference and cites the defining chunk.

---

## Hybrid

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …

### Answer

Dependency injection in FastAPI means that your code (such as *path operation functions*) can declare dependencies that it requires to work, and **FastAPI** will take care of providing those dependencies ("injecting" them) [C2]. This system allows for shared logic, database connections, security enforcement, and more to be integrated seamlessly with your API functions [C2].

### Citations

[C2] -> `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Matches the reference with direct support from C2.

---

## Reranked

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…

### Answer

Dependency injection in FastAPI means that your code (such as path operation functions) can declare dependencies that it requires to work, and FastAPI will handle providing those dependencies ("injecting" them) [C1]. This system allows for shared logic, database connections, security enforcement, and more to be managed efficiently by FastAPI [C1].

### Citations

[C1] -> `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete definition with the strongest relevant chunk ranked first.

# q002

## Question

How does FastAPI know what to do with a callable passed to Depends?

## Reference Answer

The developer passes the callable to Depends; FastAPI analyzes its parameters like a path operation function and calls it with the required values for each request, without separate registration.

---

## Dense

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…

### Answer

FastAPI knows what to do with a callable passed to `Depends` because it is designed to handle dependency injection. When a callable is passed to `Depends`, FastAPI takes care of calling the dependency function with the correct parameters, extracting the data from the request, and assigning the result to the parameter in the path operation function [C1]. This process is automated and does not require the user to create a special class or register the dependency explicitly [C1]. Additionally, FastAPI uses the `Depends` function to manage the dependency injection, allowing the framework to handle the execution of the dependency and inject the results into the path operation function [C3].

### Citations

[C1] -> `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`, [C3] -> `chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Explains automatic callable analysis, execution, and injection with supporting chunks.

---

## Hybrid

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_3f6fa1c6c1b1b4938ca0df20bef98d40da07ecc1367c188f6a4a1726eef6bb43` — cial class and pass it somewhere to **FastAPI** to "register" it or anything similar. You just pass it to `Depends` and **FastAPI** knows how to do the rest. /// ## Share `Annotated` dependencies { #share-annotated-dependencies } In the examples above, you see that there's a tiny bit of **code duplication**. When you need to use the `common_parameters()` dependency, you have to write the whole parameter with the type annotation and `Depends()`: ```Python commons: Annotated[dict, Depends(common_…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…

### Answer

FastAPI knows what to do with a callable passed to `Depends` because it is designed to handle such dependencies automatically. When a callable is passed to `Depends`, FastAPI takes care of calling the dependency function with the correct parameters, getting the result, and assigning that result to the parameter in the path operation function [C1]. This process is seamless and does not require any special registration or setup, as FastAPI inherently understands how to manage dependencies through the `Depends` function [C4].

### Citations

[C1] -> `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`, [C4] -> `chunk_3f6fa1c6c1b1b4938ca0df20bef98d40da07ecc1367c188f6a4a1726eef6bb43`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Captures execution and no-registration behavior with direct citations.

---

## Reranked

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_3f6fa1c6c1b1b4938ca0df20bef98d40da07ecc1367c188f6a4a1726eef6bb43` — cial class and pass it somewhere to **FastAPI** to "register" it or anything similar. You just pass it to `Depends` and **FastAPI** knows how to do the rest. /// ## Share `Annotated` dependencies { #share-annotated-dependencies } In the examples above, you see that there's a tiny bit of **code duplication**. When you need to use the `common_parameters()` dependency, you have to write the whole parameter with the type annotation and `Depends()`: ```Python commons: Annotated[dict, Depends(common_…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…

### Answer

FastAPI knows what to do with a callable passed to `Depends` because it is designed to handle dependencies through its **Dependency Injection** system [C1]. When you pass a callable to `Depends`, FastAPI takes care of calling the dependency function with the correct parameters, extracting the data from the request, and assigning the result to the parameter in your *path operation function* [C4]. This process is automated and seamless, allowing you to focus on writing your application logic without manually managing the dependency lifecycle.

### Citations

[C1] -> `chunk_3f6fa1c6c1b1b4938ca0df20bef98d40da07ecc1367c188f6a4a1726eef6bb43`, [C4] -> `chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 1
- Requires human review: False

### Notes

Core answer is supported, but the final dependency-lifecycle statement is uncited.

# q003

## Question

How are dependency requirements represented in FastAPI's generated API documentation?

## Reference Answer

Parameters, validations, and requirements declared by dependencies and sub-dependencies are added to the OpenAPI schema and shown in the interactive documentation.

---

## Dense

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_fee15b5d598f2287c67e16d13e6154cd0cbfdd3bb62221de78c4c917fea951b6` — ot specific to **FastAPI**. But because **FastAPI** is based on the Python standards, including `Annotated`, you can use this trick in your code. 😎 /// The dependencies will keep working as expected, and the **best part** is that the **type information will be preserved**, which means that your editor will be able to keep providing you with **autocompletion**, **inline errors**, etc. The same for other tools like `mypy`. This will be especially useful when you use it in a **large code base** wh…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrectly abstains; the exact OpenAPI chunk is absent from Dense top-5.

---

## Hybrid

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrectly abstains because Hybrid top-5 does not expose the needed OpenAPI passage.

---

## Reranked

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_9db97dc956598985fc2d6d5b05fff372b8447de5f695a1c1d28785be304f0559` — tems/public/` * `/items/private/` * `/users/{user_id}/activate` * `/items/pro/` then you could add different permission requirements for each of them just with dependencies and sub-dependencies: ```mermaid graph TB current_user(["current_user"]) active_user(["active_user"]) admin_user(["admin_user"]) paying_user(["paying_user"]) public["/items/public/"] private["/items/private/"] activate_user["/users/{user_id}/activate"] pro_items["/items/pro/"] current_user --> active_user active_user --> adm…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…

### Answer

Dependency requirements in FastAPI's generated API documentation are represented through the integration with **OpenAPI**. Specifically, all the request declarations, validations, and requirements of your dependencies (and sub-dependencies) are integrated into the same OpenAPI schema. This means that the interactive documentation systems will have all the information from these dependencies, including parameters and validations, as described in the documentation [C5].

### Citations

[C5] -> `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Reranking surfaces the exact OpenAPI passage and the answer matches the reference.

# q004

## Question

How can a Transformers Pipeline be assigned to CPU, GPU, or Apple Silicon?

## Reference Answer

Configure the Pipeline device, using the supported device identifier or an Accelerate device map so model weights are placed on suitable hardware.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653` — cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then moves the weights to other devices (CPU, hard drive) as needed. Set `device_map="auto"` to let Accelerate choose the device. > [!TIP] > Make sure have [Accelerate](https://hf.co/docs/accelerate/basic_tutorials/install) is installed. > > ```py > !pip install -U accelerate > ``` `…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45` — is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma 2](./model_doc/gemma2), set `task="text-generation"` and `model="google/gemma-2-2b"`. ```py from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b") pipeline("the secret to baking a really good cake is ") [{'generated_text': 'the …
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…

### Answer

A Transformers Pipeline can be assigned to CPU, GPU, or Apple Silicon by using the `device` parameter. For CPU, set `device=-1` [C1]. For GPU, set `device` to the associated CUDA device id, such as `device=0` for the first GPU [C1]. For Apple Silicon, set `device="mps"` [C1][C2].

### Citations

[C1] -> `chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87`, [C2] -> `chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct CPU, CUDA, MPS, and device-map guidance.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653` — cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then moves the weights to other devices (CPU, hard drive) as needed. Set `device_map="auto"` to let Accelerate choose the device. > [!TIP] > Make sure have [Accelerate](https://hf.co/docs/accelerate/basic_tutorials/install) is installed. > > ```py > !pip install -U accelerate > ``` `…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_c8936735f55bfff48d9212a06467d7e5d988d43ca865728564151d87be607712` — , 'score': 0.03240183740854263}, {'label': 'Egyptian cat', 'score': 0.02394474856555462}, {'label': 'tiger cat', 'score': 0.02288915030658245}] ``` </hfoption> <hfoption id="visual question answering"> ```py from transformers import pipeline pipeline = pipeline(task="visual-question-answering", model="Salesforce/blip-vqa-base") pipeline( image="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/idefics-few-shot.jpg", question="What is in the image?"…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…

### Answer

To assign a Transformers Pipeline to CPU, GPU, or Apple Silicon, you can use the `device` parameter. Here's how:

- For CPU: By default, the pipeline runs on a CPU, which is specified by `device=-1` [C1].
- For GPU: Set the `device` parameter to the associated CUDA device ID, such as `device=0` for the first GPU [C1].
- For Apple Silicon: Set the `device` parameter to `"mps"` [C1].

### Citations

[C1] -> `chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct device identifiers, directly supported by C1.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_c8936735f55bfff48d9212a06467d7e5d988d43ca865728564151d87be607712` — , 'score': 0.03240183740854263}, {'label': 'Egyptian cat', 'score': 0.02394474856555462}, {'label': 'tiger cat', 'score': 0.02288915030658245}] ``` </hfoption> <hfoption id="visual question answering"> ```py from transformers import pipeline pipeline = pipeline(task="visual-question-answering", model="Salesforce/blip-vqa-base") pipeline( image="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/idefics-few-shot.jpg", question="What is in the image?"…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653` — cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then moves the weights to other devices (CPU, hard drive) as needed. Set `device_map="auto"` to let Accelerate choose the device. > [!TIP] > Make sure have [Accelerate](https://hf.co/docs/accelerate/basic_tutorials/install) is installed. > > ```py > !pip install -U accelerate > ``` `…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…

### Answer

To assign a Transformers Pipeline to CPU, GPU, or Apple Silicon, you can use the `device` parameter. For CPU, set `device=-1` [C1]. For GPU, specify the CUDA device ID, such as `device=0` for the first GPU [C1]. For Apple Silicon, set `device="mps"` [C1][C4]. Additionally, you can use `device_map="auto"` with the Accelerate library to let it automatically choose the optimal device [C1][C4].

### Citations

[C1] -> `chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87`, [C4] -> `chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete hardware assignment answer including Accelerate device mapping.

# q005

## Question

Why does the Transformers documentation caution against batching inputs with unknown sequence lengths?

## Reference Answer

Uneven sequence lengths can introduce heavy padding, reduce throughput, and cause out-of-memory failures, so batching should be measured and guarded with OOM checks.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_09006fa517bbcf8d797adaa6324d1032de7f102d6a6d0a7f449c48532886f1e4` — cess data in chunks. - for some data types, a single input (for example, a really long audio file) may need to be chunked into multiple parts before it can be processed - for some tasks, like zero-shot classification or question answering, a single input may need multiple forward passes which can cause issues with the `batch_size` parameter The [ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) clas…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2cf13751b83f628b996a5ab028f18018f93c4f193eb20391875b7879d7bb0927` — nt-batch-size <MAX_CLIENT_BATCH_SIZE> Control the maximum number of inputs that a client can send in a single request [env: MAX_CLIENT_BATCH_SIZE=] [default: 32] --auto-truncate Control automatic truncation of inputs that exceed the model's maximum supported size. Defaults to `true` (truncation enabled). Set to `false` to disable truncation; when disabled and the model's maximum input length exceeds `--max-batch-tokens`, the server will refuse to start with an error instead of silently truncati…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…

### Answer

The Transformers documentation cautions against batching inputs with unknown sequence lengths because batch inference can lead to out-of-memory (OOM) errors if the model's input size exceeds the available GPU memory. This is particularly relevant when the sequence lengths of the inputs are not uniform or known in advance. The documentation suggests measuring performance, iteratively adjusting the sequence length, and including OOM checks to handle such failures [C3].

### Citations

[C3] -> `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct OOM guidance but omits padding and throughput degradation.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_09006fa517bbcf8d797adaa6324d1032de7f102d6a6d0a7f449c48532886f1e4` — cess data in chunks. - for some data types, a single input (for example, a really long audio file) may need to be chunked into multiple parts before it can be processed - for some tasks, like zero-shot classification or question answering, a single input may need multiple forward passes which can cause issues with the `batch_size` parameter The [ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) clas…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2cf13751b83f628b996a5ab028f18018f93c4f193eb20391875b7879d7bb0927` — nt-batch-size <MAX_CLIENT_BATCH_SIZE> Control the maximum number of inputs that a client can send in a single request [env: MAX_CLIENT_BATCH_SIZE=] [default: 32] --auto-truncate Control automatic truncation of inputs that exceed the model's maximum supported size. Defaults to `true` (truncation enabled). Set to `false` to disable truncation; when disabled and the model's maximum input length exceeds `--max-batch-tokens`, the server will refuse to start with an error instead of silently truncati…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_56ced0128a5ddf048ad3bb5ed5e8ae3707188daec6694a12610c11fb90edd35c` — worry about the number of forward passes your inputs trigger. Instead, you can optimize `batch_size` independently of the inputs. The example below shows how it differs from [`Pipeline`]. ```py # ChunkPipeline all_model_outputs = [] for preprocessed in pipeline.preprocess(inputs): model_outputs = pipeline.model_forward(preprocessed) all_model_outputs.append(model_outputs) outputs =pipeline.postprocess(all_model_outputs) # Pipeline preprocessed = pipeline.preprocess(inputs) model_outputs = pipel…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_207016b93856d6d4fed91ec1fc1aff09392fa5edde3baac1bb012fa565fceb16` — xt': ' of', 'timestamp': (11.4, 11.64)}, {'text': ' its', 'timestamp': (11.64, 11.8)}, {'text': ' creed.', 'timestamp': (11.8, 12.3)}]} ``` </hfoption> <hfoption id="text generation"> Pass `return_full_text=False` to [`Pipeline`] to only return the generated text instead of the full text (prompt and generated text). [`~TextGenerationPipeline.__call__`] also supports additional keyword arguments from the [`~GenerationMixin.generate`] method. To return more than one generated sequence, set `num_r…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention after the relevant batching chunk falls outside Hybrid top-5.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_09006fa517bbcf8d797adaa6324d1032de7f102d6a6d0a7f449c48532886f1e4` — cess data in chunks. - for some data types, a single input (for example, a really long audio file) may need to be chunked into multiple parts before it can be processed - for some tasks, like zero-shot classification or question answering, a single input may need multiple forward passes which can cause issues with the `batch_size` parameter The [ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) clas…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2cf13751b83f628b996a5ab028f18018f93c4f193eb20391875b7879d7bb0927` — nt-batch-size <MAX_CLIENT_BATCH_SIZE> Control the maximum number of inputs that a client can send in a single request [env: MAX_CLIENT_BATCH_SIZE=] [default: 32] --auto-truncate Control automatic truncation of inputs that exceed the model's maximum supported size. Defaults to `true` (truncation enabled). Set to `false` to disable truncation; when disabled and the model's maximum input length exceeds `--max-batch-tokens`, the server will refuse to start with an error instead of silently truncati…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_56ced0128a5ddf048ad3bb5ed5e8ae3707188daec6694a12610c11fb90edd35c` — worry about the number of forward passes your inputs trigger. Instead, you can optimize `batch_size` independently of the inputs. The example below shows how it differs from [`Pipeline`]. ```py # ChunkPipeline all_model_outputs = [] for preprocessed in pipeline.preprocess(inputs): model_outputs = pipeline.model_forward(preprocessed) all_model_outputs.append(model_outputs) outputs =pipeline.postprocess(all_model_outputs) # Pipeline preprocessed = pipeline.preprocess(inputs) model_outputs = pipel…

### Answer

The Transformers documentation cautions against batching inputs with unknown sequence lengths because batch inference may not improve speed and can lead to out-of-memory (OOM) errors. This is due to the variability in input sizes, which can affect how efficiently the model processes batches [C2].

### Citations

[C2] -> `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Relevant passage is cited, but padding and throughput effects remain omitted.

# q006

## Question

How can the default pretrained model used by a Transformers Pipeline be replaced?

## Reference Answer

Pass the desired model identifier through the Pipeline model parameter instead of relying on the task's default pretrained model and preprocessor.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45` — is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma 2](./model_doc/gemma2), set `task="text-generation"` and `model="google/gemma-2-2b"`. ```py from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b") pipeline("the secret to baking a really good cake is ") [{'generated_text': 'the …
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653` — cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then moves the weights to other devices (CPU, hard drive) as needed. Set `device_map="auto"` to let Accelerate choose the device. > [!TIP] > Make sure have [Accelerate](https://hf.co/docs/accelerate/basic_tutorials/install) is installed. > > ```py > !pip install -U accelerate > ``` `…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_66ef2f775808fa370e4266983ad788d939b5ec41d0f875eaf868f1322135302e` — ine(task="automatic-speech-recognition", model="openai/whisper-large-v3") pipeline("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac") {'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'} ``` </hfoption> <hfoption id="image classification"> ```py from transformers import pipeline pipeline = pipeline(task="image-classification", model="google/vit-base-patch16-224") pipeline(images="https://huggingface.co/datasets/hugg…

### Answer

The default pretrained model used by a Transformers Pipeline can be replaced by specifying a different model using the `model` parameter when initializing the pipeline. For example, to use the [`TextGenerationPipeline`] with [Gemma 2], set `task="text-generation"` and `model="google/gemma-2-2b"` [C1].

### Citations

[C1] -> `chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correctly identifies the model parameter and supplies the documented example.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45` — is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma 2](./model_doc/gemma2), set `task="text-generation"` and `model="google/gemma-2-2b"`. ```py from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b") pipeline("the secret to baking a really good cake is ") [{'generated_text': 'the …
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653` — cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then moves the weights to other devices (CPU, hard drive) as needed. Set `device_map="auto"` to let Accelerate choose the device. > [!TIP] > Make sure have [Accelerate](https://hf.co/docs/accelerate/basic_tutorials/install) is installed. > > ```py > !pip install -U accelerate > ``` `…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…

### Answer

The default pretrained model used by a Transformers Pipeline can be replaced by specifying a different model using the `model` parameter when initializing the pipeline. This is supported by the documentation, which states that the `model` parameter can be used to override the default pretrained model and preprocessor [C1].

### Citations

[C1] -> `chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Concise and fully supported model-override answer.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45` — is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma 2](./model_doc/gemma2), set `task="text-generation"` and `model="google/gemma-2-2b"`. ```py from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b") pipeline("the secret to baking a really good cake is ") [{'generated_text': 'the …
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd` — The Hugging Face model ID, can be any model listed on <https://huggingface.co/models> with the `text-embeddings-inference` tag (meaning it's compatible with Text Embeddings Inference). Alternatively, the specified ID can also be a path to a local directory containing the necessary model files saved by the `save_pretrained(...)` methods of either Transformers or Sentence Transformers. [env: MODEL_ID=] --revision <REVISION> The actual revision of the model if you're referring to a model on the hu…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…

### Answer

The default pretrained model used by a Transformers Pipeline can be replaced by specifying a different model using the `model` parameter when initializing the pipeline. This allows you to override the default model with a different one, such as `google/gemma-2-2b` for the `text-generation` task [C1].

### Citations

[C1] -> `chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Directly answers with the correctly ranked source passage.

# q007

## Question

What is Hugging Face Text Embeddings Inference designed to serve?

## Reference Answer

Text Embeddings Inference is a production-oriented toolkit for deploying and serving open-source text embedding and sequence-classification models with features such as dynamic batching and observability.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_e95404e0b269c82494c202057acd3450571e4e07e555f1b5c7e073cf6746b310` — <div align="center"> # Text Embeddings Inference <a href="https://github.com/huggingface/text-embeddings-inference"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/huggingface/text-embeddings-inference?style=social"> </a> <a href="https://huggingface.github.io/text-embeddings-inference"> <img alt="Swagger API documentation" src="https://img.shields.io/badge/API-Swagger-informational"> </a> A blazing fast inference solution for text embeddings models. Benchmark for [BAAI/b…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd` — The Hugging Face model ID, can be any model listed on <https://huggingface.co/models> with the `text-embeddings-inference` tag (meaning it's compatible with Text Embeddings Inference). Alternatively, the specified ID can also be a path to a local directory containing the necessary model files saved by the `save_pretrained(...)` methods of either Transformers or Sentence Transformers. [env: MODEL_ID=] --revision <REVISION> The actual revision of the model if you're referring to a model on the hu…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…

### Answer

Hugging Face Text Embeddings Inference is designed to serve as a blazing fast inference solution for text embeddings models [C1].

### Citations

[C1] -> `chunk_e95404e0b269c82494c202057acd3450571e4e07e555f1b5c7e073cf6746b310`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correctly identifies embedding serving but omits sequence classification and operational features.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd` — The Hugging Face model ID, can be any model listed on <https://huggingface.co/models> with the `text-embeddings-inference` tag (meaning it's compatible with Text Embeddings Inference). Alternatively, the specified ID can also be a path to a local directory containing the necessary model files saved by the `save_pretrained(...)` methods of either Transformers or Sentence Transformers. [env: MODEL_ID=] --revision <REVISION> The actual revision of the model if you're referring to a model on the hu…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_0e460d3383f0d3dacc39a5376a47ee8fd7dc198bdae236fd06900daa62c7637c` — <!--Copyright 2024 The HuggingFace Team. All rights reserved. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License fo…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…

### Answer

Hugging Face Text Embeddings Inference is designed to serve as a powerful inference API for a variety of machine learning tasks, specifically tailored for text embeddings. It allows users to leverage pre-trained models from the Hugging Face Hub to generate text embeddings efficiently, supporting both public and private models, and offers features like tokenization control, dtype specification, and deployment options for different hardware configurations [C1][C4].

### Citations

[C1] -> `chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd`, [C4] -> `chunk_0e460d3383f0d3dacc39a5376a47ee8fd7dc198bdae236fd06900daa62c7637c`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: False

### Notes

Partially describes TEI but adds broad task and deployment claims weakly supported by the cited chunks.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd` — The Hugging Face model ID, can be any model listed on <https://huggingface.co/models> with the `text-embeddings-inference` tag (meaning it's compatible with Text Embeddings Inference). Alternatively, the specified ID can also be a path to a local directory containing the necessary model files saved by the `save_pretrained(...)` methods of either Transformers or Sentence Transformers. [env: MODEL_ID=] --revision <REVISION> The actual revision of the model if you're referring to a model on the hu…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_509d82c8d8885a9fcd4b8833678df9904c416eec1cfff5d33c37246bb6e12a30` — ghcr.io/huggingface/text-embeddings-inference:cpu-1.9 | | CPU | aarch64 | ghcr.io/huggingface/text-embeddings-inference:cpu-arm64-1.9 | | Volta | x86_64 | NOT SUPPORTED | | Turing (T4, RTX 2000 series, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:turing-1.9 (experimental) | | Ampere 8.0 (A100, A30) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:1.9 | | Ampere 8.6 (A10, A40, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:86-1.9 | | Ada Lovelace (RTX 4000…

### Answer

Hugging Face Text Embeddings Inference (TEI) is designed to serve open source text embeddings and sequence classification models, enabling high-performance extraction for the most popular models such as FlagEmbedding, Ember, GTE, and E5 [C1].

### Citations

[C1] -> `chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct model families, but production batching and observability are omitted.

# q008

## Question

What does the max_batch_tokens setting control in Text Embeddings Inference?

## Reference Answer

It limits the total potential tokens in a batch, controlling how many requests of different token lengths can fit together to maximize hardware utilization.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097` — CH_TOKENS> **IMPORTANT** This is one critical control to allow maximum usage of the available hardware. This represents the total amount of potential tokens within a batch. For `max_batch_tokens=1000`, you could fit `10` queries of `total_tokens=100` or a single query of `1000` tokens. Overall this number should be the largest possible until the model is compute bound. Since the actual memory overhead depends on the model implementation, text-embeddings-inference cannot infer this number automa…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_3f5df0268c752247091a3728d871f54b99d5caeba3db70efd302359a8c6756cc` — -embeddings): CPU-friendly embedding models without attention. - [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors. ## Application Examples You can use this framework for: - **Computing Sentence Embeddings** - [Dense Embeddings](https://www.sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html) - [Sparse Embeddings](https://www…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…

### Answer

The `max_batch_tokens` setting controls the total amount of potential tokens within a batch, which determines how many tokens can be processed in a single batch. This setting is crucial for maximizing the usage of available hardware and should be set to the largest possible value until the model becomes compute bound [C1].

### Citations

[C1] -> `chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct token-budget and hardware-utilization explanation.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097` — CH_TOKENS> **IMPORTANT** This is one critical control to allow maximum usage of the available hardware. This represents the total amount of potential tokens within a batch. For `max_batch_tokens=1000`, you could fit `10` queries of `total_tokens=100` or a single query of `1000` tokens. Overall this number should be the largest possible until the model is compute bound. Since the actual memory overhead depends on the model implementation, text-embeddings-inference cannot infer this number automa…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5771221e0b787b418f462ff20bdef31eb1fe1d36686044ef48f2549047121008` — [env: POOLING=] Possible values: - cls: Select the CLS token as embedding - mean: Apply Mean pooling to the model embeddings - splade: Apply SPLADE (Sparse Lexical and Expansion) to the model embeddings. This option is only available if the loaded model is a `ForMaskedLM` Transformer model - last-token: Select the last token as embedding --max-concurrent-requests <MAX_CONCURRENT_REQUESTS> The maximum amount of concurrent requests for this particular deployment. Having a low limit will refuse cl…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2cf13751b83f628b996a5ab028f18018f93c4f193eb20391875b7879d7bb0927` — nt-batch-size <MAX_CLIENT_BATCH_SIZE> Control the maximum number of inputs that a client can send in a single request [env: MAX_CLIENT_BATCH_SIZE=] [default: 32] --auto-truncate Control automatic truncation of inputs that exceed the model's maximum supported size. Defaults to `true` (truncation enabled). Set to `false` to disable truncation; when disabled and the model's maximum input length exceeds `--max-batch-tokens`, the server will refuse to start with an error instead of silently truncati…

### Answer

The `max_batch_tokens` setting controls the total amount of potential tokens within a batch, which is a critical parameter to allow maximum usage of the available hardware [C1]. This value determines how many tokens can be processed in a single batch, influencing the model's performance and resource utilization.

### Citations

[C1] -> `chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Accurately explains the batch token budget and resource effect.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097` — CH_TOKENS> **IMPORTANT** This is one critical control to allow maximum usage of the available hardware. This represents the total amount of potential tokens within a batch. For `max_batch_tokens=1000`, you could fit `10` queries of `total_tokens=100` or a single query of `1000` tokens. Overall this number should be the largest possible until the model is compute bound. Since the actual memory overhead depends on the model implementation, text-embeddings-inference cannot infer this number automa…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5771221e0b787b418f462ff20bdef31eb1fe1d36686044ef48f2549047121008` — [env: POOLING=] Possible values: - cls: Select the CLS token as embedding - mean: Apply Mean pooling to the model embeddings - splade: Apply SPLADE (Sparse Lexical and Expansion) to the model embeddings. This option is only available if the loaded model is a `ForMaskedLM` Transformer model - last-token: Select the last token as embedding --max-concurrent-requests <MAX_CONCURRENT_REQUESTS> The maximum amount of concurrent requests for this particular deployment. Having a low limit will refuse cl…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7` — r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in an air-gapped environment, first download the weights and then mount them inside the container using a volume. For example: ```shell # (Optional) create a `models` directory mkdir models cd models # Make sure you have git-lfs installed (https://git-lfs.com) git lfs install git c…

### Answer

The `max_batch_tokens` setting in Text Embeddings Inference controls the total amount of potential tokens within a batch. It is a critical control to allow maximum usage of the available hardware. This setting determines how many tokens can be processed in a single batch, which affects the model's performance and resource utilization [C1][C2].

### Citations

[C1] -> `chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097`, [C2] -> `chunk_5771221e0b787b418f462ff20bdef31eb1fe1d36686044ef48f2549047121008`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 1
- Requires human review: False

### Notes

Answer is correct; C1 supports it, while the additional C2 pooling citation is irrelevant.

# q009

## Question

How does Text Embeddings Inference support deployment in an air-gapped environment?

## Reference Answer

Download the model weights in advance, mount them into the container as a volume, and start TEI with the mounted local model path.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_3f5df0268c752247091a3728d871f54b99d5caeba3db70efd302359a8c6756cc` — -embeddings): CPU-friendly embedding models without attention. - [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors. ## Application Examples You can use this framework for: - **Computing Sentence Embeddings** - [Dense Embeddings](https://www.sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html) - [Sparse Embeddings](https://www…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_e95404e0b269c82494c202057acd3450571e4e07e555f1b5c7e073cf6746b310` — <div align="center"> # Text Embeddings Inference <a href="https://github.com/huggingface/text-embeddings-inference"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/huggingface/text-embeddings-inference?style=social"> </a> <a href="https://huggingface.github.io/text-embeddings-inference"> <img alt="Swagger API documentation" src="https://img.shields.io/badge/API-Swagger-informational"> </a> A blazing fast inference solution for text embeddings models. Benchmark for [BAAI/b…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention because the air-gapped passage is absent from Dense top-5.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7` — r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in an air-gapped environment, first download the weights and then mount them inside the container using a volume. For example: ```shell # (Optional) create a `models` directory mkdir models cd models # Make sure you have git-lfs installed (https://git-lfs.com) git lfs install git c…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_e95404e0b269c82494c202057acd3450571e4e07e555f1b5c7e073cf6746b310` — <div align="center"> # Text Embeddings Inference <a href="https://github.com/huggingface/text-embeddings-inference"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/huggingface/text-embeddings-inference?style=social"> </a> <a href="https://huggingface.github.io/text-embeddings-inference"> <img alt="Swagger API documentation" src="https://img.shields.io/badge/API-Swagger-informational"> </a> A blazing fast inference solution for text embeddings models. Benchmark for [BAAI/b…

### Answer

Text Embeddings Inference supports deployment in an air-gapped environment by allowing users to download the model weights externally and then mount them inside the container using a volume. This is achieved by first creating a directory for the models, cloning the required model repository, and then running the container with the models directory mounted as a volume. The model ID is specified within the container to point to the downloaded weights [C1].

### Citations

[C1] -> `chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct predownload, volume mount, and local model-path procedure.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7` — r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in an air-gapped environment, first download the weights and then mount them inside the container using a volume. For example: ```shell # (Optional) create a `models` directory mkdir models cd models # Make sure you have git-lfs installed (https://git-lfs.com) git lfs install git c…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_15224cac5bf613f21353d55b2d3c5f1adc44076acf1ac9c76332f3d2b8ce9d11` — sult the OpenAPI documentation of the `text-embeddings-inference` REST API using the `/docs` route. The Swagger UI is also available at: [https://huggingface.github.io/text-embeddings-inference](https://huggingface.github.io/text-embeddings-inference). ### Using a private or gated model You have the option to utilize the `HF_TOKEN` environment variable for configuring the token employed by `text-embeddings-inference`. This allows you to gain access to protected resources. For example: 1. Go to …
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2dd6b523ad0477751aa2ad487a723183349e5448f496eac4bcded3b4d36f844f` — s32-tp.png" width="400" /> </p> </div> ## Table of contents - [Get Started](#get-started) - [Supported Models](#supported-models) - [Docker](#docker) - [Docker Images](#docker-images) - [API Documentation](#api-documentation) - [Using a private or gated model](#using-a-private-or-gated-model) - [Air gapped deployment](#air-gapped-deployment) - [Using Re-rankers models](#using-re-rankers-models) - [Using Sequence Classification models](#using-sequence-classification-models) - [Using SPLADE pooli…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…

### Answer

Text Embeddings Inference supports deployment in an air-gapped environment by allowing the download of model weights and mounting them inside the container using a volume [C1]. For example, you can clone the model repository, set the models directory as the volume path, and run the container with the model ID pointing to the local directory [C1]. This approach ensures that the model weights are available within the container without requiring an internet connection [C1].

### Citations

[C1] -> `chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Fully supported air-gapped deployment answer.

# q010

## Question

When does a Qdrant Match Any payload condition succeed?

## Reference Answer

It succeeds when the stored keyword or integer value equals any configured value; for an array, at least one stored element must match one of them.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1` — ric | Default is `Dot product`, no need to specify it | `Distance` has supported metrics e.g. Dot, Cosine | | Search Type | Always exact in Qdrant | HNSW is an approximate NN | | Return Behaviour | Returns only vectors with non-zero values in the same indices as the query vector | Returns `limit` vectors | In general, the speed of the search is proportional to the number of non-zero values in the query vector. {{< code-snippet path="/documentation/headless/snippets/query-points/sparse-vectors/"…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention; Match Any details are not in Dense top-5.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_10f7f680ea1f254d70ca96b95847982ed72e3c166d190625d6967dcf39eb46ca` — s://qdrant.tech/documentation"`, but the prefix `"qdrant"` does not. Matching is byte-wise and, for valid UTF-8 strings, therefore character-wise. It is also case-sensitive, consistent with exact keyword matching. Unlike [Full Text Match](#full-text-match), prefix matching does not tokenize the value, so it is well suited to identifiers such as URLs, paths, or SKUs. {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-prefix/" >}} <aside role="status"> For efficient pr…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_1171fd126b59204972d153645236057db9c263eee8ad304b7407cd897ac5b7f7` — /documentation/manage-data/payload/#keyword) and [integer](/documentation/manage-data/payload/#integer) payloads. Example: {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-except/" >}} In this example, the condition will be satisfied if the stored value is neither `black` nor `yellow`. If the stored value is an array, it should have at least one value not matching any of the given values. E.g. if the stored value is `["black", "green"]`, the condition will be satis…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c` — on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/documentation/headless/snippets/query-points/score-boost-tags/" >}} There are multiple expressions available. Check the [API docs for specific details](https://api.qdrant.tech/v-1-14-x/api-reference/search/query-points#request.body.query.Query%20Interface.Query.Formul…

### Answer

A Qdrant Match Any payload condition succeeds when the stored value is neither one of the specified values. For example, if the stored value is an array, it should have at least one value that does not match any of the given values [C4].

### Citations

[C4] -> `chunk_1171fd126b59204972d153645236057db9c263eee8ad304b7407cd897ac5b7f7`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 0
- Citation Correctness: 0
- Requires human review: False

### Notes

Reverses Match Any by answering with Match Except semantics and cites that misleading chunk.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_73e05c7c749937560da314c21fee1c0824c319f114bc145e3a8ff11681528838` — d: {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-integer/" >}} The simplest kind of condition is one that checks if the stored value equals the given one. If several values are stored, at least one of them should match the condition. You can apply it to [keyword](/documentation/manage-data/payload/#keyword), [integer](/documentation/manage-data/payload/#integer) and [bool](/documentation/manage-data/payload/#bool) payloads. ### Match Any *Available as of v1.1.0*…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_10f7f680ea1f254d70ca96b95847982ed72e3c166d190625d6967dcf39eb46ca` — s://qdrant.tech/documentation"`, but the prefix `"qdrant"` does not. Matching is byte-wise and, for valid UTF-8 strings, therefore character-wise. It is also case-sensitive, consistent with exact keyword matching. Unlike [Full Text Match](#full-text-match), prefix matching does not tokenize the value, so it is well suited to identifiers such as URLs, paths, or SKUs. {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-prefix/" >}} <aside role="status"> For efficient pr…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c` — on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/documentation/headless/snippets/query-points/score-boost-tags/" >}} There are multiple expressions available. Check the [API docs for specific details](https://api.qdrant.tech/v-1-14-x/api-reference/search/query-points#request.body.query.Query%20Interface.Query.Formul…

### Answer

A Qdrant Match Any payload condition succeeds when the stored value is one of the multiple specified values. It functions as a logical OR for the given values and can be applied to keyword and integer payloads [C3].

### Citations

[C3] -> `chunk_73e05c7c749937560da314c21fee1c0824c319f114bc145e3a8ff11681528838`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct scalar OR behavior but omits matching any element of a stored array.

# q011

## Question

Why would a Qdrant nested object filter be needed for an array of objects?

## Reference Answer

It ensures all conditions are evaluated against the same array element instead of allowing different elements to satisfy different conditions.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_f7e4ff6b3c3147768eeb0567eedef8dd535e0f817e38fc408358ca8e6bb7f065` — ippets/filter-condition/slice/" >}} Slicing is based on a hash of the point IDs. A point matches slice `index` of `total` if `hash(id) % total == index`. For a fixed `total`, slices `0` through `total - 1` are disjoint and together cover every point in the collection. The hash is [SipHash-2-4](https://en.wikipedia.org/wiki/SipHash) with a zero key over the ID bytes, and it won't change across Qdrant versions. Slices with different `total` values are correlated, so slice `0` of `total: 4` is alw…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_625dbbbce9ff475c8863acc78c17fc93bedc3acfc3bf2c918b454a251ecee22e` — city`, `village`, and `town`: {{< code-snippet path="/documentation/headless/snippets/query-points/with-payload-fields/" >}} Or use `include` or `exclude` explicitly. For example, to exclude `city`: {{< code-snippet path="/documentation/headless/snippets/query-points/exclude-fields/" >}} It is possible to target nested fields using a dot notation: * `payload.nested_field` - for a nested field * `payload.nested_array[].sub_field` - for projecting nested fields within an array Accessing array ele…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…

### Answer

A Qdrant nested object filter is needed for an array of objects to apply conditions to individual elements within the array. This allows for filtering based on specific properties of each object in the array, ensuring that the parent document matches the condition if at least one element of the array meets the nested filter criteria [C1].

### Citations

[C1] -> `chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Explains per-element evaluation but not the failure mode where different elements satisfy different conditions.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_625dbbbce9ff475c8863acc78c17fc93bedc3acfc3bf2c918b454a251ecee22e` — city`, `village`, and `town`: {{< code-snippet path="/documentation/headless/snippets/query-points/with-payload-fields/" >}} Or use `include` or `exclude` explicitly. For example, to exclude `city`: {{< code-snippet path="/documentation/headless/snippets/query-points/exclude-fields/" >}} It is possible to target nested fields using a dot notation: * `payload.nested_field` - for a nested field * `payload.nested_array[].sub_field` - for projecting nested fields within an array Accessing array ele…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_a282621a2723161981f462410af989360fd12b0422e4b4d47eb1b61c07d923be` — ightseeing. ### Nested object filter *Available as of v1.2.0* By default, the conditions are taking into account the entire payload of a point. For instance, given two points with the following payload: ```json [ { "id": 1, "dinosaur": "t-rex", "diet": [ { "food": "leaves", "likes": false}, { "food": "meat", "likes": true} ] }, { "id": 2, "dinosaur": "diplodocus", "diet": [ { "food": "leaves", "likes": true}, { "food": "meat", "likes": false} ] } ] ``` The following query would match both point…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…

### Answer

A Qdrant nested object filter is needed for an array of objects to apply conditions to specific elements within the array. This allows for filtering based on criteria that are nested within the array elements, ensuring that the query matches the required conditions on individual elements rather than the entire array [C3].

### Citations

[C3] -> `chunk_a282621a2723161981f462410af989360fd12b0422e4b4d47eb1b61c07d923be`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct per-element scope, but the contrasting non-nested behavior is omitted.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_3af51a31bbbc0f3575860a94af5242bdcc036b967b34a316676f6be760688823` — and likes=true on `diet[1].likes` - the "diplodocus" matches food=meat on `diet[1].food` and likes=true on `diet[0].likes` To retrieve only the points which are matching the conditions on an array element basis, that is the point with id 1 in this example, you would need to use a nested object filter. Nested object filters allow arrays of objects to be queried independently of each other. It is achieved by using the `nested` condition type formed by a payload key to focus on and a filter to app…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_a282621a2723161981f462410af989360fd12b0422e4b4d47eb1b61c07d923be` — ightseeing. ### Nested object filter *Available as of v1.2.0* By default, the conditions are taking into account the entire payload of a point. For instance, given two points with the following payload: ```json [ { "id": 1, "dinosaur": "t-rex", "diet": [ { "food": "leaves", "likes": false}, { "food": "meat", "likes": true} ] }, { "id": 2, "dinosaur": "diplodocus", "diet": [ { "food": "leaves", "likes": true}, { "food": "meat", "likes": false} ] } ] ``` The following query would match both point…

### Answer

A Qdrant nested object filter is needed for an array of objects to apply conditions specifically to individual elements within the array. This allows for more granular and precise filtering, as the conditions are evaluated at the level of each array element rather than the entire payload of the point [C1]. This is particularly useful when you need to match specific criteria within the array elements, such as checking if a particular element meets certain conditions, which is not possible with standard payload filtering [C5].

### Citations

[C1] -> `chunk_3af51a31bbbc0f3575860a94af5242bdcc036b967b34a316676f6be760688823`, [C5] -> `chunk_a282621a2723161981f462410af989360fd12b0422e4b4d47eb1b61c07d923be`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

The top chunk exposes the cross-element problem and the answer explains individual-element scope.

# q012

## Question

How does Qdrant optimize cosine similarity calculations for stored vectors?

## Reference Answer

Qdrant normalizes each vector once when it is added to the collection, then uses a dot-product-style comparison during search.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_f841a27b7401b391d1a21346ce29d4f0dddcccb7fbd57e2da93ae0d29762cff6` — tation/headless/snippets/query-points/simple-dense/" >}} **Search By Id** {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id/" >}} ## Metrics There are many ways to estimate the similarity of vectors with each other. In Qdrant terms, these ways are called metrics. The choice of metric depends on the vectors obtained and, in particular, on the neural network encoder training method. Qdrant supports these most popular types of metrics: * Dot product: `Dot` - <http…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_b73f3f31650931d93081d9fc37a06a81ce80fc6020214525d6ed8705300b9763` — --- title: Search short_description: "Run similarity search in Qdrant to find points whose vectors are nearest to a query in the configured vector space." description: "Run similarity search in Qdrant to retrieve nearest-neighbor points for text, image, and multimodal queries using configurable distance metrics and HNSW." weight: 5 cta: "Run your first similarity search. Free, no infrastructure needed." aliases: - ../search - /documentation/concepts/search/ --- # Similarity Search Searching for…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…

### Answer

Qdrant optimizes cosine similarity calculations for stored vectors by normalizing the vector when adding it to the collection, which happens only once for each vector [C1]. The second step involves comparing vectors, which is equivalent to a dot product—a very fast operation due to SIMD (Single Instruction, Multiple Data) technology [C1]. This two-step process enhances search speed.

### Citations

[C1] -> `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct one-time normalization and fast dot-product comparison.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_f841a27b7401b391d1a21346ce29d4f0dddcccb7fbd57e2da93ae0d29762cff6` — tation/headless/snippets/query-points/simple-dense/" >}} **Search By Id** {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id/" >}} ## Metrics There are many ways to estimate the similarity of vectors with each other. In Qdrant terms, these ways are called metrics. The choice of metric depends on the vectors obtained and, in particular, on the neural network encoder training method. Qdrant supports these most popular types of metrics: * Dot product: `Dot` - <http…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_b73f3f31650931d93081d9fc37a06a81ce80fc6020214525d6ed8705300b9763` — --- title: Search short_description: "Run similarity search in Qdrant to find points whose vectors are nearest to a query in the configured vector space." description: "Run similarity search in Qdrant to retrieve nearest-neighbor points for text, image, and multimodal queries using configurable distance metrics and HNSW." weight: 5 cta: "Run your first similarity search. Free, no infrastructure needed." aliases: - ../search - /documentation/concepts/search/ --- # Similarity Search Searching for…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_dcd484a9c9aee332c70456bd44ba665e675d034e8e0d0ac5aeacf93d98f85c5e` — pictures, or songs of the same genre. {{< figure src="/docs/encoders.png" caption="This is how vector similarity works" width="70%" >}} ## Query API *Available as of v1.10.0* Qdrant provides a single interface for all kinds of search and exploration requests - the `Query API`. Here is a reference list of what kind of queries you can perform with the `Query API` in Qdrant: Depending on the `query` parameter, Qdrant might prefer different strategies for the search. | | | | --- | --- | | Nearest N…

### Answer

Qdrant optimizes cosine similarity calculations for stored vectors by normalizing the vector when adding it to the collection, which happens only once for each vector [C2]. This normalization step ensures that the vectors are on the same scale, making the cosine similarity calculation more efficient. Additionally, during the comparison of vectors, Qdrant uses a strategy that is equivalent to the dot product, which is a very fast operation due to SIMD (Single Instruction, Multiple Data) optimizations [C2].

### Citations

[C2] -> `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete and directly supported cosine optimization explanation.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_f841a27b7401b391d1a21346ce29d4f0dddcccb7fbd57e2da93ae0d29762cff6` — tation/headless/snippets/query-points/simple-dense/" >}} **Search By Id** {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id/" >}} ## Metrics There are many ways to estimate the similarity of vectors with each other. In Qdrant terms, these ways are called metrics. The choice of metric depends on the vectors obtained and, in particular, on the neural network encoder training method. Qdrant supports these most popular types of metrics: * Dot product: `Dot` - <http…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_dcd484a9c9aee332c70456bd44ba665e675d034e8e0d0ac5aeacf93d98f85c5e` — pictures, or songs of the same genre. {{< figure src="/docs/encoders.png" caption="This is how vector similarity works" width="70%" >}} ## Query API *Available as of v1.10.0* Qdrant provides a single interface for all kinds of search and exploration requests - the `Query API`. Here is a reference list of what kind of queries you can perform with the `Query API` in Qdrant: Depending on the `query` parameter, Qdrant might prefer different strategies for the search. | | | | --- | --- | | Nearest N…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1` — ric | Default is `Dot product`, no need to specify it | `Distance` has supported metrics e.g. Dot, Cosine | | Search Type | Always exact in Qdrant | HNSW is an approximate NN | | Return Behaviour | Returns only vectors with non-zero values in the same indices as the query vector | Returns `limit` vectors | In general, the speed of the search is proportional to the number of non-zero values in the query vector. {{< code-snippet path="/documentation/headless/snippets/query-points/sparse-vectors/"…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_b73f3f31650931d93081d9fc37a06a81ce80fc6020214525d6ed8705300b9763` — --- title: Search short_description: "Run similarity search in Qdrant to find points whose vectors are nearest to a query in the configured vector space." description: "Run similarity search in Qdrant to retrieve nearest-neighbor points for text, image, and multimodal queries using configurable distance metrics and HNSW." weight: 5 cta: "Run your first similarity search. Free, no infrastructure needed." aliases: - ../search - /documentation/concepts/search/ --- # Similarity Search Searching for…

### Answer

Qdrant optimizes cosine similarity calculations for stored vectors by normalizing the vector when adding it to the collection, which happens only once for each vector [C1]. The second step involves comparing vectors, which is equivalent to a dot product—a very fast operation due to SIMD [C1]. This two-step process enhances search speed.

### Citations

[C1] -> `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete and directly supported cosine optimization explanation.

# q013

## Question

What does score_threshold do in a Qdrant search request?

## Reference Answer

It removes results whose scores are worse than the threshold, with the direction of worse depending on the configured distance metric.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C2] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1` — ric | Default is `Dot product`, no need to specify it | `Distance` has supported metrics e.g. Dot, Cosine | | Search Type | Always exact in Qdrant | HNSW is an approximate NN | | Return Behaviour | Returns only vectors with non-zero values in the same indices as the query vector | Returns `limit` vectors | In general, the speed of the search is proportional to the number of non-zero values in the query vector. {{< code-snippet path="/documentation/headless/snippets/query-points/sparse-vectors/"…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66` — vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retrieval iteration to surface more relevant documents. Qdrant provides a subtype of relevance feedback-based retrieval, where feedback is given by any model (relevance oracle) in a granular fashion: it rescores top retrieved results by their relative relevance to…

### Answer

The `score_threshold` parameter in a Qdrant search request filters out results with a similarity score that is worse than the given threshold. It excludes all results with a score below (or above, depending on the context) this threshold [C3].

### Citations

[C3] -> `chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correctly explains exclusion of worse scores and metric-dependent direction.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1` — ric | Default is `Dot product`, no need to specify it | `Distance` has supported metrics e.g. Dot, Cosine | | Search Type | Always exact in Qdrant | HNSW is an approximate NN | | Return Behaviour | Returns only vectors with non-zero values in the same indices as the query vector | Returns `limit` vectors | In general, the speed of the search is proportional to the number of non-zero values in the query vector. {{< code-snippet path="/documentation/headless/snippets/query-points/sparse-vectors/"…
- [C2] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225` — get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vectors. <aside role="status">Disable the HNSW index for vectors used only for rescoring by setting <code>m=0</code> in the vector's HNSW configuration. Rescoring does not use the HNSW index, so disabling it will free up memory.</aside> ### Re-Scoring Examples Fetch 1000 results us…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c` — on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/documentation/headless/snippets/query-points/score-boost-tags/" >}} There are multiple expressions available. Check the [API docs for specific details](https://api.qdrant.tech/v-1-14-x/api-reference/search/query-points#request.body.query.Query%20Interface.Query.Formul…

### Answer

The `score_threshold` parameter in a Qdrant search request is used to filter out results with a similarity score that is worse than a specified threshold. It excludes all results with a score that does not meet or exceed this threshold, thereby allowing users to focus on the most relevant results based on their defined similarity criteria [C1].

### Citations

[C1] -> `chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct threshold behavior with sufficient adjacent context.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1` — ric | Default is `Dot product`, no need to specify it | `Distance` has supported metrics e.g. Dot, Cosine | | Search Type | Always exact in Qdrant | HNSW is an approximate NN | | Return Behaviour | Returns only vectors with non-zero values in the same indices as the query vector | Returns `limit` vectors | In general, the speed of the search is proportional to the number of non-zero values in the query vector. {{< code-snippet path="/documentation/headless/snippets/query-points/sparse-vectors/"…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_2ab6cbd06f6e3de15c08df1239957715b8eb194bb2ba9477b596d1a5ad62d9d0` — can use `score_threshold` parameter of the search query. It will exclude all results with a score worse than the given. <aside role="status">This parameter may exclude lower or higher scores depending on the used metric. For example, higher scores of Euclidean metric are considered more distant and, therefore, will be excluded.</aside> ### Payload and Vector in the Result By default, retrieval methods do not return any stored information such as payload and vectors. Additional parameters `with_…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c` — on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/documentation/headless/snippets/query-points/score-boost-tags/" >}} There are multiple expressions available. Check the [API docs for specific details](https://api.qdrant.tech/v-1-14-x/api-reference/search/query-points#request.body.query.Query%20Interface.Query.Formul…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…

### Answer

The `score_threshold` parameter in a Qdrant search request is used to exclude results with a score worse than the given threshold. It filters out results that do not meet the specified similarity score, which can be based on the used metric. This parameter may exclude lower or higher scores depending on the metric, as higher scores of the Euclidean metric are considered more distant and thus excluded [C1][C2].

### Citations

[C1] -> `chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1`, [C2] -> `chunk_2ab6cbd06f6e3de15c08df1239957715b8eb194bb2ba9477b596d1a5ad62d9d0`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Exact threshold passage is retrieved and cited.

# q014

## Question

Why can large offset pagination be unreliable for HNSW vector search?

## Reference Answer

HNSW is not designed to retrieve an arbitrary Nth neighbor without first retrieving earlier neighbors, so offsets can be expensive and may duplicate or skip points as the index changes.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033` — ery-points/with-offset/" >}} This is equivalent to retrieving the 11th page with 10 records per page. <aside role="alert">Large offset values may cause performance issues</aside> Vector-based retrieval in general, and the HNSW index in particular, are not designed to be paginated. It is impossible to retrieve the Nth closest vector without internally retrieving the first N vectors first. However, using the `offset` parameter saves resources by reducing network traffic and the number of times th…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_add09af55ae85b47c39406570995c783b243b6072562555b84ea4ea6dd3789be` — s. As a result, paginating with `offset` can return the same point on multiple pages or skip points entirely. There are several ways to work around this: #### Client-Side Pagination Retrieve a large batch in a single request and paginate through it on the client. For example, fetch the top 100 results at once and let the user browse them 10 at a time. This avoids multiple round-trips and guarantees no duplicates. The trade-off is increased latency, and returning more data than the user actually…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_3d8734a8c97773c4562bfc683f42655851425a6f39a3afb7528f96a80150fabc` — nce/search/query-points) {{< code-snippet path="/documentation/headless/snippets/query-points/basic-with-filter-and-params/" >}} In this example, we are looking for vectors similar to vector `[0.2, 0.1, 0.9, 0.7]`. Parameter `limit` (or its alias - `top`) specifies the amount of most similar results we would like to retrieve. Values under the key `params` specify custom parameters for the search. Currently, it could be: * `hnsw_ef` - value that specifies `ef` parameter of the HNSW algorithm. * …
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_6f85e1bc9aabbf16fbc5fd7ba3ebd89e40fc5efdda1a92343322239fc82d5f6b` — he vector with that name. It is also possible to reference an ID from a different collection, by setting the `lookup_from` parameter. {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id-with-lookup/" >}} In the case above, Qdrant will fetch the `"image-512"` vector from the specified point id in the collection `another_collection`. <aside role="status"> The fetched vector(s) must match the characteristics of the <code>using</code> vector, otherwise, an error will…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_effe795c19ee0c01b9ae4ebe9b5ff8c26444740a20befb28c3555ed12092f4ca` — s partitioned into smaller fractions of similar embeddings. This index can be searched efficiently and the embeddings with the highest similarity (the nearest neighbors) can be retrieved within milliseconds, even if you have millions of vectors. However, the results are not necessarily exact. It is possible that some vectors with high similarity will be missed. For all ANN methods, there are usually one or more parameters to tune that determine the recall-speed trade-off. If you want the highes…

### Answer

Large offset pagination can be unreliable for HNSW vector search because the ranking of results can shift slightly between requests due to the approximate nature of HNSW search [C1]. As a result, paginating with `offset` can return the same point on multiple pages or skip points entirely [C1][C2]. This instability makes it difficult to reliably navigate through results using offset-based pagination.

### Citations

[C1] -> `chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033`, [C2] -> `chunk_add09af55ae85b47c39406570995c783b243b6072562555b84ea4ea6dd3789be`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Explains duplicate/skip instability but omits the expensive arbitrary-Nth-neighbor limitation.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033` — ery-points/with-offset/" >}} This is equivalent to retrieving the 11th page with 10 records per page. <aside role="alert">Large offset values may cause performance issues</aside> Vector-based retrieval in general, and the HNSW index in particular, are not designed to be paginated. It is impossible to retrieve the Nth closest vector without internally retrieving the first N vectors first. However, using the `offset` parameter saves resources by reducing network traffic and the number of times th…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_add09af55ae85b47c39406570995c783b243b6072562555b84ea4ea6dd3789be` — s. As a result, paginating with `offset` can return the same point on multiple pages or skip points entirely. There are several ways to work around this: #### Client-Side Pagination Retrieve a large batch in a single request and paginate through it on the client. For example, fetch the top 100 results at once and let the user browse them 10 at a time. This avoids multiple round-trips and guarantees no duplicates. The trade-off is increased latency, and returning more data than the user actually…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_6f85e1bc9aabbf16fbc5fd7ba3ebd89e40fc5efdda1a92343322239fc82d5f6b` — he vector with that name. It is also possible to reference an ID from a different collection, by setting the `lookup_from` parameter. {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id-with-lookup/" >}} In the case above, Qdrant will fetch the `"image-512"` vector from the specified point id in the collection `another_collection`. <aside role="status"> The fetched vector(s) must match the characteristics of the <code>using</code> vector, otherwise, an error will…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225` — get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vectors. <aside role="status">Disable the HNSW index for vectors used only for rescoring by setting <code>m=0</code> in the vector's HNSW configuration. Rescoring does not use the HNSW index, so disabling it will free up memory.</aside> ### Re-Scoring Examples Fetch 1000 results us…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_3d8734a8c97773c4562bfc683f42655851425a6f39a3afb7528f96a80150fabc` — nce/search/query-points) {{< code-snippet path="/documentation/headless/snippets/query-points/basic-with-filter-and-params/" >}} In this example, we are looking for vectors similar to vector `[0.2, 0.1, 0.9, 0.7]`. Parameter `limit` (or its alias - `top`) specifies the amount of most similar results we would like to retrieve. Values under the key `params` specify custom parameters for the search. Currently, it could be: * `hnsw_ef` - value that specifies `ef` parameter of the HNSW algorithm. * …

### Answer

Large offset pagination can be unreliable for HNSW vector search because the ranking of results can shift slightly between requests due to the approximate nature of HNSW search. This can lead to the same point being returned on multiple pages or points being skipped entirely [C1].

### Citations

[C1] -> `chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct instability symptoms but incomplete explanation of large-offset cost.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033` — ery-points/with-offset/" >}} This is equivalent to retrieving the 11th page with 10 records per page. <aside role="alert">Large offset values may cause performance issues</aside> Vector-based retrieval in general, and the HNSW index in particular, are not designed to be paginated. It is impossible to retrieve the Nth closest vector without internally retrieving the first N vectors first. However, using the `offset` parameter saves resources by reducing network traffic and the number of times th…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_add09af55ae85b47c39406570995c783b243b6072562555b84ea4ea6dd3789be` — s. As a result, paginating with `offset` can return the same point on multiple pages or skip points entirely. There are several ways to work around this: #### Client-Side Pagination Retrieve a large batch in a single request and paginate through it on the client. For example, fetch the top 100 results at once and let the user browse them 10 at a time. This avoids multiple round-trips and guarantees no duplicates. The trade-off is increased latency, and returning more data than the user actually…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_6f85e1bc9aabbf16fbc5fd7ba3ebd89e40fc5efdda1a92343322239fc82d5f6b` — he vector with that name. It is also possible to reference an ID from a different collection, by setting the `lookup_from` parameter. {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id-with-lookup/" >}} In the case above, Qdrant will fetch the `"image-512"` vector from the specified point id in the collection `another_collection`. <aside role="status"> The fetched vector(s) must match the characteristics of the <code>using</code> vector, otherwise, an error will…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_fbc9a0b0fa15c781ede9ad96be48677d5be8be58f6f9d046d2e2e216920eaf0f` — use a combined [filterable index](/documentation/manage-data/indexing/#filterable-hnsw-index). However, when combining multiple strict payload filters, this mechanism might not provide sufficient accuracy. In such cases, you can use the ACORN search algorithm. It is an extension to the regular HNSW search algorithm, based on the ACORN-1 algorithm described in the paper [ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data](https://arxiv.org/abs/2403.04871).…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_4fe8478599f5a15a745adb4be67947689f6bd8245b325b5b9072d4c30b81880e` — * Only [keyword](/documentation/manage-data/payload/#keyword) and [integer](/documentation/manage-data/payload/#integer) payload values are supported for the `group_by` parameter. Payload values with other types will be ignored. * At the moment, pagination is not enabled when using **groups**, so the `offset` parameter is not allowed. ### Lookup in Groups When the points in a group share large fields like titles, abstracts, or full document vectors, copying that data onto every point inflates s…

### Answer

Large offset pagination can be unreliable for HNSW vector search because the ranking of results can shift slightly between requests due to the approximate nature of HNSW search. This means that paginating with `offset` can return the same point on multiple pages or skip points entirely [C1].

### Citations

[C1] -> `chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct duplicate/skip effect but omits the underlying offset retrieval limitation.

# q015

## Question

How does reciprocal rank fusion reward a document appearing in multiple result lists?

## Reference Answer

RRF sums contributions based on the document's rank in each result list, so documents near the top of one or several rankings receive larger fused scores.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92` — se you can get an empty result.</aside> ## Hybrid Search One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result. {{< figure src="/docs/fusion-idea.png" caption="Fusing results from multiple queries" width="80%" >}} For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise wo…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178` — y and boosts those that appear closer to the top in multiple sets of results. The score of a document is calculated using its rank in each result set: $$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r} - 1} $$ Where: - $D$ the set of points across all results - $R(d)$ is the set of rankings for a particular document - $k$ is a constant (set to 2 by default) - $r$ is an ordered set of results from one source - $r_d$ is the rank of document $d$ in ranking $r$ - $w_r$ is the we…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…

### Answer

Reciprocal rank fusion (RRF) rewards a document appearing in multiple result lists by boosting its score based on its rank in each result set. The score of a document is calculated using its rank in each result set with the formula:

$$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + r_d} $$

where $k$ is a constant (set to 2 by default) and $r_d$ is the rank of the document in each ranking [C2]. This means that documents appearing closer to the top in multiple result lists receive higher scores, as their ranks are smaller, leading to larger values in the reciprocal function.

### Citations

[C2] -> `chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correctly explains summed reciprocal-rank contributions.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92` — se you can get an empty result.</aside> ## Hybrid Search One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result. {{< figure src="/docs/fusion-idea.png" caption="Fusing results from multiple queries" width="80%" >}} For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise wo…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178` — y and boosts those that appear closer to the top in multiple sets of results. The score of a document is calculated using its rank in each result set: $$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r} - 1} $$ Where: - $D$ the set of points across all results - $R(d)$ is the set of rankings for a particular document - $k$ is a constant (set to 2 by default) - $r$ is an ordered set of results from one source - $r_d$ is the rank of document $d$ in ranking $r$ - $w_r$ is the we…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_68fead02254360d99f7653254b8ad4865b2a5f2a88a56eed779ce1f3b88d4bec` — -decay/" >}} <aside role="status">Calibrate the decay weight against the scale of your fused <code>$score</code>. RRF scores are small (sums of <code>1/(k+rank)</code> terms), while decay functions return values in <code>[0, 1]</code>, so an unweighted decay term will dominate the fused score unless you multiply it by a smaller coefficient. Wrap the decay in a multiplication expression with a coefficient tuned to your workload.</aside> The [Choosing a Fusion Method notebook](https://githubtocol…

### Answer

Reciprocal rank fusion (RRF) rewards a document appearing in multiple result lists by boosting its score based on its rank in each result set. The score of a document is calculated using its rank in each result set with the formula:

$$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + r_d} $$

Where $k$ is a constant (set to 2 by default) and $r_d$ is the rank of document $d$ in ranking $r$ [C3]. This means that documents appearing closer to the top in multiple result sets receive higher scores, as their ranks are smaller, leading to larger reciprocal values in the sum.

### Citations

[C3] -> `chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correctly explains higher scores for repeated high ranks.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92` — se you can get an empty result.</aside> ## Hybrid Search One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result. {{< figure src="/docs/fusion-idea.png" caption="Fusing results from multiple queries" width="80%" >}} For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise wo…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178` — y and boosts those that appear closer to the top in multiple sets of results. The score of a document is calculated using its rank in each result set: $$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r} - 1} $$ Where: - $D$ the set of points across all results - $R(d)$ is the set of rankings for a particular document - $k$ is a constant (set to 2 by default) - $r$ is an ordered set of results from one source - $r_d$ is the rank of document $d$ in ranking $r$ - $w_r$ is the we…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_76f1595996b9fc24a98741c470092b714dbcc142a4d3e31b2ed722e1ab00d59a` — en you have multiple points for the same item, and you want to avoid redundancy of the same item in the results. For example, if you have a large document split into multiple chunks, and you want to search or [recommend](/documentation/search/explore/#recommendation-api) on a per-document basis, you can group the results by the document ID. Consider having points with the following payloads: ```json [ { "id": 0, "payload": { "chunk_part": 0, "document_id": "a" }, "vector": [0.91] }, { "id": 1, …

### Answer

Reciprocal rank fusion (RRF) rewards a document appearing in multiple result lists by boosting its score based on its rank in each result set. The score of a document is calculated using its rank in each result set with the formula:

$$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r} - 1} $$

Where $ k $ is a constant (set to 2 by default), $ r_d $ is the rank of the document in a ranking, and $ w_r $ is the weight of the ranking (set to 1 by default). This formula ensures that documents appearing higher in multiple result lists receive a higher score [C3].

### Citations

[C3] -> `chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete weighted RRF explanation supported by the cited formula.

# q016

## Question

How does Qdrant's distribution-based score fusion normalize retriever scores?

## Reference Answer

DBSF uses each result set's score distribution to map scores into a comparable range before summing them; it is stateless and derives limits from the current query's returned points.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92` — se you can get an empty result.</aside> ## Hybrid Search One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result. {{< figure src="/docs/fusion-idea.png" caption="Fusing results from multiple queries" width="80%" >}} For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise wo…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_0ceb74e1146eca5c16899ac6970e7b950af2f7588df3235277cee45a57a3f4bf` — igher separation to the already selected points. $$ MMR = \arg \max_{D_i \in R\setminus S}[\lambda sim(D_i, Q) - (1 - \lambda)\max_{D_j \in S}sim(D_i, D_j)] $$ <figcaption align="center">Where $R$ is the candidates set, $S$ is the selected set, $Q$ is the query vector, $sim$ is the similarity function, and $\lambda = 1 - diversity$.</figcaption> <br> This is implemented in Qdrant as a parameter of a nearest neighbors query. You define the vector to get the nearest candidates, and a `diversity` …
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…

### Answer

Qdrant's distribution-based score fusion (DBSF) normalizes retriever scores by computing the mean $\mu$ and sample standard deviation $\sigma$ for each retriever's returned set. It then normalizes every score using the 3-sigma extremes as endpoints:

$$ \hat{s} = \frac{s - (\mu - 3\sigma)}{6\sigma} $$

This normalization ensures that scores from different retrievers are on a comparable range, allowing them to be summed effectively [C1].

### Citations

[C1] -> `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Captures per-result-set distribution normalization and comparable summed scores.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…
- [C2] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_5e3fb0fa5c2e973d53ebace2400b476efb750959536c41d378c5cb964e7279f0` — stics come from the prefetch top-k (a small sample), and a single dominant outlier in that top-k can skew normalization for that query. Increase the prefetch `limit` if you see unstable rankings. {{< code-snippet path="/documentation/headless/snippets/query-points/hybrid-dbsf/" >}} ### Choosing a Fusion Method | If you have... | Use | | --- | --- | | An eval set (queries with known-relevant docs) to tune on | Weighted RRF, with weights tuned on a train/val split | | Trust in your retrievers' ra…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…

### Answer

Qdrant's distribution-based score fusion (DBSF) normalizes retriever scores by computing the mean $\mu$ and sample standard deviation $\sigma$ for each retriever's returned set. It then normalizes every score using the 3-sigma extremes as endpoints:

$$ \hat{s} = \frac{s - (\mu - 3\sigma)}{6\sigma} $$

Normalized scores are summed across retrievers, ensuring that different score magnitudes no longer matter because each retriever contributes on the same comparable range [C1].

### Citations

[C1] -> `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Detailed DBSF normalization formula and summation are correct.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…

### Answer

Qdrant's distribution-based score fusion (DBSF) normalizes retriever scores by computing the mean $\mu$ and sample standard deviation $\sigma$ for each retriever's returned set. It then normalizes every score using the 3-sigma extremes as endpoints:

$$ \hat{s} = \frac{s - (\mu - 3\sigma)}{6\sigma} $$

This normalization ensures that scores from different retrievers are on a comparable range before being summed [C1].

### Citations

[C1] -> `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct distribution-based mapping into a comparable range.

# q017

## Question

What problem is semantic search intended to solve beyond literal keyword matching?

## Reference Answer

Semantic search tries to understand query and corpus meaning, allowing relevant matches despite synonyms, abbreviations, and misspellings.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_55f82d46216116757678b11d0a5de037a2a07f4d430e9e19af78ef0d8d207221` — nswlib/). Examples: - [semantic_search_quora_hnswlib.py](semantic_search_quora_hnswlib.py) - [semantic_search_quora_annoy.py](semantic_search_quora_annoy.py) - [semantic_search_quora_faiss.py](semantic_search_quora_faiss.py) ## Retrieve & Re-Rank For complex semantic search scenarios, a two-stage retrieve & re-rank pipeline is advisable: ![InformationRetrieval](https://raw.githubusercontent.com/huggingface/sentence-transformers/main/docs/img/InformationRetrieval.png) For further details, see [R…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79` — fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine both approaches. For an example implementation, see [semantic_search_nq_opensearch.py](semantic_search_nq_opensearch.py), which shows how to use OpenSearch with the Natural Questions dataset, demonstrating both semantic search and BM25 search capabilities. ## Approximate Nearest N…

### Answer

Semantic search is intended to solve the problem of finding documents that have a high semantic similarity with the query, even when there are synonyms, abbreviations, or misspellings, unlike keyword search engines that can only find documents based on lexical matches [C1].

### Citations

[C1] -> `chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Directly contrasts learned meaning with literal matching.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79` — fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine both approaches. For an example implementation, see [semantic_search_nq_opensearch.py](semantic_search_nq_opensearch.py), which shows how to use OpenSearch with the Natural Questions dataset, demonstrating both semantic search and BM25 search capabilities. ## Approximate Nearest N…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69` — **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and you want to find the paragraph *"Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy ..."*. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense. - Related training example: [MS M…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_e7cb4194151d952f056f76892bf3babf9c012b6cb75a5b8aa2fe83551fba3122` — arch](https://www.elastic.co/elasticsearch/) has the possibility to [index dense vectors](https://www.elastic.co/what-is/vector-search) and to use them for document scoring. We can easily index embedding vectors, store other data alongside our vectors and, most importantly, efficiently retrieve relevant entries using [approximate nearest neighbor search](https://www.elastic.co/blog/introducing-approximate-nearest-neighbor-search-in-elasticsearch-8-0) (HNSW, see also below) on the embeddings. Fo…

### Answer

Semantic search is intended to solve the problem of literal keyword matching by understanding the semantic meaning of the search query and the corpus to search over. It can perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches [C2].

### Citations

[C2] -> `chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete synonyms, abbreviations, and misspellings answer.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79` — fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine both approaches. For an example implementation, see [semantic_search_nq_opensearch.py](semantic_search_nq_opensearch.py), which shows how to use OpenSearch with the Natural Questions dataset, demonstrating both semantic search and BM25 search capabilities. ## Approximate Nearest N…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_293b419bb31d44e5b59d6b65009b2708fa24711d3372d2db12d3ea963c260721` — ased on artificial neural networks with representation learning. .. literalinclude:: semantic_search.py ``` ## Optimized Implementation ```{eval-rst} Instead of implementing semantic search by yourself, you can use the :func:`~sentence_transformers.util.semantic_search` function. ``` The function accepts the following parameters: ```{eval-rst} .. autofunction:: sentence_transformers.util.semantic_search ``` By default, up to 100 queries are processed in parallel. Further, the corpus is chunked …
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69` — **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and you want to find the paragraph *"Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy ..."*. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense. - Related training example: [MS M…

### Answer

Semantic search is intended to solve the problem of finding documents that have a high semantic similarity with the search query, even when there are synonyms, abbreviations, or misspellings, unlike keyword search engines that can only find documents based on lexical matches [C1][C2].

### Citations

[C1] -> `chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456`, [C2] -> `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete answer supported by both semantic and lexical passages.

# q018

## Question

What efficiency and quality trade-off does a CrossEncoder reranker introduce?

## Reference Answer

A CrossEncoder can substantially improve the final ordering of candidates but is too slow to score a very large corpus, so an efficient retriever first narrows the candidate set.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62` — gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re-rankers models are Sequence Classification cross-encoders models with a single class that scores the similarity between a query and a text. See [this blogpost](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by the LlamaIndex tea…

### Answer

The CrossEncoder reranker introduces a trade-off between efficiency and quality. It is more accurate than a bi-encoder because it evaluates the relevance of each (query, document) pair by considering the interaction between the query and the document, which leads to higher performance [C1]. However, this increased accuracy comes at the cost of computational efficiency, as scoring thousands or millions of pairs is slow [C1]. To mitigate this, a retriever is used to generate a smaller set of candidate documents, which are then re-ranked by the CrossEncoder [C1][C4].

### Citations

[C1] -> `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`, [C4] -> `chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct quality/latency trade-off and candidate narrowing.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_5f9769f965866f6b1f7bb94a0cf9a924e7c62e09bb7fc8eb1daaceef465305ff` — inetuning Sparse Embedding Models](https://huggingface.co/blog/train-sparse-encoder): training SPLADE and other sparse encoders. **Multimodal:** - [Multimodal Embedding & Reranker Models](https://huggingface.co/blog/multimodal-sentence-transformers): using text, image, audio, and video models through a single API. - [Training and Finetuning Multimodal Embedding & Reranker Models](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal models, with a Visual Docum…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62` — gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re-rankers models are Sequence Classification cross-encoders models with a single class that scores the similarity between a query and a text. See [this blogpost](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by the LlamaIndex tea…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_3119cb0c2a7b12e9cd954a6e8b47d18c24c3626e3d3e791e1573d0435ddfa0da` — shape) # => (3, 384) ``` And that's already it. We now have numpy arrays with the embeddings, one for each text. We can use these to compute similarities. ```python similarities = model.similarity(embeddings, embeddings) print(similarities) # tensor([[1.0000, 0.6660, 0.1046], # [0.6660, 1.0000, 0.1411], # [0.1046, 0.1411, 1.0000]]) ``` ### Reranker Models First download a pretrained reranker a.k.a. Cross Encoder model. ```python from sentence_transformers import CrossEncoder # 1. Load a pretrai…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_effe795c19ee0c01b9ae4ebe9b5ff8c26444740a20befb28c3555ed12092f4ca` — s partitioned into smaller fractions of similar embeddings. This index can be searched efficiently and the embeddings with the highest similarity (the nearest neighbors) can be retrieved within milliseconds, even if you have millions of vectors. However, the results are not necessarily exact. It is possible that some vectors with high similarity will be missed. For all ANN methods, there are usually one or more parameters to tune that determine the recall-speed trade-off. If you want the highes…

### Answer

A CrossEncoder reranker introduces a trade-off between efficiency and quality. It provides higher performance by performing attention across the query and the document, which results in more accurate relevance scores. However, this comes at the cost of slower performance when scoring a large number of (query, document)-pairs, as noted in the documentation [C1]. This trade-off is managed by using a retriever to generate a smaller set of candidate documents, which are then re-ranked by the CrossEncoder, thus balancing efficiency and quality.

### Citations

[C1] -> `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete retrieve-then-rerank efficiency explanation.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_5f9769f965866f6b1f7bb94a0cf9a924e7c62e09bb7fc8eb1daaceef465305ff` — inetuning Sparse Embedding Models](https://huggingface.co/blog/train-sparse-encoder): training SPLADE and other sparse encoders. **Multimodal:** - [Multimodal Embedding & Reranker Models](https://huggingface.co/blog/multimodal-sentence-transformers): using text, image, audio, and video models through a single API. - [Training and Finetuning Multimodal Embedding & Reranker Models](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal models, with a Visual Docum…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62` — gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re-rankers models are Sequence Classification cross-encoders models with a single class that scores the similarity between a query and a text. See [this blogpost](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by the LlamaIndex tea…

### Answer

A CrossEncoder reranker introduces a trade-off between efficiency and quality by performing a more accurate but computationally intensive scoring of (query, document) pairs. This higher accuracy comes at the cost of slower performance, especially when scoring a large number of pairs, as noted in the documentation [C1]. The use of a retriever to generate a smaller set of candidate documents before applying the CrossEncoder helps mitigate this inefficiency [C2].

### Citations

[C1] -> `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`, [C2] -> `chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete and directly supported CrossEncoder trade-off.

# q019

## Question

Describe the path from declaring a FastAPI dependency to receiving its value during a request.

## Reference Answer

A callable declares parameters like a path operation, it is passed to Depends in a dependent function, FastAPI resolves and calls it for each request, and injects its return value while reusing the declarations for validation and documentation.

---

## Dense

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…

### Answer

When you declare a FastAPI dependency, it is typically done using the `Depends` class. This dependency is then used within a *path operation function* by passing it as a parameter. When a request arrives, **FastAPI** will handle the following steps:

1. Call the dependency function with the correct parameters, extracting the data from the request [C2].
2. Get the result from the function.
3. Assign that result to the parameter in your *path operation function* [C2].

This process ensures that the value from the dependency is received and utilized by the *path operation function* during the request.

### Citations

[C2] -> `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct request-time execution and injection, but omits reused validation/documentation declarations.

---

## Hybrid

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…

### Answer

When you declare a FastAPI dependency, you typically use the `Depends` function to specify that a particular function or value is required for a path operation. Here's the path from declaring a dependency to receiving its value during a request:

1. **Declaration**: You declare a dependency by using the `Depends` function, which tells FastAPI that a specific function or value is needed for a path operation. For example, you might have a function that retrieves a database connection or checks for authentication [C3].

2. **Request Arrival**: When a new request arrives at the server, FastAPI starts the process of handling the request by looking at the declared dependencies [C2].

3. **Dependency Execution**: FastAPI calls the dependency function with the correct parameters. This function is designed to provide the required value or perform a specific task, such as fetching data from a database or validating user credentials [C2].

4. **Result Retrieval**: After the dependency function is executed, FastAPI retrieves the result from the function. This result is the value that the dependency was supposed to provide [C2].

5. **Value Injection**: The result from the dependency function is then assigned to the parameter in the path operation function. This means that the value is "injected" into the path operation function, making it available for use within the function [C2].

This process ensures that the path operation function has access to the necessary dependencies, which are provided by the dependency injection system in FastAPI [C3].

### Citations

[C3] -> `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`, [C2] -> `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Covers declaration, execution, result retrieval, and injection with supported examples.

---

## Reranked

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_f42b8d1fcf27f42a881f7ffc0f4664e4f6e7f3dad6183cc8ed5f6db97d9696c9` — that all your *path operation functions* have. You can think of it as a *path operation function* without the "decorator" (without the `@app.get("/some-path")`). And it can return anything you want. In this case, this dependency expects: * An optional query parameter `q` that is a `str`. * An optional query parameter `skip` that is an `int`, and by default is `0`. * An optional query parameter `limit` that is an `int`, and by default is `100`. And then it just returns a `dict` containing those …
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…

### Answer

When you declare a FastAPI dependency, you define a function that will be called by FastAPI when a request is made. This function can take parameters, which can be extracted from the request, such as query parameters, headers, or body data. FastAPI will handle calling this dependency function with the correct parameters and then inject the result into the path operation function. The value from the dependency is then available as a parameter in the path operation function, allowing you to use it in your logic [C3].

### Citations

[C3] -> `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 1
- Requires human review: False

### Notes

Core execution path is correct, but Depends and documentation reuse are omitted and C3 weakly supports the full claim.

# q020

## Question

How do synchronous and asynchronous dependencies interact with path operations, and how are their requirements exposed?

## Reference Answer

FastAPI permits def and async def dependencies with either def or async def path operations, handles their execution, and integrates their declared requirements into OpenAPI and interactive docs.

---

## Dense

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1` — ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request. Actually, all (or most) of the web frameworks work in this same way. You never call those functions directly. They are called by your framework (in this case, **FastAPI**). With the Dependency Injection system, you can also tell **FastAPI** that your *path o…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_fee15b5d598f2287c67e16d13e6154cd0cbfdd3bb62221de78c4c917fea951b6` — ot specific to **FastAPI**. But because **FastAPI** is based on the Python standards, including `Annotated`, you can use this trick in your code. 😎 /// The dependencies will keep working as expected, and the **best part** is that the **type information will be preserved**, which means that your editor will be able to keep providing you with **autocompletion**, **inline errors**, etc. The same for other tools like `mypy`. This will be especially useful when you use it in a **large code base** wh…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_701640dfc97b818a5443785d9a30dc027e8cae69c4a5e7d608792c3237509f31` — when you need to: * Have shared logic (the same code logic again and again). * Share database connections. * Enforce security, authentication, role requirements, etc. * And many other things... All these, while minimizing code repetition. ## First Steps { #first-steps } Let's see a very simple example. It will be so simple that it is not very useful, for now. But this way we can focus on how the **Dependency Injection** system works. ### Create a dependency, or "dependable" { #create-a-dependen…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…

### Answer

Synchronous and asynchronous dependencies can be used interchangeably with path operations in FastAPI. You can declare dependencies with `async def` inside of normal `def` path operation functions, or `def` dependencies inside of `async def` path operation functions [C3]. FastAPI will handle the execution of these dependencies appropriately, ensuring that the correct parameters are extracted from the request and passed to the dependency functions.

The requirements of these dependencies are integrated into the OpenAPI schema, which means that the interactive documentation will include all the information from these dependencies [C1]. This integration allows the dependencies' requirements to be exposed and understood by clients interacting with the API.

### Citations

[C3] -> `chunk_fee15b5d598f2287c67e16d13e6154cd0cbfdd3bb62221de78c4c917fea951b6`, [C1] -> `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 1
- Requires human review: False

### Notes

Correct sync/async and OpenAPI answer; the citation labels are imperfectly associated with their claims.

---

## Hybrid

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_fee15b5d598f2287c67e16d13e6154cd0cbfdd3bb62221de78c4c917fea951b6` — ot specific to **FastAPI**. But because **FastAPI** is based on the Python standards, including `Annotated`, you can use this trick in your code. 😎 /// The dependencies will keep working as expected, and the **best part** is that the **type information will be preserved**, which means that your editor will be able to keep providing you with **autocompletion**, **inline errors**, etc. The same for other tools like `mypy`. This will be especially useful when you use it in a **large code base** wh…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72` — # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to use, and to make it very easy for any developer to integrate other components with **FastAPI**. ## What is "Dependency Injection" { #what-is-dependency-injection } **"Dependency Injection"** means, in programming, that there is a way for your code (in this case,…

### Answer

Synchronous and asynchronous dependencies can interact with path operations in **FastAPI** by using either `def` or `async def` functions. **FastAPI** will handle both types of dependencies appropriately, regardless of whether they are synchronous or asynchronous [C1][C5]. 

The requirements of these dependencies are exposed through the **OpenAPI schema**, which integrates all the request declarations, validations, and requirements of the dependencies (and sub-dependencies) into the same schema. This means that the interactive documentation will have all the information from these dependencies [C1]. 

When a new request arrives, **FastAPI** will call the dependency function with the correct parameters, get the result, and assign it to the parameter in the *path operation function* [C3]. This process is seamless and does not require special registration of dependencies, as **FastAPI** handles it by using the `Depends` function [C3]. 

The use of `Annotated` allows for preserving type information, which is beneficial for autocompletion and inline errors in editors and tools like `mypy` [C4]. 

In summary, **FastAPI** ensures that both synchronous and asynchronous dependencies are properly integrated with path operations and their requirements are exposed through the OpenAPI schema.

### Citations

[C1] -> `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`, [C5] -> `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`, [C3] -> `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`, [C4] -> `chunk_fee15b5d598f2287c67e16d13e6154cd0cbfdd3bb62221de78c4c917fea951b6`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete supported answer, with some extra but relevant dependency details.

---

## Reranked

### Retrieved Context

- [C1] source=`fastapi_dependencies.md` chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85` — ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't matter. **FastAPI** will know what to do. /// note If you don't know, check the [Async: *"In a hurry?"*](../../async.md#in-a-hurry) section about `async` and `await` in the docs. /// ## Integrated with OpenAPI { #integrated-with-openapi } All the request declarat…
- [C2] source=`fastapi_dependencies.md` chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5` — * injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using dependencies it's possible to declare an infinite number of integrations and interactions that become available to your *path operation functions*. And dependencies can be created in a very simple and intuitive way that allows you to just import the Python packages…
- [C3] source=`fastapi_dependencies.md` chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134` — )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, **FastAPI** will take care of: * Calling your dependency ("dependable") function with the correct parameters. * Get the result from your function. * Assign that result to the parameter in your *path operation function*. ```mermaid graph TB common_parameters(["c…
- [C4] source=`fastapi_dependencies.md` chunk_id=`chunk_701640dfc97b818a5443785d9a30dc027e8cae69c4a5e7d608792c3237509f31` — when you need to: * Have shared logic (the same code logic again and again). * Share database connections. * Enforce security, authentication, role requirements, etc. * And many other things... All these, while minimizing code repetition. ## First Steps { #first-steps } Let's see a very simple example. It will be so simple that it is not very useful, for now. But this way we can focus on how the **Dependency Injection** system works. ### Create a dependency, or "dependable" { #create-a-dependen…
- [C5] source=`fastapi_dependencies.md` chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105` — ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection systems * etc. ## Simple and Powerful { #simple-and-powerful } Although the hierarchical dependency injection system is very simple to define and use, it's still very powerful. You can define dependencies that in turn can define dependencies themselves. In the end, …

### Answer

Synchronous and asynchronous dependencies can be used interchangeably with path operations in FastAPI. You can declare synchronous dependencies (`def`) within asynchronous path operation functions (`async def`) and vice versa. FastAPI will handle the execution of these dependencies appropriately, ensuring that the correct parameters are passed and the results are assigned to the path operation function parameters [C1].

The requirements of dependencies, including their validation and requirements, are integrated into the OpenAPI schema. This means that the interactive documentation will display all the information related to these dependencies, making their requirements transparent and accessible [C1].

### Citations

[C1] -> `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

The top chunk supports both cross-style execution and OpenAPI exposure.

# q021

## Question

What practical guidance does the Transformers Pipeline documentation give for deciding whether to batch inference?

## Reference Answer

Benchmark on the target hardware and data, use batch_size only when throughput benefits, account for padding and sequence lengths, and add OOM safeguards because batching can either accelerate or severely degrade inference.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_09006fa517bbcf8d797adaa6324d1032de7f102d6a6d0a7f449c48532886f1e4` — cess data in chunks. - for some data types, a single input (for example, a really long audio file) may need to be chunked into multiple parts before it can be processed - for some tasks, like zero-shot classification or question answering, a single input may need multiple forward passes which can cause issues with the `batch_size` parameter The [ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) clas…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_46d56a255d1e286050a88cffde66dcf5cc823f9a5db6c306c0492336c7c7c29e` — e = Accelerator().device # KeyDataset is a utility that returns the item in the dict returned by the dataset dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=device) for out in pipeline(KeyDataset(dataset, "text"), batch_size=8, truncation="only_first"): print(out) ``` Keep the following general rules of thumb in mind for determin…

### Answer

The Transformers Pipeline documentation provides the following practical guidance for deciding whether to batch inference:

1. The only way to know for sure is to measure performance on your model, data, and hardware [C4].
2. Don't batch inference if you're constrained by latency (a live inference product for example) [C4].
3. Don't batch inference if you're using a CPU [C4].
4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures [C1].

### Citations

[C4] -> `chunk_09006fa517bbcf8d797adaa6324d1032de7f102d6a6d0a7f449c48532886f1e4`, [C1] -> `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Substantially complete benchmark, latency, CPU, sequence-length, and OOM guidance.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_46d56a255d1e286050a88cffde66dcf5cc823f9a5db6c306c0492336c7c7c29e` — e = Accelerator().device # KeyDataset is a utility that returns the item in the dict returned by the dataset dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=device) for out in pipeline(KeyDataset(dataset, "text"), batch_size=8, truncation="only_first"): print(out) ``` Keep the following general rules of thumb in mind for determin…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_56ced0128a5ddf048ad3bb5ed5e8ae3707188daec6694a12610c11fb90edd35c` — worry about the number of forward passes your inputs trigger. Instead, you can optimize `batch_size` independently of the inputs. The example below shows how it differs from [`Pipeline`]. ```py # ChunkPipeline all_model_outputs = [] for preprocessed in pipeline.preprocess(inputs): model_outputs = pipeline.model_forward(preprocessed) all_model_outputs.append(model_outputs) outputs =pipeline.postprocess(all_model_outputs) # Pipeline preprocessed = pipeline.preprocess(inputs) model_outputs = pipel…

### Answer

The Transformers Pipeline documentation provides the following practical guidance for deciding whether to batch inference:

1. The only way to know for sure is to measure performance on your model, data, and hardware [C3].
2. Don't batch inference if you're constrained by latency (e.g., a live inference product) [C3].
3. Don't batch inference if you're using a CPU [C3].
4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures [C3].
5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is [C2].

### Citations

[C3] -> `chunk_46d56a255d1e286050a88cffde66dcf5cc823f9a5db6c306c0492336c7c7c29e`, [C2] -> `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete practical batching decision checklist.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_46d56a255d1e286050a88cffde66dcf5cc823f9a5db6c306c0492336c7c7c29e` — e = Accelerator().device # KeyDataset is a utility that returns the item in the dict returned by the dataset dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=device) for out in pipeline(KeyDataset(dataset, "text"), batch_size=8, truncation="only_first"): print(out) ``` Keep the following general rules of thumb in mind for determin…

### Answer

The Transformers Pipeline documentation provides the following practical guidance for deciding whether to batch inference:

1. The only way to know for sure is to measure performance on your model, data, and hardware [C5].
2. Don't batch inference if you're constrained by latency (a live inference product for example) [C5].
3. Don't batch inference if you're using a CPU [C5].
4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures [C2].
5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is [C2].

### Citations

[C5] -> `chunk_46d56a255d1e286050a88cffde66dcf5cc823f9a5db6c306c0492336c7c7c29e`, [C2] -> `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete practical batching decision checklist.

# q022

## Question

How can Transformers Pipeline place a large model across hardware and reduce its memory requirements?

## Reference Answer

It can use Accelerate device mapping to distribute weights across available devices and lower-precision dtypes such as float16 or bfloat16 when supported to reduce memory use.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3` — especially for larger ones. If your hardware supports it, you can enable torch.bfloat16 instead for more range. > [!TIP] > Inputs are internally converted to torch.float16 and it only works for models with a PyTorch backend. Lastly, [`Pipeline`] also accepts quantized models to reduce memory usage even further. Make sure you have the [bitsandbytes](https://hf.co/docs/bitsandbytes/installation) library installed first, and then add `quantization_config` to `model_kwargs` in the pipeline. ```py i…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_56ced0128a5ddf048ad3bb5ed5e8ae3707188daec6694a12610c11fb90edd35c` — worry about the number of forward passes your inputs trigger. Instead, you can optimize `batch_size` independently of the inputs. The example below shows how it differs from [`Pipeline`]. ```py # ChunkPipeline all_model_outputs = [] for preprocessed in pipeline.preprocess(inputs): model_outputs = pipeline.model_forward(preprocessed) all_model_outputs.append(model_outputs) outputs =pipeline.postprocess(all_model_outputs) # Pipeline preprocessed = pipeline.preprocess(inputs) model_outputs = pipel…

### Answer

Transformers Pipeline can place a large model across hardware and reduce its memory requirements by using quantized models and the `torch.bfloat16` data type. Quantized models reduce memory usage, and `torch.bfloat16` provides a balance between range and memory efficiency [C4]. Additionally, the `device_map="auto"` parameter allows the model to be automatically placed on the appropriate hardware [C4].

### Citations

[C4] -> `chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Covers automatic device mapping and lower-precision/quantized memory reduction.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3` — especially for larger ones. If your hardware supports it, you can enable torch.bfloat16 instead for more range. > [!TIP] > Inputs are internally converted to torch.float16 and it only works for models with a PyTorch backend. Lastly, [`Pipeline`] also accepts quantized models to reduce memory usage even further. Make sure you have the [bitsandbytes](https://hf.co/docs/bitsandbytes/installation) library installed first, and then add `quantization_config` to `model_kwargs` in the pipeline. ```py i…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_56ced0128a5ddf048ad3bb5ed5e8ae3707188daec6694a12610c11fb90edd35c` — worry about the number of forward passes your inputs trigger. Instead, you can optimize `batch_size` independently of the inputs. The example below shows how it differs from [`Pipeline`]. ```py # ChunkPipeline all_model_outputs = [] for preprocessed in pipeline.preprocess(inputs): model_outputs = pipeline.model_forward(preprocessed) all_model_outputs.append(model_outputs) outputs =pipeline.postprocess(all_model_outputs) # Pipeline preprocessed = pipeline.preprocess(inputs) model_outputs = pipel…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_225eb5db3693cb0136dbb65555425525067c8e7c038456a523bd705494271f76` — 00): yield f"My example {i}" pipeline = pipeline(model="openai-community/gpt2", device=0) generated_characters = 0 for out in pipeline(data()): generated_characters += len(out[0]["generated_text"]) ``` ## Large models [Accelerate](https://hf.co/docs/accelerate/index) enables a couple of optimizations for running large models with [`Pipeline`]. Make sure Accelerate is installed first. ```py !pip install -U accelerate ``` The `device_map="auto"` setting is useful for automatically distributing th…

### Answer

Transformers Pipeline can place a large model across hardware and reduce its memory requirements by using the `device_map="auto"` setting, which automatically distributes the model across the fastest devices (GPUs) first before dispatching to other slower devices if available (CPU, hard drive) [C5]. Additionally, it supports half-precision weights (torch.float16), which can be significantly faster and save memory. Performance loss is negligible for most models, especially for larger ones. If your hardware supports it, you can enable torch.bfloat16 instead for more range [C5]. Furthermore, quantized models can be used to reduce memory usage even further, provided the bitsandbytes library is installed [C2].

### Citations

[C5] -> `chunk_225eb5db3693cb0136dbb65555425525067c8e7c038456a523bd705494271f76`, [C2] -> `chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete hardware distribution and precision guidance.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3` — especially for larger ones. If your hardware supports it, you can enable torch.bfloat16 instead for more range. > [!TIP] > Inputs are internally converted to torch.float16 and it only works for models with a PyTorch backend. Lastly, [`Pipeline`] also accepts quantized models to reduce memory usage even further. Make sure you have the [bitsandbytes](https://hf.co/docs/bitsandbytes/installation) library installed first, and then add `quantization_config` to `model_kwargs` in the pipeline. ```py i…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_225eb5db3693cb0136dbb65555425525067c8e7c038456a523bd705494271f76` — 00): yield f"My example {i}" pipeline = pipeline(model="openai-community/gpt2", device=0) generated_characters = 0 for out in pipeline(data()): generated_characters += len(out[0]["generated_text"]) ``` ## Large models [Accelerate](https://hf.co/docs/accelerate/index) enables a couple of optimizations for running large models with [`Pipeline`]. Make sure Accelerate is installed first. ```py !pip install -U accelerate ``` The `device_map="auto"` setting is useful for automatically distributing th…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87` — imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hardware type with the `device` parameter. By default, [`Pipeline`] runs on a CPU which is given by `device=-1`. <hfoptions id="device"> <hfoption id="GPU"> To run [`Pipeline`] on a GPU, set `device` to the associated CUDA device id. For example, `device=0` runs on the first GPU. ``…

### Answer

Transformers Pipeline can place a large model across hardware and reduce its memory requirements by using the `device_map="auto"` setting, which automatically distributes the model across the fastest devices (GPUs) first before dispatching to other slower devices if available (CPU, hard drive) [C3]. Additionally, it supports half-precision weights (torch.float16), which can significantly save memory and improve speed, and for hardware that supports it, torch.bfloat16 can be used for more range [C3]. Furthermore, quantized models can be used to reduce memory usage even further, requiring the installation of the bitsandbytes library and adding `quantization_config` to `model_kwargs` in the pipeline [C1].

### Citations

[C3] -> `chunk_225eb5db3693cb0136dbb65555425525067c8e7c038456a523bd705494271f76`, [C1] -> `chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete device-map, precision, and quantization answer.

# q023

## Question

What steps and configuration are involved in starting Text Embeddings Inference and requesting an embedding?

## Reference Answer

Start the appropriate TEI container with a model ID and mounted cache or model data, expose its port, then POST input text as JSON to the embed endpoint; compatible model IDs or local model directories can be used.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_3f5df0268c752247091a3728d871f54b99d5caeba3db70efd302359a8c6756cc` — -embeddings): CPU-friendly embedding models without attention. - [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors. ## Application Examples You can use this framework for: - **Computing Sentence Embeddings** - [Dense Embeddings](https://www.sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html) - [Sparse Embeddings](https://www…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_30cbd154b92eedaf317578819825a0bf77465f5dc606df6bcc4bf4e679fee357` — ode, Codex, Cursor, Gemini CLI, ...)? Install the [`train-sentence-transformers`](skills/) Hugging Face Agent Skill via `hf skills add train-sentence-transformers [--claude] [--global]` and ask your agent to fine-tune a model on your data. This framework allows you to fine-tune your own sentence embedding methods, so that you get task-specific sentence embeddings. You have various options to choose from in order to get perfect sentence embeddings for your specific task. - Embedding Models - [Se…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_464bc98da7e8879d2635d9eb9580dc9f94c6582d606c2a654f4a90d3c65ddc1d` — cument_embeddings) print(scores) # tensor([[9.6037, 9.4055]]) ``` ## Pre-Trained Models We provide a large list of pretrained models for more than 100 languages. Some models are general purpose models, while others produce embeddings for specific use cases. - [Pretrained Sentence Transformer (Embedding) Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html) - [Pretrained Cross Encoder (Reranker) Models](https://sbert.net/docs/cross_encoder/pretrained_models.html) - [Pretrai…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_b651190dc991598f552ad3b5c19153cb5143cc5b30867ce73d946efe43655fec` — ditionally, it is easy to train or finetune your own [embedding models](https://sbert.net/docs/sentence_transformer/training_overview.html), [reranker models](https://sbert.net/docs/cross_encoder/training_overview.html), [sparse encoder models](https://sbert.net/docs/sparse_encoder/training_overview.html) or [multi-vector encoder models](https://sbert.net/docs/multi_vector_encoder/training_overview.html) using Sentence Transformers, enabling you to create custom models for your specific use cas…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention because TEI startup/request passages are absent from Dense top-5.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0` — ransformers ``` See [Installation](https://www.sbert.net/docs/installation.html) in the docs for uv, conda, source, and editable installs, CUDA setup, and extras (`[image]`, `[audio]`, `[video]`, `[train]`, `[onnx]`, `[openvino]`, `[dev]`). ## Getting Started See [Quickstart](https://www.sbert.net/docs/quickstart.html) in our documentation. ### Embedding Models First download a pretrained embedding a.k.a. Sentence Transformer model. ```python from sentence_transformers import SentenceTransforme…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_5f9769f965866f6b1f7bb94a0cf9a924e7c62e09bb7fc8eb1daaceef465305ff` — inetuning Sparse Embedding Models](https://huggingface.co/blog/train-sparse-encoder): training SPLADE and other sparse encoders. **Multimodal:** - [Multimodal Embedding & Reranker Models](https://huggingface.co/blog/multimodal-sentence-transformers): using text, image, audio, and video models through a single API. - [Training and Finetuning Multimodal Embedding & Reranker Models](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal models, with a Visual Docum…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7` — r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in an air-gapped environment, first download the weights and then mount them inside the container using a volume. For example: ```shell # (Optional) create a `models` directory mkdir models cd models # Make sure you have git-lfs installed (https://git-lfs.com) git lfs install git c…

### Answer

To start Text Embeddings Inference and request an embedding, follow these steps and configuration:

1. **Install the necessary dependencies**: Ensure you have the required software installed, such as the transformers library and any specific CUDA or ROCm setup as needed [C2].

2. **Download a Pretrained Model**: Use the `SentenceTransformer` class to download a pretrained embedding model. For example:
   ```python
   from sentence_transformers import SentenceTransformer
   model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
   ```

3. **Provide Texts to the Model**: Input the texts you want to convert into embeddings:
   ```python
   sentences = [
       "The weather is lovely today.",
       "It's so sunny outside!",
       "He drove to the stadium."
   ]
   ```

4. **Generate Embeddings**: Use the model to generate embeddings for the provided texts:
   ```python
   embeddings = model.encode(sentences)
   print(embeddings.shape)
   # => (3, 384)
   ```

5. **Use the Embeddings**: The generated embeddings can be used for various tasks such as computing similarities:
   ```python
   similarities = model.similarity(embeddings)
   ```

For deployment, you can use the `text-embeddings-inference` toolkit, which allows for high-performance extraction of embeddings and supports various configurations and environments, including air-gapped deployments [C3][C5].

### Citations

[C2] -> `chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0`, [C3] -> `chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`, [C5] -> `chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Answers local SentenceTransformer usage instead of starting TEI and calling its embed endpoint.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7` — r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in an air-gapped environment, first download the weights and then mount them inside the container using a volume. For example: ```shell # (Optional) create a `models` directory mkdir models cd models # Make sure you have git-lfs installed (https://git-lfs.com) git lfs install git c…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_91886f8dfcacd49ebef6dff8176cb02b7e42ce717d47fd6ceeedc343f7d9f183` — lt-api) * [Safetensors](https://github.com/huggingface/safetensors) weight loading * [ONNX](https://github.com/onnx/onnx) weight loading * Production ready (distributed tracing with Open Telemetry, Prometheus metrics) ## Get Started ### Supported Models #### Text Embeddings Text Embeddings Inference currently supports Nomic, BERT, CamemBERT, XLM-RoBERTa models with absolute positions, JinaBERT model with Alibi positions and Mistral, Alibaba GTE, Qwen2 models with Rope positions, MPNet, ModernBE…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_e95404e0b269c82494c202057acd3450571e4e07e555f1b5c7e073cf6746b310` — <div align="center"> # Text Embeddings Inference <a href="https://github.com/huggingface/text-embeddings-inference"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/huggingface/text-embeddings-inference?style=social"> </a> <a href="https://huggingface.github.io/text-embeddings-inference"> <img alt="Swagger API documentation" src="https://img.shields.io/badge/API-Swagger-informational"> </a> A blazing fast inference solution for text embeddings models. Benchmark for [BAAI/b…

### Answer

To start Text Embeddings Inference and request an embedding, follow these steps and configurations:

1. **Docker Deployment**: Use Docker to deploy the Text Embeddings Inference service. The command to run the container is:
   ```shell
   docker run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model
   ```
   This command mounts a volume for the model weights, sets the environment variable for the Hugging Face token, and maps the container's port 80 to the host's port 80 [C3].

2. **Air-Gapped Deployment (Optional)**: If deploying in an air-gapped environment, download the model weights and mount them inside the container using a volume. For example:
   ```shell
   # (Optional) create a `models` directory
   mkdir models
   cd models

   # Make sure you have git-lfs installed (https://git-lfs.com)
   git lfs install
   git clone https://huggingface.co/Qwen/Qwen3-Embedding-0.6B

   # Set the models directory as the volume path
   volume=$PWD

   # Mount the models directory inside the container with a volume and set the model ID
   docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B
   ```
   This ensures the model weights are available within the container [C3].

3. **Requesting an Embedding**: Once the service is running, you can request an embedding by sending a request to the API endpoint. The exact endpoint and method depend on the setup, but typically, you would use a REST API to send the text input and receive the embedding vector in return. The service supports various models, including Qwen3, BERT, CamemBERT, XLM-RoBERTa, and others [C4].

### Citations

[C3] -> `chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7`, [C4] -> `chunk_91886f8dfcacd49ebef6dff8176cb02b7e42ce717d47fd6ceeedc343f7d9f183`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Correct container setup but gives an incorrect port description and never supplies the required embed request.

# q024

## Question

How are reranker models deployed and queried through Text Embeddings Inference?

## Reference Answer

TEI supports sequence-classification cross-encoders as rerankers; launch a compatible reranker model, then POST a query and candidate texts to the rerank endpoint to receive similarity-based ranks.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention; Dense does not retrieve the TEI reranker endpoint passage.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62` — gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re-rankers models are Sequence Classification cross-encoders models with a single class that scores the similarity between a query and a text. See [this blogpost](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by the LlamaIndex tea…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_3119cb0c2a7b12e9cd954a6e8b47d18c24c3626e3d3e791e1573d0435ddfa0da` — shape) # => (3, 384) ``` And that's already it. We now have numpy arrays with the embeddings, one for each text. We can use these to compute similarities. ```python similarities = model.similarity(embeddings, embeddings) print(similarities) # tensor([[1.0000, 0.6660, 0.1046], # [0.6660, 1.0000, 0.1411], # [0.1046, 0.1411, 1.0000]]) ``` ### Reranker Models First download a pretrained reranker a.k.a. Cross Encoder model. ```python from sentence_transformers import CrossEncoder # 1. Load a pretrai…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_865469e0360fadf03d8d8ac585b7cfb077109928466d6666db47fdf7bde73c36` — loss functions](https://www.sbert.net/docs/package_reference/sparse_encoder/losses.html) for sparse embedding models, allowing you to tune models specifically for semantic search, paraphrase mining, semantic similarity comparison, clustering, triplet loss, contrastive loss, etc. ## Companion Blog Posts The following Hugging Face blog posts complement this documentation with narrative walkthroughs and full training examples: **Training guides:** - [Training and Finetuning Embedding Models](https…

### Answer

Reranker models are deployed and queried through Text Embeddings Inference by using the `text-embeddings-inference` tool, which supports these models as Sequence Classification cross-encoders. To deploy a reranker model, you can run a Docker container with the specific model ID, as shown in the example:

```shell
docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model
```

Once deployed, you can query the model to rank the similarity between a query and a list of texts using a `curl` command, such as:

```bash
curl 127.0.0.1:8080/re
```

This process leverages the reranker models to score the similarity between a query and a text, which is essential for improving downstream performance in a RAG (Retrieval-Augmented Generation) pipeline [C2].

### Citations

[C2] -> `chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct deployment concept but the rerank request is truncated and omits the JSON payload.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62` — gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re-rankers models are Sequence Classification cross-encoders models with a single class that scores the similarity between a query and a text. See [this blogpost](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by the LlamaIndex tea…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7` — r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in an air-gapped environment, first download the weights and then mount them inside the container using a volume. For example: ```shell # (Optional) create a `models` directory mkdir models cd models # Make sure you have git-lfs installed (https://git-lfs.com) git lfs install git c…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_f4d2887c85245189307680a3dc340510b9ff3096e825399fac5e4bd4e873d43a` — pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` And then you can rank the similarity between a query and a list of texts with: ```bash curl 127.0.0.1:8080/rerank \ -X POST \ -d '{"query": "What is Deep Learning?", "texts": ["Deep Learning is not...", "Deep learning is..."]}' \ -H 'Content-Type: application/json' ``` ### Using Sequence Classification models You can also use classic Sequence Classification models like `SamLowe/roberta-base-go_emotions`: ``…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…

### Answer

Reranker models are deployed using the `text-embeddings-inference` tool by specifying the model ID with the `--model-id` flag in a Docker run command. For example:

```shell
docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model
```

Once deployed, reranker models can be queried by sending a POST request to the `rerank` endpoint with a JSON payload containing the query and a list of texts:

```bash
curl 127.0.0.1:8080/rerank \
    -X POST \
    -d '{"query": "What is Deep Learning?", "texts": ["Deep Learning is not...", "Deep learning is..."]}' \
    -H 'Content-Type: application/json'
```

This process is detailed in [C1] and [C3].

### Citations

[C1] -> `chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62`, [C3] -> `chunk_f4d2887c85245189307680a3dc340510b9ff3096e825399fac5e4bd4e873d43a`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete Docker launch and POST /rerank example with query and texts.

# q025

## Question

Compare Qdrant's must, should, and must_not filtering clauses.

## Reference Answer

must requires every listed condition like AND, should requires at least one like OR, and must_not requires none of the listed conditions to match; clauses can be combined and nested.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf` — ense, `must_not` is equivalent to the expression `(NOT A) AND (NOT B) AND (NOT C)`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-must-not-filter/" >}} Filtered points would be: ```json [ { "id": 5, "city": "Moscow", "color": "green" }, { "id": 6, "city": "Moscow", "color": "blue" } ] ``` ### Clauses combination It is also possible to use several clauses simultaneously: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-multiple-clau…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1` — ric | Default is `Dot product`, no need to specify it | `Distance` has supported metrics e.g. Dot, Cosine | | Search Type | Always exact in Qdrant | HNSW is an approximate NN | | Return Behaviour | Returns only vectors with non-zero values in the same indices as the query vector | Returns `limit` vectors | In general, the speed of the search is proportional to the number of non-zero values in the query vector. {{< code-snippet path="/documentation/headless/snippets/query-points/sparse-vectors/"…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…

### Answer

Qdrant's filtering clauses `must`, `should`, and `must_not` are used to construct complex boolean expressions for filtering search results. 

- The `must` clause is used to specify conditions that must be met for a document to be included in the results. It is equivalent to the logical AND operation, meaning all conditions in the `must` clause must be satisfied [C3].
- The `should` clause is used to specify conditions that are optional. It is equivalent to the logical OR operation, meaning at least one of the conditions in the `should` clause must be satisfied for a document to be included in the results [C3].
- The `must_not` clause is used to specify conditions that must not be met for a document to be included in the results. It is equivalent to the logical NOT operation, meaning the conditions in the `must_not` clause must be excluded from the results [C3].

These clauses can be combined and nested to create more complex filtering conditions, allowing for precise control over which documents are returned in search results.

### Citations

[C3] -> `chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 1
- Requires human review: False

### Notes

Clause semantics are correct, but one cited chunk does not cleanly support all clauses and nesting is uncited.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf` — ense, `must_not` is equivalent to the expression `(NOT A) AND (NOT B) AND (NOT C)`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-must-not-filter/" >}} Filtered points would be: ```json [ { "id": 5, "city": "Moscow", "color": "green" }, { "id": 6, "city": "Moscow", "color": "blue" } ] ``` ### Clauses combination It is also possible to use several clauses simultaneously: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-multiple-clau…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8` — ide `should` is satisfied. In this sense, `should` is equivalent to the operator `OR`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-should-filter/" >}} Filtered points would be: ```json [ { "id": 1, "city": "London", "color": "green" }, { "id": 2, "city": "London", "color": "red" }, { "id": 3, "city": "London", "color": "blue" }, { "id": 4, "city": "Berlin", "color": "red" } ] ``` <aside role="status">If all conditions inside <code>should</code> target the…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_09e6d8556030eaaddb06afe2568a4ba025b04a46d5a8b30b1a163c800da4000a` — he following payload: ```json [ { "id": 1, "city": "London", "color": "green" }, { "id": 2, "city": "London", "color": "red" }, { "id": 3, "city": "London", "color": "blue" }, { "id": 4, "city": "Berlin", "color": "red" }, { "id": 5, "city": "Moscow", "color": "green" }, { "id": 6, "city": "Moscow", "color": "blue" } ] ``` ### Must When using `must`, the clause becomes `true` only if every condition listed inside `must` is satisfied. In this sense, `must` is equivalent to the operator `AND`. Ex…

### Answer

Qdrant's filtering clauses `must`, `should`, and `must_not` are used to define conditions for filtering search results. 

- `must` requires all conditions within it to be satisfied for a point to be included in the results. It is equivalent to the logical `AND` operator [C5].
- `should` requires at least one condition within it to be satisfied for a point to be included in the results. It is equivalent to the logical `OR` operator [C4].
- `must_not` requires that none of the conditions within it are satisfied for a point to be included in the results. It is equivalent to the logical expression `(NOT A) AND (NOT B) AND (NOT C)` [C3].

### Citations

[C5] -> `chunk_09e6d8556030eaaddb06afe2568a4ba025b04a46d5a8b30b1a163c800da4000a`, [C4] -> `chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8`, [C3] -> `chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Each clause is correctly described and tied to its supporting chunk.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf` — ense, `must_not` is equivalent to the expression `(NOT A) AND (NOT B) AND (NOT C)`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-must-not-filter/" >}} Filtered points would be: ```json [ { "id": 5, "city": "Moscow", "color": "green" }, { "id": 6, "city": "Moscow", "color": "blue" } ] ``` ### Clauses combination It is also possible to use several clauses simultaneously: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-multiple-clau…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8` — ide `should` is satisfied. In this sense, `should` is equivalent to the operator `OR`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-should-filter/" >}} Filtered points would be: ```json [ { "id": 1, "city": "London", "color": "green" }, { "id": 2, "city": "London", "color": "red" }, { "id": 3, "city": "London", "color": "blue" }, { "id": 4, "city": "Berlin", "color": "red" } ] ``` <aside role="status">If all conditions inside <code>should</code> target the…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_10f7f680ea1f254d70ca96b95847982ed72e3c166d190625d6967dcf39eb46ca` — s://qdrant.tech/documentation"`, but the prefix `"qdrant"` does not. Matching is byte-wise and, for valid UTF-8 strings, therefore character-wise. It is also case-sensitive, consistent with exact keyword matching. Unlike [Full Text Match](#full-text-match), prefix matching does not tokenize the value, so it is well suited to identifiers such as URLs, paths, or SKUs. {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-prefix/" >}} <aside role="status"> For efficient pr…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…

### Answer

Qdrant's filtering clauses `must`, `should`, and `must_not` are used to define conditions for filtering search results. Here's a comparison:

1. **`must`**: This clause is used to specify conditions that must be satisfied for a point to be included in the results. It is equivalent to the logical AND operator, meaning all conditions within `must` must be true for the point to be included [C1][C3].

2. **`should`**: This clause is used to specify conditions that should be satisfied, but it is equivalent to the logical OR operator. This means that at least one of the conditions within `should` needs to be true for the point to be included in the results [C3].

3. **`must_not`**: This clause is used to specify conditions that must not be satisfied. It is equivalent to the logical NOT operator applied to each condition within `must_not`, meaning all conditions within `must_not` must be false for the point to be included in the results [C1][C3].

These clauses can be combined and nested to create complex filtering conditions, allowing for precise control over which points are returned in search results.

### Citations

[C1] -> `chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`, [C3] -> `chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 1
- Requires human review: False

### Notes

Clause descriptions are correct, but the combined/nested conclusion is uncited and must has weak label support.

# q026

## Question

How does Qdrant filter nested fields and ensure conditions match within one array element?

## Reference Answer

Dot notation addresses nested fields and [] projects values through arrays, while a nested object filter scopes all conditions to each individual array element and accepts a parent when one element satisfies them together.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_625dbbbce9ff475c8863acc78c17fc93bedc3acfc3bf2c918b454a251ecee22e` — city`, `village`, and `town`: {{< code-snippet path="/documentation/headless/snippets/query-points/with-payload-fields/" >}} Or use `include` or `exclude` explicitly. For example, to exclude `city`: {{< code-snippet path="/documentation/headless/snippets/query-points/exclude-fields/" >}} It is possible to target nested fields using a dot notation: * `payload.nested_field` - for a nested field * `payload.nested_array[].sub_field` - for projecting nested fields within an array Accessing array ele…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_f7e4ff6b3c3147768eeb0567eedef8dd535e0f817e38fc408358ca8e6bb7f065` — ippets/filter-condition/slice/" >}} Slicing is based on a hash of the point IDs. A point matches slice `index` of `total` if `hash(id) % total == index`. For a fixed `total`, slices `0` through `total - 1` are disjoint and together cover every point in the collection. The hash is [SipHash-2-4](https://en.wikipedia.org/wiki/SipHash) with a zero key over the ID bytes, and it won't change across Qdrant versions. Slices with different `total` values are correlated, so slice `0` of `total: 4` is alw…

### Answer

Qdrant filters nested fields by applying the filter to each element of the array individually. A parent document is considered to match the condition if at least one element of the array matches the nested filter [C5]. This approach ensures that conditions are checked against each array element, allowing for precise filtering even with nested data structures.

### Citations

[C5] -> `chunk_f7e4ff6b3c3147768eeb0567eedef8dd535e0f817e38fc408358ca8e6bb7f065`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 0
- Requires human review: True

### Notes

Explains element-level matching but omits dot/array notation; the emitted citation points to a slicing chunk rather than nested filtering.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_625dbbbce9ff475c8863acc78c17fc93bedc3acfc3bf2c918b454a251ecee22e` — city`, `village`, and `town`: {{< code-snippet path="/documentation/headless/snippets/query-points/with-payload-fields/" >}} Or use `include` or `exclude` explicitly. For example, to exclude `city`: {{< code-snippet path="/documentation/headless/snippets/query-points/exclude-fields/" >}} It is possible to target nested fields using a dot notation: * `payload.nested_field` - for a nested field * `payload.nested_array[].sub_field` - for projecting nested fields within an array Accessing array ele…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_1171fd126b59204972d153645236057db9c263eee8ad304b7407cd897ac5b7f7` — /documentation/manage-data/payload/#keyword) and [integer](/documentation/manage-data/payload/#integer) payloads. Example: {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-except/" >}} In this example, the condition will be satisfied if the stored value is neither `black` nor `yellow`. If the stored value is an array, it should have at least one value not matching any of the given values. E.g. if the stored value is `["black", "green"]`, the condition will be satis…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_a282621a2723161981f462410af989360fd12b0422e4b4d47eb1b61c07d923be` — ightseeing. ### Nested object filter *Available as of v1.2.0* By default, the conditions are taking into account the entire payload of a point. For instance, given two points with the following payload: ```json [ { "id": 1, "dinosaur": "t-rex", "diet": [ { "food": "leaves", "likes": false}, { "food": "meat", "likes": true} ] }, { "id": 2, "dinosaur": "diplodocus", "diet": [ { "food": "leaves", "likes": true}, { "food": "meat", "likes": false} ] } ] ``` The following query would match both point…

### Answer

Qdrant filters nested fields by allowing conditions to be applied to specific nested fields using a dot notation, such as `payload.nested_field` or `payload.nested_array[].sub_field` [C2]. When applying conditions to array elements, Qdrant considers a parent document to match if at least one element of the array matches the nested filter [C1]. This means that for an array, the filter checks each element individually, and the document is considered a match if any element satisfies the condition.

### Citations

[C2] -> `chunk_625dbbbce9ff475c8863acc78c17fc93bedc3acfc3bf2c918b454a251ecee22e`, [C1] -> `chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Substantially answers notation and per-element scope, but the dot-notation citation source is weak and the same-element guarantee is implicit.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b` — rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array matches the nested filter. **Limitations** The `has_id` and `slice` conditions are not supported within the nested object filter. If you need them, place them in an adjacent `must` clause. {{< code-snippet path="/documentation/headless/snippets/scroll-points/w…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_3af51a31bbbc0f3575860a94af5242bdcc036b967b34a316676f6be760688823` — and likes=true on `diet[1].likes` - the "diplodocus" matches food=meat on `diet[1].food` and likes=true on `diet[0].likes` To retrieve only the points which are matching the conditions on an array element basis, that is the point with id 1 in this example, you would need to use a nested object filter. Nested object filters allow arrays of objects to be queried independently of each other. It is achieved by using the `nested` condition type formed by a payload key to focus on and a filter to app…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C5] source=`qdrant_filtering.md` chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c` — uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter on. For best results, create payload indexes before ingesting data. Refer to <a href="/documentation/manage-data/indexing/#create-a-payload-index">Create a Payload Index</a> for more information. </aside> ## Filtering clauses Qdrant allows you to combine cond…

### Answer

Qdrant filters nested fields by applying the nested filter to each element of the array individually. A parent document is considered to match the condition if at least one element of the array matches the nested filter [C2]. The matching logic is modified to be applied at the level of an array element within the payload [C2]. This ensures that conditions are checked against each array element independently.

### Citations

[C2] -> `chunk_3af51a31bbbc0f3575860a94af5242bdcc036b967b34a316676f6be760688823`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct same-element nested logic but omits dot notation and [] projection.

# q027

## Question

How can Qdrant group chunk-level search hits by document and attach document-level metadata without duplicating it on every chunk?

## Reference Answer

Store document_id on chunk points, group search hits by that field, keep titles or abstracts once in a separate document collection, and use with_lookup to attach the matching document payload.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_4fe8478599f5a15a745adb4be67947689f6bd8245b325b5b9072d4c30b81880e` — * Only [keyword](/documentation/manage-data/payload/#keyword) and [integer](/documentation/manage-data/payload/#integer) payload values are supported for the `group_by` parameter. Payload values with other types will be ignored. * At the moment, pagination is not enabled when using **groups**, so the `offset` parameter is not allowed. ### Lookup in Groups When the points in a group share large fields like titles, abstracts, or full document vectors, copying that data onto every point inflates s…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb` — <aside role="status">Store only document-level metadata (e.g., titles, abstracts) in the lookup collection, not chunks or duplicated data.</aside> Set up the two collections. `chunks` holds one point per chunk with its own vector. `documents` holds one point per document with payload only. The payload index on `document_id` lets `group_by` work on that field. {{< code-snippet path="/documentation/headless/snippets/query-groups/with-lookup-setup/" >}} Ingest both collections, with `documents` po…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_c9d85bcf5b9d79c7deb8d237e25898f0f93356fa3af0634a80440df11edb9653` — --- title: Hybrid Queries short_description: "Combine dense, sparse, and multivector queries in Qdrant with hybrid search, weighted RRF tuning, DBSF, and multi-stage rescoring with Formula Query." description: "Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer custom scoring with Formula Query, and pick the right method for your data." weight: 15 cta: "Run hybrid queries on a free Cloud cluster." aliases: - ../hybrid-queries hideInSidebar: false -…

### Answer

Qdrant can group chunk-level search hits by document and attach document-level metadata without duplicating it on every chunk by using the `with_lookup` feature. This involves setting up two collections: `chunks` and `documents`. The `chunks` collection holds one point per chunk with its own vector, while the `documents` collection holds one point per document with payload only. The payload index on `document_id` allows the `group_by` parameter to work on that field. The lookup is a plain join by point id, not a vector search, which means the `documents` collection must already contain a point whose id matches the `group_by` value from each chunk [C1][C2].

### Citations

[C1] -> `chunk_4fe8478599f5a15a745adb4be67947689f6bd8245b325b5b9072d4c30b81880e`, [C2] -> `chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete two-collection, group_by, and with_lookup design.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_4fe8478599f5a15a745adb4be67947689f6bd8245b325b5b9072d4c30b81880e` — * Only [keyword](/documentation/manage-data/payload/#keyword) and [integer](/documentation/manage-data/payload/#integer) payload values are supported for the `group_by` parameter. Payload values with other types will be ignored. * At the moment, pagination is not enabled when using **groups**, so the `offset` parameter is not allowed. ### Lookup in Groups When the points in a group share large fields like titles, abstracts, or full document vectors, copying that data onto every point inflates s…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb` — <aside role="status">Store only document-level metadata (e.g., titles, abstracts) in the lookup collection, not chunks or duplicated data.</aside> Set up the two collections. `chunks` holds one point per chunk with its own vector. `documents` holds one point per document with payload only. The payload index on `document_id` lets `group_by` work on that field. {{< code-snippet path="/documentation/headless/snippets/query-groups/with-lookup-setup/" >}} Ingest both collections, with `documents` po…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_80975e17bfc65b11fe528eebb42f08b825e4c5e9e5b78fc487cd65a97795d8ce` — "title": "Document B", "text": "This is document B" } } } ] }, "status": "ok", "time": 0.001 } ``` For a collection of 20 000 documents with around 24 chunks each, duplicating ~3 KB of document-level data on every chunk adds up to ~1.4 GB. Storing those fields once per document in the `documents` collection brings that down to ~60 MB. The split pays off when the shared fields are large or change often, since updating one point in `documents` shows up under every chunk's group at query time. ## …
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_87346f39468b342c5af8df04c039b2317abfb529aee8e4a69504c1c523bc4067` — ` value from each chunk. - The id types must match. A string `group_by` value against integer point ids returns an empty `lookup` field with no error. - Group ids without a matching point in `documents` get an empty `lookup` field. Query the `chunks` collection with `group_by="document_id"` and `with_lookup` pointing at the `documents` collection: {{< code-snippet path="/documentation/headless/snippets/query-groups/with-lookup/" >}} You can also pass `with_lookup="documents"` as a shorthand. It…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_76f1595996b9fc24a98741c470092b714dbcc142a4d3e31b2ed722e1ab00d59a` — en you have multiple points for the same item, and you want to avoid redundancy of the same item in the results. For example, if you have a large document split into multiple chunks, and you want to search or [recommend](/documentation/search/explore/#recommendation-api) on a per-document basis, you can group the results by the document ID. Consider having points with the following payloads: ```json [ { "id": 0, "payload": { "chunk_part": 0, "document_id": "a" }, "vector": [0.91] }, { "id": 1, …

### Answer

Qdrant can group chunk-level search hits by document and attach document-level metadata without duplicating it on every chunk by using the `with_lookup` feature. This involves setting up two collections: `chunks` and `documents`. The `chunks` collection holds one point per chunk with its own vector, while the `documents` collection holds one point per document with payload only. The payload index on `document_id` allows the `group_by` parameter to work on that field. When querying the `chunks` collection with `group_by="document_id"` and `with_lookup` pointing at the `documents` collection, the document-level metadata is attached to each group at query time, avoiding duplication [C1][C2].

### Citations

[C1] -> `chunk_4fe8478599f5a15a745adb4be67947689f6bd8245b325b5b9072d4c30b81880e`, [C2] -> `chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete design and query-time metadata attachment.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_80975e17bfc65b11fe528eebb42f08b825e4c5e9e5b78fc487cd65a97795d8ce` — "title": "Document B", "text": "This is document B" } } } ] }, "status": "ok", "time": 0.001 } ``` For a collection of 20 000 documents with around 24 chunks each, duplicating ~3 KB of document-level data on every chunk adds up to ~1.4 GB. Storing those fields once per document in the `documents` collection brings that down to ~60 MB. The split pays off when the shared fields are large or change often, since updating one point in `documents` shows up under every chunk's group at query time. ## …
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb` — <aside role="status">Store only document-level metadata (e.g., titles, abstracts) in the lookup collection, not chunks or duplicated data.</aside> Set up the two collections. `chunks` holds one point per chunk with its own vector. `documents` holds one point per document with payload only. The payload index on `document_id` lets `group_by` work on that field. {{< code-snippet path="/documentation/headless/snippets/query-groups/with-lookup-setup/" >}} Ingest both collections, with `documents` po…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_6233fd013f990d7e934e558a3374c2e58d2cb5e47aa09191ace849a4ac11ab75` — ument_id": "a" }, "vector": [0.2] }, { "id": 3, "payload": { "chunk_part": 0, "document_id": 123 }, "vector": [0.79] }, { "id": 4, "payload": { "chunk_part": 1, "document_id": 123 }, "vector": [0.75] }, { "id": 5, "payload": { "chunk_part": 0, "document_id": -10 }, "vector": [0.6] } ] ``` With the ***groups*** API, you will be able to get the best *N* points for each document, assuming that the payload of the points contains the document ID. Of course there will be times where the best *N* poin…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_87346f39468b342c5af8df04c039b2317abfb529aee8e4a69504c1c523bc4067` — ` value from each chunk. - The id types must match. A string `group_by` value against integer point ids returns an empty `lookup` field with no error. - Group ids without a matching point in `documents` get an empty `lookup` field. Query the `chunks` collection with `group_by="document_id"` and `with_lookup` pointing at the `documents` collection: {{< code-snippet path="/documentation/headless/snippets/query-groups/with-lookup/" >}} You can also pass `with_lookup="documents"` as a shorthand. It…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_2708bfc1f2558ba508fbc71be5215b20208226980988cc254fd48fdb31bf23b9` — its `document_id` payload is an array (`[200, 201]`), placing the chunk into every matching group. ```json { "result": { "groups": [ { "id": 200, "hits": [ { "id": 0, "score": 0.91 }, { "id": 1, "score": 0.85 } ], "lookup": { "id": 200, "payload": { "title": "Document A", "text": "This is document A" } } }, { "id": 201, "hits": [ { "id": 1, "score": 0.85 } ], "lookup": { "id": 201, "payload": { "title": "Document B", "text": "This is document B" } } } ] }, "status": "ok", "time

### Answer

Qdrant groups chunk-level search hits by document and attaches document-level metadata without duplicating it on every chunk by using a lookup collection. Specifically, you set up two collections: `chunks` and `documents`. The `chunks` collection holds one point per chunk with its own vector, while the `documents` collection holds one point per document with only the payload (such as titles and abstracts). The payload index on `document_id` in the `documents` collection allows the `group_by` functionality to work on that field. When querying, you use the `group_by="document_id"` parameter with `with_lookup` pointing to the `documents` collection, which retrieves the document-level metadata for each group of chunk-level search hits [C2][C4].

### Citations

[C2] -> `chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb`, [C4] -> `chunk_87346f39468b342c5af8df04c039b2317abfb529aee8e4a69504c1c523bc4067`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Mostly correct but places the document_id payload index on the documents collection rather than the chunk points being grouped.

# q028

## Question

How does Qdrant use prefetches for a coarse-to-fine multi-stage search?

## Reference Answer

Prefetch subqueries first produce candidates using cheaper or smaller representations, and the main query then scores or rescoring those candidates with a more accurate representation; prefetch limits must supply enough candidates.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_c9d85bcf5b9d79c7deb8d237e25898f0f93356fa3af0634a80440df11edb9653` — --- title: Hybrid Queries short_description: "Combine dense, sparse, and multivector queries in Qdrant with hybrid search, weighted RRF tuning, DBSF, and multi-stage rescoring with Formula Query." description: "Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer custom scoring with Formula Query, and pick the right method for your data." weight: 15 cta: "Run hybrid queries on a free Cloud cluster." aliases: - ../hybrid-queries hideInSidebar: false -…
- [C3] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225` — get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vectors. <aside role="status">Disable the HNSW index for vectors used only for rescoring by setting <code>m=0</code> in the vector's HNSW configuration. Rescoring does not use the HNSW index, so disabling it will free up memory.</aside> ### Re-Scoring Examples Fetch 1000 results us…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…

### Answer

Qdrant uses prefetches for a coarse-to-fine multi-stage search by enabling sub-requests through the `prefetch` parameter. Specifically, whenever a query has at least one prefetch, Qdrant performs the prefetch query (or queries) first, and then applies the main query over the results of its prefetch(es). Prefetches can have prefetches themselves, allowing for nested prefetches. This mechanism allows for a multi-stage search where initial coarse results are fetched, and then refined with more detailed queries [C1].

### Citations

[C1] -> `chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Explains prefetch then main-query refinement but omits cheaper representations and prefetch limit requirements.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_c9d85bcf5b9d79c7deb8d237e25898f0f93356fa3af0634a80440df11edb9653` — --- title: Hybrid Queries short_description: "Combine dense, sparse, and multivector queries in Qdrant with hybrid search, weighted RRF tuning, DBSF, and multi-stage rescoring with Formula Query." description: "Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer custom scoring with Formula Query, and pick the right method for your data." weight: 15 cta: "Run hybrid queries on a free Cloud cluster." aliases: - ../hybrid-queries hideInSidebar: false -…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225` — get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vectors. <aside role="status">Disable the HNSW index for vectors used only for rescoring by setting <code>m=0</code> in the vector's HNSW configuration. Rescoring does not use the HNSW index, so disabling it will free up memory.</aside> ### Re-Scoring Examples Fetch 1000 results us…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728` — expensive to compute. Splitting the search into two stages is a known technique to mitigate this effect: - First, use a smaller and cheaper representation to get a large list of candidates. - Then, re-score the candidates using the larger and more accurate representation. There are a few ways to build search architectures around this idea: - The quantized vectors as a first stage, and the full-precision vectors as a second stage. - Leverage Matryoshka Representation Learning (<a href=https://ar…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c` — on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/documentation/headless/snippets/query-points/score-boost-tags/" >}} There are multiple expressions available. Check the [API docs for specific details](https://api.qdrant.tech/v-1-14-x/api-reference/search/query-points#request.body.query.Query%20Interface.Query.Formul…

### Answer

Qdrant uses prefetches for a coarse-to-fine multi-stage search by first fetching a large list of candidate results using a smaller and cheaper representation, and then re-scoring these candidates using a larger and more accurate representation. This is achieved by setting the `prefetch` parameter, which allows making sub-requests. The main query is applied over the results of its prefetch(es), and prefetches can have their own prefetches, enabling nested prefetches [C1][C4]. Additionally, the `offset` parameter only affects the main query, meaning that the prefetches must have a `limit` of at least `limit + offset` of the main query to avoid getting an empty result [C1].

### Citations

[C1] -> `chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7`, [C4] -> `chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete coarse-to-fine and limit-plus-offset explanation.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225` — get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vectors. <aside role="status">Disable the HNSW index for vectors used only for rescoring by setting <code>m=0</code> in the vector's HNSW configuration. Rescoring does not use the HNSW index, so disabling it will free up memory.</aside> ### Re-Scoring Examples Fetch 1000 results us…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_c9d85bcf5b9d79c7deb8d237e25898f0f93356fa3af0634a80440df11edb9653` — --- title: Hybrid Queries short_description: "Combine dense, sparse, and multivector queries in Qdrant with hybrid search, weighted RRF tuning, DBSF, and multi-stage rescoring with Formula Query." description: "Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer custom scoring with Formula Query, and pick the right method for your data." weight: 15 cta: "Run hybrid queries on a free Cloud cluster." aliases: - ../hybrid-queries hideInSidebar: false -…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c` — on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/documentation/headless/snippets/query-points/score-boost-tags/" >}} There are multiple expressions available. Check the [API docs for specific details](https://api.qdrant.tech/v-1-14-x/api-reference/search/query-points#request.body.query.Query%20Interface.Query.Formul…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728` — expensive to compute. Splitting the search into two stages is a known technique to mitigate this effect: - First, use a smaller and cheaper representation to get a large list of candidates. - Then, re-score the candidates using the larger and more accurate representation. There are a few ways to build search architectures around this idea: - The quantized vectors as a first stage, and the full-precision vectors as a second stage. - Leverage Matryoshka Representation Learning (<a href=https://ar…

### Answer

Qdrant uses prefetches for a coarse-to-fine multi-stage search by enabling sub-requests that fetch initial results (coarse) and then refine them with more accurate or detailed queries (fine). Specifically, whenever a query has at least one prefetch, Qdrant performs the prefetch query (or queries) first, and then applies the main query over the results of its prefetch(es) [C1]. This allows for a layered approach where initial, less computationally intensive searches are conducted to get a large list of candidate results, which are then re-scored using more accurate or detailed representations [C5]. The use of prefetches can be nested, allowing for complex, multi-stage search processes [C1].

### Citations

[C1] -> `chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7`, [C5] -> `chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct coarse-to-fine flow but omits required candidate-limit sizing.

# q029

## Question

How should query and document encoding differ for symmetric versus asymmetric semantic search?

## Reference Answer

Symmetric search uses similarly sized query and corpus texts, while asymmetric search maps short queries to longer answer passages; recommended models may use encode_query and encode_document so prompts and routing reflect those roles.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0` — ## Symmetric vs. Asymmetric Semantic Search A **critical distinction** for your setup is *symmetric* vs. *asymmetric semantic search*: - For **symmetric semantic search** your query and the entries in your corpus are of about the same length and have the same amount of content. An example would be searching for similar questions: Your query could for example be *"How to learn Python online?"* and you want to find an entry like *"How to learn Python on the web?"*. For symmetric tasks, you could …
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69` — **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and you want to find the paragraph *"Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy ..."*. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense. - Related training example: [MS M…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_62596d162f72d39a62714058316f7eb1a0267f72501b85a8e0e03255e16d13d2` — lgbJWkIMT0xJH6PWF1?usp=sharing) ]: This example uses a model that was trained on the [Natural Questions dataset](https://huggingface.co/datasets/sentence-transformers/natural-questions). It consists of about 100k real Google search queries, together with an annotated passage from Wikipedia that provides the answer. It is an example of an **asymmetric search task**. As corpus, we use the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) so that it fits easily into m…

### Answer

For symmetric semantic search, the query and document encoding should be similar in terms of length and content, allowing for the possibility of flipping the query and documents. This means using models that can effectively encode both queries and documents into a shared vector space [C2]. 

For asymmetric semantic search, the query is typically short, and the documents are longer. Therefore, the encoding should reflect this difference, with the query encoded using a method that is suitable for short inputs and the documents encoded using a method that can handle longer texts. This is often achieved by using specialized methods for encoding queries and documents, such as `encode_query` for queries and `encode_document` for documents [C4].

### Citations

[C2] -> `chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0`, [C4] -> `chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct symmetric/asymmetric roles and encode_query/encode_document guidance.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0` — ## Symmetric vs. Asymmetric Semantic Search A **critical distinction** for your setup is *symmetric* vs. *asymmetric semantic search*: - For **symmetric semantic search** your query and the entries in your corpus are of about the same length and have the same amount of content. An example would be searching for similar questions: Your query could for example be *"How to learn Python online?"* and you want to find an entry like *"How to learn Python on the web?"*. For symmetric tasks, you could …
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69` — **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and you want to find the paragraph *"Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy ..."*. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense. - Related training example: [MS M…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C5] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949` — [semantic search](../semantic-search/README.md)). Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cross-Encoder are presented to the user. * **[in_document_search_crossencoder.py](in_document_search_crossencoder.py):** If you only have a small set of paragraphs, we don't do the retrieval stage. This is for example the case if you want to perform search within a single document. In this example, we take the Wikipedia artic…

### Answer

For **symmetric semantic search**, the query and documents should be encoded using models that treat both equally, typically producing sentence or paragraph embeddings that capture the semantic meaning of both the query and the documents [C1]. This allows for similarity computation between the query and documents.

For **asymmetric semantic search**, the query is usually short, and the documents are longer. Therefore, it is recommended to use different encoding methods: use `encode_query` for queries and `encode_document` for documents to ensure appropriate representation for their respective roles [C3]. This distinction helps maintain the relevance and accuracy of search results.

### Citations

[C1] -> `chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0`, [C3] -> `chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete role-sensitive encoding explanation.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0` — ## Symmetric vs. Asymmetric Semantic Search A **critical distinction** for your setup is *symmetric* vs. *asymmetric semantic search*: - For **symmetric semantic search** your query and the entries in your corpus are of about the same length and have the same amount of content. An example would be searching for similar questions: Your query could for example be *"How to learn Python online?"* and you want to find an entry like *"How to learn Python on the web?"*. For symmetric tasks, you could …
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69` — **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and you want to find the paragraph *"Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy ..."*. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense. - Related training example: [MS M…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…

### Answer

For symmetric semantic search, the query and document encoding should be done using the same model, as both are of similar length and content [C1]. For asymmetric semantic search, the query and document encoding should use different methods, with the query encoded using `encode_query` and documents encoded using `encode_document` to maintain the distinction between short queries and longer documents [C3].

### Citations

[C1] -> `chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0`, [C3] -> `chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete and directly supported encoding distinction.

# q030

## Question

What options does Sentence Transformers describe for scaling semantic search beyond a manual in-memory implementation?

## Reference Answer

Use the optimized semantic_search utility for suitable corpora, keep query and corpus embeddings on the same GPU when possible, or use approximate-nearest-neighbor/vector systems such as FAISS, Annoy, HNSWlib, Elasticsearch, or OpenSearch for larger corpora.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_62596d162f72d39a62714058316f7eb1a0267f72501b85a8e0e03255e16d13d2` — lgbJWkIMT0xJH6PWF1?usp=sharing) ]: This example uses a model that was trained on the [Natural Questions dataset](https://huggingface.co/datasets/sentence-transformers/natural-questions). It consists of about 100k real Google search queries, together with an annotated passage from Wikipedia that provides the answer. It is an example of an **asymmetric search task**. As corpus, we use the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) so that it fits easily into m…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_55f82d46216116757678b11d0a5de037a2a07f4d430e9e19af78ef0d8d207221` — nswlib/). Examples: - [semantic_search_quora_hnswlib.py](semantic_search_quora_hnswlib.py) - [semantic_search_quora_annoy.py](semantic_search_quora_annoy.py) - [semantic_search_quora_faiss.py](semantic_search_quora_faiss.py) ## Retrieve & Re-Rank For complex semantic search scenarios, a two-stage retrieve & re-rank pipeline is advisable: ![InformationRetrieval](https://raw.githubusercontent.com/huggingface/sentence-transformers/main/docs/img/InformationRetrieval.png) For further details, see [R…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_293b419bb31d44e5b59d6b65009b2708fa24711d3372d2db12d3ea963c260721` — ased on artificial neural networks with representation learning. .. literalinclude:: semantic_search.py ``` ## Optimized Implementation ```{eval-rst} Instead of implementing semantic search by yourself, you can use the :func:`~sentence_transformers.util.semantic_search` function. ``` The function accepts the following parameters: ```{eval-rst} .. autofunction:: sentence_transformers.util.semantic_search ``` By default, up to 100 queries are processed in parallel. Further, the corpus is chunked …
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a` — mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>` as well as for our query with :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>`, and then calculating the `semantic textual similarity <../../../../docs/sentence_transformer/usage/semantic_textual_simil…

### Answer

Sentence Transformers describe two main options for scaling semantic search beyond a manual in-memory implementation:

1. **Using vector engines**: This involves using tools like Elasticsearch for lexical search, which can handle large-scale retrieval tasks [C1].
2. **Dense retrieval with representation learning**: This approach uses models trained on large datasets, such as the Natural Questions dataset, to perform dense retrieval, which is more effective for complex search tasks [C2].

### Citations

[C1] -> `chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10`, [C2] -> `chunk_62596d162f72d39a62714058316f7eb1a0267f72501b85a8e0e03255e16d13d2`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Answers lexical versus dense retrieval rather than the documented scaling options.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a` — mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>` as well as for our query with :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>`, and then calculating the `semantic textual similarity <../../../../docs/sentence_transformer/usage/semantic_textual_simil…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485` — , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` module, it will use the "query" or "document" task type to route the input through the appropriate submodules. Note that :meth:`SentenceTransformer.encode <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode>` is the most general method and can be used for any…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_293b419bb31d44e5b59d6b65009b2708fa24711d3372d2db12d3ea963c260721` — ased on artificial neural networks with representation learning. .. literalinclude:: semantic_search.py ``` ## Optimized Implementation ```{eval-rst} Instead of implementing semantic search by yourself, you can use the :func:`~sentence_transformers.util.semantic_search` function. ``` The function accepts the following parameters: ```{eval-rst} .. autofunction:: sentence_transformers.util.semantic_search ``` By default, up to 100 queries are processed in parallel. Further, the corpus is chunked …

### Answer

Sentence Transformers describes two main options for scaling semantic search beyond a manual in-memory implementation:

1. **Lexical Search**: This involves using vector engines like Elasticsearch for lexical search, which looks for literal matches of the query words in the document collection [C4].

2. **Dense Retrieval (Semantic Search)**: This involves using a bi-encoder implemented in Sentence Transformers, which encodes the search query into vector space and retrieves document embeddings that are close in vector space, overcoming the shortcomings of lexical search [C4].

### Citations

[C4] -> `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Also answers retrieval-method choice instead of semantic_search, GPU placement, and ANN systems.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_293b419bb31d44e5b59d6b65009b2708fa24711d3372d2db12d3ea963c260721` — ased on artificial neural networks with representation learning. .. literalinclude:: semantic_search.py ``` ## Optimized Implementation ```{eval-rst} Instead of implementing semantic search by yourself, you can use the :func:`~sentence_transformers.util.semantic_search` function. ``` The function accepts the following parameters: ```{eval-rst} .. autofunction:: sentence_transformers.util.semantic_search ``` By default, up to 100 queries are processed in parallel. Further, the corpus is chunked …
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a` — mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>` as well as for our query with :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>`, and then calculating the `semantic textual similarity <../../../../docs/sentence_transformer/usage/semantic_textual_simil…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79` — fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine both approaches. For an example implementation, see [semantic_search_nq_opensearch.py](semantic_search_nq_opensearch.py), which shows how to use OpenSearch with the Natural Questions dataset, demonstrating both semantic search and BM25 search capabilities. ## Approximate Nearest N…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485` — , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` module, it will use the "query" or "document" task type to route the input through the appropriate submodules. Note that :meth:`SentenceTransformer.encode <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode>` is the most general method and can be used for any…

### Answer

Sentence Transformers describes two main options for scaling semantic search beyond a manual in-memory implementation:

1. **Using the `semantic_search` function**: This function allows for efficient semantic search by processing queries in parallel and chunking the corpus into manageable sizes. It can be optimized for speed by ensuring both `query_embeddings` and `corpus_embeddings` are on the same GPU device [C1].

2. **Approximate Nearest Neighbor (ANN) algorithms**: For large corpora with millions of embeddings, exact nearest neighbor search can be time-consuming. ANN algorithms can be used to partition the data into smaller, more manageable fractions, enabling efficient retrieval of the most similar embeddings [C4].

### Citations

[C1] -> `chunk_293b419bb31d44e5b59d6b65009b2708fa24711d3372d2db12d3ea963c260721`, [C4] -> `chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correctly identifies optimized semantic_search/GPU placement and ANN scaling.

# q031

## Question

Why can dense semantic retrieval find matches that lexical search misses?

## Reference Answer

Dense semantic retrieval compares learned meaning representations and can match synonyms, abbreviations, and misspellings, whereas lexical retrieval depends on literal query-word matches and may miss equivalent wording.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_55f82d46216116757678b11d0a5de037a2a07f4d430e9e19af78ef0d8d207221` — nswlib/). Examples: - [semantic_search_quora_hnswlib.py](semantic_search_quora_hnswlib.py) - [semantic_search_quora_annoy.py](semantic_search_quora_annoy.py) - [semantic_search_quora_faiss.py](semantic_search_quora_faiss.py) ## Retrieve & Re-Rank For complex semantic search scenarios, a two-stage retrieve & re-rank pipeline is advisable: ![InformationRetrieval](https://raw.githubusercontent.com/huggingface/sentence-transformers/main/docs/img/InformationRetrieval.png) For further details, see [R…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79` — fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine both approaches. For an example implementation, see [semantic_search_nq_opensearch.py](semantic_search_nq_opensearch.py), which shows how to use OpenSearch with the Natural Questions dataset, demonstrating both semantic search and BM25 search capabilities. ## Approximate Nearest N…

### Answer

Dense semantic retrieval can find matches that lexical search misses because it encodes the search query and documents into a vector space, allowing it to recognize semantic similarities, synonyms, acronyms, and spelling variations, unlike lexical search which relies on exact keyword matches [C2].

### Citations

[C2] -> `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete learned-vector versus literal-match explanation.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_1a2ea5c65a9dbe1477bb5fe1bfd0a98f9d5740b308ff45b61acefa9e68f0c188` — ions/semantic_textual_similarity/README.html) - **Semantic Search** - [Dense Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) - [Sparse Search](https://www.sbert.net/examples/sparse_encoder/applications/semantic_search/README.html) - **Retrieve & Re-Rank** - [Dense only Retrieval](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) - [Sparse/Dense/Hybrid Retrieval](https://www.sbert.net/examples/sente…
- [C5] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…

### Answer

Dense semantic retrieval can find matches that lexical search misses because it encodes the search query and document embeddings into a vector space, allowing it to recognize semantic similarities, synonyms, acronyms, and spelling variations, unlike lexical search which only looks for literal matches [C1].

### Citations

[C1] -> `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete learned-vector versus literal-match explanation.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456` — # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviations, and misspellings, unlike keyword search engines that can only find documents based on lexical matches. ## Background The idea behind semantic search is to embed all entries in your corpus, whether they be sentences, paragraphs, or documents, into a vector space. At search t…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_1a2ea5c65a9dbe1477bb5fe1bfd0a98f9d5740b308ff45b61acefa9e68f0c188` — ions/semantic_textual_similarity/README.html) - **Semantic Search** - [Dense Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) - [Sparse Search](https://www.sbert.net/examples/sparse_encoder/applications/semantic_search/README.html) - **Retrieve & Re-Rank** - [Dense only Retrieval](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) - [Sparse/Dense/Hybrid Retrieval](https://www.sbert.net/examples/sente…

### Answer

Dense semantic retrieval can find matches that lexical search misses because it encodes the search query and document embeddings into a vector space, allowing it to recognize semantic similarities, synonyms, acronyms, and spelling variations, unlike lexical search which only looks for literal matches [C1][C2].

### Citations

[C1] -> `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`, [C2] -> `chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete answer supported by both documents.

# q032

## Question

How does a bi-encoder and CrossEncoder two-stage retrieval pipeline work?

## Reference Answer

A fast bi-encoder independently embeds the query and corpus to retrieve a candidate set; a slower CrossEncoder then scores query-candidate pairs and reranks the best candidates for final presentation.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949` — [semantic search](../semantic-search/README.md)). Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cross-Encoder are presented to the user. * **[in_document_search_crossencoder.py](in_document_search_crossencoder.py):** If you only have a small set of paragraphs, we don't do the retrieval stage. This is for example the case if you want to perform search within a single document. In this example, we take the Wikipedia artic…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C5] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…

### Answer

A bi-encoder and CrossEncoder two-stage retrieval pipeline works as follows:

1. **Bi-Encoder (Retrieval Stage):** The bi-encoder produces embeddings independently for your paragraphs and for your search queries. It is used to retrieve a set of candidate documents that are potentially relevant to the query. This can be done using lexical search or dense retrieval with the bi-encoder [C1]. The retriever is efficient for large document collections but might return irrelevant candidates [C3].

2. **CrossEncoder (Re-ranker Stage):** The retrieved candidates are then scored by a CrossEncoder re-ranker, which scores the relevancy of all candidates for the given search query. The CrossEncoder takes the query and a possible document and outputs a single score between 0 and 1 indicating how relevant the document is for the given query [C3]. This stage improves the final results by re-ranking the retrieved candidates [C2]. The CrossEncoder performs attention across the query and the document, which enhances performance, but scoring a large number of (query, document)-pairs is slow, so the retriever is used to create a smaller set of candidates [C3]. 

The output is a ranked list of hits that can be presented to the user [C2].

### Citations

[C1] -> `chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949`, [C3] -> `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`, [C2] -> `chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete efficient candidate retrieval and slower pairwise reranking flow.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949` — [semantic search](../semantic-search/README.md)). Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cross-Encoder are presented to the user. * **[in_document_search_crossencoder.py](in_document_search_crossencoder.py):** If you only have a small set of paragraphs, we don't do the retrieval stage. This is for example the case if you want to perform search within a single document. In this example, we take the Wikipedia artic…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C5] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…

### Answer

A bi-encoder and CrossEncoder two-stage retrieval pipeline works as follows:

1. **Bi-Encoder (Retrieval Stage):** The bi-encoder produces embeddings independently for your paragraphs and for your search queries. It is used to retrieve a set of candidate documents that are potentially relevant to the query. This can be done using lexical search or dense retrieval with the bi-encoder [C1]. The retriever is efficient for large document collections but might return irrelevant candidates [C3].

2. **CrossEncoder (Re-ranker Stage):** The retrieved candidates are then scored by a CrossEncoder re-ranker, which scores the relevancy of all candidates for the given search query. The CrossEncoder takes the query and a possible document and outputs a single score between 0 and 1 indicating how relevant the document is for the given query [C3]. This stage improves the final results by re-ranking the retrieved candidates [C2]. The CrossEncoder performs attention across the query and the document, which enhances performance, but scoring a large number of (query, document)-pairs is slow, so the retriever is used to create a smaller set of candidates [C3]. 

The output is a ranked list of hits that can be presented to the user [C2].

### Citations

[C1] -> `chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949`, [C3] -> `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`, [C2] -> `chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete efficient candidate retrieval and slower pairwise reranking flow.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949` — [semantic search](../semantic-search/README.md)). Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cross-Encoder are presented to the user. * **[in_document_search_crossencoder.py](in_document_search_crossencoder.py):** If you only have a small set of paragraphs, we don't do the retrieval stage. This is for example the case if you want to perform search within a single document. In this example, we take the Wikipedia artic…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C5] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38` — w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize synonyms, acronyms or spelling variations. In contrast, semantic search (or dense retrieval) encodes the search query into vector space and retrieves the document embeddings that are close in vector space. ![SemanticSearch](https://raw.githubusercontent.com/huggingface/sentence-tran…

### Answer

A bi-encoder and CrossEncoder two-stage retrieval pipeline works by first using a bi-encoder to retrieve a set of candidate documents that are potentially relevant to the query. The bi-encoder generates embeddings for both the query and the documents, and retrieves documents that are close in vector space, which can be done through lexical search or semantic search [C1]. This stage is efficient for large document collections but may return irrelevant candidates [C5].

In the second stage, a CrossEncoder re-ranker scores the relevancy of all the retrieved candidates for the given search query. The CrossEncoder processes the query and each candidate document simultaneously, outputting a single score between 0 and 1 indicating the relevance of the document to the query [C3]. This re-ranking step improves the final results by focusing on the most relevant documents, thus providing a ranked list of hits to present to the user [C1].

### Citations

[C1] -> `chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7`, [C5] -> `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`, [C3] -> `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete two-stage explanation with supported efficiency trade-off.

# q033

## Question

How do local SentenceTransformer embedding calls differ from serving embeddings with Text Embeddings Inference?

## Reference Answer

SentenceTransformer loads a model in the Python process and returns arrays from encode, while TEI runs compatible models as a serving system and exposes endpoints such as /embed with batching and operational features.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0` — ransformers ``` See [Installation](https://www.sbert.net/docs/installation.html) in the docs for uv, conda, source, and editable installs, CUDA setup, and extras (`[image]`, `[audio]`, `[video]`, `[train]`, `[onnx]`, `[openvino]`, `[dev]`). ## Getting Started See [Quickstart](https://www.sbert.net/docs/quickstart.html) in our documentation. ### Embedding Models First download a pretrained embedding a.k.a. Sentence Transformer model. ```python from sentence_transformers import SentenceTransforme…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_464bc98da7e8879d2635d9eb9580dc9f94c6582d606c2a654f4a90d3c65ddc1d` — cument_embeddings) print(scores) # tensor([[9.6037, 9.4055]]) ``` ## Pre-Trained Models We provide a large list of pretrained models for more than 100 languages. Some models are general purpose models, while others produce embeddings for specific use cases. - [Pretrained Sentence Transformer (Embedding) Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html) - [Pretrained Cross Encoder (Reranker) Models](https://sbert.net/docs/cross_encoder/pretrained_models.html) - [Pretrai…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_3f5df0268c752247091a3728d871f54b99d5caeba3db70efd302359a8c6756cc` — -embeddings): CPU-friendly embedding models without attention. - [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors. ## Application Examples You can use this framework for: - **Computing Sentence Embeddings** - [Dense Embeddings](https://www.sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html) - [Sparse Embeddings](https://www…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485` — , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` module, it will use the "query" or "document" task type to route the input through the appropriate submodules. Note that :meth:`SentenceTransformer.encode <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode>` is the most general method and can be used for any…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention; Dense retrieves only local SentenceTransformer material.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0` — ransformers ``` See [Installation](https://www.sbert.net/docs/installation.html) in the docs for uv, conda, source, and editable installs, CUDA setup, and extras (`[image]`, `[audio]`, `[video]`, `[train]`, `[onnx]`, `[openvino]`, `[dev]`). ## Getting Started See [Quickstart](https://www.sbert.net/docs/quickstart.html) in our documentation. ### Embedding Models First download a pretrained embedding a.k.a. Sentence Transformer model. ```python from sentence_transformers import SentenceTransforme…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485` — , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` module, it will use the "query" or "document" task type to route the input through the appropriate submodules. Note that :meth:`SentenceTransformer.encode <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode>` is the most general method and can be used for any…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad` — ings-inference:89-1.9 | | Hopper (H100) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:hopper-1.9 | | Blackwell 10.0 (B200, GB200, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:100-1.9 (experimental) | | Blackwell 12.0 (GeForce RTX 50X0, ...) | x86_64 | ghcr.io/huggingface/text-embeddings-inference:120-1.9 (experimental) | | Blackwell 12.1 (DGX Spark GB10, ...) | multi | ghcr.io/huggingface/text-embeddings-inference:121-1.9 (experimental) | **Warning**: Flash Attention…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a` — mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>` as well as for our query with :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>`, and then calculating the `semantic textual similarity <../../../../docs/sentence_transformer/usage/semantic_textual_simil…

### Answer

Local SentenceTransformer embedding calls involve directly using the `SentenceTransformer` library to compute embeddings on a local machine, which requires installing the library and its dependencies [C1]. This method is suitable for small-scale tasks and provides direct control over the embedding process.

In contrast, serving embeddings with Text Embeddings Inference involves using a pre-deployed service, typically hosted on a server or cloud platform, which provides a REST API for embedding computation [C4]. This approach is more scalable and suitable for large-scale applications, as it offloads the computational load from the client machine and allows for efficient resource management.

### Citations

[C1] -> `chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0`, [C4] -> `chunk_1bb8a52544383df16282351701a652dbd2b9ea0ffea9714bf04374530545c7ad`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Provides a high-level local-versus-service distinction but omits encode arrays, /embed, batching, and adds unsupported scale claims.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C2] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd` — The Hugging Face model ID, can be any model listed on <https://huggingface.co/models> with the `text-embeddings-inference` tag (meaning it's compatible with Text Embeddings Inference). Alternatively, the specified ID can also be a path to a local directory containing the necessary model files saved by the `save_pretrained(...)` methods of either Transformers or Sentence Transformers. [env: MODEL_ID=] --revision <REVISION> The actual revision of the model if you're referring to a model on the hu…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_5e84c695db29b7c3652b51e77f0907090b98a11994518c25f5afdd2c27bb716a` — explore the list of best performing text embeddings models, visit the [Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). #### Sequence Classification and Re-Ranking Text Embeddings Inference currently supports CamemBERT, and XLM-RoBERTa Sequence Classification models with absolute positions. Below are some examples of the currently supported models: | Task | Model Type | Model ID | |--------------------|-------------|--------------------------…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_2dd6b523ad0477751aa2ad487a723183349e5448f496eac4bcded3b4d36f844f` — s32-tp.png" width="400" /> </p> </div> ## Table of contents - [Get Started](#get-started) - [Supported Models](#supported-models) - [Docker](#docker) - [Docker Images](#docker-images) - [API Documentation](#api-documentation) - [Using a private or gated model](#using-a-private-or-gated-model) - [Air gapped deployment](#air-gapped-deployment) - [Using Re-rankers models](#using-re-rankers-models) - [Using Sequence Classification models](#using-sequence-classification-models) - [Using SPLADE pooli…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62` — gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re-rankers models are Sequence Classification cross-encoders models with a single class that scores the similarity between a query and a text. See [this blogpost](https://blog.llamaindex.ai/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) by the LlamaIndex tea…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Incorrectly abstains despite receiving multiple TEI chunks; the complementary local SentenceTransformer passage is absent from top-5.

# q034

## Question

How are embeddings and cosine similarity used from Sentence Transformers through Qdrant search?

## Reference Answer

Sentence Transformers encodes text into numeric vectors whose similarity can be compared; Qdrant stores those vectors, normalizes them for cosine distance when inserted, and retrieves nearest vectors by similarity.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a` — mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>` as well as for our query with :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>`, and then calculating the `semantic textual similarity <../../../../docs/sentence_transformer/usage/semantic_textual_simil…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_b73f3f31650931d93081d9fc37a06a81ce80fc6020214525d6ed8705300b9763` — --- title: Search short_description: "Run similarity search in Qdrant to find points whose vectors are nearest to a query in the configured vector space." description: "Run similarity search in Qdrant to retrieve nearest-neighbor points for text, image, and multimodal queries using configurable distance metrics and HNSW." weight: 5 cta: "Run your first similarity search. Free, no infrastructure needed." aliases: - ../search - /documentation/concepts/search/ --- # Similarity Search Searching for…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_35ab976d6b507e00e337b3f239ed56f27d6119bbc2f8548f921fb8eb4daaaba6` — nslated Sentence Mining](https://www.sbert.net/examples/sentence_transformer/applications/parallel-sentence-mining/README.html) - [Multilingual Image Search, Clustering & Duplicate Detection](https://www.sbert.net/examples/sentence_transformer/applications/image-search/README.html) and many more use-cases. For all examples, see [examples/sentence_transformer/applications](https://github.com/huggingface/sentence-transformers/tree/main/examples/sentence_transformer/applications). ## Development s…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Incorrect abstention because Dense top-5 lacks enough Qdrant cosine detail for synthesis.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C2] source=`qdrant_vector_search.md` chunk_id=`chunk_b73f3f31650931d93081d9fc37a06a81ce80fc6020214525d6ed8705300b9763` — --- title: Search short_description: "Run similarity search in Qdrant to find points whose vectors are nearest to a query in the configured vector space." description: "Run similarity search in Qdrant to retrieve nearest-neighbor points for text, image, and multimodal queries using configurable distance metrics and HNSW." weight: 5 cta: "Run your first similarity search. Free, no infrastructure needed." aliases: - ../search - /documentation/concepts/search/ --- # Similarity Search Searching for…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C4] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79` — fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine both approaches. For an example implementation, see [semantic_search_nq_opensearch.py](semantic_search_nq_opensearch.py), which shows how to use OpenSearch with the Natural Questions dataset, demonstrating both semantic search and BM25 search capabilities. ## Approximate Nearest N…

### Answer

Sentence Transformers generate embeddings, which are vector representations of text, and Qdrant uses cosine similarity to find the nearest neighbors in the vector space. Cosine similarity measures the similarity between vectors by calculating the cosine of the angle between them, which is efficient in Qdrant due to vector normalization during addition and fast comparison using SIMD operations [C1][C4].

### Citations

[C1] -> `chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06`, [C4] -> `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct embedding generation, cosine normalization, and nearest-neighbor search synthesis.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb` — sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed is achieved. The first step is to normalize the vector when adding it to the collection. It happens only once for each vector. The second step is the comparison of vectors. In this case, it becomes equivalent to dot production - a very fast operation due to SIMD. Depending on the…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_8bbef1194ad9bfb82c7947d11885368e88bea5ff7389e12665eeb1f28a01dc56` — paragraphs and for your search queries. You can use it like this: ```python from sentence_transformers import SentenceTransformer model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1") docs = [ "My first paragraph. That contains information", "Python is a programming language.", ] document_embeddings = model.encode(docs) query = "What is Python?" query_embedding = model.encode(query) ``` For more details how to compare the embeddings, see [semantic search](../semantic-s…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a` — mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>` as well as for our query with :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>`, and then calculating the `semantic textual similarity <../../../../docs/sentence_transformer/usage/semantic_textual_simil…
- [C5] source=`qdrant_vector_search.md` chunk_id=`chunk_f841a27b7401b391d1a21346ce29d4f0dddcccb7fbd57e2da93ae0d29762cff6` — tation/headless/snippets/query-points/simple-dense/" >}} **Search By Id** {{< code-snippet path="/documentation/headless/snippets/query-points/by-existing-id/" >}} ## Metrics There are many ways to estimate the similarity of vectors with each other. In Qdrant terms, these ways are called metrics. The choice of metric depends on the vectors obtained and, in particular, on the neural network encoder training method. Qdrant supports these most popular types of metrics: * Dot product: `Dot` - <http…

### Answer

Sentence Transformers compute embeddings for text, which can then be used for semantic search. These embeddings are stored in Qdrant, where they are indexed using the cosine similarity metric, which is the most typical metric used in similarity learning models [C1][C5]. Qdrant optimizes the cosine similarity calculation by normalizing vectors when adding them to the collection and performing a fast comparison during searches, leveraging SIMD operations [C1][C5]. This allows efficient retrieval of vectors similar to a given query embedding, which is generated by Sentence Transformers [C3][C4].

### Citations

[C1] -> `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`, [C5] -> `chunk_f841a27b7401b391d1a21346ce29d4f0dddcccb7fbd57e2da93ae0d29762cff6`, [C3] -> `chunk_8bbef1194ad9bfb82c7947d11885368e88bea5ff7389e12665eeb1f28a01dc56`, [C4] -> `chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Complete cross-document path from SentenceTransformer encoding through Qdrant search.

# q035

## Question

What is the difference between filtering Qdrant candidates and boosting their final ranking with metadata?

## Reference Answer

Filtering uses payload or ID conditions to include or exclude candidates according to constraints, while formula-based score boosting keeps candidates but adjusts their ranking using payload values, conditions, or prefetch scores.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66` — vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retrieval iteration to surface more relevant documents. Qdrant provides a subtype of relevance feedback-based retrieval, where feedback is given by any model (relevance oracle) in a granular fashion: it rescores top retrieved results by their relative relevance to…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…

### Answer

Filtering Qdrant candidates involves setting conditions on the payload or ID of points to narrow down the search results, ensuring that only relevant candidates based on specific criteria are considered [C2]. On the other hand, boosting the final ranking with metadata involves adjusting the relevance scores of the search results based on additional factors, such as business signals or user preferences, to influence the order of the results [C1].

### Citations

[C2] -> `chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`, [C1] -> `chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct include/exclude filtering versus post-retrieval score adjustment.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C2] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728` — expensive to compute. Splitting the search into two stages is a known technique to mitigate this effect: - First, use a smaller and cheaper representation to get a large list of candidates. - Then, re-score the candidates using the larger and more accurate representation. There are a few ways to build search architectures around this idea: - The quantized vectors as a first stage, and the full-precision vectors as a second stage. - Leverage Matryoshka Representation Learning (<a href=https://ar…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0` — business logic needs to be considered for ranking the final list of results. A quick example is [our own documentation search bar](https://github.com/qdrant/page-search). It has vectors for every part of the documentation site. If one were to perform a search by "just" using the vectors, all kinds of elements would be equally considered good results. However, when searching for documentation, we can establish a hierarchy of importance: `title > content > snippets` One way to solve this is to we…

### Answer

Filtering Qdrant candidates involves setting conditions on the metadata or IDs of points to narrow down the search results, ensuring only relevant candidates are considered [C2]. Boosting the final ranking with metadata, on the other hand, involves adjusting the scores of the retrieved results based on additional factors like business logic or metadata, which can change the order of the results after they have been filtered [C1].

### Citations

[C2] -> `chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`, [C1] -> `chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct constraint versus ranking distinction.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C2] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0` — business logic needs to be considered for ranking the final list of results. A quick example is [our own documentation search bar](https://github.com/qdrant/page-search). It has vectors for every part of the documentation site. If one were to perform a search by "just" using the vectors, all kinds of elements would be equally considered good results. However, when searching for documentation, we can establish a hierarchy of importance: `title > content > snippets` One way to solve this is to we…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_f7e4ff6b3c3147768eeb0567eedef8dd535e0f817e38fc408358ca8e6bb7f065` — ippets/filter-condition/slice/" >}} Slicing is based on a hash of the point IDs. A point matches slice `index` of `total` if `hash(id) % total == index`. For a fixed `total`, slices `0` through `total - 1` are disjoint and together cover every point in the collection. The hash is [SipHash-2-4](https://en.wikipedia.org/wiki/SipHash) with a zero key over the ID bytes, and it won't change across Qdrant versions. Slices with different `total` values are correlated, so slice `0` of `total: 4` is alw…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…

### Answer

Filtering Qdrant candidates involves applying conditions to narrow down the set of points considered during a search, based on metadata or IDs [C1]. Boosting the final ranking with metadata, on the other hand, involves adjusting the scores of the retrieved points to reflect additional factors such as business logic or importance hierarchy, which can influence the order of the results [C3].

### Citations

[C1] -> `chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`, [C3] -> `chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Correct constraint versus business-aware score adjustment distinction.

# q036

## Question

How can Qdrant apply business signals after a hybrid retrieval stage?

## Reference Answer

Fuse prefetched retriever results, then use a Formula Query to compose a final score from fused scores, payload fields, conditions, and optional decay terms, calibrated so business signals do not dominate unintentionally.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_search_relevance.md` chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e` — rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, which is a discrepancy with the retriever's ranking. Hence, this feedback can potentially help make the next iteration of retrieval better. --- To leverage the feedback in search across the entire collection, Qdrant provides a query interface that requires: 1.…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0` — by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-naive/" >}} Internally, Qdrant combines the feedback list into pairs, based on the relevance scores, and then uses these pairs in a formula that modifies vector space traversal during retrieval (changes the strategy of retrieval). This relevance feedback-based re…
- [C4] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…

### Answer

Qdrant can apply business signals after a hybrid retrieval stage by combining vector similarity with payload filters. This allows for enforcing business rules and refining search results based on specific conditions such as stock availability, user location, or desired price range [C4].

### Citations

[C4] -> `chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Answers filtering rather than Formula Query scoring after fusion; the needed passage is outside candidates.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C2] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C3] source=`qdrant_filtering.md` chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9` — --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs, combining database-style clauses with vector similarity for precise retrieval." weight: 10 cta: "Try filtered vector search on a free Cloud cluster." aliases: - ../filtering --- # Filtering With Qdrant, you can set conditions when searching or retrieving poin…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_c9d85bcf5b9d79c7deb8d237e25898f0f93356fa3af0634a80440df11edb9653` — --- title: Hybrid Queries short_description: "Combine dense, sparse, and multivector queries in Qdrant with hybrid search, weighted RRF tuning, DBSF, and multi-stage rescoring with Formula Query." description: "Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer custom scoring with Formula Query, and pick the right method for your data." weight: 15 cta: "Run hybrid queries on a free Cloud cluster." aliases: - ../hybrid-queries hideInSidebar: false -…
- [C5] source=`qdrant_search_relevance.md` chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66` — vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retrieval iteration to surface more relevant documents. Qdrant provides a subtype of relevance feedback-based retrieval, where feedback is given by any model (relevance oracle) in a granular fashion: it rescores top retrieved results by their relative relevance to…

### Answer

Qdrant can apply business signals after a hybrid retrieval stage by using the `prefetch` parameter to combine different types of queries, such as dense, sparse, and multivector queries, and then applying payload-based ranking or filtering based on business rules. This is achieved through the `Query API`, which allows for nested prefetches and the integration of additional conditions on metadata and IDs [C1][C3]. Additionally, relevance feedback can be used to refine results by incorporating signals from a relevance oracle, which rescores top retrieved results based on their relative relevance to the query [C2][C5].

### Citations

[C1] -> `chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7`, [C3] -> `chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`, [C2] -> `chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`, [C5] -> `chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Discusses prefetch, filtering, and relevance feedback but not formula-based score composition or decay calibration.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7` — an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combinations of queries possible is the `prefetch` parameter, which enables making sub-requests. Specifically, whenever a query has at least one prefetch, Qdrant will: 1. Perform the prefetch query (or queries), 2. Apply the main query over the results of its prefetch(es). Additionall…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225` — get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vectors. <aside role="status">Disable the HNSW index for vectors used only for rescoring by setting <code>m=0</code> in the vector's HNSW configuration. Rescoring does not use the HNSW index, so disabling it will free up memory.</aside> ### Re-Scoring Examples Fetch 1000 results us…
- [C3] source=`qdrant_search_relevance.md` chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796` — --- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payload-based ranking, and incorporating business signals to reorder vector search results." weight: 30 cta: "Tune search relevance on a free Qdrant Cloud cluster." aliases: - /documentation/concepts/search-relevance/ --- # Search Relevance By default, Qdrant rank…
- [C4] source=`qdrant_search_relevance.md` chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66` — vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retrieval iteration to surface more relevant documents. Qdrant provides a subtype of relevance feedback-based retrieval, where feedback is given by any model (relevance oracle) in a granular fashion: it rescores top retrieved results by their relative relevance to…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_c9d85bcf5b9d79c7deb8d237e25898f0f93356fa3af0634a80440df11edb9653` — --- title: Hybrid Queries short_description: "Combine dense, sparse, and multivector queries in Qdrant with hybrid search, weighted RRF tuning, DBSF, and multi-stage rescoring with Formula Query." description: "Run hybrid queries in Qdrant: fuse dense, sparse, and multivector results with RRF or DBSF, layer custom scoring with Formula Query, and pick the right method for your data." weight: 15 cta: "Run hybrid queries on a free Cloud cluster." aliases: - ../hybrid-queries hideInSidebar: false -…

### Answer

Qdrant can apply business signals after a hybrid retrieval stage by using the `score` parameter in the `Query API` to adjust the relevance of search results based on custom scoring, payload-based ranking, and business-aware result ordering [C3]. This allows for the integration of additional factors that reflect business logic or specific criteria when ranking the final list of results.

### Citations

[C3] -> `chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Invents a score parameter and remains unable to answer because the relevant Formula Query chunks are absent from the fixed candidate set.

# q037

## Question

What corpus guidance helps keep retrieval evaluation reproducible and avoids tuning bias?

## Reference Answer

Use fixed query/relevance splits so parameters are tuned and measured on different data, retest when retrievers or corpora change, and use reproducible sampling rather than fresh random samples when constructing evaluation subsets.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_62596d162f72d39a62714058316f7eb1a0267f72501b85a8e0e03255e16d13d2` — lgbJWkIMT0xJH6PWF1?usp=sharing) ]: This example uses a model that was trained on the [Natural Questions dataset](https://huggingface.co/datasets/sentence-transformers/natural-questions). It consists of about 100k real Google search queries, together with an annotated passage from Wikipedia that provides the answer. It is an example of an **asymmetric search task**. As corpus, we use the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) so that it fits easily into m…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_19b72a4ab4b2d383f2a67beaf219457831a2f94ef5cd270c202d6bd4d13de949` — [semantic search](../semantic-search/README.md)). Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cross-Encoder are presented to the user. * **[in_document_search_crossencoder.py](in_document_search_crossencoder.py):** If you only have a small set of paragraphs, we don't do the retrieval stage. This is for example the case if you want to perform search within a single document. In this example, we take the Wikipedia artic…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Incorrect abstention; corpus-evaluation guidance is absent from Dense top-5.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C2] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f15918e3139823fd58c308097a43c0c7a8c8806b9d61377e1e26125ddc9e78f7` — ublications.py) [ [Colab version](https://colab.research.google.com/drive/12hfBveGHRsxhPIUMmJYrll2lFU4fOX06?usp=sharing) ] shows an example how to find similar scientific publications. As corpus, we use all publications that have been presented at the EMNLP 2016 - 2018 conferences. As search query, we input the title and abstract of more recent publications and find related publications from our corpus. We use the [SPECTER](https://huggingface.co/sentence-transformers/allenai-specter) model. Th…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69` — **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and you want to find the paragraph *"Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy ..."*. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense. - Related training example: [MS M…
- [C4] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485` — , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` module, it will use the "query" or "document" task type to route the input through the appropriate submodules. Note that :meth:`SentenceTransformer.encode <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode>` is the most general method and can be used for any…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0` — ## Symmetric vs. Asymmetric Semantic Search A **critical distinction** for your setup is *symmetric* vs. *asymmetric semantic search*: - For **symmetric semantic search** your query and the entries in your corpus are of about the same length and have the same amount of content. An example would be searching for similar questions: Your query could for example be *"How to learn Python online?"* and you want to find an entry like *"How to learn Python on the web?"*. For symmetric tasks, you could …

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Incorrect abstention; Hybrid top-5 lacks the fixed-split and reproducible-sampling guidance.

---

## Reranked

### Retrieved Context

- [C1] source=`qdrant_vector_search.md` chunk_id=`chunk_898688bf990e34cdc55f47c24c42ca0a948d72069a895f6ab9b13b0ff55631ae` — or providing entry points for exploration. Random sampling API is a part of [Universal Query API](#query-api) and can be used in the same way as regular search API. {{< code-snippet path="/documentation/headless/snippets/query-points/random-sample/" >}} <aside role="status">If you need a sample that's reproducible across queries, for example for recall evaluation or a train/test split, use the <a href="/documentation/search/filtering/#slice">slice filter condition</a> instead. It returns the sa…
- [C2] source=`qdrant_search_relevance.md` chunk_id=`chunk_dac54b8a64f99694d50519695bd723cf6014b1c28324228976f4af25c6b5ce66` — ermine the relevance of search results. --- The idea behind using relevance feedback-based retrieval is the following: 1. Run a basic nearest neighbors search. Let's call its results **Retriever Similarity** and the algorithm behind this search -- **retriever**. 2. Use any **feedback model** to assign a relevance score to the top X search results (X is not expected to be large, 3-5 is a good option). Let's call these scores **Feedback Score**. 3. Through analyzing the Feedback Score for the top…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_bb8e3f0d06c7af0619a884ab227019958efbf2131176dd7e32325fadb6c8cd64` — antic_search` method, it is advisable to have the ``query_embeddings`` as well as the ``corpus_embeddings`` on the same GPU-device. This significantly boost the performance. Further, we can normalize the corpus embeddings so that each corpus embeddings is of length 1. In that case, we can use dot-product for computing scores. .. code-block:: python from sentence_transformers.util import dot_score, normalize_embeddings, semantic_search corpus_embeddings = corpus_embeddings.to("cuda") corpus_embe…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0` — PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch inference if your `sequence_length` is regular, and keep pushing it until you reach an OOM error. The larger the GPU, the more helpful batch inference is. 6. Do make sure you can handle OOM errors if you decide to do batch inference. ### Task-specific parameters [`Pipeline`] acce…
- [C5] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Incorrect abstention; candidate retrieval fails before reranking can expose the required passages.

# q038

## Question

How does rank or score fusion differ from candidate retrieve-and-rerank?

## Reference Answer

Fusion combines rankings or normalized scores from multiple retrievers into one ordering, while retrieve-and-rerank uses a fast first-stage retriever to select candidates and a more accurate model to rescore those candidates.

---

## Dense

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92` — se you can get an empty result.</aside> ## Hybrid Search One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result. {{< figure src="/docs/fusion-idea.png" caption="Fusing results from multiple queries" width="80%" >}} For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise wo…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178` — y and boosts those that appear closer to the top in multiple sets of results. The score of a document is calculated using its rank in each result set: $$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r} - 1} $$ Where: - $D$ the set of points across all results - $R(d)$ is the set of rankings for a particular document - $k$ is a constant (set to 2 by default) - $r$ is an ordered set of results from one source - $r_d$ is the rank of document $d$ in ranking $r$ - $w_r$ is the we…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…

### Answer

Rank or score fusion differs from candidate retrieve-and-rerank in that it combines results from multiple sources (e.g., dense and sparse vectors) by normalizing and combining their scores, rather than re-ranking a single set of candidate results. Score fusion techniques like RRF and DBSF aim to produce a unified ranking by leveraging the relative positions or normalized scores of documents across different retrievers, whereas retrieve-and-rerank involves first retrieving a set of candidate documents and then re-ranking them based on a different model or criteria [C1][C3].

### Citations

[C1] -> `chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076`, [C3] -> `chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Correct comparison, but top-5 mainly supports fusion and only weakly supports the retrieve-and-rerank half.

---

## Hybrid

### Retrieved Context

- [C1] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_e09d7508ba19a494354ce3dc4ddfe1e52638bbb156c5e559d89411c85dafaa92` — se you can get an empty result.</aside> ## Hybrid Search One of the most common problems when you have different representations of the same data is to combine the queried points for each representation into a single result. {{< figure src="/docs/fusion-idea.png" caption="Fusing results from multiple queries" width="80%" >}} For example, in text search, it is often useful to combine dense and sparse vectors to get the best of both worlds: semantic understanding from dense vectors and precise wo…
- [C2] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_5e3fb0fa5c2e973d53ebace2400b476efb750959536c41d378c5cb964e7279f0` — stics come from the prefetch top-k (a small sample), and a single dominant outlier in that top-k can skew normalization for that query. Increase the prefetch `limit` if you see unstable rankings. {{< code-snippet path="/documentation/headless/snippets/query-points/hybrid-dbsf/" >}} ### Choosing a Fusion Method | If you have... | Use | | --- | --- | | An eval set (queries with known-relevant docs) to tune on | Weighted RRF, with weights tuned on a train/val split | | Trust in your retrievers' ra…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…

### Answer

Rank or score fusion combines results from multiple queries (e.g., dense and sparse vectors) into a single ranked list by normalizing and summing scores, whereas candidate retrieve-and-rerank first retrieves candidate items and then re-ranks them using a separate model [C5].

### Citations

[C5] -> `chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Correct concise distinction, but the sole citation only partially establishes the two-stage reranker behavior.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0` — a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-encoder. If a new query / question is entered, it is encoded by the same bi-encoder and the paragraphs with the highest cosine-similarity are retrieved. Next, the retrieved candidates are scored by a Cross-Encoder re-ranker and the 5 passages with the highest score from the Cros…
- [C2] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17` — r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final results for the user. The query and a possible document is passed simultaneously to transformer network, which then outputs a single score between 0 and 1 indicating how relevant the document is for the given query. ![CrossEncoder](https://raw.githubusercontent.com/huggingface/sentenc…
- [C3] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_4023c8bfc2f5bd193937c2eb57120d7ed88baa8adff635f1c44062db89561eb1` — ### Fusion in Distributed Collections The previous example puts the fusion inside a prefetch. In a multi-shard collection, a fusion merges results across all shards only when it is the main query, held in the top-level `query` field with the retrievers as its prefetches, as in the [RRF](#reciprocal-rank-fusion-rrf) and [DBSF](#distribution-based-score-fusion-dbsf) examples. When it instead sits inside a prefetch, each shard computes the fusion on its local results, so the fused ranking is per s…
- [C4] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_463932fdac84be96e58eced760ba530f4e7d8ddf41a522f9a02c08e3ea267076` — fusion-dbsf-for-hybrid-search). To layer business logic (recency, popularity, geo) on top of a fused result, see [Custom scoring with a formula query](#custom-scoring-with-a-formula-query). <aside role="status">A common request is "alpha-weighted linear combination of dense and sparse scores." This is unreliable without first normalizing the scores: dense (cosine, bounded) and sparse (BM25, unbounded) scores live on different scales that also shift per query, so a fixed alpha over raw scores te…
- [C5] source=`qdrant_hybrid_queries.md` chunk_id=`chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf` — etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1.11.0_ <a href=https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18 target="_blank">DBSF</a> keeps the raw scores from each query but normalizes their distributions before combining. For each retriever…

### Answer

Rank or score fusion differs from candidate retrieve-and-rerank in that it combines scores from multiple retrievers or sources, normalizing their distributions before combining, whereas retrieve-and-rerank involves first retrieving a set of candidate documents and then re-ranking them using a more accurate but computationally intensive model [C5].

### Citations

[C5] -> `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`

Invalid labels: None

### Scores

- Answer Correctness: 2
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: False

### Notes

Both fusion and candidate reranking are represented in the supplied contexts.

# q039

## Question

When would an application use a Transformers Pipeline directly instead of a Text Embeddings Inference server?

## Reference Answer

Pipeline provides in-process task inference with configurable models and task parameters, while TEI is intended to deploy embedding or sequence-classification models behind a high-performance service API with batching and production observability.

---

## Dense

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_3f5df0268c752247091a3728d871f54b99d5caeba3db70efd302359a8c6756cc` — -embeddings): CPU-friendly embedding models without attention. - [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors. ## Application Examples You can use this framework for: - **Computing Sentence Embeddings** - [Dense Embeddings](https://www.sbert.net/examples/sentence_transformer/applications/computing-embeddings/README.html) - [Sparse Embeddings](https://www…
- [C3] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485` — , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` module, it will use the "query" or "document" task type to route the input through the appropriate submodules. Note that :meth:`SentenceTransformer.encode <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode>` is the most general method and can be used for any…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_8669f110e12d0b9f7d09cb4f11400e4c26490b48c7612e3ea1d9d831498d98c7` — batches yourself. Try [Batch inference](#batch-inference) with the `batch_size` parameter to see if it improves performance. ```py from transformers.pipelines.pt_utils import KeyDataset from transformers import pipeline from accelerate import Accelerator from datasets import load_dataset device = Accelerator().device dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipeline(task="text-classification", model="distilbert/distilbert-base-uncas…

### Answer

An application would use a Transformers Pipeline directly instead of a Text Embeddings Inference server when the application requires fine-grained control over the inference process, such as processing small batches of data, leveraging specific hardware (like Macs with Metal support), or when the application is designed for local execution and does not require the scalability and performance optimizations provided by the Text Embeddings Inference server [C1]. Additionally, if the application needs to integrate with other systems or requires custom processing steps, using the Transformers Pipeline directly might be more appropriate.

### Citations

[C1] -> `chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 0
- Requires human review: True

### Notes

Plausible Pipeline use cases, but TEI comparison is incomplete and C1 does not support the hardware/control claims attached to it.

---

## Hybrid

### Retrieved Context

- [C1] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_09006fa517bbcf8d797adaa6324d1032de7f102d6a6d0a7f449c48532886f1e4` — cess data in chunks. - for some data types, a single input (for example, a really long audio file) may need to be chunked into multiple parts before it can be processed - for some tasks, like zero-shot classification or question answering, a single input may need multiple forward passes which can cause issues with the `batch_size` parameter The [ChunkPipeline](https://github.com/huggingface/transformers/blob/99e0ab6ed888136ea4877c6d8ab03690a1478363/src/transformers/pipelines/base.py#L1387) clas…
- [C3] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_45e5cbdf579dcb31c0aa2de3736dbf6936c507a56b191bdf3aa9411328fd3651` — curl 127.0.0.1:8080/embed_sparse \ -X POST \ -d '{"inputs":"I like you."}' \ -H 'Content-Type: application/json' ``` ### Distributed Tracing `text-embeddings-inference` is instrumented with distributed tracing using OpenTelemetry. You can use this feature by setting the address to an OTLP collector with the `--otlp-endpoint` argument. ### gRPC `text-embeddings-inference` offers a gRPC API as an alternative to the default HTTP API for high performance deployments. The API protobuf definition can…
- [C4] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…
- [C5] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…

### Answer

An application would use a Transformers Pipeline directly instead of a Text Embeddings Inference server when the task requires fine-grained control over the inference process, such as adding specific parameters for task-specific configurations (e.g., timestamps in automatic speech recognition pipelines) or when deploying on environments that do not support the server infrastructure of Text Embeddings Inference [C4]. Additionally, if the application needs to leverage features like GPU acceleration, Apple Silicon support, or half-precision weights for memory optimization, the Transformers Pipeline provides these capabilities directly [C4].

### Citations

[C4] -> `chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Pipeline capabilities are partly supported, but the answer omits TEI service/batching/observability and adds an unsupported infrastructure claim.

---

## Reranked

### Retrieved Context

- [C1] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e` — - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification models. TEI enables high-performance extraction for the most popular models, including FlagEmbedding, Ember, GTE and E5. TEI implements many features such as: * No model graph compilation step * Metal support for local execution on Macs * Small docker images and fast boot times. G…
- [C2] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a` — werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters such as adding timestamps to an automatic speech recognition (ASR) pipeline for transcribing meeting notes. [`Pipeline`] supports GPUs, Apple Silicon, and half-precision weights to accelerate inference and save memory. <Youtube id=tiZFewofSLM/> Transformers has two pipeline clas…
- [C3] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01` — from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch inference [`Pipeline`] can also process batches of inputs with the `batch_size` parameter. Batch inference may improve speed, especially on a GPU, but it isn't guaranteed. Other variables such as hardware, data, and the model itself can affect whether batch inference improves speed. F…
- [C4] source=`huggingface_text_embeddings_inference.md` chunk_id=`chunk_45e5cbdf579dcb31c0aa2de3736dbf6936c507a56b191bdf3aa9411328fd3651` — curl 127.0.0.1:8080/embed_sparse \ -X POST \ -d '{"inputs":"I like you."}' \ -H 'Content-Type: application/json' ``` ### Distributed Tracing `text-embeddings-inference` is instrumented with distributed tracing using OpenTelemetry. You can use this feature by setting the address to an OTLP collector with the `--otlp-endpoint` argument. ### gRPC `text-embeddings-inference` offers a gRPC API as an alternative to the default HTTP API for high performance deployments. The API protobuf definition can…
- [C5] source=`huggingface_pipeline_tutorial.md` chunk_id=`chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45` — is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma 2](./model_doc/gemma2), set `task="text-generation"` and `model="google/gemma-2-2b"`. ```py from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b") pipeline("the secret to baking a really good cake is ") [{'generated_text': 'the …

### Answer

An application would use a Transformers Pipeline directly instead of a Text Embeddings Inference server when the application requires fine-grained control over the model execution, such as when running on local hardware (e.g., Macs with Apple Silicon) or when deploying in environments where lightweight and quick setup is essential [C2]. Additionally, if the application needs to process inputs in a batch or requires specific configurations like using half-precision weights for memory optimization, the Transformers Pipeline provides these capabilities directly [C3]. The Transformers Pipeline is also suitable for scenarios where the application needs to integrate with other systems or workflows without the overhead of deploying a dedicated server [C2].

### Citations

[C2] -> `chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a`, [C3] -> `chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Pipeline details are supported, but comparative claims about lightweight setup, workflow overhead, and when to prefer it are weakly grounded; TEI context is not cited.

# q040

## Question

How do the Sentence Transformers and TEI documents characterize reranker models?

## Reference Answer

Both describe rerankers as CrossEncoder or sequence-classification models that score a query together with candidate text; they improve candidate ordering but operate after a smaller candidate set has been retrieved.

---

## Dense

### Retrieved Context

- [C1] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10` — # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. For complex search tasks, for example question answering retrieval, the search can significantly be improved by using **Retrieve & Re-Rank**. ## Retrieve & Re-Rank Pipeline The following pipeline for Information Retrieval / Question Answering Retrieval works very well. All compon…
- [C4] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185` — 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.google.com/github/huggingface/sentence-transformers/blob/main/examples/sentence_transformer/applications/retrieve_rerank/retrieve_rerank_simple_wikipedia.ipynb) ]: This script uses the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) as document coll…
- [C5] source=`sentence_transformers_semantic_search.md` chunk_id=`chunk_62596d162f72d39a62714058316f7eb1a0267f72501b85a8e0e03255e16d13d2` — lgbJWkIMT0xJH6PWF1?usp=sharing) ]: This example uses a model that was trained on the [Natural Questions dataset](https://huggingface.co/datasets/sentence-transformers/natural-questions). It consists of about 100k real Google search queries, together with an annotated passage from Wikipedia that provides the answer. It is an example of an **asymmetric search task**. As corpus, we use the smaller [Simple English Wikipedia](https://simple.wikipedia.org/wiki/Main_Page) so that it fits easily into m…

### Answer

The provided documentation does not contain enough information to answer this reliably.

### Citations

None

Invalid labels: None

### Scores

- Answer Correctness: 0
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Incorrect abstention because Dense top-5 contains only the Sentence Transformers side and lacks TEI reranker content.

---

## Hybrid

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_865469e0360fadf03d8d8ac585b7cfb077109928466d6666db47fdf7bde73c36` — loss functions](https://www.sbert.net/docs/package_reference/sparse_encoder/losses.html) for sparse embedding models, allowing you to tune models specifically for semantic search, paraphrase mining, semantic similarity comparison, clustering, triplet loss, contrastive loss, etc. ## Companion Blog Posts The following Hugging Face blog posts complement this documentation with narrative walkthroughs and full training examples: **Training guides:** - [Training and Finetuning Embedding Models](https…
- [C3] source=`sentence_transformers_overview.md` chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0` — Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html), [semantic textual similarity](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html), and [paraphrase mining](https://sbert.net/examples/applications/paraphrase-mining/README.html). A wide selection of over [15,000 pre-trained Sen…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_464bc98da7e8879d2635d9eb9580dc9f94c6582d606c2a654f4a90d3c65ddc1d` — cument_embeddings) print(scores) # tensor([[9.6037, 9.4055]]) ``` ## Pre-Trained Models We provide a large list of pretrained models for more than 100 languages. Some models are general purpose models, while others produce embeddings for specific use cases. - [Pretrained Sentence Transformer (Embedding) Models](https://sbert.net/docs/sentence_transformer/pretrained_models.html) - [Pretrained Cross Encoder (Reranker) Models](https://sbert.net/docs/cross_encoder/pretrained_models.html) - [Pretrai…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_41c5dd4ee9ff890e5e9b8ad1643b1a0ba92fe0c806443d81296513b468450d11` — - Multi-Vector (Late Interaction) Models - [Multi-Vector Encoder > Training Overview](https://www.sbert.net/docs/multi_vector_encoder/training_overview.html) - [Training examples on GitHub](https://github.com/huggingface/sentence-transformers/tree/main/examples/multi_vector_encoder/training). Some highlights across the different types of training are: - Support of various transformer networks including BERT, RoBERTa, XLM-R, DistilBERT, Electra, BART, ... - Multilingual and multi-task learning -…

### Answer

The Sentence Transformers and TEI documents characterize reranker models as Cross-Encoder models, which are used to calculate similarity scores and are part of the second stage of retrieve-and-rerank pipelines [C2]. These models are specifically trained for tasks such as semantic search, paraphrase mining, and semantic similarity comparison [C3].

### Citations

[C2] -> `chunk_865469e0360fadf03d8d8ac585b7cfb077109928466d6666db47fdf7bde73c36`, [C3] -> `chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 1
- Citation Correctness: 1
- Requires human review: True

### Notes

Mentions CrossEncoders and second-stage scoring but does not synthesize TEI sequence classification, and the cited overview chunks only weakly support the claims.

---

## Reranked

### Retrieved Context

- [C1] source=`sentence_transformers_overview.md` chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06` — go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. It can be used to compute embeddings using Sentence Transformer models ([quickstart](https://sbert.net/docs/quickstart.html#sentence-transformer)), to calculate similarity scores using Cross-Encoder (a.k.a. reranker) m…
- [C2] source=`sentence_transformers_overview.md` chunk_id=`chunk_b651190dc991598f552ad3b5c19153cb5143cc5b30867ce73d946efe43655fec` — ditionally, it is easy to train or finetune your own [embedding models](https://sbert.net/docs/sentence_transformer/training_overview.html), [reranker models](https://sbert.net/docs/cross_encoder/training_overview.html), [sparse encoder models](https://sbert.net/docs/sparse_encoder/training_overview.html) or [multi-vector encoder models](https://sbert.net/docs/multi_vector_encoder/training_overview.html) using Sentence Transformers, enabling you to create custom models for your specific use cas…
- [C3] source=`sentence_transformers_retrieve_rerank.md` chunk_id=`chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7` — sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transformers.sentence_transformer.model.SentenceTransformer` (a.k.a. bi-encoder). However, the retrieval system might retrieve documents that are not that relevant for the search query. Hence, in a second stage, we use a **re-ranker** based on a :class:`~sentence_transformers.cross_encod…
- [C4] source=`sentence_transformers_overview.md` chunk_id=`chunk_5f9769f965866f6b1f7bb94a0cf9a924e7c62e09bb7fc8eb1daaceef465305ff` — inetuning Sparse Embedding Models](https://huggingface.co/blog/train-sparse-encoder): training SPLADE and other sparse encoders. **Multimodal:** - [Multimodal Embedding & Reranker Models](https://huggingface.co/blog/multimodal-sentence-transformers): using text, image, audio, and video models through a single API. - [Training and Finetuning Multimodal Embedding & Reranker Models](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal models, with a Visual Docum…
- [C5] source=`sentence_transformers_overview.md` chunk_id=`chunk_3119cb0c2a7b12e9cd954a6e8b47d18c24c3626e3d3e791e1573d0435ddfa0da` — shape) # => (3, 384) ``` And that's already it. We now have numpy arrays with the embeddings, one for each text. We can use these to compute similarities. ```python similarities = model.similarity(embeddings, embeddings) print(similarities) # tensor([[1.0000, 0.6660, 0.1046], # [0.6660, 1.0000, 0.1411], # [0.1046, 0.1411, 1.0000]]) ``` ### Reranker Models First download a pretrained reranker a.k.a. Cross Encoder model. ```python from sentence_transformers import CrossEncoder # 1. Load a pretrai…

### Answer

Reranker models, as characterized by Sentence Transformers and TEI documents, are used to score the relevancy of all candidate documents for a given search query after an initial retrieval stage. These models are based on the `CrossEncoder` class and are designed to refine the search results by ranking the retrieved documents according to their relevance to the query [C3]. The reranker models can be pretrained or fine-tuned for specific use cases, and they are part of the broader set of models provided by Sentence Transformers, which also includes embedding models, sparse encoder models, and multi-vector encoder models [C2].

### Citations

[C3] -> `chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7`, [C2] -> `chunk_b651190dc991598f552ad3b5c19153cb5143cc5b30867ce73d946efe43655fec`

Invalid labels: None

### Scores

- Answer Correctness: 1
- Faithfulness: 2
- Citation Correctness: 2
- Requires human review: True

### Notes

Accurately describes Sentence Transformers rerankers but omits the TEI sequence-classification characterization.
