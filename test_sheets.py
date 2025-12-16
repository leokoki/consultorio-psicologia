import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("🧪 Teste de Conexão com Google Sheets")

try:
    # 1. Autenticar
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds_dict = dict(st.secrets["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    st.success("✅ Autenticação funcionou!")

    # 2. Listar todas as planilhas acessíveis
    st.subheader("📊 Planilhas Disponíveis:")

    spreadsheets = client.openall()

    if spreadsheets:
        for sheet in spreadsheets:
            st.write(f"- **{sheet.title}** (ID: {sheet.id})")
    else:
        st.warning("⚠️ Nenhuma planilha encontrada. Certifique-se de compartilhar a planilha com o service account.")

    # 3. Tentar abrir a planilha específica
    st.subheader("🔍 Tentando abrir: 'Consultório Psicologia'")

    try:
        target_sheet = client.open("Consultório Psicologia")
        st.success(f"✅ Planilha encontrada! ID: {target_sheet.id}")

        # Listar abas
        worksheets = target_sheet.worksheets()
        st.write("**Abas disponíveis:**")
        for ws in worksheets:
            st.write(f"- {ws.title}")

    except gspread.exceptions.SpreadsheetNotFound:
        st.error("❌ Planilha 'Consultório Psicologia' não encontrada.")
        st.info("💡 Certifique-se de:")
        st.write("1. O nome está exatamente igual (com acentos)")
        st.write("2. A planilha foi compartilhada com o service account")
        st.write(f"3. Email do service account: `{creds_dict['client_email']}`")

except Exception as e:
    st.error(f"❌ Erro: {e}")
    st.write("**Detalhes:**")
    st.exception(e)
