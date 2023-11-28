//variaveis globais

const urlBaseApi = 'http://localhost:5000/books'

///funcoes auxiliares

function limpaFormulario(){
                //limpa  o formulario
                document.getElementById('inserirCategoria').value = "",
                document.getElementById("inserirTitulo").value = "",
                document.getElementById("inserirPreco").value = "",
                document.getElementById("inserirDescricao").value = "",
                document.getElementById("inserirTotalDisponivel").value = ""
}
function mostrarAlerta(data){
            /*
            funcao exibe o retorno da api na
            console e em forma de alert para o usuario
             e limpa o formulario
            */
            console.log(data.api_return) ;  //mostrar objeto no "inspecionar"
            switch(data.api_return) {
                case "row updated!":
                    alert("Livro alterado com sucesso")
                    break;
                case "data inserted":
                    alert("Livro Inserido com sucesso")
                    break;
                case "row deleted!":
                    alert("Livro deletado com sucesso")
                    break;
                default:
                    alert("Erro ao alterar registro")
                    break

            }
            limpaFormulario()
        }
 //*************** funcoes crud ***************

// Funcao insere 15 primeiros registros  da base de dados na tela inicial da aplicação
function consultarLivrosFull(event, form) {
    event.preventDefault();
    function preencherTabela(dados) {
            var tabela = document.getElementById('tabelaLivros').getElementsByTagName('tbody')[0];

            for (let i = 0; i < 20; i++) {
                var livro = dados[i];
                var linha = tabela.insertRow();

                // Propriedades da tabela boos
                var propriedades = [
                    'ID_BOOK',
                    'DT_PROCESS_DATE',
                    'DS_BOOK_CATEGORY',
                    'DS_BOOK_TITLE',
                    'NR_BOOK_PRICE',
                    'DS_BOOK_DESCRIPTION',
                    'NR_UPC_NUMBER',
                    'TP_PRODUCT_TYPE',
                    'NR_NO_TAX_PRICE',
                    'NR_W_TAX_PRICE',
                    'NR_TOTAL_AVAILABLE',
                    'DS_BOOK_STAR'
                ];

                for (let j = 0; j < propriedades.length; j++) {
                    var celula = linha.insertCell(j);
                    celula.textContent = livro[propriedades[j]];
                }
            }
        }

    fetch(urlBaseApi, {method: 'GET'})
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na resposta da API');
            }
            return response.json();
        })
        .then(data => preencherTabela(data))
        .catch(error => console.log('Erro na requisição:', error));

}
//funcao deleta registro baseado no id
function deletarLivro(event, form) {
    //comando usado para prevenir cancelamento do evento
    event.preventDefault();

    const idBook = document.getElementById('livroId').value;

    if (idBook !== "") {
        const URL = `${urlBaseApi}/${idBook}`;
        fetch(URL, { method: 'DELETE'})
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na resposta da API');
                }
                return response.json();
            })
            .then(data => mostrarAlerta(data))
            .catch(error => console.log('Erro na requisição:', error));
    }
}

//altera um registro baseado no id
function inserirLivro(event, form){
    function leDadosFormulario() {
    /*
    funcao realiza a leitura dos dados
    inseridos e transforma em um dicionario
     */

    const dados_formulario =  {
                DS_BOOK_CATEGORY: document.getElementById('inserirCategoria').value,
                DS_BOOK_TITLE: document.getElementById("inserirTitulo").value,
                NR_BOOK_PRICE: document.getElementById("inserirPreco").value,
                DS_BOOK_DESCRIPTION: document.getElementById("inserirDescricao").value,
                NR_TOTAL_AVAILABLE: document.getElementById("inserirTotalDisponivel").value
            };

    return dados_formulario
    }

    //comando usado para prevenir cancelamento do evento
    event.preventDefault();

    //cria json com os dados que serão alterados
    const dados = leDadosFormulario();
    //uma lista para dados de configuração
    const options = {
        method: 'POST', //método 'put': para alterar os dados
        headers: {
        'Content-Type': 'application/json',
        },
        //De formato JSON para formato texto normal
        body: JSON.stringify(dados),
    };

    fetch(urlBaseApi , options )
                //para transformar a resposta de texto puro para JSON
                /*Uma Arrow function é exatamente como uma função/callback normal */
                .then(resp => resp.json())
                .then(data => mostrarAlerta(data))
                //Além disso podemos utilizar o método catch() para tratar erros.
                //e a mensagem de erros estará console
                .catch(erro => console.log(erro));
}

// Chame a função ao carregar a página, passando os dados JSON como parâmetro
window.onload = consultarLivrosFull;



