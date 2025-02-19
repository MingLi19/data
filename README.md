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
    subgraph Domain-BE
        direction TB
        FastAPI --> Starlette & Pydantic;
        SQLModel --> SQLAlchemy & Pydantic;
        SQLAlchemy --> MySQL;
    end
    subgraph Domain-Data
        Pandas --> PyMongo;
        PyMongo --> MongoDB;
    end
    subgraph Domain-ML
        Train --> Pandas*[Pandas] & Scikit-learn & XGBoost;
        Predict --> MLflow & Domain-BE;
    end
    subgraph Domain-FE
        React
        Nextjs
        Shadcn
    end
    classDef red fill:#FAD2CF
    classDef green fill:#CEEAD6
    classDef blue fill:#D2E3FC
    classDef yellow fill:#FEEFC3
    classDef grey fill:#F1F3F4
    class Domain-BE blue
    class Domain-Data green
    class Domain-FE yellow
    class Domain-ML grey
```