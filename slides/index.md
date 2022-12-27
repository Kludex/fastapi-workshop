---
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: "@marcelotryle"
marp: true
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Getting Started with FastAPI

![bg:40% 80%](assets/marcelo.png)
Marcelo Trylesinski

---

# About me

![w:600](https://live.staticflickr.com/4458/37545736336_93f1591985_b.jpg)

---

## FastAPI Expert

![w:950 center](assets//fastapi-expert.png)

---

## OSS Maintainer

### Uvicorn

![w:450](https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png)

---

## OSS Maintainer

### Starlette

![w:600](https://www.starlette.io/img/starlette.png)

---

## What is FastAPI?

**FastAPI** is a modern web framework used to build APIs based on Python type hints.

---

## Why FastAPI?

- Fast Development
- Easy to learn
- Intuitive
- Fewer bugs

---

# FastAPI Application

![w:500 center](assets/fastapi-simple.svg)

![w:500 center](assets/curl-simple.svg)

[Run it yourself!](https://github.com/Kludex/fastapi-workshop/blob/main/slides/src/1_fastapi_features/main.py)

---

## Path Parameters

![w:500 center](assets/fastapi-path-params.svg)

![w:500 center](assets/curl-path-params.svg)

[Run it yourself!](https://github.com/Kludex/fastapi-workshop/blob/main/slides/src/1_fastapi_features/path_params.py)

---

## Query Parameters

![w:500 center](assets/fastapi-query-params.svg)

![w:500 center](assets/curl-query-params.svg)

[Run it yourself!](https://github.com/Kludex/fastapi-workshop/blob/main/slides/src/1_fastapi_features/query_params.py)

---

## Request Body

![w:400 center](assets/fastapi-body-params.svg)

![w:600 center](assets/curl-body-params.svg)

[Run it yourself!](https://github.com/Kludex/fastapi-workshop/blob/main/slides/src/1_fastapi_features/body_params.py)

---

## Header Parameters

![w:500 center](assets/fastapi-header-params.svg)

![w:500 center](assets/curl-header-params.svg)

[Run it yourself!](https://github.com/Kludex/fastapi-workshop/blob/main/slides/src/1_fastapi_features/header_params.py)

---

## Documentation (`/docs`)

![w:950 center](assets/fastapi-docs.png)

---

## Documentation (`/redoc`)

![w:1200 center](assets/fastapi-redoc.png)

---

## Data Validation

![w:700 center](assets/fastapi-data-validation.svg)

---

## Data Validation

![w:900 center](assets/curl-data-validation.svg)

---

## Data Validation (`/docs`)

![w:800 center](assets/create-item.png)

---

## Autocomplete

![w:800 center](assets/autocompletion.png)

---

## Dependency Injection


![w:800 center](assets/dependency-injection.svg)

---

## Background Tasks

![w:800 center](assets/fastapi-background-tasks.svg)

[Run it yourself!](https://github.com/Kludex/fastapi-workshop/blob/main/slides/src/1_fastapi_features/background_tasks.py)

---

## WebSockets

![w:800 center](assets/fastapi-websockets.svg)

---

# FastAPI Features

https://fastapi.tiangolo.com/features/

---

## Q&A

![w:500 center](assets/q&a.jpeg)

---

## Hands-on FastAPI

---

## The Project

The project we are going to create is a simple API that allows us to create, read, update and delete items.

1. The items will have a name and a price.
2. We will store the items in a database.
3. We will be able to retrieve the items, create new items, update existing items and delete items.
4. We will be able to retrieve a single item with a specific name.
5. We will be able to retrieve only the items that cost less than a specific price.

---

## Create the Project

Follow up on [FastAPI Workshop](https://github.com/Kludex/fastapi-workshop/).

---

## Exercise: Test the application

---

## Q&A

![w:500 center](assets/q&a.jpeg)

---

## Let's Deploy!

![bg:40% 80%](assets/lets-deploy-in.jpg)

---

## Let's Deploy!

Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk)

(If you are on Ubuntu: `snap install google-cloud-cli --classic`)

---

## Let's Deploy!

Read [FastAPI documentation](https://fastapi.tiangolo.com/deployment/) about deployment

---

## Q&A

![w:500 center](assets/q&a.jpeg)

---

## How to proceed from here?

Read the documentation: https://fastapi.tiangolo.com/

---

## You can help the FastAPI Community

1. Answer issues
2. Join the Discord server
3. Help on underneath projects like Starlette and Pydantic

---

## Follow me

- Twitter: https://twitter.com/marcelotryle
- GitHub: https://github.com/kludex
- LinkedIn: https://www.linkedin.com/in/marcelotryle/

---

## Q&A

![w:500 center](assets/q&a.jpeg)
