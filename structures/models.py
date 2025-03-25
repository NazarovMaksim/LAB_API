from config import db

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Страна', db.String(100), nullable=False)

    cities = db.relationship("City", back_populates="country")

    def __repr__(self):
        return f"id: {self.id}, Страна: {self.name}"

class TypeBuilding(db.Model):
    __tablename__ = 'type_building'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column('Тип', db.String(50), nullable=False)

    buildings = db.relationship("Building", back_populates="type_building")

    def __repr__(self):
        return f"id: {self.id}, Тип: {self.type}"

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Город', db.String(100))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    country = db.relationship("Country", back_populates="cities")
    buildings = db.relationship("Building", back_populates="city")

    def __repr__(self):
        return f"id: {self.id}, Город: {self.name}, country_id: {self.country_id}"

class Building(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Название', db.String(200))
    type_building_id = db.Column(db.Integer, db.ForeignKey('type_building.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    year = db.Column(db.Integer)
    height = db.Column(db.Integer)

    type_building = db.relationship("TypeBuilding", back_populates="buildings")
    city = db.relationship("City", back_populates="buildings")

    def __repr__(self):
        return (f"id: {self.id}, Здание: {self.title}, type_building_id: {self.type_building_id}, "
                f"city_id: {self.city_id}, Год: {self.year}, Высота: {self.height}")

def get_all_buildings():
    return Building.query.all()

def get_building(building_id):
    query = Building.query.filter(Building.id == building_id).one_or_none()
    return query

def insert_building(new_building):
    building = Building(
        title=new_building['title'],
        type_building_id=new_building['type_building_id'],
        city_id=new_building['city_id'],
        year=new_building['year'],
        height=new_building['height']
    )
    db.session.add(building)
    db.session.commit()
    return building
