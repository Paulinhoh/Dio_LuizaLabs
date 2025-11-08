"""
8 -> Exemplo Completo de Estrutura de Rotas RESTful
Estrutura de Rotas RESTful
  REST (Representational State Transfer) é um estilo arquitetônico para criar serviços web. Ele usa métodos HTTP para realizar operações em recursos, e a estrutura de rotas é uma forma de mapear esses recursos para URLs específicas.

Recursos de Usuários
    * GET /users: Lista todos os usuários.
    * POST /users: Cria um novo usuário.
    * GET /users/{userId}: Obtém detalhes de um usuário específico.
    * PUT /users/{userId}: Atualiza um usuário existente.
    * DELETE /users/{userId}: Exclui um usuário.
"""

"""
Analogia (biblioteca):
    * POST /users é como adicionar um novo livro à biblioteca.
    * GET /users/{userId} é como consultar os detalhes de um livro específico na biblioteca.
    * PUT /users/{userId} é como atualizar as informações de um livro existente na biblioteca.
    * DELETE /users/{userId} é como remover um livro da biblioteca.

Recursos de pedidos (aninhado com Usuarios):
    * GET /users/{userId}/orders: Lista os pedidos de um usuário específico.
    * POST /users/{userId}/orders: Cria um novo pedido para um usuário.

Analogias: na mesma biblioteca, agora imagine que cada livro pode ter um registro de quem pegou emprestado
    * GET /users/{userId}/orders é como listar todos os livros emprestados por um usuário específico.
    * POST /users/{userId}/orders é como adicionar um novo empréstimo para um usuário específico
"""

# Exemplo:
from flask import Flask, request, jsonify  # type: ignore

app = Flask(__name__)
users = []  # Banco de dados simulado


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users", methods=["POST"])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return "User not found", 404


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    else:
        return "User not found", 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return "", 204


@app.route("/users/<int:user_id>/orders", methods=["GET"])
def get_orders(user_id):
    # Supondo que temos um método para obter pedidos de um usuário
    orders = get_orders_for_user(user_id)
    return jsonify(orders)


@app.route("/users/<int:user_id>/orders", methods=["POST"])
def create_order(user_id):
    order = request.json
    # Adiciona o pedido ao usuário
    add_order_to_user(user_id, order)
    return jsonify(order), 201


def get_orders_for_user(user_id):
    # Função simulada para obter pedidos
    return []


def add_order_to_user(user_id, order):
    # Função simulada para adicionar pedido
    pass


if __name__ == "__main__":
    app.run(port=5000)

"""
Resumo
  Esses exemplos mostram como criar e manipular recursos em uma API RESTful para gerenciar usuários e seus pedidos. Cada método HTTP e URL tem uma função específica, refletindo a forma como você pode interagir com os recursos em uma API.
"""
