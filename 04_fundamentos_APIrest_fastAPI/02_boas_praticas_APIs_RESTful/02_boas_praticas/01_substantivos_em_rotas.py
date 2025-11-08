"""
1 -> Utilização de Substantivos em Rotas
Por Que Usar Substantivos Plurais em Rotas?
  Quando projetamos rotas para APIs, um dos princípios fundamentais é usar substantivos plurais para representar recursos. Isso ajuda a manter uma API clara, intuitiva e consistente. Vamos entender o motivo disso e como aplicá-lo, utilizando analogias simples, exemplos em diferentes linguagens de programação e boas práticas.


1. Representação de Recursos:
  Uma API é uma interface para interagir com os recursos de um sistema. Um "recurso" pode ser qualquer coisa que você deseja manipular: usuários, produtos, pedidos, etc. Quando você define rotas, o objetivo é representar essas entidades de forma clara.

Analogia:
  Imagine que você é o gerente de uma loja e deseja saber quantos tipos de produtos estão disponíveis. Você não diria "Me mostre as informações de todos os produtos disponíveis"; em vez disso, você simplesmente pediria para ver "...os produtos".

  A mesma lógica se aplica às APIs RESTful: seja simples e direto! Lembre-se, quando queremos acessar diretamente "users" ou "products" sem adicionar verbos desnecessários.


2. Consistência e Clareza:
  Usar substantivos no plural como nomes de rotas segue a lógica de que a rota é um ponto de acesso aos dados sobre um conjunto de recursos, e não uma ação específica. As ações (como obter, criar, atualizar) são representadas pelos métodos HTTP (GET, POST, PUT, DELETE).

Analogia:
  Pense em uma biblioteca onde as seções são nomeadas pelos tipos de livros que você pode encontrar ali: "romances", "histórias", "ciência". As seções são nomeadas de forma que você saiba o que esperar ao entrar nelas, sem precisar dizer "vá buscar romances" ou "traga histórias".

  Da mesma forma, em uma API, a rota /users deixa claro que você está lidando com um conjunto de usuários.
"""

# Exemplo pratico:
app = Flask(__name__)  # type: ignore


# Rota correta com substantivo no plural
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"message": "Listando todos os produtos"})  # type: ignore


# Rota incorreta com verbo
@app.route("/retrieveAllProducts", methods=["GET"])
def retrieve_all_products():
    return jsonify({"message": "Listando todos os produtos"})  # type: ignore


"""
Analogias:
  Cardápio de Restaurante: 
    Imagine que o cardápio de um restaurante está organizado por categorias como "entradas", "pratos principais", "sobremesas". Cada uma dessas categorias é um substantivo plural que representa um grupo de itens. Da mesma forma, a rota /products representa um grupo de produtos disponíveis na API.

  Estoque de uma Loja: 
    Em uma loja, você tem seções como "calçados", "vestuário", "acessórios". Estas seções são substantivos plurais, porque representam coleções de itens. Em uma API, você usaria /products para acessar todos os produtos disponíveis, assim como acessaria a seção "calçados" para ver todos os tipos de calçados disponíveis.


Ao projetar rotas para uma API, o uso de substantivos plurais ajuda a manter uma API limpa, consistente e fácil de entender. Este princípio está alinhado com a boa prática de RESTful APIs, onde cada rota representa um recurso específico de forma clara, sem a necessidade de verbos adicionais que indicariam uma ação. Isso torna as rotas mais intuitivas, tanto para os desenvolvedores que as implementam quanto para aqueles que as utilizam.
"""
