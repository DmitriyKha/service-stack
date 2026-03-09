from pymongo import MongoClient

def get_database(db_name: str, username, password):
    CONNECTION_STRING = "mongodb://mongo:27017/"

    # client = MongoClient(f'mongodb://{username}:{password}@mongo:27017/?authSource=admin')
    client = MongoClient(f'mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0')
    
    return client[db_name]


if __name__ == "__main__":
    dbname = get_database()