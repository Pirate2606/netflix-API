from flask import Flask
from flask_restful import Api, Resource
import data_analysis

app = Flask(__name__)
api = Api(app)


class AllTitles(Resource):
    def get(self):
        return data_analysis.get_all_titles()


class Info(Resource):
    def get(self, title):
        return data_analysis.get_info_title(title)


class ShowType(Resource):
    def get(self, type_):
        return data_analysis.get_type(type_)


class Directors(Resource):
    def get(self, director):
        return data_analysis.get_directors(director)


class Years(Resource):
    def get(self):
        return data_analysis.get_year()


class ParticularYear(Resource):
    def get(self, year):
        return data_analysis.get_particular_year(year)


api.add_resource(AllTitles, '/titles')
api.add_resource(Info, '/title/<string:title>')
api.add_resource(ShowType, '/type/<string:type_>')
api.add_resource(Directors, '/director/<string:director>')
api.add_resource(Years, '/years')
api.add_resource(ParticularYear, '/year/<int:year>')


if __name__ == '__main__':
    app.run()
