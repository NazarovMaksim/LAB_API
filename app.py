from flask import Flask, jsonify, request, abort
from config import app  # Абсолютный импорт из config.py
import structures.views  # Абсолютный импорт для views

# Обработчик ошибки 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

# Обработчик ошибки 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.route('/')
def hello_world():
    return jsonify({'app': 'Самые высокие здания и сооружения'})

app.json.ensure_ascii = False

if __name__ == '__main__':
    app.run(debug=True)
