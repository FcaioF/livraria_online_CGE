//variaveis globais

const urlBaseApi = 'http://localhost:5000/books'

/*****
 funcoes auxiliares
******/

//exibe as informacoes na tela do usuario
function mostrarRespostaConsulta(data) {
    if (data.length !== 0) {
        document.getElementById('data').value = data[0].DT_PROCESS_DATE;
        document.getElementById('categoria').value = data[0].DS_BOOK_CATEGORY;
        document.getElementById('titulo').value = data[0].DS_BOOK_TITLE;
        document.getElementById('preco').value = data[0].NR_BOOK_PRICE;
        document.getElementById('descricao').value = data[0].DS_BOOK_DESCRIPTION;
        document.getElementById('totalDisponivel').value = data[0].NR_TOTAL_AVAILABLE;
    }
    else
        alert("Livro não localizado")
}

function limpaFormulario() {
    //limpa  o formulario
    document.getElementById('id').value = "",
    document.getElementById("data").value = "",
    document.getElementById("categoria").value = "",
    document.getElementById("titulo").value = "",
    document.getElementById("preco").value = "",
    document.getElementById("descricao").value = "",
    document.getElementById("totalDisponivel").value = ""
}

    function mostrarAlerta(data) {
        /*
        funcao exibe o retorno da api na
        console e em forma de alert para o usuario
         e limpa o formulario
        */
        console.log(data.api_return);  //mostrar objeto no "inspecionar"
        switch (data.api_return) {
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

    /*****
     funcoes CRUD
     ******/

//consulta livros por id
    function consultarLivrosId(event, form) {
        event.preventDefault();

        const idBook = document.getElementById('id').value;

        if (idBook !== "") {
            const URL = `${urlBaseApi}/${idBook}`;
            fetch(URL, {method: 'GET'})
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro na resposta da API');
                    }
                    return response.json();
                })
                .then(data => mostrarRespostaConsulta(data))
                .catch(error => console.log('Erro na requisição:', error));
        }
    }

//altera um registro baseado no id
    function editarLivros(event, form) {
        //comando usado para prevenir cancelamento do evento
        event.preventDefault();
        //variavel para obter o id do registro que sera alterado
        //cria json com os dados que serão alterados
        //uma lista para dados de configuração
        const dados = {
            ID_BOOK: document.getElementById('id').value,
            DT_PROCESS_DATE: document.getElementById('data').value,
            DS_BOOK_CATEGORY: document.getElementById('categoria').value,
            DS_BOOK_TITLE: document.getElementById('titulo').value,
            NR_BOOK_PRICE: document.getElementById('preco').value,
            DS_BOOK_DESCRIPTION: document.getElementById('descricao').value,
            NR_TOTAL_AVAILABLE: document.getElementById('totalDisponivel').value
        }
        const idBook = dados.ID_BOOK;
        const options = {
            method: 'PUT', //método 'put': para alterar os dados
            headers: {
                'Content-Type': 'application/json',
            },
            //De formato JSON para formato texto normal
            body: JSON.stringify(dados),
        };

        if (idBook != "") { //RA não pode ser null, pois através dele para buscar dados
            //Endereço do api que construimos
            const URL = `${urlBaseApi}/${idBook}`;
            //Realizar a operação de acordo com método definido
            fetch(URL, options)
                //para transformar a resposta de texto puro para JSON
                /*Uma Arrow function é exatamente como uma função/callback normal */
                .then(resp => resp.json())
                .then(data => mostrarAlerta(data))
                //Além disso podemos utilizar o método catch() para tratar erros.
                //e a mensagem de erros estará console
                .catch(erro => console.log(erro));
        }
    }
