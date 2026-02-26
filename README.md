# 📘 CRUD Alunos — Streamlit + Supabase

Aplicação web simples para gerenciamento de alunos, desenvolvida com **Python + Streamlit** e integrada ao banco de dados **Supabase** (PostgreSQL na nuvem).

---

## 🚀 Funcionalidades

- **👀 Ver Alunos** — Lista todos os alunos cadastrados, exibindo nome, e-mail e cidade.
- **➕ Criar Aluno** — Formulário para cadastrar um novo aluno com nome, e-mail e cidade.
- **✏️ Atualizar Aluno** — Seleciona um aluno existente e permite editar seus dados.
- **❌ Deletar Aluno** — Seleciona e remove permanentemente um aluno do banco de dados.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| [Python](https://www.python.org/) | Linguagem principal do projeto |
| [Streamlit](https://streamlit.io/) | Framework para criação da interface web |
| [Supabase](https://supabase.com/) | Backend as a Service — banco de dados PostgreSQL na nuvem |
| [supabase-py](https://github.com/supabase-community/supabase-py) | SDK Python para comunicação com o Supabase |

---

## ☁️ Integração com o Supabase

O projeto utiliza o **Supabase** como banco de dados remoto. A conexão é feita via SDK oficial (`supabase-py`) usando as credenciais armazenadas nos **Secrets do Streamlit**.

A tabela utilizada é a `alunos`, com a seguinte estrutura esperada:

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | `int` (auto) | Identificador único |
| `nome` | `text` | Nome do aluno |
| `email` | `text` | E-mail do aluno |
| `cidade` | `text` | Cidade do aluno |

---

## ⚙️ Como Executar Localmente

### 1. Pré-requisitos

- Python 3.8 ou superior
- Conta no [Supabase](https://supabase.com/) com a tabela `alunos` criada

### 2. Instalação das dependências

```bash
pip install streamlit supabase
```

### 3. Configuração dos Secrets

Crie o arquivo `.streamlit/secrets.toml` na raiz do projeto com suas credenciais do Supabase:

```toml
SUPABASE_URL = "https://seu-projeto.supabase.co"
SUPABASE_KEY = "sua-chave-anon-ou-service-role"
```

> ⚠️ **Nunca** compartilhe ou versione este arquivo. Adicione `.streamlit/secrets.toml` ao seu `.gitignore`.

### 4. Executando a aplicação

```bash
streamlit run app.py
```

Acesse no navegador: `http://localhost:8501`

---

## 📁 Estrutura do Projeto

```
.
├── app.py                  # Código principal da aplicação
└── .streamlit/
    └── secrets.toml        # Credenciais do Supabase (não versionar)
```

---

## 🌐 Deploy

Para fazer o deploy no [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Suba o projeto em um repositório público no GitHub (sem o `secrets.toml`).
2. Acesse [share.streamlit.io](https://share.streamlit.io) e conecte o repositório.
3. Vá em **Advanced settings → Secrets** e adicione as variáveis:
   ```
   SUPABASE_URL = "https://seu-projeto.supabase.co"
   SUPABASE_KEY = "sua-chave-anon"
   ```

---

## 📝 Observações

- Os dados são persistidos diretamente no Supabase, sendo acessíveis de qualquer lugar após o deploy.
- Após atualizar ou deletar um aluno, a aplicação aguarda alguns segundos e recarrega a página automaticamente para refletir as mudanças.
