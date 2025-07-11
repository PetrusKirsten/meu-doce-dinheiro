# Meu Doce Dinheiro

**Sistema de controle de finanças pessoais**, desenvolvido em Python (FastAPI) no backend e Next.js no frontend. Uma aplicação simples e didática para registrar, visualizar e gerenciar receitas, despesas e planejamentos financeiros.

---

## 📋 Funcionalidades Principais

- CRUD completo de **usuários**, **categorias**, **transações** e **planejamentos**
- API RESTful criada com **FastAPI**, com documentação automática via Swagger UI
- Dashboard interativo em **Next.js** com gráficos (linhas, pizza, barras) usando Recharts
- CLI de manutenção (`menu_cli.py`) para operações como reset de banco, seed e consultas rápidas
- Banco de dados **SQLite**, leve e portátil (`backend/data/financas.db`)
- Integração contínua básica com **GitHub Actions** (lint e testes)

---

## 🛠 Tech Stack

- **Backend**: Python 3.x, FastAPI, SQLAlchemy, Pydantic
- **Banco de Dados**: SQLite
- **Frontend**: Next.js (React), TypeScript, Tailwind CSS, Recharts
- **CLI**: Script Python para menu de terminal
- **CI**: GitHub Actions (pytest, flake8)

---

## 🚀 Pré-requisitos

- Python 3.10+ e `pip`
- Node.js 16+ e `npm` ou `yarn`
- (Opcional) Docker e Docker Compose para containerização futura

---

## 💻 Instalação e Execução

### 1. Clone do Repositório
```bash
git clone https://github.com/seu-usuario/meu-doce-dinheiro.git
cd meu-doce-dinheiro
```

### 2. Configuração do Backend

1. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate  # Windows
   ```
2. Instale dependências:
   ```bash
   pip install --upgrade pip
   pip install -r backend/requirements.txt
   ```
3. (Opcional) Ajuste configurações em `backend/app/config.py` ou via variáveis de ambiente.
4. Inicie o servidor FastAPI:
   ```bash
   uvicorn backend.app.main:app --reload
   ```
5. Acesse a documentação interativa:
   - HTTP API: `http://localhost:8000/docs`
   - Redoc: `http://localhost:8000/redoc`

### 3. Uso do CLI de Manutenção

Ainda no backend, você pode usar o menu de terminal para tarefas auxiliares:
```bash
python backend/app/menu_cli.py
```
- **Reset do banco**
- **Seed de dados**
- **Consultas rápidas**

### 4. Configuração do Frontend

1. Acesse a pasta do frontend:
   ```bash
   cd frontend
   ```
2. Instale dependências:
   ```bash
   npm install
   # ou yarn
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   # abre em http://localhost:3000
   ```
4. O frontend consome a API em `http://localhost:8000` por padrão.

---

## ✅ Testes e Lint

- **Testes** com pytest:
  ```bash
  pytest -q
  ```
- **Lint** com flake8:
  ```bash
  flake8 backend/app
  ```

Na pipeline do GitHub Actions, estes comandos são executados automaticamente em cada PR.

---

## 📈 CI/CD

O repositório inclui um workflow básico em `.github/workflows/ci.yml` que:

1. Faz **checkout** do código
2. Configura Python 3.10
3. Instala dependências e flake8
4. Executa lint e testes

Após merge em `main` ou `develop`, o CI roda automaticamente e sinaliza erros no GitHub.

---

## 🎯 Roadmap

- Containerização com **Docker** e **Docker Compose**
- Deploy contínuo automático (Docker Registry, Heroku, Vercel)
- Autenticação JWT e perfis de usuários
- Relatórios avançados e agendamento de avisos
- App móvel com React Native / Expo

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório
2. Crie uma branch feature: `git checkout -b feature/nome-da-feature`
3. Faça commit das suas mudanças: `git commit -m "feat: descrição da feature"`
4. Push na branch: `git push origin feature/nome-da-feature`
5. Abra um Pull Request


---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

