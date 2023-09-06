import re
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style

# Final project https://cs50.harvard.edu/python/2022/project/

def main():
    conn = sqlite3.connect("screentime.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS screentime(date TEXT, hours INTEGER)''')
    conn.commit()

    while True:
        print(menu())
        option = input("What would you like to do? ")
        if option.lower().strip() == "log":
            fetch_data(conn)
        elif option.lower().strip() == "graph":
            graph_data(conn)
            continue
        elif option.lower().strip() == "delete":
            delete(conn)
        elif option.lower().strip() == "credits":
            print(credits())
        elif option.lower().strip() == "exit":
            print("Goodbye.\n")
            cur.close()
            conn.close()
            break
        else:
            print("\nPlease select from one of the listed options.\n")
            continue

def fetch_data(conn):
    cur = conn.cursor()
    date = input("Date: ")
    while True:
        try:
            hours = int(input("Hours: "))
            break
        except ValueError:
            print("Input must be a number.")
            continue
    cur.execute('''INSERT INTO screentime (date, hours) VALUES (?, ?)''', (date, hours))
    conn.commit()
    print("\nLogged")
    return

def graph_data(conn):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM screentime ORDER BY date ASC''')
    data = cur.fetchall()

    dates = []
    hours = []

    for row in data:
        dates.append(row[0])
        hours.append(row[1])

    plt.plot(dates, hours)

    plt.xlabel("Date")
    plt.ylabel("Hours of Screen Time")
    plt.title("My Screen Time")

    plt.show()

def menu():
    return "Welcome to Screentime!\n\nType 'log' to log an entry\nType 'graph' to view a graph of your screen time\nType 'delete' to reset your data\nType 'credits' to view credits\nType 'exit' to exit"

def credits():
    return "\nScreen Time CLI Log\nCopyright 2023 Spencer Poulin\nwww.github.com/sjpoulin\n"

def delete(conn):
    cur = conn.cursor()
    while True:
        option = (input("\nAre you sure you want to reset? 'y' or 'n': "))
        if option.lower().strip() == 'y':
            cur.execute('''DELETE FROM screentime''')
            print("Data cleared\n")
            break
        elif option.lower().strip() == 'n':
            break
        else:
            print("\nPlease select 'y' or 'n'")
            continue

if __name__ == "__main__":
    main()