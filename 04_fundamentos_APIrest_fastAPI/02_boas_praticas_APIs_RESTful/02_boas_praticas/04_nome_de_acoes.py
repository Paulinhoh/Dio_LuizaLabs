"""
4 -> Nomes de Ações
Explicação Detalhada sobre Nomes de Ações em URLs:
  Quando estamos desenvolvendo APIs (Application Programming Interfaces), é essencial seguir boas práticas para garantir que os endpoints (URLs) sejam intuitivos e fáceis de usar. Um dos principais princípios é evitar o uso de verbos ou ações nos URLs, como createUser ou deleteUser. Em vez disso, devemos utilizar o método HTTP apropriado (GET, POST, PUT, DELETE, etc.) para indicar a ação que queremos realizar.

Por Que Evitar Verbos em URLs?
  A ideia é que os métodos HTTP já foram criados para representar as operações que queremos realizar em um recurso. Ao evitar verbos nos URLs e usar corretamente os métodos HTTP, deixamos nossas APIs mais consistentes, previsíveis e alinhadas com as convenções RESTful. Isso facilita o entendimento e uso por outros desenvolvedores.

Exemplo Prático:
  Vamos imaginar que estamos criando uma API para gerenciar usuários. Suponha que queremos criar um novo usuário.

  * Abordagem Não Recomendada:
        * URL: POST /createUser
        * Aqui, createUser é um verbo que indica a ação de criar um usuário. Esse tipo de URL é mais descritivo, mas vai contra as convenções RESTful.

  * Abordagem Recomendada:
        * URL: POST /users
        * Aqui, estamos utilizando o método HTTP POST, que é tradicionalmente usado para criar novos recursos. O recurso em questão é users. Portanto, POST /users indica a criação de um novo usuário.

Analogias do Dia a Dia
  Imagine que você está em uma biblioteca. Para pegar um livro emprestado, você não precisa dizer ao bibliotecário: "Eu gostaria de criar um empréstimo para este livro". Em vez disso, você simplesmente entrega o livro ao bibliotecário e ele já sabe que deve registrar o empréstimo.

  Da mesma forma, na programação, quando usamos POST /users, estamos entregando as informações do usuário à API, e ela entende que deve criar um novo usuário.
"""

# Exemplo pratico:
app = Flask(__name__)  # type: ignore


@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.json  # type: ignore
    # Lógica para criar usuario
    return jsonify({"message": "Usuario criado com sucesso "}), 201 # type: ignore


if __name__ == "__main__":
    app.run(port=5000)
