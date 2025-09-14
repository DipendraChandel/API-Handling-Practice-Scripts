import requests
import sqlite3

def randomBooks():
    books = []

    url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"

    response = requests.get(url)
    bookApi = response.json()

    if bookApi["success"] and "data" in bookApi:

        bookData = bookApi["data"]["data"]

        for book in bookData[:3]:
            bookId = book.get("id")
            volumeInfo = book.get("volumeInfo", {})

            title = volumeInfo.get("title")
            author = volumeInfo.get("authors")[0]
            publishedDate = volumeInfo.get("publishedDate")

            books.append({
                "Id": bookId,
                "Title": title,
                "Author": author,
                "Published Date": publishedDate,
                })

        return books
    
    else:
        print("Unable to fetch Data.")


def saveToDb(books):
    try:
        conn = sqlite3.connect('BooksData.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS books(title TEXT NOT NULL, author TEXT NOT NULL, pub_date DATE NOT NULL, book_id INT)
        ''')


        #inserting date to db
        for book in books:
            cur.execute(""" INSERT OR REPLACE INTO books (title, author, pub_date, book_id) VALUES (?, ?, ?, ?)
            """, (book["Title"], book["Author"], book["Published Date"], book["Id"])
            )
            
    
        conn.commit()
        conn.close()

    except Exception as e:
        print(str(e), 'savetoDb')




def main():
    # try:
    #     books = randomBooks()

    #     for book in books:
    #         b_id = book["Id"]
    #         title = book["Title"]
    #         author = book["Author"]
    #         publishedDate = book["Published Date"]

    #         print(f"Title: {title},\n Author: {author},\n Pubhised Date:  {publishedDate},\n Book Id:{b_id}\n")

    # except Exception as e:
    #     print(str(e))

    books = randomBooks()
    saveToDb(books)

    conn = sqlite3.connect("BooksData.db")
    cur = conn.cursor()

    cur.execute("SELECT  * FROM books")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
    


