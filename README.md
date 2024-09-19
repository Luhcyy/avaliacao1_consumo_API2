# avaliacao1_consumo_API2

## Catálogo de Animes em Python :japanese_castle:

### Descrição :page_facing_up:
<img src="https://gifdb.com/images/high/luffy-spinning-straw-hat-7t9ab5hrcqtv0ffg.webp" alt="Monkey D. Luffy" width="500" />

<p>A seguinte aplicação foi desenvolvida com o intuito de ser apresentada como entrega para a primeira avaliação da disciplina: Desenvolvimento Web lll</p>
<p>O catálogo de animes possibilita buscar qualquer anime disponivel por nome, e ainda ver os detalhes de um anime especifico ao pesquisar pelo ID.</p>
<p>Professor Aplicante: Orlando Saraiva Jr</p>

#### Tecnologias Usadas :computer:

<ul>
  <li>Python3: https://www.python.org/</li>
  <li>GraphQL: https://graphql.org/</li>
  <li>AniList APIv2: https://anilist.gitbook.io/anilist-apiv2-docs</li>
</ul>

### Funcionalidades :mag_right:
<img src="https://gifdb.com/images/high/luffy-hungry-eyes-m3tpxssw9lxk7f8z.webp" alt="Excited Luffy" width="500" />

#### Menu interativo 
<ul>
  <li>Escolha entre buscar os animes pelo nome ou pelo ID, além da opção de sair da aplicação.</li>
  <li>O menu utiliza do loop "while True" para que a exibição do menu seja repetida até o usúario escolher sair.</li>
</ul>

#### Pesquisa por nome
<ul>
  <li>Ao escolher em pesquisar pelo nome, Exibe todos os resultados disponiveis que mais se assemelham com a sua pesquisa.</li>
  <li>Letras e números são aceitos.</li>
  <li>todos os resultados exibidos contém seus IDs para usar na pesquisa por ID.</li>
</ul>

#### Pesquisa por ID
<ul>
  <li>Ao escolher pesquisar pelo ID, apenas números inteiros são permitidos.</li>
  <li>A pesquisa por ID mostra apenas um resultado por pesquisa.</li>
  <li>O resultado da pesquisa ira exibir o anime com seu respectivo ID, e também exibirá alguns detalhes desse anime em especifico.</li>
</ul>

### Requisitos
<ul>
  <li>Python 3.x instalado</li>
  <li>Biblioteca Requests instalada: pip install requests</li>
</ul>

### Como usar? :eyes:
<img src="https://gifdb.com/images/high/luffy-thinking-with-chopper-48o2dibk5xc5xpug.webp" alt="Luffy Thinking" width="500" />

#### Instale e crie um ambiente virtual
<ul>
  <li>Abra um terminal ou prompt de comando.</li>
  <li>Instale o "VirtualEnv" do python com o seguinte comando:</li>
  <br>
  
  ```
  pip install virtualenv
  ```
  <li>Navegue até o diretório "app" do projeto e siga os seguintes passos:</li>
  <br>
  <p>No Windows</p>
  
  ```
  - python -m virtualenv venv
  - cd venv
  - cd Scripts
  - activate.bat
  ```

  <br>
  <p>No Linux</p>
  
  ```
  - virtualenv -p python3 venv
  - cd venv
  - cd bin
  - source activate
  ```

  <li>Volte para o diretório "app" do projeto e instale os requisitos com o comando:</li>
  <br>

  ```
  pip install -r requirements.txt
  ```

  <li>Por último, execute o seguinte comando para executar a aplicação:</li>
  <br>

  ```
  python app.py
  ```
  </ul>

  ### Exemplos de Uso :pencil:
  <img src="https://gifdb.com/images/high/sleepy-luffy-snoring-e0fbfblmxqqyi4jh.webp" alt="Luffy imitating chopper" width="500" />

  ```
  python app.py

  ---------------------------------

  Boas-vindas ao catalogo de animes!

  Escolha uma opção para começar:

  1 - buscar anime por nome

  2 - buscar anime por ID

  3 - Sair

  Digite sua Escolha: 2

  ---------------------------------

  Digite o ID do Anime que deseja: 813

  ---------------------------------

  ID: 813
  Titulo (Romaji): Dragon Ball Z
  Titulo (Inglês): Dragon Ball Z
  Titulo (Nativo): ドラゴンボールZ
  Número de Episódios: 291
  Data de lançamento: 1989 

  descrição (Inglês): Goku is back with his new son, Gohan, but just when things are getting settled down, the adventures continue. Whether he is facing enemies such as Freeza, Cell, or   Boo, Goku is proven to be an elite of his own and discovers his race, Saiyan. He meets many new people, gaining allies as well as enemies, as he still finds time to raise a family and   be the happy-go-lucky Saiyan he is.<br><br>
  (Source: Anime News Network)

  Pressione Enter para ao menu...  
  ```
  ## Por enquanto é só! :skull:
  ### Muito Obrigado por ler até aqui.
  <img src="https://gifdb.com/images/high/happy-farewell-kid-luffy-qwl2ued5zqgtt859.webp" alt="Kid Luffy giving a farewell" width="500" />
  
  
