import psycopg2
from config import host, user, password, db_mame

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_mame
)
connection.autocommit = True
try:
#Version PSQL!
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        print(f'Version: {cursor.fetchone()}')
#CREATED TABLES!
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE users_test(
            id serial PRIMARY KEY,
            first_name varchar(150) NOT NULL,
            nick_name varchar(150) NOT NULL);"""
            )
            print('Table created!')
#Fill in the table!
            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO users_test (first_name, nick_name) VALUES
                ('Ruslan', 'ygwhitte');"""
                )
                print('...................................................................................................................................................................................................................')
                print('Table filled')
#Search of the table!
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT nick_name FROM users_test WHERE first_name = 'Ruslan';"""
                    )
                    print(cursor.fetchone())
# DROP TABLES!
                    with connection.cursor() as cursor:
                        cursor.execute(
                            """DROP TABLE users_test;"""
                        )
                        print('Table was deleted')
except Exception:
    print('ERROR with PSQL(')
