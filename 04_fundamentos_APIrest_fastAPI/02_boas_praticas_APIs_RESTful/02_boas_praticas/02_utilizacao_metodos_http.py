"""
2 -> Utilização de Métodos HTTP
Introdução aos Métodos HTTP
  Os métodos HTTP são fundamentais para a comunicação entre clientes (como navegadores) e servidores na web. Eles definem a ação que o cliente deseja realizar no servidor. Esses métodos são padronizados e possuem finalidades específicas.

Exemplo Simples de uma API RESTful
  Um exemplo clássico de API RESTful seria um serviço que gerencia um catálogo de produtos. A API poderia ter endpoints como:

  * `GET /products` - Recupera uma lista de todos os produtos.

  * `GET /products/{id}` - Recupera detalhes de um produto específico.

  * `POST /products` - Adiciona um novo produto ao catálogo.

  * `PUT /products/{id}` - Atualiza as informações de um produto existente.

  * `DELETE /products/{id}` - Remove um produto do catálogo.

OBS: Esses endpoints são acessados via HTTP e retornam dados no formato JSON ou XML.
"""

"""
1. GET: Recuperar Recursos
O que é?
  O método `GET` é usado para solicitar dados de um servidor. Ele não altera o estado dos dados no servidor; apenas os recupera.

Analogia:
  Imagine que você vai a uma biblioteca e pede ao bibliotecário um livro específico. O bibliotecário pega o livro da prateleira e entrega a você. Nesse cenário, você está "recuperando" o livro sem alterar seu conteúdo ou localização na prateleira.
"""

# Exemplo pratico:
app = Flask(__name__)  # type: ignore

users = []


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200  # type: ignore


@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.get_json()  # type: ignore
    users.append(new_user)
    return jsonify(new_user), 201  # type: ignore


if __name__ == "__main__":
    app.run(debug=True)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
2. POST: Criar Novos Recursos
O que é?
  O método `POST` é usado para enviar dados ao servidor para criar um novo recurso. Diferente do GET, ele altera o estado do servidor, geralmente criando um novo registro.

Analogia:
  Vamos supor que você preenche um formulário para abrir uma nova conta bancária. Ao entregar o formulário ao gerente, ele cria uma nova conta em seu nome. Nesse caso, você está "criando" um novo recurso no banco.
"""

# Exemplo pratico:
novo_usuario = {"nome": "João", "idade": 30}
response = requests.post("https://api.exemplo.com/usuarios", json=novo_usuario)  # type: ignore
print(response.json())

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
3. PUT/PATCH: Atualizar Recursos Existentes
O que é?

  * `PUT` substitui completamente um recurso existente no servidor.

  * `PATCH` realiza uma atualização parcial, alterando apenas os campos especificados.

Analogia:
  Imagine que você já tem uma conta bancária, mas quer atualizar seu endereço. Você pode fornecer um novo endereço ao banco sem mudar o resto das informações da conta. Com PUT, você substituiria toda a informação da conta; com PATCH, você apenas mudaria o endereço.
"""

# Exemplo pratico:
atualizacao_usuario = {"idade": 31}
response = requests.patch("https://api.exemplo.com/usuarios/1", json=atualizacao_usuario)  # type: ignore
print(response.json())

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
4. DELETE: Excluir Recursos
O que é?
  O método `DELETE` é usado para remover um recurso específico do servidor.

Analogia:
  Imagine que você decide fechar uma conta bancária que não usa mais. Você informa ao banco que quer fechar a conta, e eles removem todos os registros relacionados a essa conta.
"""

# Exemplo pratico:
response = requests.delete("https://api.exemplo.com/usuarios/1")  # type: ignore
print(response.json())

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
Revisando
  Os métodos HTTP são ferramentas essenciais para interagir com APIs RESTful. Cada método tem uma função específica e deve ser usado conforme a intenção da operação:

  * GET para recuperar dados sem modificar o servidor.

  * POST para criar novos recursos.

  * PUT ou PATCH para atualizar recursos existentes.

  * DELETE para remover recursos.
"""
