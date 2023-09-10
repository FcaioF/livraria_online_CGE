from flask import Flask, jsonify, request
from web_scraping_tools.postgree_tools import *
from json_tools.Jtools import *
app = Flask(__name__)

#insert new books in the database
@app.route('/books',methods = ['POST'])
def insert_books():
    raw_data = order_json_data(request.get_json())
    for i in raw_data:
        insert_book_data(postgree_connect(), i)

    return jsonify(api_return= 'data inserted')


#get all books
@app.route('/books', methods=['GET'])
def select_books():
    raw_data= get_books(postgree_connect())
    return format_json(raw_data)
#get books by id
@app.route('/books/<int:id>',methods = ['GET'])
def select_book_by_id(id):
    raw_data= get_books_by_id(postgree_connect(),(id,))
    return format_json(raw_data)

#edit books price
@app.route('/books_price/<int:id>',methods= ['PUT'])
def edit_book_price(id):
    _json_data = list(
        request
        .get_json()
        .values()
    )[0]
    _raw_data= update_book_price(postgree_connect(), (_json_data,id))

    return jsonify(api_return= str(_raw_data))

#edit books quantity
@app.route('/books_quantity/<int:id>', methods=['PUT'])
def edit_book_quantity(id):
    _json_data = list(
        request
        .get_json()
        .values()
    )[0]
    _raw_data = update_book_quantity(postgree_connect(), (_json_data, id))
    print(_raw_data)

    return jsonify(api_return=str(_raw_data))



#delete books
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_books_by_id(id):
    delete_books(postgree_connect(),(id,))
    return format_json('book deleted')
app.run(port=5000,host='localhost',debug=True)