from pymongo import MongoClient
from utils import simple_data_types, complex_data_types

client = MongoClient('mongodb://localhost:27017/')
db = client['index-wizard']

def setup_index_experiments(collection_schema, query):
    pass

print(complex_data_types["array"]["datetime"])
