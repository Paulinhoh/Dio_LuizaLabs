# =-=-=-=-=-=-=-=-= O que são pacotes e uso do pip =-=-=-=-=-=-=-=-=
'''
    O que são pacotes em Python?
      Pacotes são módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você
    utilize código que foi escrito por outras pessoas, economizando tempo e esforço.

    O papel do pip:
      Pip é o gerenciador de pacotes do Python. Ele nos permite instalar, atualizar e remover pacotes facilmente. Ele
    se comunica com o PyPi (Python Package Index), que é onde a maioria dos pacotes Python são armazenados.

    https://pypi.org

    Uso de ambientes virtuais:
      Ambientes virtuais, como os criados por venvs, nos permitem manter as dependencias de diferentes projetos. Isso
    é importante para evitar conflitos entre versões de pacotes.

    python -m venv <myenv>
    python -m venv .env
    source myenv/bin/activate
    deactivate
'''

'''
    Comandos do pip:
    
    # instalar um pacote
    pip install nome_do_pacote
    
    # desistalar um pacote
    pip install nome_do_pacote
    
    # listar pacotes instalados
    pip list
    
    # atualizar pacotes
    pip install --upgrade nome_do_pacote
    
    # procurar por pacotes (não funciona mais)
    pip search termo_de_busca
'''

# =-=-=-=-=-=-=-=-= Gerenciando dependencias com Pipenv =-=-=-=-=-=-=-=-=
'''
    Introdução ao pipenv:
      Pipenv é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências de pacotes que combina 
    a gestão de depend~encias com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes 
    automaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.
    
    Comandos do pipenv:
    * pip install pipenv
    * pipenv install numpy
    * pipenv unistall numpy
    * pipenv lock
    * pipenv graph
    * pipenv clean
'''

# =-=-=-=-=-=-=-=-= Gerenciando dependencias com Poetry =-=-=-=-=-=-=-=-=
'''
    Introdução ao poetry:
      Poetry é outra ferramenta de gerenciamento de depedências para Python que permite declarar as bibliotecas de que 
    seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas para você. Ela também suporta o 
    empacotamento e publicação de projetos no PyPi.
    
    Comandos do poetry:
    * pip install poetry
    * poetry new myproject
    * cd myproject
    * poetry add numpy
    * poetry remove numpy
    * poetry init
    * poetry install
'''

# =-=-=-=-=-=-=-=-= Boas práticas =-=-=-=-=-=-=-=-=
'''
    Introdução:
      Python tem uma série de convenções e melhores práticas codificadas em PEPs (Propostas de Melhorias de Python). A 
    mais coneheciada destas é provavelmente a PEP 8, que cobre o estilo de codificação.
    
    O que é PEP 8:
      PEP 8 é o guia de estilo para codificar em Python. Ele inclui convenções sobre nomes de variaveis, uso de espaços
    em branco, comprimento da linha e muitas outras coisas que ajudam a manter o código Python consistente e legível.

    Principais recomendações da PEP 8:
      Algumas das priciapis recomendações da PEP 8 incluem usar 4 espaços para a identação, limitar as linhas a 79
    caracteres, usar nomes de variaveis em snake_case para funções e variaveis, e CamelCase para classes.
'''


def somar(argumento_1, argumento_2):
    # está é uma função de exemplo seguindo a PEP 8
    pass


class ContaBancaria:
    # está é uma classe de exemplo seguindo a PEP 8
    pass


'''
    Uso de ferramentas de checagem de estilo:
      Para nos ajudar a seguir as recomendações da PEP 8, podemos usar ferramentas de checagem de estilo como flake8. 
    Essas ferramentas verificam nosso código e nos informam onde estamos desviando do guia de estilo.
    
    * pip install flake8
    * flake9 meu_script.py
    
    Formatação automatica de código:
      Black é uma ferramenta de formatação de código Python que segue a filosofia "formato único". Black reformata todo 
    o seu arquivo em um estilo consistente, simplificando a tarefa de manter o código em confirmidade com a PEP 8.
    
    * pip install black
    * black meu_script.py
    
    Organização de imports com isort:
      Isort é um ferramenta Python para classificar importações alfabeticamente e separa-las automaticamente em seções. 
    Ele proporciona uma maneira rápida e fácil de ordenar e categorizar susa importações. 
    
    * pip install isort
    * isort meu_script.py
'''
