from project import fetch_data, graph_data, menu


def test_menu():
    assert menu() == "Welcome to Screentime!\n\nType 'log' to log an entry\nType 'graph' to view a graph of your screen time\nType 'delete' to reset your data\nType 'exit' to exit"
