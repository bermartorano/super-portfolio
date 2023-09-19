# 💻📂 Super Portifólio

Aplicação em que implementei a arquitetura MTV (Model Template View), modelando um banco com tabelas de perfis, projetos, certificados e instituições certificadoras. Com a aplicação, é possível realizar operações CRUD, com as devidas autenticações.

## Ferramentas Utilizadas
* Python
* Django Rest Framework
* SimpleJWT
* Docker

## Como Executar a Aplicação
1. Clone o repositório.
2. Na raiz do projeto crie o ambiente virtual `python3 -m venv .venv`.
3. Ative o ambiente virtual `source .venv/bin/activate`.
4. Instale as dependências `python3 -m pip install -r dev-requirements.txt`.
6. Utilize os seguintes comandos para criar o banco.
```bash
  docker build -t super-portfolio-db .
  docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db
  ```
7. Faça as migrações com `python3 manage.py migrate`.
8. Suba a aplicação usando `python3 manage.py runserver`.

## Detalhes do Desenvolvimento
![requisitos](https://github.com/bermartorano/super-portfolio/assets/110858573/4fb7f59d-d06e-4053-846c-d4585dbaf14a)
