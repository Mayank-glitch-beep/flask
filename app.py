from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def get_data():
    try:
        with open('data.json') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 500

if __name__ == '__main__':
    app.run(debug=True)