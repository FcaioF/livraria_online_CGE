function consultarLivros(event, form) {
    event.preventDefault();

    const idClient = document.Consultar.IdClient.value;

    if (idClient !== "") {
        const URL = 'http://localhost:5000/clients/' + idClient;
        fetch(URL, { method: 'GET'})
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na resposta da API');
                }
                return response.json();
            })
            .then(data => mostrarResposta(data))
            .catch(error => console.log('Erro na requisição:', error));
    }
}

function mostrarResposta(data) {
    //alert('Dados buscados com sucesso!!');
    //inserindo registros da api no formulario
    document.Consultar.DateRegister.value = data[0].DATE_REGISTER;
    document.Consultar.Name.value = data[0].NAME;
    document.Consultar.Email.value = data[0].EMAIL;

    document.Consultar.DDD.value = data[0].DDD;
    document.Consultar.Cell.value = data[0].CELL;
    document.Consultar.Cpf.value = data[0].CPF;
    document.Consultar.Complement.value = data[0].COMPLEMENT;
    document.Consultar.Streets.value = data[0].STREETS;
    document.Consultar.City.value = data[0].CITY;
    document.Consultar.Uf.value = data[0].UF;
    document.Consultar.Cep.value = data[0].CEP;
}

 


/*

// Funções para carregar dados da API
function consultarLivros(event, form) {
    //Comando para prevenir o cancelamento de evento: click->buscar os dados
    event.preventDefault();
    //recebe variavel ra para consulta na API
    const idClient = document.Consultar.IdClient.value
    console.log(idClient)

    if ( idClient != "" ) { 
        //RA não pode ser null, pois através dele para buscar dados
        //Endereco api
        const URL = 'http://localhost:5000/clients/'+ idClient;
        //fetch(URL , options)
        fetch( URL , {method: 'GET', mode: 'no-cors'} )
            
            //Uma Arrow function é exatamente como uma função/callback normal 
            //para transformar a resposta de texto puro para JSON  
            .then(resp => resp.json())                                    
            .then(data => mostrarResposta(data))
            //Além disso podemos utilizar o método catch() para tratar erros.
            //e a mensagem de erros estará console
            .catch(erro => console.log(erro));
        }

//Uma função para mostar uma mensagem e os dados buscados
function mostrarResposta(data){
    alert("Dados buscados com sucesso !!"); //pode ter ou não
    console.log(data) ;
    //colocando os dados buscados nos campos do formulário  
    //document.Consultar.IdClient.value = data.information.ID_CLIENT;
    document.Consultar.Name.value = data.information.NAME;
    /*document.Consultar.txtTelefone.value = data.information.telefone;    
    }
}

*/



/*

function excluirLivro() {
    var livroId = document.getElementById("livroId").value;

    // Verifica se o ID do livro foi fornecido
    if (livroId.trim() === "") {
        alert("Por favor, digite o ID do livro.");
        return;
    }

    // Lógica para chamar a API de exclusão com o livroId
    // Aqui você deve implementar a lógica para chamar a API de exclusão
    // e lidar com a resposta (por exemplo, exibir uma mensagem de sucesso ou erro).
    
    // Exemplo de chamada de API fictícia (substitua com sua lógica real):
    // deleteLivroAPI(livroId);

    // Limpa o campo após a exclusão
    document.getElementById("livroId").value = "";
}

 function inserirLivro() {
    // Coletar dados do formulário
    var novoLivro = {
        id: document.getElementById("inserirId").value,
        data: document.getElementById("inserirData").value,
        categoria: document.getElementById("inserirCategoria").value,
        titulo: document.getElementById("inserirTitulo").value,
        preco: document.getElementById("inserirPreco").value,
        descricao: document.getElementById("inserirDescricao").value,
        totaldisponivel: document.getElementById("inserirTotalDisponivel").value
        // Adicione mais campos conforme necessário
    };

    // Lógica para chamar a API de inserção com os dados do novo livro
    // Aqui você deve implementar a lógica para chamar a API de inserção
    // e lidar com a resposta (por exemplo, exibir uma mensagem de sucesso ou erro).

    // Exemplo de chamada de API fictícia (substitua com sua lógica real):
    // inserirLivroAPI(novoLivro);

    // Limpa os campos após a inserção
    document.getElementById("inserirId").value = "";
    document.getElementById("inserirData").value = "";
    document.getElementById("inserirCategoria").value = "";
    document.getElementById("inserirTitulo").value = "";
    document.getElementById("inserirPreco").value = "";
    document.getElementById("inserirDescricao").value = "";
    document.getElementById("inserirTotalDisponivel").value = "";            

    // Recarrega a tabela após a inserção
    carregarLivros();
}
*/