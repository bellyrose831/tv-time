from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return jsonify({
        "message": "TV Tracker API is running"
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"})