def task_1_add_new_record_to_db(conn) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customername': 'Thomas',
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
    INSERT INTO customers (customername, contactname, address, city, postalcode, country)
    VALUES ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM customers;")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM customers WHERE country = 'Germany';")
    return cur.fetchall()


def task_4_update_customer(conn):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        conn: psycopg cursor

    Returns: 91 records with updated customer

    """
    sql = """
    UPDATE customers SET customername = 'Johnny Depp'
    WHERE customerid = (SELECT MIN(customerid) FROM customers);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def task_5_delete_the_last_customer(conn) -> None:
    """
    Delete the last customer

    Args:
        conn: psycopg connection
    """
    del_sql = """DELETE FROM customers WHERE customerid = 91;"""
    cur = conn.cursor()
    cur.execute(del_sql)
    conn.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("SELECT country FROM suppliers;")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("SELECT country FROM suppliers ORDER BY country DESC;")
    return cur.fetchall()


def task_8_count_customers_by_city(cur) -> list:
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records

    """
    cur.execute("SELECT COUNT(customerid), city FROM customers GROUP BY city ORDER BY city DESC;")
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur) -> list:
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("SELECT COUNT(*), country FROM customers GROUP BY country HAVING COUNT(*) > 10;")
    return cur.fetchall()


def task_10_list_first_10_customers(cur) -> list:
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("SELECT * FROM customers ORDER BY customerid LIMIT 10;")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur) -> list:
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 90 records
    """
    cur.execute("SELECT * FROM customers WHERE customerid > 11;")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    sql = """
    SELECT supplierid, suppliername, contactname, city, country FROM suppliers WHERE country IN ('USA', 'UK', 'Japan');
    """
    cur.execute(sql)
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur) -> list:
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql = """
    SELECT products.productname FROM products, suppliers
    WHERE country = 'Sweden' AND products.supplierid = suppliers.supplierid;
    """
    cur.execute(sql)
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur) -> list:
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    sql = """
    SET LOCAL lc_monetary = 'en_US.UTF-8';
    SELECT productid, productname, unit, price, country, city, suppliername
    FROM products, suppliers WHERE products.supplierid = suppliers.supplierid;
    """
    cur.execute(sql)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur) -> list:
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    sql = """
    SELECT customername, contactname, country, orderid
    FROM customers, orders WHERE customers.customerid = orders.customerid;
    """
    cur.execute(sql)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur) -> list:
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    sql = """
        SELECT customername, a.address as address, a.country as customercountry, 
        b.country as suppliercountry, b.suppliername 
        FROM customers as a FULL JOIN suppliers as b ON a.country = b.country 
        ORDER BY customercountry, suppliercountry;
        """
    cur.execute(sql)
    return cur.fetchall()
