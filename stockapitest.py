import requests

def stock_data_api():
    stocks = []

    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response = requests.get(url)
    stockApi = response.json()

    try:

        if stockApi["success"] and "data" in stockApi:
            stock_data = stockApi["data"]["data"]

            for i in stock_data:
                stockName = i.get("Name")
                marketCap = i.get("MarketCap")
                currentPrice = i.get("CurrentPrice")

                stocks.append({
                    "Name": stockName,
                    "Market Cap": marketCap,
                    "Current Price": currentPrice
                })
            return stocks
        
        else:
            raise Exception("Unable to fetch Data")
    except Exception as e:
        print(str(e))

# stock_data_api()


def main():
    try:
        stocks = stock_data_api()

        for stock in stocks:
            stockName = stock["Name"]
            marketCap = stock["Market Cap"]
            currentPrice = stock["Current Price"]

            print(f"Stock Name: {stockName},\nMarketCap: {marketCap},\nCurrent Price: {currentPrice}\n")
    
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()