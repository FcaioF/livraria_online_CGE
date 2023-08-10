# web_scraping-books
Repository created to store data engineering project that aims to collect data from a website


Ideia de portifolio retirado do site:https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823


Contexto do Desafio:
A Book Club é uma Startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários, cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele não queira oferecer outro livro em troca.

Umas das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Você é um Data Scientist contrato pela empresa para construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários. Porém, a Book Club não coleta e nem armazena os livros enviados pelos usuários.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

O nome do livro.
A categoria do livro.
O número de estrelas que o livro recebeu.
O preço do livro.
Se o livro está em Estoque ou não.
Os Dados do desafio:
Os dados para serem coletados e armazenados, estão disponíveis neste site. http://books.toscrape.com/

Esse site foi desenvolvido e disponibilizado especialmente para praticar web scraping. Não existe nenhum tipo de problema legal ao fazer a coleta de dados.

Como solucionar esse desafio?
Esse é um desafio de Data Engineering. Ele é bem mais complicado do que parece, mas é um ótimo exercício para você desenvolver habilidades de Programação e Engenharia de Softwares para criar pipeline de dados.

Eu vou deixar aqui um roteiro para você se orientar, ele pode ser modificado da forma que você preferir ou simplesmente ignorado. Provavelmente, você já tem um roteiro de resolução melhor para abordar esse desafio.

E o mais importante, tenha paciência, criar uma solução leva tempo, assuma uma postura resiliente e nunca desista, afinal você quer ser um Data Scientist e ganhar um ótimo salário, não quer?

Roteiro Sugerido para a Resolução:
Esse é o roteiro de resolução do desafio que eu sugiro:

Faça o web scraper, necessariamente, utilizando a linguagem Python.
Utiliza a biblioteca Selenium do Python para navegar entre os links das categorias e as páginas.
Utiliza a biblioteca BeautifulSoup do Python para coletar os dados das páginas HTML.
Instale no seu computador e configure um banco de dados Postgres.
Crie uma tabela para armazenar os dados.
Agende seu script para rodar todos os dias em um horário específico. ( Não tem problema armazenar dados repetidos, já que o site não tem atualizações diárias )
Garanta que seu script saiba lidar com possíveis erros e não pare de funcionar por qualquer problema ( internet lenta, página não encontrada, objeto não carregado, etc ).
Salve seu projeto em um repositório público Github ou Bitbucket.
Escreva o README com todos os passos necessários, para que outras pessoas consigam usar sua solução.
Tornar sua solução Profissionalmente Respeitada:
Crie sua solução modularizada. O Script em Python deve salvar um arquivo csv em alguma pasta da sua máquina e então outro script em bash, deve fazer a inserção dos dados no banco de dados.
Sincronize esse dois script ( Python para coletar e salvar os dados e o Bash script para inserir no banco Postgres ).
Faça o gerenciamento desses jobs utilizando o Airflow ( Framework de gerenciamento de Jobs ). Um script só pode rodar, quando o outro terminar.
Paraleliza seu script de coleta. Crie workers que trabalham em paralelo, cada um coleta e armazena os dados dos livros de uma página.
Vá em Frente!
Não existe caminho fácil, de curto prazo em nenhum profissão, muito menos em Data Science, mas existe o caminho certo. E o caminho certo é adquirir experiência através do desenvolvimento de projetos para mostrar sua capacidade.

Volto a repetir, os projetos do seu portfólio precisam demonstrar que você é tão capaz de resolver desafios de negócio quantos os Data Scientists que já atuam profissionalmente nas empresas.

Quando você conseguir solucionar esse desafio, armazena seus códigos no Github ou no Bitbucket e escreva um artigo, explicando como sua solução funciona, o contexto do problema e o resultado final. Faça gráficos a partir do seu banco de dados, para mostrar que você conseguiu coletar e armazenar os dados da Book Club.

