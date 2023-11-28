"""
biblioteca criada para desenvolver função que manipulam arquivos json

return_book_json_values(): Recebe um arquivo json ordena seguindo o schema da tabela books e devolve os valores em formato de tupla

format_json_output():recebe uma lista de tuplas,itera sobre cada tupla, converte em dicionario e armazena em uma lista de dicionarios
"""

"""
21/11/2023

alinhado que não faz sentido o usuario 
inserir os campos:

DT_PROCESS_DATE
NR_UPC_NUMBER
TP_PRODUCT_TYPE
NR_NO_TAX_PRICE
NR_W_TAX_PRICE
DS_BOOK_STAR 

"""
import datetime
import secrets

def return_book_json_values(json_file,operation = 'insert'):
    """
    Recebe um arquivo json
    ordena seguindo o schema da tabela books
    e devolve os valores em formato de tupla

    @param operation:
    'insert': retorna todos os campos da tabela insert
    'update': retorna somente campos que serão alterados do registro
    """
    def calculate_tax(base_price):
        """
        insere  15% de taxa
        sobre o valor do livro
        """
        try:
            base_price = float(base_price)
            priceWithTax = (base_price + (base_price * 15) / 100)
        except:
            priceWithTax = base_price
        return priceWithTax

    def gen_upc_number():
        """
        ao chamar esta funcao
        é gerado um hash de 16
        caracteres aleatoriamente
        """
        return secrets.token_hex(8)
    if(operation == 'insert'):
        order_json = {
            "DT_PROCESS_DATE": str(datetime.datetime.now()),
            "DS_BOOK_CATEGORY": json_file['DS_BOOK_CATEGORY'],
            "DS_BOOK_TITLE": json_file['DS_BOOK_TITLE'],
            "NR_BOOK_PRICE": json_file['NR_BOOK_PRICE'],
            "DS_BOOK_DESCRIPTION": json_file['DS_BOOK_DESCRIPTION'],
            "NR_UPC_NUMBER": gen_upc_number(),
            "TP_PRODUCT_TYPE": 'books',
            "NR_NO_TAX_PRICE": json_file['NR_BOOK_PRICE'],
            "NR_W_TAX_PRICE": calculate_tax(json_file['NR_BOOK_PRICE']),
            "NR_TOTAL_AVAILABLE": json_file['NR_TOTAL_AVAILABLE'],
            "DS_BOOK_STAR": "0" #por se tratar de um livro novo sempre inicia com 0

        }
    else:
        order_json = {
            "DS_BOOK_CATEGORY": json_file['DS_BOOK_CATEGORY'],
            "DS_BOOK_TITLE": json_file['DS_BOOK_TITLE'],
            "NR_BOOK_PRICE": json_file['NR_BOOK_PRICE'],
            "DS_BOOK_DESCRIPTION": json_file['DS_BOOK_DESCRIPTION'],
            "NR_TOTAL_AVAILABLE": json_file['NR_TOTAL_AVAILABLE'],

        }

    formated_data = tuple(order_json.values())

    return formated_data

def format_json_output(tupled_data):
    """
    recebe uma lista de tuplas,
    itera sobre cada tupla, converte em dicionario e armazena
    em uma lista de dicionarios
    """
    dict_list = []

    for data in tupled_data:
        formated_json = {
            'ID_BOOK': str(data[0]),
            'DT_PROCESS_DATE': data[1].strftime('%Y-%m-%d %H:%M:%S'),
            'DS_BOOK_CATEGORY': data[2],
            'DS_BOOK_TITLE': data[3],
            'NR_BOOK_PRICE': data[4],
            'DS_BOOK_DESCRIPTION': data[5],
            'NR_UPC_NUMBER': data[6],
            'TP_PRODUCT_TYPE': data[7],
            'NR_NO_TAX_PRICE': float(data[8]),
            'NR_W_TAX_PRICE': float(data[9]),
            'NR_TOTAL_AVAILABLE': data[10],
            'DS_BOOK_STAR': data[11],
        }
        dict_list.append(formated_json)

    return dict_list
