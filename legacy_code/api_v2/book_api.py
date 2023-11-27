"""
import biblioteca usada para se conectar com banco de dados
"""
from postgre_tools.postgre_database_connection import postgree_connect
"""
import biblioteca que realiza 
convesao de dados json em tupla
"""
from jsonTools.JTools import return_book_json_values, format_json_output
"""
import biblioteca usada pra 
realizar operacoes de crud no banco de dados
"""
from postgre_tools.crud_book import *
"""
Import bibliotecas flask
"""
from flask import Flask, request, jsonify
from flask_cors import CORS

"""
Instanciando objeto flask
"""
app = Flask(__name__)

"""
habilitando CORS para todas 
requisicoes da api
"""
CORS(app)

@app.route('/books',methods = ['POST'])
def insert_books():
    """
    funcao insere novos registros na
    base de dados
    """
    new_book_data =  return_book_json_values(request.get_json())
    insert_book_data(postgree_connect(),new_book_data )
    return jsonify(api_return= 'data inserted')

#get all books
@app.route('/books', methods=['GET'])
def select_books():
    """
    funcao realiza  select full na base de dados e
    retorna todos os registros
    """
    raw_data = read_book_data(postgree_connect())
    formated_data = format_json_output(raw_data) #realiza formatacao dos dados
    return jsonify(formated_data)

#get books by id
@app.route('/books/<int:id>',methods = ['GET'])
def select_book_by_id(id):
    """
        funcao realiza  select com clausula where na base de dados
        trazendo apenas o registro solicitado
        """
    raw_data= read_book_data(postgree_connect(),id)
    formated_data = format_json_output(raw_data)  # realiza formatacao dos dados
    return jsonify(formated_data)

@app.route('/books/<int:id>',methods= ['PUT'])
def edit_book_data(id):
    """
    funcao realiza a
    alteracao de registro na tabela books
    """
    raw_edit_data = return_book_json_values(request.get_json())
    _updated_data = update_book_data(postgree_connect(),raw_edit_data,id)
    return jsonify(api_return= str(_updated_data))


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_books_by_id(id):
    object_message = delete_books(postgree_connect(),(id,))
    return jsonify(api_return=str(object_message))

app.run(port=5000,host='localhost',debug=True)