from fastapi import APIRouter, Depends, FastAPI
from typing import Union
import auth.jwt_auth as auth
import products.service as product_services 
router  =APIRouter()



@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None, current_user: dict = Depends(auth.get_current_active_user)):
    await product_services.get_all_products()
    return {"item_id": item_id, "q": q}

@router.get('/products/')
async def get_products(current_user: dict = Depends(auth.get_current_active_user)):
    return await product_services.get_all_products()

@router.get('/products/{id}')
async def get_product(id: int, current_user: dict = Depends(auth.get_current_active_user)):
    product = await product_services.get_product_by_id(id)
    return product

@router.get('/products/tag/{tag}')
async def get_pro_by_tags(tag:str,current_user: dict = Depends(auth.get_current_active_user)):
    product = await product_services.get_product_by_tag(tag)
    return product if product else ({"error": "no product found with this tag"})

@router.get('/products/{id}/reviews')
async def get_reviews(id: int, current_user: dict = Depends(auth.get_current_active_user)):
    reviews = await product_services.get_product_reviews(id)
    return reviews if reviews else ({"error": "no reviews found for this product"})

@router.get('/products/category/{category}')
async def get_pro_by_category(category: str, current_user: dict = Depends(auth.get_current_active_user)):
    products = await product_services.get_product_by_category(category)
    return products if products else ({"error": "no product found" })