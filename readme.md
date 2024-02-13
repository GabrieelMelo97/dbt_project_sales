# DBT Project Sales

Este projeto é uma exploração prática do framework dbt (data build tool), criado para praticar a criação de um pipeline fictício de dados de vendas. O objetivo é demonstrar como o dbt pode ser usado para transformar e modelar dados em um banco de dados PostgreSQL.

## Pré-requisitos

- Docker
- Poetry

## Estrutura de Diretórios

- **data/:**
  - (Arquivos de dados brutos ou de entrada necessários para o projeto)

- **dbt/:**
  - **models/:**
    - (Arquivos SQL contendo modelos dbt para transformação de dados)
  - **analyses/:**
    - (Arquivos SQL com análises e consultas específicas do dbt)
  - (Outros artefatos relacionados ao dbt)

- **postgresql/:**
  - (Scripts SQL para PostgreSQL, incluindo operações de criação de tabelas, procedimentos armazenados, etc.)

## Como executar o projeto

1. Clone o repositório:
2. Instale o poetry e execute:

`` poetry install & poetry shell ``

3. Execute os comandos abaixo para iniciar o postgresql:

`` make init ``

4. Execute o comando abaixo para iniciar o pipeline:

`` dbt run ``