"""
Tratamento de Erros
O que são Códigos de Status HTTP?
  Os códigos de status HTTP são mensagens enviadas pelo servidor para o cliente (navegador, aplicativo, etc.) após o processamento de uma requisição. Eles indicam se a requisição foi bem-sucedida, se houve um erro ou se algo precisa ser corrigido.

1xx  ->  Informational codes: O servidor reconhece e está processando a situação.

2xx  ->  Success codes: O servidor recebeu, compreendeu e processou com sucesso a solicitação.

3xx  ->  Redirection codes: O servidor recebeu a solicitação, mas ha um redirecionamento para outro lugar (ou, em casos raros, alguma ação adicional além do redirecionamento deve ser concluida).

4xx  ->  Client error codes: O sevidor não conseguiu encontrar (ou alcançar) a pagina ou o site. Este é um erro do lado do site.

5xx  ->  Server error codes: O cliente fez uma soicitação valida, mas o servidor falhou ao completar a solicitação.

"""

"""
Códigos Comuns e Suas Significações
200 OK
    * Significado: A requisição foi bem-sucedida e o servidor retornou a resposta esperada.
    * Analogia: Imagine que você vai a uma loja e faz um pedido. O atendente confirma que o pedido foi recebido corretamente e entrega o produto. Isso é um 200 OK.

400 Bad Request
    * Significado: A requisição não pode ser entendida pelo servidor devido a sintaxe inválida. É um erro do lado do cliente.
    * Analogia: Você vai a uma loja e faz um pedido que não faz sentido (como pedir um produto que não existe). O atendente diz que o pedido não pode ser processado porque não está claro. Isso é um 400 Bad Request.

404 Not Found
    * Significado: O recurso solicitado não foi encontrado no servidor.
    * Analogia: Você pede um produto específico que não está disponível na loja. O atendente informa que o produto não está na loja. Isso é um 404 Not Found.
"""

# Exemplo pratico:
app = Flask(__name__)  # type: ignore


@app.route("/resource")
def get_resource():
    resource = None  # Suponha que o recurso não foi encontrado
    if resource:
        return jsonify(resource), 200  # type: ignore
    else:
        abort(404, description="Recurso não encontrado")  # type: ignore


@app.errorhandler(400)
def bad_request(error):
    return str(error), 400


if __name__ == "__main__":
    app.run(port=3000)


"""
💡 Códigos de Status HTTP Adicionais
201 Created
    * Significado: A requisição foi bem-sucedida e um novo recurso foi criado. O local do novo recurso é retornado no cabeçalho Location.
    * Analogia: Imagine que você vai a uma loja e faz um pedido para um produto personalizado. O atendente confirma que o pedido foi criado e informa que o produto estará disponível para retirada em breve. Isso é um 201 Created.

204 No Content
    * Significado: A requisição foi bem-sucedida, mas não há conteúdo para retornar. Usado principalmente para requisições DELETE.
    * Analogia: Você vai a uma loja para devolver um item. A devolução é processada com sucesso, mas não há necessidade de fornecer um recibo ou outro documento. Isso é um 204 No Content.

301 Moved Permanently
    * Significado: O recurso solicitado foi movido permanentemente para um novo URI. O cliente deve usar o novo URI para futuras requisições.
    * Analogia: Você visita uma loja em um endereço antigo, e o atendente informa que a loja foi movida para um novo endereço. Isso é um 301 Moved Permanently.

302 Found
    * Significado: O recurso solicitado foi encontrado, mas a requisição deve ser redirecionada temporariamente para um URI diferente.
    * Analogia: Você vai a uma loja e o produto que você quer está fora de estoque. O atendente direciona você para outra loja temporariamente. Isso é um 302 Found.

304 Not Modified
    * Significado: O recurso não foi modificado desde a última requisição. Usado para cache.
    * Analogia: Você visita uma loja regularmente para verificar se há novidades. Quando você visita novamente e nada mudou, a loja informa que não há novas atualizações desde a última visita. Isso é um 304 Not Modified.

401 Unauthorized
    * Significado: A requisição requer autenticação. O cliente deve fornecer credenciais válidas.
    * Analogia: Você tenta entrar em uma área restrita da loja, mas é necessário um crachá de acesso. O atendente informa que você precisa fornecer as credenciais apropriadas para entrar. Isso é um 401 Unauthorized.

403 Forbidden
    * Significado: O servidor entendeu a requisição, mas se recusa a autorizá-la. O cliente não tem permissão para acessar o recurso.
    * Analogia: Você tenta acessar um setor restrito da loja, mas mesmo com as credenciais corretas, você não tem permissão para entrar. O atendente informa que o acesso é proibido. Isso é um 403 Forbidden.

408 Request Timeout
    * Significado: O servidor expirou a requisição do cliente devido a inatividade. O cliente deve tentar novamente.
    * Analogia: Você está fazendo um pedido na loja, mas demora muito para decidir o que deseja. O atendente encerra a operação após um período de inatividade e pede para você fazer o pedido novamente. Isso é um 408 Request Timeout.

500 Internal Server Error
    * Significado: O servidor encontrou uma condição inesperada que impediu o atendimento da requisição.
    * Analogia: Você vai a uma loja e, ao tentar processar seu pedido, a máquina registradora quebra inesperadamente. O atendente informa que houve um erro interno e pede para você tentar mais tarde. Isso é um 500 Internal Server Error.

502 Bad Gateway
    * Significado: O servidor, enquanto agia como um gateway ou proxy, recebeu uma resposta inválida do servidor upstream.
    * Analogia: Você faz um pedido em uma loja, mas a loja depende de um fornecedor para completar o pedido. O fornecedor envia uma resposta inválida, então a loja não pode concluir seu pedido. Isso é um 502 Bad Gateway.

503 Service Unavailable
    * Significado: O servidor não está disponível no momento, geralmente devido a sobrecarga ou manutenção.
    * Analogia: Você vai a uma loja, mas ela está fechada temporariamente para manutenção. O atendente informa que a loja não está disponível no momento. Isso é um 503 Service Unavailable.

504 Gateway Timeout
    * Significado: O servidor, enquanto agia como um gateway ou proxy, não recebeu uma resposta a tempo do servidor upstream.
    * Analogia: Você faz um pedido em uma loja, mas o fornecedor está demorando muito para responder. A loja encerra a requisição após um período de tempo sem resposta. Isso é um 504 Gateway Timeout.
"""

"""
Resumo
    * 200 OK: Sucesso, o servidor cumpriu sua parte e entregou o que foi solicitado.
    * 400 Bad Request: A requisição não foi entendida devido a um erro do cliente.
    * 404 Not Found: O recurso solicitado não foi encontrado no servidor.

  Esses códigos são essenciais para uma boa comunicação entre clientes e servidores, ajudando a identificar problemas e a gerenciar o fluxo de informações de maneira eficaz.
"""
