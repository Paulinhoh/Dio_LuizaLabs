# Banco de dados

Um banco de dados é uma coleção organozada de informações (ou dados) estruturados, normalmente armazenados
eletronicamente em um sistema de computador.

## Tipos de banco de dados

**Banco de dados relacional:** O tipo mais usado atualmente, armazenando dados estruturados, sendo organizado
em tabelas, com colunas e linhas, que se relacionam entre si.<br>
Exemplos: SQL Server, Oracle Database, MySQL, PostgreSQL

## Entendendo uma tabela

**Tabela:** São dados estruturados e organizados logicamente em formato de linha e coluna.

**Clientes**

| Id | Nome     | Sobrenome | Email           | AceitaComunicados | DataCadastro |
|----|----------|-----------|-----------------|-------------------|--------------|
| 1  | Leonardo | Buta      | email@gmail.com | 1                 | 29/04/2022   |
| 2  | Peter    | Anderson  | email@gmail.com | 0                 | 29/04/2022   |
| 3  | Taylor   | Adams     | email@gmail.com | 1                 | 29/04/2022   |

**Endereços**

| Id | Rua   | Bairro   | Cidade   | Estado   | IdCliente |
|----|-------|----------|----------|----------|-----------|
| 1  | Rua 1 | Bairro 1 | Cidade 1 | Estado 1 | 1         |

## Banco de dados não relacional

**Banco de dados não relacional:** Banco de dados onde os dados não são armazenados em tabelas, e sim armazenado de
maneira não estruturada ou semi-estruturada.<br>
Exemplos: MongoDB<br>
**Existem varios tipos:** document database, key-value database, wide-column store, e graph databases.

## Tipos de dados

**Semi estruturado**

```JavaScript
{
  {
    "id": 1,
    "Nome_Produto": "Material de escritorio",
    "Preco": "25.00",
    "DataVenda": "2022-04-23T01:23:26:9666539-03:00",
    "Desconto": null
  },
  {
    "id": 2,
    "Nome_Produto": "Licença de software",
    "Preco": "110.00",
    "DataVenda": "2022-04-23T01:23:26:9666539-03:00",
    "Desconto": null,
    "Cupom": "1234"
  }
}
```

**Estruturado**

**Clientes**

| Id | Nome     | Sobrenome | Email           | AceitaComunicados | DataCadastro |
|----|----------|-----------|-----------------|-------------------|--------------|
| 1  | Leonardo | Buta      | email@gmail.com | 1                 | 29/04/2022   |
| 2  | Peter    | Anderson  | email@gmail.com | 0                 | 29/04/2022   |
| 3  | Taylor   | Adams     | email@gmail.com | 1                 | 29/04/2022   |

**Endereços**

| Id | Rua   | Bairro   | Cidade   | Estado   | IdCliente |
|----|-------|----------|----------|----------|-----------|
| 1  | Rua 1 | Bairro 1 | Cidade 1 | Estado 1 | 1         |

## Entendendo o DBMS

**Database Management System:** É um software utilizado para acessar, manipular e monitoriar um sistema de banco de
dados.
