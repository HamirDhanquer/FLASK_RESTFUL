'''
SQLAlchemy 
'''
from sqlalchemy import create_engine,Column, Integer, String 
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)
    
    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

def init_db():
    Base.metadata.create_all(bind=engine)

def consulta(Pessoas):
    pessoa = Pessoas.query.all()
    print(pessoa)



if __name__ == '__main__':
    init_db()