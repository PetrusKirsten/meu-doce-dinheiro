# Changelog

Todas as mudanças importantes deste projeto serão documentadas aqui.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/)
e usa [SemVer](https://semver.org/lang/pt-BR/) para versionamento.

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
