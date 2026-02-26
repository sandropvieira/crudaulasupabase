import streamlit as st
from supabase import create_client, Client
import time

# =============================
# Configuração Supabase
# =============================
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(URL, KEY)

# =============================
# Funções de Banco
# =============================
def get_alunos():
    return supabase.table("alunos").select("*").order("nome").execute().data

def add_aluno(nome, email, cidade):
    supabase.table("alunos").insert({
        "nome": nome,
        "email": email,
        "cidade": cidade
    }).execute()

def update_alunos(id, nome, email, cidade):
    supabase.table("alunos").update({
        "nome" : nome,
        "email": email,
        "cidade": cidade
    }).eq("id", id).execute()

def delete_aluno(id):
    supabase.table("alunos").delete().eq("id", id).execute()

# =============================
# UI
# =============================
st.set_page_config(page_title="CRUD Alunos", layout="centered")
st.title("📘 CRUD com Streamlit + Supabase")

tab_ver, tab_criar, tab_atualizar, tab_deletar = st.tabs(["👀 Ver Alunos", "➕ Criar Aluno", "✏️ Atualizar Alunos", "❌ Deletar Alunos"])

# =============================
# ABA VER ALUNOS
# =============================
with tab_ver:
    alunos = get_alunos()

    if alunos:
        for aluno in alunos:
            st.write(
                f"**{aluno['nome']}** — {aluno['email']} — {aluno['cidade']}"
            )
    else:
        st.info("Nenhum aluno cadastrado.")

# =============================
# ABA CRIAR ALUNO
# =============================
with tab_criar:
    st.subheader("Cadastrar novo aluno")

    with st.form("form_criar_aluno", clear_on_submit=True):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        cidade = st.text_input("Cidade")

        submitted = st.form_submit_button("Salvar")

        if submitted:
            if nome and email and cidade:
                add_aluno(nome, email, cidade)
                st.success(f"Aluno **{nome}** cadastrado com sucesso! 🎉")
            else:
                st.warning("Preencha todos os campos 😒")


# =============================
# ABA ATUALIZAR ALUNOS
# =============================
with tab_atualizar:
    alunos = get_alunos()

    if not alunos:
        st.info("Nenhum aluno para editar")
    else:
        opcoes = {} #dicionario vazio para carregar as opções
        chaves = [] # lista para vazia para adicionar as chaves dos alunos

        for aluno in alunos:
            chave_unica =  aluno["nome"] +" (" + aluno["email"] + ")" # armazenando dentro da lista
            opcoes[chave_unica] = aluno
            chaves.append(chave_unica)

        aluno_selecionado = st.selectbox(
            "Selecione",
            chaves,
            key="edit_select"
        )

        aluno_selecionado_para_atualizar = opcoes[aluno_selecionado]

        with st.form("form_editar"):
            novo_nome = st.text_input("Nome", value = aluno_selecionado_para_atualizar["nome"])
            novo_email = st.text_input("Email", value= aluno_selecionado_para_atualizar["email"])
            nova_cidade = st.text_input("Cidade", value= aluno_selecionado_para_atualizar["cidade"])

            if st.form_submit_button("Salvar"):
                update_alunos(aluno_selecionado_para_atualizar["id"], novo_nome, novo_email, nova_cidade)
                st.success("Dados do aluno atualizado")
                time.sleep(20)
                st.rerun()

with tab_deletar:
    alunos = get_alunos()

    if not alunos:
        st.info("Nenhum aluno selecionado para excluir")
    else:
        opcoes = {}
        chaves = []

        for aluno in alunos:
            chave_unica = aluno["nome"] + " ( " + aluno["email"] + ")"
            opcoes[chave_unica] = aluno
            chaves.append(chave_unica)

        selecionado = st.selectbox(
            "Selecione o Aluno",
            chaves,
            key = "del_select"
        )

        aluno_selecionado = opcoes[selecionado]

        st.warning("**Você esta prestes a excluir: **" + aluno_selecionado["nome"])

        if st.button("Excluir", type="primary"):
            delete_aluno(aluno_selecionado["id"])
            st.success("Aluno excluido com sucesso!")
            time.sleep(10)
            st.rerun()