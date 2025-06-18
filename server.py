from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace or expand this dictionary with your keys
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
    app.run(host='0.0.0.0', port=5000)
