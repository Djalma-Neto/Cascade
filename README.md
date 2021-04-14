<body class="px-3">
<div class="d-flex justify-content-center py-2"><h1>Cascade on Windows</h1></div>
<div class="py-2">
    <div class="bg-info py-2">
        <div class="d-flex justify-content-center">ATENÇÃO</div>
        <div class="d-flex justify-content-center">PARA EXECUTAR ESSE PASSOA A PASSO NO LINUX SERÁ 
            NECESSARIO MUDAR ALGUMAS LINHAS DE CÓDIGO POIS A SINTAXE IRÁ MUDAR!!
        </div>
    </div>
</div>

<div class="py-4">
    <div class="bg-warning py-2">
        <div class="d-flex justify-content-center">ATENÇÃO</div>
        <div class="d-flex justify-content-center">OS PASSOS A SEGUIR PODEM SER EXECUTADOS UM POR VEZ OU SE PREFERIR PODE USAR
            O ARQUIVO "executarTreiner.py" QUE TODOS OS PASSOS SERÃO EXECUTADOS NA ORDEM CORRETA DE FORMA ALTOMATICA!!
        </div>
        <p class="bg-dark text-light"> > python executarTreiner.py</p>
    </div>
</div>
        

<div class="bg-light py-6">
    <h3>1º - É necessario ter instalado as seguintes ferramentas</h3>
    <li class="bg-white">Python</li>
    <li class="bg-light">Numpy</li>
    <li class="bg-white">OpenCV</li>
</div>

<div class="bg-light py-5">
    <h3>2º Baixando o Dataset De Imagens</h3>
    <h5 class="bg-light">Positivas</h5>
    <p class="bg-white">Imagens do objeto que se deseja detectar, contém diferentes representações
        do objeto que se deseja detectar sob diferentes perspectivas, condições de iluminação, tamanhos e etc.</p>
    <h5 class="bg-light">Negativas</h5>
    <p class="bg-white">Imagens sem o objeto que se deseja detectar.Contém tudo o que não se deseja detectar com o modelo.</p>


<p class="bg-light">Ao executar o arquivo download.py sera criado alguns diretorios necessarios para o treinamento entre eles estará "negativas" onde ficara todas as imagens negativas:</p>
<p class="bg-dark text-light"> > python download.py</p>
</div>

<div class="py-4">
    <div class="bg-danger py-2">
        <div class="d-flex justify-content-center">ATENÇÃO</div>
        <div class="d-flex justify-content-center">É IMPORTANTE ABASTECER AS IMAGENS POSITIVAS COM IMAGENS
            SEM FUNDO(PNG), CONTENDO APENAS O OBJETO A SER IDENTIFICADO!!</div>
    </div>
</div>

<div class="bg-light py-5">
    <h3>3º - Removendo Imagens Falhas</h3>
    <p class="bg-light">Ao executar o arquivo imgFeia.py sera deletado do diretorio
        "negativas" as imagens que não fazem parte do rerpetório:</p>
    <p class="bg-dark text-light"> > python imgFeia.py</p>
</div>

<div class="bg-light py-5">
    <h3>4º - Renomeando Arquivos Da Pasta De Images</h3>
    <p class="bg-light">Ao executar o arquivo renomear.py sera renomeado todas as imagens do
        diretorio "negativas" para que fique mais facil identificalas:</p>
    <p class="bg-dark text-light"> > python renomear.py</p>
</div>

<div class="bg-light py-5">
    <h3>5º - Gerando Lista De Imagens Negativas</h3>
    <p class="bg-light">Ao executar o arquivo listar.py sera criado um arquivo "bg.txt" que irá
        armazenar o nome de todas as imagens:</p>
    <p class="bg-dark text-light"> > python listar.py</p>
</div>

<div class="bg-light py-5">
    <h3>6º - Criando Amostras</h3>
    <p class="bg-light">Ao executar o arquivo listar.py sera criado um arquivo "bg.txt" que irá
        armazenar o nome de todas as imagens:</p>
    <p class="bg-dark text-light"> > python amostras.py</p>
</div>

<div class="bg-light py-5">
    <h3>7º - Criando os Vetores</h3>
    <p class="bg-light">Ao executar o arquivo vetores.py sera criado um diretorio com vetores que
        serão usados no passo final do processo:</p>
    <p class="bg-dark text-light"> > python vetores.py</p>
</div>

<div class="bg-light py-5">
    <h3>8º - Treinando o Algoritmo</h3>
    <p class="bg-light">Ao executar o arquivo treinar.py sera iniciado o processo que fornecerá como
        saída um arquivo .xml para ser usado, para isso apos executar o aruivo ele ira pedir o numero de
        estágios(quanto maior mais preciso se torna, mas o tempo também aumenta):</p>
    <p class="bg-dark text-light"> > python treinar.py</p>
</div>

<script src="style/jquery.js" async defer></script>
<script src="style/bootstrap.js" async defer></script>
</body>