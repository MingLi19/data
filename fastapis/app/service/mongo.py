from bson import ObjectId

from app.model.mongo import ItemCreate, collection

# 业务逻辑层封装了对数据库操作的调用


async def list_items():
    items = []
    async for item in collection.find():
        items.append({"id": str(item["_id"]), "name": item["name"], "description": item["description"]})
    return items


async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        return None
    return {"id": str(item["_id"]), "name": item["name"], "description": item["description"]}


async def add_item(item: ItemCreate):
    item_dict = item.dict()
    result = await collection.insert_one(item_dict)
    return {**item_dict, "id": str(result.inserted_id)}


async def update_item(item_id: str, item: ItemCreate):
    existing_item = await get_item(item_id)
    if not existing_item:
        return None
    update_data = item.dict(exclude_unset=True)  # 只更新传递的字段
    result = await collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    if result.modified_count > 0:
        # 返回更新后的项目信息
        updated_item = await get_item(item_id)
        return updated_item
    return None


async def remove_item(item_id: str):
    item = await get_item(item_id)
    if item:
        await collection.delete_one({"_id": ObjectId(item_id)})
    return item
