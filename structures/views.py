from config import app  # Абсолютный импорт из config.py
from flask import jsonify, abort, request
from structures.models import get_all_buildings, get_building, insert_building  # Абсолютный импорт для моделей

# Маршрут для получения списка всех зданий
@app.route('/structures/api/v1/buildings', methods=['GET'])
def get_buildings():
    buildings = get_all_buildings()
    buildings_list = [
        {
            "id": b.id,
            "title": b.title,
            "type_building_id": b.type_building_id,
            "city_id": b.city_id,
            "year": b.year,
            "height": b.height
        }
        for b in buildings
    ]
    return jsonify({"buildings": buildings_list})

# Маршрут для получения одного здания по id
@app.route('/structures/api/v1/buildings/<int:id>', methods=['GET'])
def get_one_building(id):
    building = get_building(id)
    if building is None:
        abort(404)
    return jsonify({"building": str(building)})

# Маршрут для добавления нового здания (POST-запрос)
@app.route('/structures/api/v1/buildings', methods=['POST'])
def create_building():
    # Проверка на корректность данных (обязательные поля)
    if not request.json or 'title' not in request.json or 'type_building_id' not in request.json or 'city_id' not in request.json:
        abort(400, 'The request must contain the required fields: title, type_building_id, city_id.')

    # Получаем данные JSON из запроса
    new_building = request.get_json()

    # Устанавливаем значения по умолчанию, если они не переданы
    if 'height' not in request.json:
        new_building['height'] = 0
    if 'year' not in request.json:
        new_building['year'] = 2000

    # Вставляем новое здание в базу данных
    building_new = insert_building(new_building)

    # Возвращаем добавленную запись
    return jsonify({'building': str(building_new)}), 201
