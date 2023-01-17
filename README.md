## Project description

Esse projeto usa o Fastapi framework e Playwright para acessar o site (https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops) e pegar todos os notebooks Lenovo ordenando do mais barato para o mais caro.

Foi feito uma rota adicional, onde é possível passar a marcar como parâmetro pegar os notebooks pela marca.

Também desenvolvi uma autenticação e autorização bem simples, a rota para criação de usuário está desprotegida para facilitar a criação.

## Requirements

Python 3.10

## Installation

```console
$ pip install -r requirements.txt
```

## Run it

Run the server with:

```console
$ uvicorn app.main:app --reload
```

Devido a um problema com o loop de eventos padrão Uvicorn, use o comando
Abaixo para rodar o projeto.(https://github.com/microsoft/playwright-python/issues/1099).

```console
$ uvicorn app.main:app 
```

## Interactive API docs

http://127.0.0.1:8000/docs

## Alternative API docs

http://127.0.0.1:8000/redoc
