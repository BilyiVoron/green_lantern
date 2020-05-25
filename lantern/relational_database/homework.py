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
    fields = "customername, contactname, address, city, postalcode, country"
    table = "customers"
    values = ("Thomas", "David", "Some Address", "London", "774", "Singapore")
    sql = (f"INSERT INTO {table} ({fields}) "
           f"VALUES {values};")
    with conn.cursor() as cur:
        cur.execute(sql)


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    table = "customers"
    fields = "*"
    sql = (f"SELECT {fields} "
           f"FROM {table};")
    cur.execute(sql)
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    table = "customers"
    fields = "*"
    conditions = "country = 'Germany'"
    sql = (f"SELECT {fields} FROM {table} "
           f"WHERE {conditions};")
    cur.execute(sql)
    return cur.fetchall()


def task_4_update_customer(conn):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        conn: psycopg cursor

    Returns: 91 records with updated customer

    """
    table = "customers"
    field = "customerid"
    conditions = "customername = 'Johnny Depp'"
    sql = (f"UPDATE {table} SET {conditions} "
           f"WHERE {field} = "
           f"(SELECT MIN({field}) FROM {table});")
    with conn.cursor() as cur:
        cur.execute(sql)


def task_5_delete_the_last_customer(conn) -> None:
    """
    Delete the last customer

    Args:
        conn: psycopg connection
    """
    table = "customers"
    field = "customerid"
    sql = (f"DELETE FROM {table} "
           f"WHERE {field} = "
           f"(SELECT MAX({field}) FROM {table});")
    with conn.cursor() as cur:
        cur.execute(sql)


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    table = "suppliers"
    field = "country"
    sql = (f"SELECT {field} "
           f"FROM {table};")
    cur.execute(sql)
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    table = "suppliers"
    field = "country"
    sql = (f"SELECT {field} "
           f"FROM {table} "
           f"ORDER BY {field} DESC;")
    cur.execute(sql)
    return cur.fetchall()


def task_8_count_customers_by_city(cur) -> list:
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records

    """
    table = "customers"
    field = "city"
    count_field = "customerid"
    sql = (f"SELECT COUNT({count_field}), city "
           f"FROM {table} "
           f"GROUP BY {field} "
           f"ORDER BY {field} DESC;")
    cur.execute(sql)
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur) -> list:
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    table = "customers"
    field = "country"
    count_fields = "*"
    sql = (f"SELECT COUNT({count_fields}), {field} "
           f"FROM {table} "
           f"GROUP BY {field} "
           f"HAVING COUNT({count_fields}) > 10;")
    cur.execute(sql)
    return cur.fetchall()


def task_10_list_first_10_customers(cur) -> list:
    """
    List first 10 customers from the table

    Results: 10 records
    """
    table = "customers"
    fields = "*"
    order_field = "customerid"
    sql = (f"SELECT {fields} "
           f"FROM {table} "
           f"ORDER BY {order_field} "
           f"LIMIT 10;")
    cur.execute(sql)
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur) -> list:
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 90 records
    """
    table = "customers"
    fields = "*"
    order_field = "customerid"
    sql = (f"SELECT {fields} "
           f"FROM {table} "
           f"ORDER BY {order_field} "
           f"OFFSET 11;")
    cur.execute(sql)
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    table = "suppliers"
    fields = "supplierid, suppliername, contactname, city, country"
    condition_field = "country"
    conditions = ("USA", "UK", "Japan")
    sql = (f"SELECT {fields} "
           f"FROM {table} "
           f"WHERE {condition_field} IN {conditions};")
    cur.execute(sql)
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur) -> list:
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    table_1 = "products"
    table_2 = "suppliers"
    field_table_1 = "products.productname"
    conditions = "country = 'Sweden' AND products.supplierid = suppliers.supplierid"
    sql = (f"SELECT {field_table_1} "
           f"FROM {table_1}, {table_2} "
           f"WHERE {conditions};")
    cur.execute(sql)
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur) -> list:
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    table_1 = "products"
    table_2 = "suppliers"
    fields = "productid, productname, unit, price, country, city, suppliername"
    conditions = "products.supplierid = suppliers.supplierid"
    change_money = "SET LOCAL lc_monetary = 'en_US.UTF-8'"
    sql = (f"{change_money}; "
           f"SELECT {fields} "
           f"FROM {table_1}, {table_2} "
           f"WHERE {conditions};")
    cur.execute(sql)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur) -> list:
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    table_1 = "customers"
    table_2 = "orders"
    fields = "customername, contactname, country, orderid"
    conditions = "customers.customerid = orders.customerid"
    sql = (f"SELECT {fields} "
           f"FROM {table_1}, {table_2} "
           f"WHERE {conditions};")
    cur.execute(sql)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur) -> list:
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    table_1 = "customers"
    table_2 = "suppliers"
    conditions = "a.country = b.country"
    order_fields = "customercountry, suppliercountry"
    sql = (f"SELECT a.customername, "
           f"a.address as address, "
           f"a.country as customercountry, "
           f"b.country as suppliercountry, b.suppliername "
           f"FROM {table_1} as a FULL JOIN {table_2} as b ON {conditions} "
           f"ORDER BY {order_fields};")
    cur.execute(sql)
    return cur.fetchall()
