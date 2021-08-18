from connection import client as cl, test_connection, print_db_names


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    test_connection()  # Test db connection
    print_db_names()  # Show database list


if __name__ == '__main__':
    print_hi('PyCharm')

