import requests

def get_randomJokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"

    response = requests.get(url)
    joke_api = response.json()

    if joke_api["success"] and "data":
        joke_data = joke_api["data"]
        joke_1 = joke_data["data"][0]["content"]

        return joke_1
    
    else:
        raise Exception("Failed to fetch jokes.")
        

def main():
    try:
        joke = get_randomJokes()
        print(joke)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()