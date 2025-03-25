from models import Building, TypeBuilding, Country, City
from config import ma, db


class TypeBuildingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeBuilding


class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        load_instance = True
        sqla_session = db.session

    country_id = ma.auto_field()


class BuildingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Building


building_cschema = BuildingSchema()
buildings_cschema = BuildingSchema(many=True)