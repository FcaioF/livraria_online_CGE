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

""" start book functions"""

#Returns all registers in the database
def get_books(db_connection):
    _connection = (
        db_connection
        .cursor()
    )
    (
        _connection
        .execute('select * from books')

    )
    return _connection.fetchall()

#Returns registers based in id
def get_books_by_id(db_connection, id):
    _connection = (
        db_connection
        .cursor()
    )
    _select_template = (
        """
        SELECT * 
        FROM books
        WHERE ID_BOOK = %s
        """
    )
    (_connection
     .execute(_select_template, id)
     )

    return _connection.fetchall()

def insert_book_data(db_connection, data):
    _pre_processing = tuple(data.values())
    insert_template = ("""
    INSERT INTO books
    (DT_PROCESS_DATE,DS_BOOK_CATEGORY,DS_BOOK_TITLE,NR_BOOK_PRICE,DS_BOOK_DESCRIPTION,NR_UPC_NUMBER,TP_PRODUCT_TYPE,NR_NO_TAX_PRICE,NR_W_TAX_PRICE,NR_TOTAL_AVAILABLE,DS_BOOK_STAR) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """)
    # execute the command in the database
    try:
        (
            db_connection
            .cursor()
            .execute(insert_template, _pre_processing)
        )

        # write the alteration in the database;
        (
            db_connection
            .commit()
        )

        # db_connection.fetchall()
        print('row added!')
    except Exception as e:
        print('error when add register in databse\n', e, '\n', _pre_processing)

    db_connection.close()


# function used to update book price based in id
def update_book_price(db_connection, data):
    _update_template = (
        """
        UPDATE books
        SET NR_BOOK_PRICE= '%s'
        WHERE id_book = %s
        """
    )
    try:
        (
            db_connection
            .cursor()
            .execute(_update_template, data)
        )

        # write the alteration in the database;
        (
            db_connection
            .commit()
        )

        db_connection.close()
        return ('row updated!')
    except Exception as e:
        db_connection.close()
        return ('error when update register in databse\n', e, '\n', data)




# function used to update the book quantity based in id
def update_book_quantity(db_connection, data):
    _update_template = (
        """
        UPDATE books
        SET NR_TOTAL_AVAILABLE= '%s'
        WHERE id_book = %s
        """
    )
    try:
        (
            db_connection
            .cursor()
            .execute(_update_template, data)
        )

        # write the alteration in the database;
        (
            db_connection
            .commit()
        )

        db_connection.close()
        return('row updated!')
    except Exception as e:
        db_connection.close()
        return(f'error when update register in databse\n{e}\n{data}')



def delete_books(db_connection,id):
    _delete_template=(
        """
        DELETE 
        FROM books 
        WHERE id_book = %s
        """
    )
    try:
        (
            db_connection
            .cursor()
            .execute(_delete_template,id)
        )

        #write the alteration in the database;
        (
            db_connection
            .commit()
        )

        # db_connection.fetchall()
        print('row deleted!')
    except Exception as e:
        print('error when delete register in databse\n',e,'\n',data)
    db_connection.close()



""" end book functions"""

def insert_client_data(db_connection, data):
    _pre_processing = tuple(data.values())
    insert_template = ("""
    INSERT INTO clients    
    (DATE_REGISTER,NAME,EMAIL,DDD,CELL,CPF,COMPLEMENT,STREETS,CITY,UF,CEP) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """)
    # execute the command in the database
    try:
        (
            db_connection
            .cursor()
            .execute(insert_template, _pre_processing)
        )

        # write the alteration in the database;
        (
            db_connection
            .commit()
        )

        # db_connection.fetchall()
        print('row added!')
    except Exception as e:
        print('error when add register in databse\n', e, '\n', _pre_processing)

    db_connection.close()




