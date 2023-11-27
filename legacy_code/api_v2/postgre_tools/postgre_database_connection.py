import psycopg2
import json

"""
path where postgre credentials stored
"""
json_file= '/archives/postgree_credentials/postgree_credentials.json'

def postgree_connect():
    """
   Le o arquivo json e
   tranforme em  dicionario python
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