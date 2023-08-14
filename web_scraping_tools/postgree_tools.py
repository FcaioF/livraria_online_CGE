import psycopg2
import json

"""
path where the credentials 
is stored
"""
json_file= 'D:/caiof/Documents/GIT_Repos/web_scraping-books/postgree_credentials/postgree_credentials.json'

def postgree_connect():
    """
    read the json file
    and structure the python dict
    """
    _json_objct= (
        json
        .load(open(json_file))
    )

    try:
        _connection = psycopg2.connect(
            host=_json_objct['host'],
            database=_json_objct['database'],
            user=_json_objct['user'],
            password=_json_objct['password']
        )
        return _connection

    except Exception as e:
        print('Connection failed!!\nplease check your connection file\n',e)
        return

def insert_data(db_connection,data):
    pre_processing= [ (f"'{i}',") for i in list(data.values())[:-1] ]
    pre_processing.append(f"'{ list(data.values())[-1] }');")
    concat_string= str('\n'.join(pre_processing))
    insert_template= str('INSERT INTO books(process_date,book_category,book_title,book_price,book_description,upc_number,product_type,no_tax_price,w_tax_price,total_available,book_star) VALUES (')
    #execute the command in the database

    try:
        (
            db_connection
            .cursor()
            .execute(f'{insert_template + concat_string}')
        )

        #write the alteration in the database;
        (
            db_connection
            .commit()
        )

        # db_connection.fetchall()
        print('row added!')
    except:
        print('error in line: ',pre_processing)


