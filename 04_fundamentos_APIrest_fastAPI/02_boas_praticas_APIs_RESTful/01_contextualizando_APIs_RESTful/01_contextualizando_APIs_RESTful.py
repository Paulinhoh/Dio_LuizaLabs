"""
Definição e Contexto Histórico:
  APIs RESTful é uma arquitetura de software utilizada para criar serviços web escaláveis. Criado por Roy Fielding em 2000, o REST é baseado em um conjunto de princípios e restrições que promovem uma comunicação eficaz entre sistemas distribuídos. As APIs RESTful utilizam o protocolo HTTP e são amplamente adotadas no desenvolvimento de aplicativos modernos devido à sua simplicidade e flexibilidade.

Nota: As APIs REST são projetadas em torno de recursos, que são qualquer tipo de objeto, dados ou serviço que podem ser acessados pelo cliente. Um recurso tem um identificador, que é um URI que identifica exclusivamente esse recurso.

Lembrando que há outros tipos de APIs, como: Web, RESTful, SOAP, hardware, plataforma e outras. Neste curso, iremos focar nas RESTful.
"""

"""
 EXTRA: Principais diferenças do RESTful e outras APIs:
1. Estilo Arquitetural:
RESTful APIs: Baseiam-se em REST, que é um conjunto de princípios arquiteturais. Eles usam HTTP como protocolo subjacente e se concentram em recursos, identificados por URLs (Uniform Resource Locators).

Outras APIs: Podem seguir diferentes estilos arquiteturais, como SOAP (Simple Object Access Protocol), GraphQL, RPC (Remote Procedure Call), entre outros. Cada um desses estilos tem sua própria maneira de estruturar as chamadas e os dados.

2. Protocolo de Comunicação:
RESTful APIs: Usam exclusivamente HTTP para comunicação. Elas fazem uso dos métodos HTTP padrão, como GET, POST, PUT, DELETE, etc., para realizar operações sobre os recursos.

Outras APIs: Podem usar diferentes protocolos, como HTTP, HTTPS, SMTP, TCP, entre outros. Por exemplo, SOAP usa XML sobre HTTP, enquanto RPC pode usar diferentes protocolos dependendo da implementação.

3. Formato de Dados:
RESTful APIs: São agnósticas quanto ao formato de dados, mas geralmente usam JSON ou XML para transferência de dados. No entanto, o uso de JSON é predominante.

Outras APIs: SOAP, por exemplo, usa exclusivamente XML. Outras APIs, como GraphQL, têm um formato específico de consulta e resposta.

4. Estado da Sessão:
RESTful APIs: São stateless (sem estado), o que significa que cada chamada feita ao servidor é independente e não depende de chamadas anteriores. O servidor não armazena informações sobre o estado do cliente entre as requisições.

Outras APIs: Algumas APIs, como SOAP, podem ser stateful (com estado), onde o servidor mantém o estado da sessão e as interações dependem de chamadas anteriores.

5. Escalabilidade:
RESTful APIs: Por serem stateless e simples, tendem a ser mais escaláveis e adequadas para a web moderna, onde múltiplas instâncias de um serviço podem atender a diferentes partes de uma aplicação.

Outras APIs: APIs que mantêm o estado ou que seguem arquiteturas mais complexas podem ter desafios adicionais em termos de escalabilidade.

6. Flexibilidade e Simplicidade:
RESTful APIs: São geralmente mais simples e flexíveis, permitindo que os desenvolvedores criem aplicações rapidamente e com menos rigidez no formato de dados e nas chamadas.

Outras APIs: Podem ter uma estrutura mais rígida e complexa, como no caso do SOAP, que requer uma definição estrita do contrato de serviço e formatos de mensagem.

7. Cacheabilidade:
RESTful APIs: Aproveitam os mecanismos de cache HTTP, o que pode melhorar o desempenho ao reutilizar respostas antigas para chamadas semelhantes.

Outras APIs: Nem todas as APIs oferecem suporte direto a mecanismos de cache como RESTful.
"""
