import re
import sqlite3
import matplotlib.pyplot as plt

# Final project https://cs50.harvard.edu/python/2022/project/

def main():
    conn = sqlite3.connect("screentime.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS screentime(name TEXT, date TEXT, hours INTEGER)''')
    conn.commit()

    print(loaded(conn))

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
            print("\nGoodbye.\n")
            cur.close()
            conn.close()
            break
        else:
            print("\nPlease select from one of the listed options.\n")
            continue

def loaded(conn):
    if conn:
        return "\nFile Loaded\n"
    else:
        return "\nFile not loaded\n"

def fetch_data(conn):
    cur = conn.cursor()
    name = input("Name: ")
    while True:
        date = input("Date: ")
        if re.search(r"^\d\d/\d\d$", date):
            break
        else:
            print("\nUser input: MM/DD\n")
            continue
    while True:
        try:
            hours = float(input("Hours: "))
            if hours < 0:
                print("Cannot have negative hours of screen time.")
                continue
            elif hours > 24:
                print("Cannot have more screen time than hours in a day.")
                continue
            else:
                break
        except ValueError:
            print("Input must be a number.")
            continue
    cur.execute('''INSERT INTO screentime (name, date, hours) VALUES (?, ?, ?)''', (name.lower().strip(), date, hours))
    conn.commit()
    print("\nLogged\n")
    return

def graph_data(conn):
    cur = conn.cursor()
    cur.execute('''SELECT DISTINCT name FROM screentime''')
    data = cur.fetchall()

    names = []
    for row in data:
        names.append(row[0])
    if len(names) == 0:
        print("\nNo information on file.\n")
        return

    while True:
        print("\nNames on file:")
        for name in names:
            print(name.capitalize())
        name = input("\nWhose data would you like to see? ")
        if name.lower() not in names:
            print("\nUser not found")
            continue
        else:
            break
    
    cur.execute('''SELECT * FROM screentime WHERE name = ? ORDER BY date ASC''', (name.lower(),))
    data = cur.fetchall()
    
    dates = []
    hours = []
    for row in data:
        dates.append(row[1])
        hours.append(row[2])

    plt.plot(dates, hours)

    plt.xlabel("Date")
    plt.ylabel("Hours of Screen Time")
    plt.title(f"{name.capitalize().strip()}'s Screen Time")

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
            conn.commit()
            print("Data cleared\n")
            break
        elif option.lower().strip() == 'n':
            break
        else:
            print("\nPlease select 'y' or 'n'")
            continue

if __name__ == "__main__":
    main()