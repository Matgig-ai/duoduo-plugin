
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
            "email": "contact@duoduo.fr",
            "phone": "+33 1 23 45 67 89"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
