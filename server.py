from flask import Flask, request, jsonify
import os

app = Flask(__name__)

valid_keys = {
    "ABC123": {"status": "active"},
    "DEF456": {"status": "banned"},
    "FREE789": {"status": "active"}
}

@app.route('/auth', methods=['POST'])
def auth():
    data = request.json
    user_key = data.get('key')
    if user_key in valid_keys:
        return jsonify({"status": valid_keys[user_key]["status"]})
    return jsonify({"status": "invalid"}), 403

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
