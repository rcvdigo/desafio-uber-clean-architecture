from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DbConnectionHandler:
    def __init__(self, connection_string: str):
        self.__connection_string = connection_string
        self.__engine = create_engine(self.__connection_string)
        self.__session = sessionmaker(bind=self.__engine)
    
    def __enter__(self):
        self.session = self.__session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
    
    def execute(self, query):
        return self.session.execute(query)
    
    def commit(self):
        self.session.commit()
