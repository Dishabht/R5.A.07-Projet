from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB (le host est "mongo-db" car c'est le nom du service docker-compose)
client = MongoClient("mongodb://mongo-db:27017/")
db = client["mydb"]
collection = db["products"]

@app.route("/products")
def get_products():
    products = list(collection.find({}, {"_id": 0}))
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
