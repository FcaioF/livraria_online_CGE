def insert_book_data(db_connection, data):
    """
    @param db_connection: conexão postgres
    @param data: tupla de dados respeitando o schema da tabela BOOKS
    """
    insert_template = ("""
    INSERT INTO books
    (
        DT_PROCESS_DATE,
        DS_BOOK_CATEGORY,
        DS_BOOK_TITLE,
        NR_BOOK_PRICE,
        DS_BOOK_DESCRIPTION,
        NR_UPC_NUMBER,
        TP_PRODUCT_TYPE,
        NR_NO_TAX_PRICE,
        NR_W_TAX_PRICE,
        NR_TOTAL_AVAILABLE,
        DS_BOOK_STAR
    ) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """)
    # execute the command in the database
    try:
        (
            db_connection
            .cursor()
            .execute(insert_template, data)
        )

        # write the alteration in the database;
        (
            db_connection
            .commit()
        )

        # db_connection.fetchall()
        print('row added!')
    except Exception as e:
        print('error when add register in databse\n', e, '\n', data)

    db_connection.close()

def read_book_data(db_connection,id=''):
    """

    @param db_connection:  conexão postgres
    @param id: caso id seja vazio realiza select full na tabela, caso passe um id valido executa select com clausula where
    @return: retorna dados consultados
    """
    _connection_cursor = db_connection.cursor()
    _select_id_template = """
        SELECT * 
        FROM books
        WHERE ID_BOOK = %s
        """

    _select_full_template = """
    select *
    from books
    """

    if (id != ''):
        tupled_id = (id,) #insere o id em uma tupla para ser usado na consulta sql
        _connection_cursor.execute(_select_id_template, tupled_id)

    else:
        _connection_cursor.execute(_select_full_template)

    return _connection_cursor.fetchall()

#function used to update register in book table based in id
def update_book_data(db_connection, data , id):
    """
    atualiza dados da tabela book
    """
    _concat_data = data + (id,) #inclui o id do livro na tupla com os dados que seram alterados.
    _update_template = (
        """
        UPDATE books
        SET DS_BOOK_CATEGORY = %s,
            DS_BOOK_TITLE = %s,
            NR_BOOK_PRICE = %s,
            DS_BOOK_DESCRIPTION = %s,
            NR_TOTAL_AVAILABLE = %s
        WHERE id_book = %s
        """
    )
    try:
        (
            db_connection
            .cursor()
            .execute(_update_template, _concat_data)
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
        return ('error when update register in databse\n', e, '\n', _concat_data)

def delete_books(db_connection,id):
    tupled_id = (id,)
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
            .execute(_delete_template,tupled_id)
        )

        #write the alteration in the database;
        (
            db_connection
            .commit()
        )
        db_connection.close()
        return 'row deleted!'
    except Exception as e:
        db_connection.close()
        return ('error when delete register in databse\n',e)



