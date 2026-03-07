from pymongo import MongoClient

def get_database(db_name: str):
    CONNECTION_STRING = "mongodb://mongo:27017/test"
    client = MongoClient(CONNECTION_STRING)

    return client[db_name]


if __name__ == "__main__":
    dbname = get_database()