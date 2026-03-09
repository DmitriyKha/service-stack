from pymongo import MongoClient

def get_database(db_name: str, username, password):
    CONNECTION_STRING = "mongodb://mongo:27017/"

    client = MongoClient(f'mongodb://{username}:{password}@mongo:27017/?authSource=admin')

    return client[db_name]


if __name__ == "__main__":
    dbname = get_database()