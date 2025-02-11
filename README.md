<!-- Pytest Coverage Comment:Begin -->
\n<!-- Pytest Coverage Comment:End -->

# 项目使用工具

## API: [FastAPI](https://github.com/fastapi/fastapi) ![GitHub Repo stars](https://img.shields.io/github/stars/fastapi/fastapi)
 

## ORM: [SQLModel](https://github.com/fastapi/sqlmodel) ![GitHub Repo stars](https://img.shields.io/github/stars/tiangolo/sqlmodel)

## Type: [Pydantic](https://github.com/pydantic/pydantic) ![GitHub Repo stars](https://img.shields.io/github/stars/samuelcolvin/pydantic)

## Lint: [Ruff](https://github.com/astral-sh/ruff) ![GitHub Repo stars](https://img.shields.io/github/stars/astral-sh/ruff)

## Test: [Pytest](https://github.com/pytest-dev/pytest) ![GitHub Repo stars](https://img.shields.io/github/stars/pytest-dev/pytest)

## DB Migration: [alembic](https://github.com/sqlalchemy/alembic) ![GitHub Repo stars](https://img.shields.io/github/stars/sqlalchemy/alembic)

**All Open Source**

```mermaid
graph TD;
    项目 --> FastAPI & SQLModel & Alembic & Ruff & Pytest;
    FastAPI --> Starlette & Pydantic;
    SQLModel --> SQLAlchemy & Pydantic;
```