from typing import List

from fastapi import APIRouter, HTTPException

from app.model.mongo import ItemCreate, ItemInDB
from app.service.mongo import add_item, get_item, list_items, remove_item, update_item

api = APIRouter()


@api.get("/items/", summary="获取所有项目信息", response_model=List[ItemInDB])
async def get_items():
    items = await list_items()
    return items


@api.get("/items/{item_id}", summary="获取单个项目信息", response_model=ItemInDB)
async def get_item_by_id(item_id: str):
    item = await get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@api.post("/items/", summary="创建项目", response_model=ItemInDB)
async def create_item(item: ItemCreate):
    return await add_item(item)


@api.put("/items/{item_id}", summary="更新项目信息", response_model=ItemInDB)
async def update_item_by_id(item_id: str, item: ItemCreate):
    updated_item = await update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found or not updated")
    return updated_item


@api.delete("/items/{item_id}", summary="删除项目", response_model=ItemInDB)
async def delete_item(item_id: str):
    item = await remove_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
