import psycopg2

from config import DATABASE
from db_utils import init_tables, fill_tables

if __name__ == "__main__":
    conn = psycopg2.connect(**DATABASE)
    with conn.cursor() as cursor:
        try:
            init_tables(cursor)
            fill_tables(cursor)
            conn.commit()
        finally:
            if conn:
                conn.close()
