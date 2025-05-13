
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Duoduo API is live!"

@app.route("/services")
def services():
    return jsonify({
        "services": [
            "Conversion Rate Optimization (CRO)",
            "User Experience (UX)",
            "User Interface (UI)",
            "Shopify Development",
            "Webflow Design"
        ],
        "contact": {
            "website": "https://duoduo.fr",
            "email": "hello@duoduo.fr",
            "phone": "+33 6 64 11 55 74"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
