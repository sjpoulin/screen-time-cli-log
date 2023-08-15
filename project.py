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

    options = ['log', 'graph', 'exit']

    while True:
        print(menu())
        option = input("What would you like to do? ")
        if option.lower() not in options:
            print("Please select from one of the listed options.\n")
            continue
        elif option.lower() == "exit":
            print("Goodbye.")
            break

        date, hours = fetch_data()

        cur.execute('''INSERT INTO screentime (date, hours) VALUES (?, ?)''', (date, hours))
        conn.commit()
        print("Logged")

        graph_data(conn)

        cur.close()
        conn.close()

def fetch_data():
    # TODO: regex for dates
    date = input("Date: ")
    while True:
        try:
            hours = int(input("Hours: "))
            break
        except ValueError:
            print("Input must be a number.")
            continue
    return date, hours

def graph_data(conn):
    cur = conn.cursor()
    cur.execute('''SELECT date, hours FROM screentime''')
    data = cur.fetchall()

    dates = []
    hours = []

    for row in data:
        dates.append(row[0])
        hours.append(row[1])

    dates = sorted(dates)

    plt.plot(dates, hours)

    plt.xlabel("Date")
    plt.ylabel("Hours of Screen Time")
    plt.title("My Screen Time")

    plt.show()

def menu():
    return "Welcome to Screentime!\n\nType 'log' to log an entry\nType 'graph' to view a graph of your screen time\nType 'exit' to exit"


if __name__ == "__main__":
    main()