import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime
import streamlit as st
import json

def get_sheets_client():
    """Conecta ao Google Sheets usando credenciais do Streamlit Secrets"""
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Pega as credenciais do Streamlit Secrets
    creds_dict = dict(st.secrets["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    return client

def get_spreadsheet():
    """Abre a planilha do consultório"""
    client = get_sheets_client()
    # Substitua pelo nome da sua planilha
    sheet = client.open_by_key("1UKGuX_l2fd7__bkOmME22r4jSnoQj8WnQKq6h8tDfuA")
    return sheet

def get_clients():
    """Retorna todos os clientes"""
    sheet = get_spreadsheet()
    worksheet = sheet.worksheet("clients")
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def get_active_clients():
    """Retorna apenas clientes ativos"""
    df = get_clients()
    if not df.empty:
        return df[df['status'] == 'active']
    return df

def add_client(name, email, phone):
    """Adiciona um novo cliente"""
    sheet = get_spreadsheet()
    worksheet = sheet.worksheet("clients")

    # Pega o próximo ID
    data = worksheet.get_all_records()
    next_id = len(data) + 1

    # Adiciona nova linha
    row = [
        next_id,
        name,
        email,
        phone,
        datetime.now().strftime("%Y-%m-%d"),
        "active"
    ]
    worksheet.append_row(row)

def get_sessions():
    """Retorna todas as sessões com nome do cliente"""
    sheet = get_spreadsheet()
    sessions_ws = sheet.worksheet("sessions")
    clients_ws = sheet.worksheet("clients")

    sessions_data = sessions_ws.get_all_records()
    clients_data = clients_ws.get_all_records()

    sessions_df = pd.DataFrame(sessions_data)
    clients_df = pd.DataFrame(clients_data)

    if not sessions_df.empty and not clients_df.empty:
        # Merge para pegar o nome do cliente
        merged = sessions_df.merge(
            clients_df[['id', 'name']], 
            left_on='client_id', 
            right_on='id', 
            how='left'
        )
        merged.rename(columns={'name': 'client_name'}, inplace=True)
        merged.drop(columns=['id_y'], inplace=True)
        merged.rename(columns={'id_x': 'id'}, inplace=True)
        return merged

    return pd.DataFrame()

def add_session(client_id, session_date, amount, payment_method, notes=""):
    """Adiciona uma nova sessão"""
    sheet = get_spreadsheet()
    worksheet = sheet.worksheet("sessions")

    # Pega o próximo ID
    data = worksheet.get_all_records()
    next_id = len(data) + 1

    # Adiciona nova linha
    row = [
        next_id,
        client_id,
        session_date,
        amount,
        payment_method,
        notes
    ]
    worksheet.append_row(row)

def get_monthly_revenue():
    """Retorna receita mensal dos últimos 12 meses"""
    df = get_sessions()

    if df.empty:
        return pd.DataFrame()

    df['session_date'] = pd.to_datetime(df['session_date'])
    df['month'] = df['session_date'].dt.to_period('M').astype(str)

    # Últimos 12 meses
    df = df[df['session_date'] >= pd.Timestamp.now() - pd.DateOffset(months=12)]

    monthly = df.groupby('month').agg({
        'amount': 'sum',
        'id': 'count'
    }).reset_index()

    monthly.columns = ['month', 'total_revenue', 'num_sessions']

    return monthly

def get_active_clients_per_month():
    """Retorna número de clientes ativos por mês"""
    df = get_sessions()

    if df.empty:
        return pd.DataFrame()

    df['session_date'] = pd.to_datetime(df['session_date'])
    df['month'] = df['session_date'].dt.to_period('M').astype(str)

    # Últimos 12 meses
    df = df[df['session_date'] >= pd.Timestamp.now() - pd.DateOffset(months=12)]

    monthly = df.groupby('month')['client_id'].nunique().reset_index()
    monthly.columns = ['month', 'active_clients']

    return monthly

def get_current_month_stats():
    """Retorna estatísticas do mês atual"""
    df = get_sessions()

    if df.empty:
        return {"receita": 0, "sessoes": 0, "change": 0}

    df['session_date'] = pd.to_datetime(df['session_date'])

    current_month = pd.Timestamp.now().to_period('M')
    previous_month = (pd.Timestamp.now() - pd.DateOffset(months=1)).to_period('M')

    current_data = df[df['session_date'].dt.to_period('M') == current_month]
    previous_data = df[df['session_date'].dt.to_period('M') == previous_month]

    current_revenue = current_data['amount'].sum() if not current_data.empty else 0
    previous_revenue = previous_data['amount'].sum() if not previous_data.empty else 0

    change = ((current_revenue - previous_revenue) / previous_revenue * 100) if previous_revenue > 0 else 0

    return {
        "receita": current_revenue,
        "sessoes": len(current_data),
        "change": change
    }

def get_ytd_stats():
    """Retorna estatísticas do ano até agora"""
    df = get_sessions()

    if df.empty:
        return {"receita": 0, "change": 0}

    df['session_date'] = pd.to_datetime(df['session_date'])

    current_year = pd.Timestamp.now().year
    previous_year = current_year - 1
    current_month = pd.Timestamp.now().month

    current_ytd = df[
        (df['session_date'].dt.year == current_year)
    ]['amount'].sum()

    previous_ytd = df[
        (df['session_date'].dt.year == previous_year) &
        (df['session_date'].dt.month <= current_month)
    ]['amount'].sum()

    change = ((current_ytd - previous_ytd) / previous_ytd * 100) if previous_ytd > 0 else 0

    return {
        "receita": current_ytd,
        "change": change
    }

def get_sessions_per_client_current_month():
    """Retorna número de sessões por cliente no mês atual"""
    df = get_sessions()

    if df.empty:
        return pd.DataFrame()

    df['session_date'] = pd.to_datetime(df['session_date'])
    current_month = pd.Timestamp.now().to_period('M')

    current_data = df[df['session_date'].dt.to_period('M') == current_month]

    if current_data.empty:
        return pd.DataFrame()

    result = current_data.groupby('client_name').agg({
        'id': 'count',
        'amount': 'sum'
    }).reset_index()

    result.columns = ['name', 'num_sessions', 'total_amount']
    result = result.sort_values('num_sessions', ascending=False)

    return result
