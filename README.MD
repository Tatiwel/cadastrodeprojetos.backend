# Cadastro de Projetos

Este projeto é um sistema de gerenciamento de projetos desenvolvido com **FastAPI**, utilizando **PostgreSQL** como banco de dados e **SQLAlchemy** como ORM. O sistema oferece as operações básicas de CRUD para facilitar a administração de projetos.

## Funcionalidades

- **Listagem de Projetos:** Exibe todos os projetos cadastrados.
- **Criação de Novo Projeto:** Permite o cadastro de novos projetos.
- **Edição de Projeto Existente:** Possibilita a atualização das informações de projetos já cadastrados.
- **Remoção de Projeto:** Permite excluir projetos indesejados.
- **Visualização de Detalhes:** Mostra informações detalhadas sobre um projeto específico.

## Tecnologias Utilizadas

- **Backend:** FastAPI
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy

## Estrutura do Projeto

- **Módulo Raiz:** [cadastro-de-projetos](https://github.com/Tatiwel/cadastro-de-projetos.git)
- **Submódulo Backend:** [cadastrodeprojetos.backend](https://github.com/Tatiwel/cadastrodeprojetos.backend.git)

## Configuração do Ambiente

Antes de executar a aplicação, é necessário criar um arquivo `.env` na raiz do projeto com as credenciais do banco de dados.

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

## Comandos de Execução

- **Iniciar a aplicação:**

```python
python run.py run
```

- **Executar os testes:**

```python
python run.py test
```

- **Acessar a documentação via Swagger:**

```python
python run.py docs
```
