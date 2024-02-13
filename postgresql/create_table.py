import os

import pandas as pd
import psycopg2

from sqlalchemy import create_engine


# Configurações de conexão com o banco de dados
db_config = {
    "user": "posgresql",
    "password": "admin",
    "host": "localhost",
    "port": 5432,  # A porta do PostgreSQL que você mapeou para o host
    "database": "project_sales",
}


def file_generator(directory):
    """
    Generate individual files from a given directory.

    Parameters:
    - directory (str): Path to the directory containing files.

    Yields:
    str: The name of each individual file in the directory.
    """
    try:
        # Get the list of files in the directory
        files = os.listdir(directory)

        # Filter only files, excluding subdirectories
        files = [file for file in files if os.path.isfile(os.path.join(directory, file))]

        # Generate each file individually
        for file in files:
            yield file
    except OSError as e:
        print(f"Error listing files in {directory}: {e}")


def get_column_names(schema, table_name, connection_params):
    """
    Get column names of a table in a PostgreSQL database.

    Parameters:
    - schema (str): Schema name.
    - table_name (str): Name of the table.
    - connection_params (dict): Dictionary containing PostgreSQL database connection details.

    Returns:
    list or None: List of column names if successful, None if an error occurs.
    """
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**connection_params)

        # Execute a query to retrieve table information (columns)
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {schema}.{table_name} LIMIT 0")

            # Get column names
            column_names = [desc[0] for desc in cursor.description]

            return column_names

    except Exception as e:
        print(f"Error executing the query: {e}")
        return None

    finally:
        # Close the connection to the database
        if connection:
            connection.close()


def execute_sql_file(file_path, connection_params):
    """
    Execute SQL queries from a file in a PostgreSQL database.

    Parameters:
    - file_path (str): Path to the SQL file.
    - connection_params (dict): Dictionary containing PostgreSQL database connection details.

    Returns:
    None
    """
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor()

        # Read the content of the SQL file
        with open(file_path, "r") as sql_file:
            sql_query = sql_file.read()

        # Execute the content of the SQL file
        cursor.execute(sql_query)
        connection.commit()

        print("SQL file executed successfully.")

    except Exception as e:
        print(f"Error executing the SQL file: {e}")

    finally:
        # Close the connection to the database
        if connection:
            connection.close()


def insert_data(path_files, db_config):
    """
    Insert data from CSV files into PostgreSQL tables.

    Parameters:
    - path_files (str): Path to the directory containing CSV files.
    - db_config (dict): Dictionary containing PostgreSQL database connection details.

    Returns:
    None
    """
    for file_name in file_generator(path_files):

        csv_file_path = f"{path_files}{file_name}"

        # Table name in the database
        table_name = file_name[:-4]

        # Load data from the CSV file into a Pandas DataFrame
        data = pd.read_csv(csv_file_path, sep=";")
        data.columns = get_column_names("public", table_name, db_config)

        # Create a connection to the PostgreSQL database
        engine = create_engine(
            f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )

        # Insert data from the DataFrame into the PostgreSQL table
        data.to_sql(table_name, engine, if_exists="append", index=False)


if __name__ == "__main__":
    execute_sql_file("postgresql/init.sql", db_config)
    insert_data("data/", db_config)
