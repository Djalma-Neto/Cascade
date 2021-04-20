
# OpenCV e Cascade no Windows

<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="public/opencv.png" />
</h1>

<div style="background-color: red; border-radius: 10px;">
    <div align="center">ATENÇÃO</div>
    <div align="center">PARA EXECUTAR ESSE PASSOA A PASSO NO LINUX SERÁ 
        NECESSARIO MUDAR ALGUMAS LINHAS DE CÓDIGO POIS A SINTAXE IRÁ MUDAR!!
    </div>
</div>

<div style="margin-top: 10px; background-color: orange; border-radius: 10px;">
<div>
    <div align="center">ATENÇÃO</div>
    <div>OS PASSOS A SEGUIR PODEM SER EXECUTADOS UM POR VEZ OU SE PREFERIR PODE USAR
        O ARQUIVO "executarTreiner.py" QUE TODOS OS PASSOS SERÃO EXECUTADOS NA ORDEM CORRETA DE FORMA ALTOMATICA!!
    </div>
    <p style="background-color: gray;"> > python executarTreiner.py</p>
</div>
</div>

<div style="margin-top: 10px;" >
    <h3 style="font-weight: bold;">1º - É necessario ter instalado as seguintes ferramentas</h3>
    <li class="bg-white">Python</li>
    <li class="bg-light">Numpy</li>
    <li class="bg-white">OpenCV</li>
</div>

<div style="margin-top: 10px;">
<h3 style="font-weight: bold;">2º Baixando o Dataset De Imagens</h3>
<h5 align="center" style="font-weight: bold;">Positivas</h5>
<p class="bg-white">Imagens do objeto que se deseja detectar, contém diferentes representações
    do objeto que se deseja detectar sob diferentes perspectivas, condições de iluminação, tamanhos e etc.</p>
<h5 align="center" style="font-weight: bold;">Negativas</h5>
<p class="bg-white">Imagens sem o objeto que se deseja detectar.Contém tudo o que não se deseja detectar com o modelo.</p>


<p class="bg-light">Ao executar o arquivo download.py sera criado alguns diretorios necessarios para o treinamento entre eles estará "negativas" onde ficara todas as imagens negativas:</p>
<p style="background-color: gray;"> > python download.py</p>
</div>

<div style="padding: 10px; margin-top: 10px; background-color: orange; border-radius: 10px;">
    <div class="d-flex justify-content-center">ATENÇÃO</div>
    <div class="d-flex justify-content-center">É IMPORTANTE ABASTECER AS IMAGENS POSITIVAS COM IMAGENS
        SEM FUNDO(PNG), CONTENDO APENAS O OBJETO A SER IDENTIFICADO!!</div>
</div>

<h3 style="font-weight: bold;">3º - Removendo Imagens Falhas</h3>
<p>Ao executar o arquivo imgFeia.py sera deletado do diretorio
    "negativas" as imagens que não fazem parte do rerpetório:</p>
<p style="background-color: gray;"> > python imgFeia.py</p>

<h3 style="font-weight: bold;">4º - Renomeando Arquivos Da Pasta De Images</h3>
<p>Ao executar o arquivo renomear.py sera renomeado todas as imagens do
    diretorio "negativas" para que fique mais facil identificalas:</p>
<p style="background-color: gray;"> > python renomear.py</p>

<h3 style="font-weight: bold;">5º - Gerando Lista De Imagens Negativas</h3>
<p class="bg-light">Ao executar o arquivo listar.py sera criado um arquivo "bg.txt" que irá
    armazenar o nome de todas as imagens:</p>
<p style="background-color: gray;"> > python listar.py</p>

<h3 style="font-weight: bold;">6º - Criando Amostras</h3>
<p>Ao executar o arquivo listar.py sera criado um arquivo "bg.txt" que irá
    armazenar o nome de todas as imagens:</p>
<p style="background-color: gray;"> > python amostras.py</p>

<h3 style="font-weight: bold;">7º - Criando os Vetores</h3>
<p>Ao executar o arquivo vetores.py sera criado um diretorio com vetores que
    serão usados no passo final do processo:</p>
<p style="background-color: gray;"> > python vetores.py</p>

<h3 style="font-weight: bold;">8º - Treinando o Algoritmo</h3>
<p >Ao executar o arquivo treinar.py sera iniciado o processo que fornecerá como
    saída um arquivo .xml para ser usado, para isso apos executar o aruivo ele ira pedir o numero de
    estágios(quanto maior mais preciso se torna, mas o tempo também aumenta):</p>
<p style="background-color: gray;"> > python treinar.py</p>
