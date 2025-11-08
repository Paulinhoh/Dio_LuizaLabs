"""
5 -> Versionamento de Rotas
  Versionamento de rotas é uma prática essencial no desenvolvimento de APIs, permitindo que você faça mudanças na API sem afetar os clientes que dependem de versões anteriores. Vamos explorar essa prática de forma detalhada, com exemplos práticos em diferentes linguagens de programação e analogias para facilitar o entendimento.

O Que é Versionamento de Rotas?
  Quando uma API é utilizada por múltiplos clientes (aplicações, dispositivos, etc.), é comum que esses clientes dependam de uma versão específica da API. Se você precisar alterar a API – por exemplo, mudar a estrutura de dados, adicionar novos campos, ou modificar a lógica de negócio – essas mudanças podem quebrar os clientes que ainda dependem da versão antiga.

  Versionamento de rotas resolve esse problema permitindo que você mantenha múltiplas versões da API em paralelo. Cada versão da API é identificada por um número de versão que é incluído na URL das rotas. Assim, clientes antigos podem continuar usando a versão que conhecem, enquanto clientes novos podem usar a versão mais recente.


Analogia com o dia a dia:
  Pense em uma estrada com várias pistas. Cada pista representa uma versão diferente da API:
    * Pista 1 (v1): É a pista antiga, onde os carros (clientes) que já estão acostumados a andar por ela continuam a trafegar.
    * Pista 2 (v2): É uma nova pista que você construiu, mais moderna e eficiente, mas diferente da primeira. Os carros que desejam uma experiência mais nova podem usar essa pista.

  Dessa forma, você pode imaginar que novos motoristas (desenvolvedores) podem escolher em qual pista andar, dependendo das necessidades do seu veículo (aplicação).
"""

# Exemplo pratico:
app = Flask(__name__)  # type: ignore


# versão 1 da rota users
@app.route("/v1/users", methods=["GET"])
def get_users_v1():
    return jsonify({"id": 1, "name": "John Doe v1"})  # type: ignore


# versão 1 da rota users
@app.route("/v2/users", methods=["GET"])
def get_users_v2():
    return jsonify({"id": 1, "name": "John Doe v2", "email": "john@exemplo.com"})  # type: ignore


if __name__ == "__main__":
    app.run(port=5000)

# /v1/users retorna apenas o nome.
# /v2/users adiciona o email.


"""
Revisão
  Versionamento de rotas é uma prática essencial para manter a estabilidade e a evolução de uma API. Com essa prática, você pode garantir que diferentes clientes possam utilizar a versão da API que melhor atende às suas necessidades, permitindo que sua API evolua de forma segura e organizada. Seja em Node.js, Python ou Java, a implementação é simples e traz enormes benefícios para a manutenção e evolução contínua de sistemas que dependem de APIs.
"""
