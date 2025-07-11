# 📘 Guia de Boas Práticas de Desenvolvimento - Meu Doce Dinheiro

Este arquivo foi criado para registrar e aplicar boas práticas de programação, organização e estruturação de projetos Python, com foco em aprendizado e profissionalismo.

---

## 🧱 Organização do Projeto

- Cada módulo (usuários, categorias, transações, etc.) deve ter seu próprio arquivo `.py` com funções relacionadas.
- O arquivo `db.py` centraliza a conexão e criação das tabelas.
- Arquivos auxiliares como `utils.py` agrupam funções utilitárias (ex: `reset_db()`).
- A pasta `data/` armazena arquivos gerados, como o banco de dados `.db`.

---

## 🧠 Convenções de Nomeação

- Funções e variáveis em **snake_case**: `adicionar_usuario`, `reset_db`, `categoria_id`
- Arquivos em letras minúsculas com underscores: `users.py`, `categories.py`
- Nomes devem ser descritivos e claros, evitar siglas obscuras

---

## 🧾 Comentários e Documentação

- Use docstrings em funções para explicar o que fazem, parâmetros e retorno:
  Exemplo:
  """Adiciona um novo usuário ao banco de dados."""
- Comentários devem **explicar a intenção**, não repetir o óbvio.
- Cabeçalho de cada arquivo pode incluir:
  - Autor
  - Propósito do módulo
  - Data de criação (opcional)

---

## 📦 Modularização

- Funções com uma única responsabilidade → mais fáceis de testar e manter
- Evitar duplicação de código (DRY - Don't Repeat Yourself)
- Separar lógica de apresentação (ex: não misturar `print()` dentro de funções de banco)

---

## 🧪 Testes e Validações (a implementar)

- Funções devem ser previsíveis e retornar dados claros
- Podemos usar `assert` em scripts de teste ou `pytest` no futuro

---

## 💡 Dica contínua

> Escrever código é fácil. Escrever código **legível, reutilizável e confiável** é o que faz você crescer como desenvolvedor.

---

Este guia vai evoluindo com o projeto. Sempre que aplicarmos ou discutirmos uma boa prática nova, ela entra aqui. 🚀
