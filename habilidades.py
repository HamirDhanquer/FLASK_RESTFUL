from flask_restful import Resource, Api 

Listahabilidades = ['Python', 'Java','Flask','PHP','GO']
class Habilidades(Resource):
    def get(self):
        return Listahabilidades