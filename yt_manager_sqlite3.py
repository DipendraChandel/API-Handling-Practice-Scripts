import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id      INTEGER PRIMARY KEY,
                name    TEXT NOT NULL,
                time    TEXT NOT NULL
            )
''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)


def add_video(name, time):
    
    cur.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_video(vid_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, vid_id))
    conn.commit()

def delete_video(vid_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (vid_id,))
    conn.commit()

def main():
    try:
        while True:
            print("\n Youtube Manager | Choose an Option from 1 to 5")
            print("1. list all Youtube videos. ")
            print("2. Add a youtube video. ")
            print("3. Update a youtube video details. ")
            print("4. Delete a youtube video. ")
            print("5. Exit the app. ")

            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    list_videos()
                
                case '2':
                    name = input("Enter Video Name: ")
                    time = input("Enter Video Time: ")

                    add_video(name, time)


                case '3':
                    vid_id = input("Enter Video ID to update: ")
                    name = input("Enter Video Name: ")
                    time = input("Enter Video Time: ")

                    update_video(vid_id, name, time)

                case '4':
                    vid_id = input("Enter Video ID to Delete: ")
                    delete_video(vid_id)

                case '5':
                    break
                
                case _:
                    print("Invalid Choice!")
    
    except Exception as e:
        print(str(e))

    finally:
        conn.close()

if __name__ == "__main__":
    main()