from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

app = Flask(__name__)

mongo_uri=os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client[os.getenv("DB_NAME")]
collection = db[os.getenv("COLLECTION_NAME")]
print(mongo_uri,'mongo_uri')

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    collection.insert_many(data)
    return jsonify({"message": "Data saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)
