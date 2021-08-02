import models
from models import Pessoas, db_session


def insert():
    pessoa = Pessoas(nome='Carla',idade=45)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Carla').first()
    print(pessoa.idade)

def altera():
    pessoa = Pessoas.query.filter_by(nome="Hamir").first()
    pessoa.idade= 21
    pessoa.save()

def excluir():
    pessoa = Pessoas.query.filter_by(nome='Hamir').first()
    pessoa.delete()




if __name__ == '__main__':
   # insert()
   # altera()
   # excluir()
    consulta()