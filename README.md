# API-de-Contatos-Python

## Descrição do Projeto:

É um projeto simples de backend para treina alguns fundamentos básicos e novos de backend, "API de Contatos" `fucionalidades`:

* Criar contatos;
* Listar todos os contatos;
* Buscar contato por nome ou email;
* Editar contato com base no id;
* Excluir contato com base no id;

### Tecnologias usandas:

* Python:
    * Flask
    * Flask-SQLAlchemy
    * Flask-Migrate
    * Flask-Marshmallow
    * dotenv
* SQLite

### Estrutura do Projeto:

```dir
├── app.py
├── instance
│   └── contatos.db
├── LICENSE
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── __pycache__
│   │   └── env.cpython-313.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 375b125c2cf0_create_table_contatos.py
│       └── __pycache__
│           └── 375b125c2cf0_create_table_contatos.cpython-313.pyc
├── __pycache__
│   └── app.cpython-313.pyc
├── README.md
├── requirements.txt
└── src
    ├── controllers
    │   └── __init__.py
    ├── __init__.py
    ├── models
    │   ├── contato_model.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── contato_model.cpython-313.pyc
    │       └── __init__.cpython-313.pyc
    ├── __pycache__
    │   └── __init__.cpython-313.pyc
    ├── routes
    │   ├── contatos_routes.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── contatos_routes.cpython-313.pyc
    │       └── __init__.cpython-313.pyc
    ├── schemas
    │   └── __init__.py
    ├── settings
    │   ├── config.py
    │   ├── extensions.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── config.cpython-313.pyc
    │       ├── extensions.cpython-313.pyc
    │       └── __init__.cpython-313.pyc
    └── view
        └── __init__.py


```