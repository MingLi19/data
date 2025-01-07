# alembic

Alembic是一个轻量的数据库迁移工具，使用 SQLAlchemy 作为底层引擎，为数据库提供变更管理脚本的创建、管理和调用。

## 安装

```shell
# 已经更新了 pyproject.toml 及 poetry.lock 文件
# poetry add alembic --dev
# 大家可以直接使用 poetry install 安装
poetry install 
```

## 使用

### 初始化

```shell
alembic init migration
```

生成的目录结构如下：
├── migration # 二级目录
│   ├── README # readme
│   ├── env.py # 环境配置
│   ├── script.py.mako
│   └── versions # 版本
├── alembic.ini # 配置文件

### 修改 alembic.ini 文件

```ini
script_location = migration
sqlalchemy.url = mysql+pymysql://root:123456@localhost:3306/management_system
```

### 修改 env.py 文件

```python
from app.entity.meta import FuelType, ShipType, TimeZone # noqa: F401
from sqlmodel import SQLModel

target_metadata = SQLModel.metadata
```


### 创建迁移脚本

```shell
alembic revision --autogenerate -m "create meta data" # 自动生成
alembic revision -m "insert meta data" # 手动
```

### 执行迁移脚本

```shell
alembic upgrade head
```

### 所有操作

| 操作 | Alembic 命令 |
| --- | --- |
| 初始化迁移工具 | alembic init alembic |
| 生成迁移文件(自动) | alembic revision --autogenerate -m "<message>" |
| 生成迁移文件(手动) | alembic revision -m "<message>" |
| 应用迁移 | alembic upgrade head |
| 回滚迁移 | alembic downgrade <revision_id> |
| 检查数据库差异 | alembic current |
