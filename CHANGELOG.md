# Changelog

Todas as mudanças importantes deste projeto serão documentadas aqui.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/)
e usa [SemVer](https://semver.org/lang/pt-BR/) para versionamento.

---

## [0.2.3] – 2025-07-21

### Added

- Página de **signup** para cadastro de usuários (rota POST /users).
- Página de **login** com autenticação JWT e armazenamento em AuthContext.
- Fluxo de **onboarding**: telas Welcome, CategorySetup e FirstTransactionSetup.
- Middleware de roteamento para liberar `/login`, `/signup`, `/onboarding` e proteger o restante.
- Guard client-side nos componentes de onboarding que redireciona usuário já onboarded para `/dashboard`.
- Models, schemas e CRUD atualizados para suportar `hashed_password` (bcrypt) e flag `onboarded` no usuário.
- Endpoint **GET /users** (debug) incluindo hash da senha para inspecionar credenciais.

### Changed

- Ajuste nos imports TS para caminhos relativos ou configuração de `tsconfig.json`.
- Centralização das chamadas de API em `frontend/lib/api`.

---

## [0.2.2] – 2025-07-15

### Added

- **Backend**  
  - Novos schemas de update (UserUpdate, CategoryUpdate, TransactionUpdate) em `schemas.py`.  
  - Endpoints **PUT** e **DELETE** para users, categories e transactions em `main.py`.  
  - Funções `update_*` e `delete_*` em `crud.py`, com checagem de integridade (não permite apagar categoria em uso).  
  - Filtro em `get_transactions` para descartar transações órfãs, evitando `ResponseValidationError`.

- **API Client** (`frontend/lib/api`)
  - Novas funções REST:  
    - `updateUser`, `deleteUser`  
    - `updateCategory`, `deleteCategory`  
    - `updateTransaction`, `deleteTransaction`

- **Frontend UI** (Next.js + React Query)  
  - Botões de “🗑️” para excluir users, categories e transactions diretamente nas listas.  
  - Mutations de delete com React Query, incluindo _optimistic updates_ (uso de `onMutate`, `onError`, `onSettled`) para remoção instantânea do cache.  
  - Tratamento de loading e rollback automático em caso de erro.

### Changed

- Ajuste no hook de listagem de `categories` para evitar estado `undefined` (`data = []` por default).  
- Atualização dos componentes de listagem (`index.tsx`) para suportar `invalidateQueries` e remapear arrays sem causar erro de `.map` em `undefined`.

### Fixed

- ResponseValidationError ao listar transações com `category_id = None`.  
- Erro de “Cannot read properties of undefined” em `categories.map` após delete.

---

## [0.2.1]

### Test

- Adicionar testes de unidade para as funções de CRUD do backend usando pytest.
- Adicionar testes de integração para endpoints FastAPI com TestClient e SQLite in-memory.
- Configurar `conftest.py` com `StaticPool` para isolamento dos testes.

### CI

- Incluir workflow GitHub Actions (`ci.yml`) para executar lint (flake8) e testes (pytest) em cada PR.

---

## [0.1.1] – 2025-07-10

### Refactor

- Aprimorar mensagens de saída nas funções de reset do banco de dados.
- Ajustar duração do `sleep` no menu.

---

## [0.1.0] - 2025-07-10

### Adicionado

- Estrutura inicial do projeto `Meu Doce Dinheiro`
- Banco de dados SQLite com tabelas de usuários, categorias, transações e planejamentos
- Inserção de usuários e categorias padrão via função `popular_db()`
- Interface de terminal com menu principal (`menu.py`)
- Exibição formatada de tabelas no terminal (`exibir_tabela()`)
- Validações de entrada para usuários, categorias e formas de pagamento
- Padronização da data com validação
- Funções reaproveitáveis para escolha de opções (`escolher_opcao`, `escolher_item`)
- Boas práticas de modularização, cabeçalhos e documentação
- Função `print_init()` com exibição de versão, autor e descrição na inicialização

### Alterado

- Nomes de funções padronizados em português
- Adaptação do sistema para controle de múltiplos usuários (Petrus, Mel, Casal)
- Categoria com campo `metodo_pgto` e transações com `forma_pagamento`
- Coluna "compartilhada" agora exibida como "Sim/Não"

### Corrigido

- Problemas com reset e recriação das tabelas no banco de dados
- Tratamento de erros em entrada de dados inválida no menu

---
