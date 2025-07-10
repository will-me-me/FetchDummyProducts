import requests


async def get_all_products():
    res = requests.get('https://dummyjson.com/products')
    if res.status_code == 200:
        try:
            data = res.json()
            print(len(data['products']))  # or loop over them
            return data['products']
        except ValueError:
            print("Response is not valid JSON.")
        except KeyError:
            print("Key 'products' not found in response.")
    else:
        print(f"Request failed: {res.status_code}")
        print(res.text)
        return None
    
async def get_product_by_id(id: int) -> dict:
    products = await get_all_products()
    if products:
        for product in products:
            if product['id'] == id:
                return product
    return{"error": "product not found"}

async def get_product_by_tag(tag: str) -> dict:
    products = await  get_all_products()
    if products:
        for product in products:
            if tag.lower() in product.get('tags', []):
                return products
    return {"error": "product not found"}

async def get_product_reviews(id: int) -> dict:
    product = await get_product_by_id(id)
    if product and 'reviews' in product:
        return product['reviews']
    
async def get_product_by_category(category: str) -> dict:
    products = await get_all_products()
    if products:
        filtered_products = [ product for product in products if product.get('category') == category.lower()]
        return filtered_products if filtered_products else {"error": "no product is found in this category"}