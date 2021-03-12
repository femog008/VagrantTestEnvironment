import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Femogy@008",
                                  host="10.0.0.66",
                                  port="5432",
                                  database="postgres")
    #   "dbname='TestCsv' user='tester' host='10.0.0.66' password='Femogy@008'

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
finally:
    pass