# API Bancária com FastAPI 🏦🚀

Uma API RESTful assíncrona desenvolvida em **FastAPI** para gerenciar operações bancárias de clientes, contas correntes e transações (depósitos e saques). Construída como parte do desafio da plataforma DIO em conjunto com o Luiza Labs.

## 🎯 Objetivos e Funcionalidades

- **Cadastro de Clientes:** Criação de novos perfis de clientes protegidos com senhas encriptadas (bcrypt).
- **Gerenciamento de Contas:** Cada cliente pode ter uma ou mais contas correntes registradas.
- **Transações Bancárias:** Funcionalidades de depósito e saque, contando com validações que impedem valores negativos ou saques sem saldo o suficiente.
- **Extrato Bancário:** Consulta do histórico completo de todas as transações, saques e depósitos de uma conta específica.
- **Segurança (Autenticação JWT):** A grande maioria dos endpoints é protegida. O modelo exige que o usuário envie as credenciais (E-mail e Senha) na rota de `/auth/login` em troca de um Token JWT para uso nas requisições.

## 🛠️ Tecnologias e Stack

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web assíncrono, prático e ágil.
- **[Poetry](https://python-poetry.org/):** Gerenciador de dependências e ambientes virtuais.
- **[SQLite](https://sqlite.org/) + [aiosqlite](https://pypi.org/project/aiosqlite/):** Banco de Dados embutido rodando de maneira assíncrona.
- **[SQLAlchemy 2.0](https://www.sqlalchemy.org/):** ORM utilizado na modelagem das tabelas do banco de dados de maneira assíncrona.
- **[Alembic](https://alembic.sqlalchemy.org/):** Gerenciador de migrações do banco de dados.
- **[Passlib](https://passlib.readthedocs.io/) & [Python-Jose](https://pypi.org/project/python-jose/):** Tratamento de criptografia (bcrypt) e geração de Tokens (JWT).

## 🗂️ Estrutura do Projeto

```text
├── alembic/                 # Configuração e versões das migrações do Alembic
├── app/
│   ├── core/                # Configurações centrais do sistema  
│   ├── models/              # Modelos (Tabelas) do SQLAlchemy
│   ├── routes/              # Roteadores do FastAPI (Auth, Cliente, Conta, Transação)
│   ├── schemas/             # Contratos Pydantic (Entrada/Saída de dados)
│   ├── services/            # Camada de lógica de negócios e interação com o DB
│   ├── database.py          # Configurações do Engine do DB (aiosqlite)
│   ├── main.py              # Ponto de entrada do FastAPI
│   └── security.py          # Criação e Validação do JWT e Usuário Logado
├── bank.db                  # Banco de Dados SQLite (Gerado automaticamente)
├── alembic.ini              # Configuração inicial do Alembic
└── pyproject.toml           # Dependências gerenciadas pelo Poetry
```

## 🚀 Como Rodar o Projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/masagro/luisalabs-dio-api-bancaria-com-fastAPI.git
cd luisalabs-dio-api-bancaria-com-fastAPI
```

2. **Instale as dependências (via Poetry):**
```bash
poetry install
```

3. **Inicie o banco de dados (se necessário recriar):**  
*(O repositório já pode conter o banco pronto, mas caso queira aplicar novas migrações e tabelas originais, use:)*
```bash
poetry run alembic upgrade head
```

4. **Inicie o servidor (FastAPI em modo de desenvolvimento):**
```bash
poetry run fastapi dev app/main.py
```

## 📚 Documentação e Testes (Swagger UI)

Por estar desenvolvida usando APIs modernas com FastAPI, a aplicação gera **Documentação Interativa Automaticamente**.  
Com a aplicação em execução, abra o seu navegador e acesse a interface OpenAPI, também conhecida como **Swagger UI**, pelo endereço:  
👉 **http://localhost:8000/docs**

### Fluxo Rápido de Teste no Swagger:
1. Vá na aba `/clientes/` e cadastre o seu cliente. (Gravar e-mail e senha inseridos).
2. Vá no botão `Authorize` (ou cadeado fechado nas rotas), insira o seu e-mail e sua senha para obter o Token de autenticidade validando o Login.
3. Com o Token validado, Vá na aba `/contas/` e cadastre a sua primeira Conta Corrente indicando o ID do seu cliente.
4. Vá em `/transacoes/`, teste a API através de um depósito de R$ 1000 reais.
5. Em seguida, pela própria aba de `/transacoes/`, tente realizar o saque de um valor ou realize operações para testar a barreira contra valores além da conta.   
6. Teste o endpoint `GET /transacoes/extrato/{id}` preenchendo o ID da conta a qual desejar consultar, verá todo o log gerado.

---
*Projeto elaborado durante a jornada DIO, finalizado por inteligência artificial.*
