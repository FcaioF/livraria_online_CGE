from flask import Flask, jsonify, request
from flask_cors import CORS
from tools.postgre_tools.postgre_connection_tools import *
from json_tools.Jtools import *

app = Flask(__name__)

#enabling CORS to all requests
CORS(app)

"""start books routes"""
#insert new books in the database
@app.route('/books',methods = ['POST'])
def insert_books():
    raw_data = order_json_data(request.get_json(),'BOOK')
    for i in raw_data:
        insert_book_data(postgree_connect(), i)

    return jsonify(api_return= 'data inserted')

#get all books
@app.route('/books', methods=['GET'])
def select_books():
    raw_data= get_books(postgree_connect())
    return format_json(raw_data,'BOOK')
#get books by id
@app.route('/books/<int:id>',methods = ['GET'])
def select_book_by_id(id):
    raw_data= get_books_by_id(postgree_connect(),(id,))
    return format_json(raw_data,'BOOK')

#edit book data
@app.route('/books/<int:id>',methods= ['PUT'])
def edit_book_data(id):
    _json_data = order_json_data(request.get_json(), 'BOOK')[0]
    print(_json_data)
    _raw_data = update_book_data(postgree_connect(), (_json_data.values(),id))

    return jsonify(api_return= str(_raw_data))

# #edit books price
# @app.route('/books_price/<int:id>',methods= ['PUT'])
# def edit_book_price(id):
#     _json_data = list(
#         request
#         .get_json()
#         .values()
#     )[0]
#     _raw_data= update_book_price(postgree_connect(), (_json_data,id))
#
#     return jsonify(api_return= str(_raw_data))
#
# #edit books quantity
# @app.route('/books_quantity/<int:id>', methods=['PUT'])
# def edit_book_quantity(id):
#     _json_data = list(
#         request
#         .get_json()
#         .values()
#     )[0]
#     _raw_data = update_book_quantity(postgree_connect(), (_json_data, id))
#     print(_raw_data)
#
#     return jsonify(api_return=str(_raw_data))

#delete books
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_books_by_id(id):
    delete_books(postgree_connect(),(id,))
    return jsonify(api_return=str('book deleted'))
"""end books routes"""


"""start client routes"""
#insert new clients in the database
@app.route('/clients',methods = ['POST'])
def insert_clients():
    raw_data = order_json_data(request.get_json(),'CLIENTS')
    for i in raw_data:
        insert_clients_data(postgree_connect(), i)

    return jsonify(api_return= 'data inserted')

#get all clients
@app.route('/clients', methods=['GET'])
def select_clients():
    raw_data= get_clients(postgree_connect())
    return format_json(raw_data,'CLIENTS')
#get clients by id
@app.route('/clients/<int:id>',methods = ['GET'])
def select_clients_by_id(id):
    raw_data= get_clients_by_id(postgree_connect(),(id,))
    return format_json(raw_data,'CLIENTS')

#edit clients data
@app.route('/clients/<int:id>',methods= ['PUT'])
def edit_clients_by_id(id):
    _json_formated = tuple(
        order_json_data(request.get_json(), 'CLIENTS')[0]
        .values()
    )
    _raw_data= update_clients_data(postgree_connect(),_json_formated + (id,))

    return jsonify(api_return= str(_raw_data))

#delete books
@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_clients_by_id(id):
    delete_clients(postgree_connect(),(id,))
    return jsonify(api_return=str('book deleted'))


"""end client routes"""

app.run(port=5000,host='localhost',debug=True)