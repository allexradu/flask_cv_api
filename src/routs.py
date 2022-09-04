from flask_restful import Resource
from .utils import read_data_from_file


class Index(Resource):
    def get(self):
        data = {
            "api_points": [
                "http://127.0.0.1:5000/personal",
                "http://127.0.0.1:5000/experience",
                "http://127.0.0.1:5000/education",
                "http://127.0.0.1:5000/languages",
                "http://127.0.0.1:5000/skills"
            ]
        }
        return data


class Personal(Resource):
    def get(self):
        data = read_data_from_file()
        return data['cv']['personal']


class Experience(Resource):
    def get(self):
        data = read_data_from_file()
        return data['cv']['experience']


class Education(Resource):
    def get(self):
        data = read_data_from_file()
        return data['cv']['education']


class Languages(Resource):
    def get(self):
        data = read_data_from_file()
        return data['cv']['languages']


class Skills(Resource):
    def get(self):
        data = read_data_from_file()
        return data['cv']['skills']
