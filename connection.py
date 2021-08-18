import pymongo

user = "skript-dev-monitor"
password = "root"
client = pymongo.MongoClient("mongodb+srv://"+user+":"+password+"@skriptcluster.myp7l.mongodb.net/myFirstDatabase"
                                                                "?retryWrites=true&w=majority")
database = client["CE"]
collection = database["estudiantes"]


def test_connection():
    print(client.test)


def print_db_names():
    print(client.list_database_names())