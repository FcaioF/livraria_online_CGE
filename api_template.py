from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'process_date': '2023-08-16 22:46:03.705','book_category': 'Mystery','book_title': 'Sharp Objects','book_price': 47.82, 'book_description': 'WICKED above her hipbone GIRL across her heart Words are like a road map to reporter Camille Preaker’s troubled past Fresh from a brief stay at a psych hospital Camille’s first assignment from the second-rate daily paper where she works brings her reluctantly back to her hometown to cover the murders of two preteen girls NASTY on her kneecap BABYDOLL on her leg Since WICKED above her hipbone GIRL across her heart Words are like a road map to reporter Camille Preaker’s troubled past Fresh from a brief stay at a psych hospital Camille’s first assignment from the second-rate daily paper where she works brings her reluctantly back to her hometown to cover the murders of two preteen girls NASTY on her kneecap BABYDOLL on her leg Since she left town eight years ago Camille has hardly spoken to her neurotic hypochondriac mother or to the half-sister she barely knows: a beautiful thirteen-year-old with an eerie grip on the town Now installed again in her family’s Victorian mansion Camille is haunted by the childhood tragedy she has spent her whole life trying to cut from her memory HARMFUL on her wrist WHORE on her ankle As Camille works to uncover the truth about these violent crimes she finds herself identifying with the young victimsa bit too strongly Clues keep leading to dead ends forcing Camille to unravel the psychological puzzle of her own past to get at the story Dogged by her own demons Camille will have to confront what happened to her years before if she wants to survive this homecomingWith its taut crafted writing Sharp Objects is addictive haunting and unforgettable more',
     'npc_number': 'e00eb4fd7b871a48', 'product_type': 'books', 'no_tax_price': 47.82, 'w_tax_price': 47.82, 'total_available': 20, 'book_star': 4 }
]

#Consultar (todos)

@app.route('/books',methods=['GET'])
def obter_livros():
    return jsonify(books)

#Consultar por ID
@app.route('/books/<int:id>',methods = ['GET'])
def obter_livro_por_id(id):
    for livro in books:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar
@app.route('/books/<int:id>',methods= ['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(books):
        if livro.get('id') == id:
            books[indice].update(livro_alterado)
            return jsonify(books[indice])
        
#Criar
@app.route('/books',methods = ['POST'])
def incluir_livro_novo():
    livro_novo = request.get_json()
    books.append(livro_novo)
    return jsonify(books)

#Excluir
@app.route('/books/<int:id>', methods=['DELETE'])
def excluir_books(id):
    for indice, livro in enumerate(books):
        if livro.get('id') == id:
            del books[indice]

            return jsonify(books)



app.run(port=5000,host='localhost',debug=True)
