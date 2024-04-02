from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DbConnectionHandler:
    def __init__(self, connection_string: str = 'postgresql://desafio_uber_clean_architecture_user:Q8zvXP8NJdZOH40fhLnI2O4qU4Wtc49m@dpg-co62k1cf7o1s73aae2dg-a.oregon-postgres.render.com:5432/desafio_uber_clean_architecture'):
        self.__connection_string = connection_string
        self.__engine = create_engine(self.__connection_string)
        self.__Session = sessionmaker(bind=self.__engine)
    
    def __enter__(self):
        self.session = self.__Session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
    
    def execute(self, query):
        return self.session.execute(query)
    
    def commit(self):
        self.session.commit()
