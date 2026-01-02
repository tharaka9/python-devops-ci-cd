from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Cloud-Native Python DevOps App",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/favicon.ico")
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)