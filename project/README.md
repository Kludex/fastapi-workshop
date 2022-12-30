# Project

The project we are going to create is a simple API that allows us to create, read, update and delete items.

1. The items will have a name and a price.
2. We will store the items in a database.
3. We will be able to retrieve the items, create new items, update existing items and delete items.
4. We will be able to retrieve a single item with a specific name.
5. We will be able to retrieve only the items that cost less than a specific price.

## Installation

```bash
$ python -m pip install -r requirements.txt
```

## Usage

```bash
$ uvicorn app.main:app --reload
```
