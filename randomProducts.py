import requests

def get_random_products():
    products = []

    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    product_api_data = response.json()

    if product_api_data["success"] and "data":
        product_data = product_api_data["data"]["data"]

        for items in product_data[:5]:
            category = items.get("category")
            price = items.get("price")
            title = items.get("title")
            p_id = items.get("id")

            products.append({
                "Product ID": p_id,
                "Category": category,
                "Price": price,
                "Title": title
            })
        
        return products

    else:
        raise Exception("Unable to Fetch Data!")

def main():
    try:
        products = get_random_products()

        for items in products:
            category = items.get("Category")
            price = items.get("Price")
            title = items.get("Title")
            p_id = items.get("Product ID")

            print(f"Product ID: {p_id},\nCategory: {category},\nTitle: {title},\nPrice: {price}\n")
    
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()