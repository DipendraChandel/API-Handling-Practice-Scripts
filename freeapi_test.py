import requests


def fetch_randomUser_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        city = user_data["location"]["city"]

        return username, country, city
    
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username, country, city = fetch_randomUser_freeapi()
        print(f"Username: {username},\nCountry: {country},\nCity: {city}")

    except Exception as e:
        print("Exception: ", str(e))


if __name__ == "__main__":
    main()