from project import loaded, menu, credits
import sqlite3

conn = sqlite3.connect("screentime.db")

def test_loaded():
    assert loaded(conn) == "\nFile Loaded\n"
    
def test_menu():
    assert menu() == "Welcome to Screentime!\n\nType 'log' to log an entry\nType 'graph' to view a graph of your screen time\nType 'delete' to reset your data\nType 'credits' to view credits\nType 'exit' to exit"

def test_credits():
    assert credits() == "\nScreen Time CLI Log\nCopyright 2023 Spencer Poulin\nwww.github.com/sjpoulin\n"
