from flask import Flask, jsonify, request
from web_scraping_tools.postgree_tools import *

app = Flask(__name__)

def format_json(raw_objects):
    _formated_data= list()
    for i in raw_objects:
        _formated_data.append(
            {
                'ID_BOOK': str(i[0]),
                'DT_PROCESS_DATE': i[1].strftime('%Y-%m-%d %H:%M:%S'),
                'DS_BOOK_CATEGORY': i[2],
                'DS_BOOK_TITLE': i[3],
                'NR_BOOK_PRICE': i[4],
                'DS_BOOK_DESCRIPTION': i[5],
                'NR_UPC_NUMBER': i[6],
                'TP_PRODUCT_TYPE': i[7],
                'NR_NO_TAX_PRICE': float(i[8]),
                'NR_W_TAX_PRICE': float(i[9]),
                'NR_TOTAL_AVAILABLE': i[10],
                'DS_BOOK_STAR': i[11],
            }
        )
    return _formated_data
@app.route('/books', methods=['GET'])
def get_books():
    _connection = postgree_connect().cursor()

    (
        _connection
        .execute('select * from books')

    )
    _jsonify_data= jsonify(format_json(connection.fetchall()))

    return _jsonify_data

@app.route('/books/<int:id>',methods = ['GET'])
def get_book_by_id(id):
    connection = postgree_connect().cursor()
    (
        connection
        .execute(f'select * from books where ID_BOOK = {id} ')
    )
    return format_json(connection.fetchall())


app.run(port=5000,host='localhost',debug=True)