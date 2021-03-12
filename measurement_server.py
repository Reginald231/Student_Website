from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask.json import jsonify

db_connect = create_engine('sqlite:///measures.db')
app = Flask(__name__)
api = Api(app)


class Area(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from area")  # This line performs query and returns json result
        # return query.cursor.fetchall()
        return {'areas': [i[1] for i in query.cursor.fetchall()]}  # Fetches first column that is area_id


class Location(Resource):
    def get(self, area_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select name from location where location_area=%d " % int(area_id))# This line performs query and returns json result
        # return query.cursor.fetchall()
        return {'Locations': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is name.

class Measurements(Resource):
    def get(self, location_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select value from measurement where measurement_location=%d " % int(location_id))  # This line performs query and returns json result
        # return query.cursor.fetchall()
        return {'Measurements': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is measurement.


class Categories(Resource):

    def get(self, area):
        area = area.replace("_", " ")
        conn = db_connect.connect()  # connect to database
        query_string = "select area_id from area where name={} COLLATE NOCASE".format("'" + area + "'")

        query = conn.execute(query_string)
        area_ids = []
        categories_ids = []
        category_names = []
        for row in query.cursor:
            for elm in row:
                area_ids.append(elm)
        print(area_ids)

        for id in area_ids:
            query = conn.execute("select category_id from category_area where area_id=%d " % int(id))
            for row in query.cursor:
                for elm in row:
                    categories_ids.append(elm)
        print(categories_ids)

        for id in categories_ids:
            query = conn.execute("select name from category where category_id=%d " % int(id))
            for row in query.cursor:
                for elm in row:
                    category_names.append(elm)
        return jsonify(Categories=category_names)



class Average_Measurement(Resource):
    def get(self, area):
        area = area.replace("_", " ")
        print(area)
        conn = db_connect.connect()  # connect to database
        query_string = "select area_id from area where name={} COLLATE NOCASE".format("'" + area + "'")
        query = conn.execute(query_string)
        area_ids = []
        locations = []
        measurements = []
        for row in query.cursor:
            for elm in row:
                area_ids.append(elm)

        query_string = "select location_id from location where location_area={} COLLATE NOCASE".format(area_ids[0])
        query = conn.execute(query_string)
        for row in query.cursor:
            for elm in row:
                locations.append(elm)

        for location in locations:
            query_string = "select value from measurement where measurement_location={} COLLATE NOCASE".format(location)
            query = conn.execute(query_string)

            for row in query.cursor:
                for elm in row:
                    measurements.append(elm)
                    
        sum = 0
        for measurement in measurements:
            sum += measurement
        
        return jsonify(Average_Measurement=(sum/len(measurements)))


class Number_Locations(Resource):
    def get(self, area):
        print(area)
        area = area.replace("_", " ")
        print(area)
        conn = db_connect.connect()  # connect to database
        query_string = "select area_id from area where name={} COLLATE NOCASE".format("'" + area + "'")
        query = conn.execute(query_string)
        area_ids = []
        locations = []
        for row in query.cursor:
            for elm in row:
                area_ids.append(elm)
        print(area_ids[0])
        query_string = "select name from location where location_area={} COLLATE NOCASE".format(area_ids[0])
        query = conn.execute(query_string)
        for row in query.cursor:
            for elm in row:
                locations.append(elm)
        return jsonify(Number_of_Locations=len(locations))


api.add_resource(Area, '/area')  # Route_1
api.add_resource(Location,'/area/<area_id>/location')
api.add_resource(Measurements,'/area/<location_id>/measurement')
api.add_resource(Categories, '/area/<area>/category')
api.add_resource(Average_Measurement, '/area/<area>/average_measurement')
api.add_resource(Number_Locations, '/area/<area>/number_locations')

if __name__ == '__main__':
    app.run(port='5002')
