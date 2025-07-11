# Changelog

Todas as mudanças importantes deste projeto serão documentadas aqui.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/)
e usa [SemVer](https://semver.org/lang/pt-BR/) para versionamento.

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
