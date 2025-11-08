"""
3 -> Hierarquia e Aninhamento Em Rotas
  Quando trabalhamos com APIs, especialmente APIs RESTful, a forma como organizamos as rotas (endpoints) para acessar diferentes recursos é muito importante. Uma das práticas recomendadas é utilizar hierarquias e aninhamento de URLs. Isso significa que a estrutura das URLs deve refletir a relação entre os recursos que estamos manipulando.

O que é Aninhamento de Rotas?
  Aninhamento de rotas significa que você está criando uma URL que segue uma estrutura hierárquica para representar a relação entre diferentes recursos. Essa hierarquia faz com que a URL seja intuitiva e reflita como os dados estão organizados.


Analogia
  Pense em uma pasta no seu computador. Dentro dessa pasta, você pode ter subpastas que organizam melhor seus arquivos. Por exemplo:

    * Documentos/
        * Trabalho/
            * Relatórios/

  e você quer acessar um relatório específico, você precisa seguir a hierarquia de pastas: `Documentos/Trabalho/Relatórios/Relatorio1.docx`.

  Na web, as URLs funcionam de maneira semelhante. Se você tem recursos que estão logicamente relacionados, você deve organizá-los em uma estrutura de URL que reflete essa relação.


Exemplo Prático: Pedidos de Usuários
  Considere uma API que lida com usuários e os pedidos feitos por esses usuários. Se quisermos acessar todos os pedidos de um usuário específico, é comum usar uma rota que reflete essa relação:

  * URL: /users/{userId}/orders

  Aqui, {userId} é um placeholder para o ID do usuário. A URL /users/123/orders seria usada para acessar todos os pedidos do usuário com o ID 123.

Explicação do Aninhamento
  * /users/: Representa o recurso "usuários".
  * /123/: Especifica um usuário específico com ID 123.
  * /orders: Especifica os pedidos relacionados a esse usuário.

  Essa estrutura é intuitiva porque mostra claramente que os pedidos estão relacionados a um usuário específico.
"""

# Exemplo pratico:
app = Flask(__name__)  # type: ignore


@app.route("/users/<int:userId>/orders")
def get_orders(userId):
    # Lógica para buscar os pedidos do usuario
    return f"Pedidos do usuario {userId}"


if __name__ == "__main__":
    app.run(debug=True)

# No exemplo com Flask, usamos <int:userId> para capturar o ID do usuário na URL e retornamos os pedidos.