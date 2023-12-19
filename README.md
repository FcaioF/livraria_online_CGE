# web scraping de livros da pagina books.toscrape


Este projeto tem como objetivo extrair informações sobre livros do site https://books.toscrape.com/
armazenar esses dados em uma banco de dados relacional PostgreSQL e disponibilizar para consumo atraves de uma api,  


a pagina web conta com 51 categorias de livros,
Os dados extraídos incluem:

* Categoria
* Titulo
* Preco
* Descrição
* Numero UPC
* Tipo do produto
* Preço sem impostos
* Preço com impostos
* Total de livros disponiveis
* avaliação do livro (1 a 5 estrelas) 

Os dados são armazenados em tempo real na base de dados PostgreSQL que possui tabela books com schema: 

- ID_BOOK SERIAL PRIMARY KEY
- DT_PROCESS_DATE TIMESTAMP NOT NULL
- DS_BOOK_CATEGORY VARCHAR(300) NOT NULL
- DS_BOOK_TITLE VARCHAR(300) NOT NULL
- NR_BOOK_PRICE VARCHAR(300) NOT NULL
- DS_BOOK_DESCRIPTION TEXT NOT NULL
- NR_UPC_NUMBER VARCHAR(300) NOT NULL
- TP_PRODUCT_TYPE VARCHAR(300) NOT NULL
- NR_NO_TAX_PRICE DECIMAL
- NR_W_TAX_PRICE DECIMAL
- NR_TOTAL_AVAILABLE VARCHAR(300) NOT NULL
- DS_BOOK_STAR VARCHAR(300) NOT NULL

## API
Para consumo dos dados foi criado uma API python usando a biblioteca FLASK 

 Atraves da API é possivel realizar operações de CRUD 
 cadastrar, consultar, atualizar e remover livros.

ao executar o script `book_api.py` e iniciar o servidor Flask na porta 5000. 
A API terá as seguintes rotas:

- `GET /books`: Retorna uma lista de todos os livros cadastrados no banco de dados.
- `GET /books/<int:id>`: Retorna os detalhes de um Livro específico pelo seu id.
- `POST /books`: Cadastra um novo livro no banco de dados. 
O corpo da requisição deve conter um objeto JSON com os seguintes atributos:
  * `DS_BOOK_CATEGORY`
  * `DS_BOOK_DESCRIPTION`
  * `DS_BOOK_TITLE`
  * `NR_BOOK_PRICE`
  * `NR_TOTAL_AVAILABLE`
- `PUT /books/<int:id>`: Atualiza os dados de um livro específico pelo seu id.
O corpo da requisição deve conter um objeto JSON com os seguintes atributos:
  * `DS_BOOK_CATEGORY`
  * `DS_BOOK_DESCRIPTION`
  * `DS_BOOK_TITLE`
  * `NR_BOOK_PRICE`
  * `NR_TOTAL_AVAILABLE`
- `DELETE /produtos/<int:id>`: Remove um livro específico pelo seu id do banco de dados.
