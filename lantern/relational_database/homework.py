from typing import List
import psycopg2

from config import DATABASE


def task_1_add_new_record_to_db(conn) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        conn: psycopg connection

    Returns: 92 records

    """
    sql = """
    INSERT INTO customers (customer_name, contactname, address, city, postalcode, country)
    VALUES ('Thomas', 'Tom', 'Baker St. 221B', 'London', '774', 'UK')
    """
    # records = []
    # # "SELECT * FROM customers LIMIT 92"
    #
    # try:
    #     # connect to the PostgreSQL database
    #     conn = psycopg2.connect(**DATABASE)
    #     # create a new cursor
    #     cur = conn.cursor()
    #     # execute the INSERT statement
    #     # cur.execute(sql)
    #     # commit the changes to the database
    #     # conn.commit()
    #     cur.execute("SELECT * FROM customers LIMIT 92")
    #     records = cur.fetchall()
    #     # close communication with the database
    #     cur.close()
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    # return records
    return sql


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    pass


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    pass


def task_4_update_customer(cur):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    pass


def task_5_delete_the_last_customer(conn) -> None:
    """
    Delete the last customer

    Args:
        conn: psycopg connection
    """
    pass


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    pass


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    pass


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    pass


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    pass


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    pass


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    pass


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    pass


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    pass


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    pass


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    pass


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    pass


# if __name__ == '__main__':
#     result = "SELECT * FROM customers LIMIT 92"
#     print(result)
