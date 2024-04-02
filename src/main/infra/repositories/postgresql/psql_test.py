import os
from datetime import date
from src.main.infra.repositories.postgresql.settings.connection import DbConnectionHandler
from .postgresql import Postgresql
from sqlalchemy import text

# connection_str = os.getenv('POSTGRESQL_URI')
connection_str = 'postgresql://desafio_uber_clean_architecture_user:Q8zvXP8NJdZOH40fhLnI2O4qU4Wtc49m@dpg-co62k1cf7o1s73aae2dg-a.oregon-postgres.render.com:5432/desafio_uber_clean_architecture'
handler = DbConnectionHandler(connection_string=connection_str)

def test_execution():
    post = Postgresql()
    # response = post.select_postgresql_id(1)
    # response = post.select_postgresql()
    # request = {
    #             'name': 'Rodrigo C Vera',
    #             'age': 15,
    #             'value': 20,
    #             'date': date(2024, 4, 2),
    #             'key_pix': 'key_pix456',
    #             'source': 'source3',
    #             'to': 'to3',
    #             'subject': 'subject3',
    #             'body': 'body3',
    #             'phone_numbers': 'phone_numbers3'
    #         }
    # response = post.update_postgresql(
    #     filter=2,
    #     request=request
    #     )
    response = post.select_postgresql()
    
    
    print(f"\n\n\n\n{response}\n\n\n\n")



    # response = post.insert_postgresql(
    #     name='Rodrigo',
    #     age=19,
    #     value=10,
    #     date=date(2024, 4, 2),
    #     key_pix='key321',
    #     source='source2',
    #     to='to2',
    #     subject='subject2',
    #     body='body2',
    #     phone_numbers='phone_numbers2'
    # )

    # print(f"\n\n\n\n{response}\n\n\n\n")
    # psycopg2_conn = handler.get_engine().raw_connection()
    # cursor = psycopg2_conn.cursor()

    # # Cria a tabela messages
    # create_table_query = '''
    # CREATE TABLE IF NOT EXISTS messages (
    #     id SERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     age INTEGER NOT NULL,
    #     value FLOAT NOT NULL,
    #     date DATE NOT NULL,
    #     key_pix VARCHAR NOT NULL,
    #     source VARCHAR NOT NULL,
    #     "to" VARCHAR NOT NULL,
    #     subject VARCHAR NOT NULL,
    #     body VARCHAR NOT NULL,
    #     phone_numbers VARCHAR NOT NULL
    # )
    # '''
    # cursor.execute(create_table_query)
    # psycopg2_conn.commit()

    # # Insere dados na tabela messages
    # insert_query = '''
    # INSERT INTO messages (name, age, value, date, key_pix, source, "to", subject, body, phone_numbers)
    # VALUES ('John Doe', 30, 1000.50, '2024-04-02', 'key123', 'source1', 'destination@example.com', 'Test Subject', 'Test Body', '123-456-7890')
    # '''
    # cursor.execute(insert_query)
    # psycopg2_conn.commit()

    # Seleciona e imprime os dados da tabela messages
    # with handler:
    #     select_query = '''
    #     SELECT * FROM messages
    #     '''
    #     rows = handler.execute(text(select_query))

    #     for row in rows:
    #         print(row)
