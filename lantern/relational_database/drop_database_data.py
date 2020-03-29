import psycopg2

from database.config import DATABASE
from db_utils import clear_tables, drop_tables

if __name__ == "__main__":
    conn = psycopg2.connect(**DATABASE)
    with conn.cursor() as cursor:
        try:
            clear_tables(cursor)
            drop_tables(cursor)
            conn.commit()
        finally:
            if conn:
                conn.close()
