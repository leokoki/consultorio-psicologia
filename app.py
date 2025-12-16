import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import database as db

st.set_page_config(
    page_title="Consultório Tassiane - Gerenciador",
    page_icon="https://i.ibb.co/ynZx7QBP/sgs-deborapsicologa-logo-final-16.png",
    layout="wide"
)

# Senha vem dos Secrets (não aparece no código público)
PASSWORD = st.secrets["app"]["password"]

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    senha_input = st.text_input("🔐 Digite a senha para acessar", type="password")
    if senha_input == PASSWORD:
        st.session_state.autenticado = True
        st.rerun()
    else:
        st.warning("Senha incorreta.")
        st.stop()

st.sidebar.title("🧠 Gerenciador de Consultório")
page = st.sidebar.radio(
    "Navegação",
    ["📊 Dashboard Completo", "👥 Clientes", "📅 Sessões", "➕ Novo Cliente", "➕ Nova Sessão"]
)

if page == "📊 Dashboard Completo":
    st.title("📊 Dashboard Financeiro Completo")

    # Obter dados
    receita_mensal = db.get_monthly_revenue()
    clientes_ativos = db.get_active_clients_per_month()
    mes_atual = db.get_current_month_stats()
    ano_atual = db.get_ytd_stats()
    sessoes_por_cliente = db.get_sessions_per_client_current_month()

    # Calcular clientes únicos no mês
    sessoes = db.get_sessions()
    if not sessoes.empty:
        sessoes['session_date'] = pd.to_datetime(sessoes['session_date'])
        mes_atual_str = datetime.now().strftime("%Y-%m")
        clientes_mes_atual = sessoes[
            sessoes['session_date'].dt.strftime("%Y-%m") == mes_atual_str
        ]['client_name'].nunique()
    else:
        clientes_mes_atual = 0

    total_sessoes_mes = mes_atual["sessoes"]

    # CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="💰 Receita do Mês Atual",
            value=f"R$ {mes_atual['receita']:,.2f}",
            delta=f"{mes_atual['change']:+.1f}% vs mês passado"
        )

    with col2:
        st.metric(
            label="📅 Receita Acumulada no Ano",
            value=f"R$ {ano_atual['receita']:,.2f}",
            delta=f"{ano_atual['change']:+.1f}% vs ano passado"
        )

    with col3:
        st.metric(
            label="🔢 Atendimentos Realizados no Mês",
            value=int(total_sessoes_mes)
        )

    with col4:
        st.metric(
            label="👥 Clientes Atendidos no Mês",
            value=int(clientes_mes_atual)
        )

    st.divider()

    # GRÁFICO 1: Receita Mensal
    st.subheader("💵 Receita Mensal (Últimos 12 Meses)")

    if not receita_mensal.empty:
        receita_mensal = receita_mensal.tail(12)
        media_receita = receita_mensal['total_revenue'].mean()

        fig1 = go.Figure()

        fig1.add_trace(go.Bar(
            x=receita_mensal['month'],
            y=receita_mensal['total_revenue'],
            name='Receita Mensal',
            marker_color='#1f77b4',
            text=receita_mensal['total_revenue'].apply(lambda x: f'R$ {x:,.0f}'),
            textposition='outside'
        ))

        fig1.add_trace(go.Scatter(
            x=receita_mensal['month'],
            y=[media_receita] * len(receita_mensal),
            name=f'Média (R$ {media_receita:,.0f})',
            line=dict(color='red', dash='dash', width=2),
            mode='lines'
        ))

        fig1.update_layout(
            xaxis_title="Ano/Mês",
            yaxis_title="Valor Acumulado (R$)",
            hovermode='x unified',
            showlegend=True,
            height=400
        )

        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("Nenhuma receita disponível")

    st.divider()

    # GRÁFICOS 2 e 3
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Atendimentos por Mês")

        if not receita_mensal.empty:
            fig2 = go.Figure()

            fig2.add_trace(go.Bar(
                x=receita_mensal['month'],
                y=receita_mensal['num_sessions'],
                marker_color='#2ca02c',
                text=receita_mensal['num_sessions'],
                textposition='outside'
            ))

            fig2.update_layout(
                xaxis_title="Mês",
                yaxis_title="Número de Atendimentos",
                hovermode='x unified',
                height=350
            )

            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("Nenhum atendimento disponível")

    with col2:
        st.subheader("👥 Clientes Ativos por Mês")

        if not clientes_ativos.empty:
            fig3 = go.Figure()

            fig3.add_trace(go.Scatter(
                x=clientes_ativos['month'],
                y=clientes_ativos['active_clients'],
                mode='lines+markers',
                marker=dict(size=10, color='#ff7f0e'),
                line=dict(width=3, color='#ff7f0e'),
                text=clientes_ativos['active_clients'],
                textposition='top center'
            ))

            fig3.update_layout(
                xaxis_title="Mês",
                yaxis_title="Clientes Ativos",
                hovermode='x unified',
                height=350
            )

            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("Nenhum cliente ativo disponível")

    st.divider()

    # GRÁFICO 4: Atendimentos por Cliente
    st.subheader("🔢 Atendimentos por Cliente no Mês Atual")

    if not sessoes_por_cliente.empty:
        fig4 = go.Figure()

        fig4.add_trace(go.Bar(
            x=sessoes_por_cliente['name'],
            y=sessoes_por_cliente['num_sessions'],
            marker_color='#9467bd',
            text=sessoes_por_cliente['num_sessions'],
            textposition='outside'
        ))

        fig4.update_layout(
            xaxis_title="Cliente",
            yaxis_title="Número de Atendimentos",
            xaxis_tickangle=-45,
            height=400
        )

        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("Nenhum atendimento neste mês")

elif page == "👥 Clientes":
    st.title("👥 Gestão de Clientes")

    clientes = db.get_clients()

    if not clientes.empty:
        col1, col2 = st.columns([3, 1])
        with col1:
            busca = st.text_input("🔍 Buscar por nome", "")
        with col2:
            filtro_status = st.selectbox("Status", ["Todos", "active", "inactive"])

        filtrados = clientes.copy()
        if busca:
            filtrados = filtrados[filtrados['name'].str.contains(busca, case=False, na=False)]
        if filtro_status != "Todos":
            filtrados = filtrados[filtrados['status'] == filtro_status]

        st.dataframe(
            filtrados,
            use_container_width=True,
            hide_index=True
        )

        st.metric("Total de Clientes", len(filtrados))
    else:
        st.info("Nenhum cliente registrado ainda")

elif page == "📅 Sessões":
    st.title("📅 Histórico de Sessões")

    sessoes = db.get_sessions()

    if not sessoes.empty:
        sessoes['session_date'] = pd.to_datetime(sessoes['session_date'])

        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.date_input("De", value=sessoes['session_date'].min())
        with col2:
            data_fim = st.date_input("Até", value=sessoes['session_date'].max())

        filtradas = sessoes[
            (sessoes['session_date'] >= pd.to_datetime(data_inicio)) &
            (sessoes['session_date'] <= pd.to_datetime(data_fim))
        ]

        st.dataframe(
            filtradas,
            use_container_width=True,
            hide_index=True
        )

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total de Sessões", len(filtradas))
        with col2:
            st.metric("Receita Total", f"R$ {filtradas['amount'].sum():,.2f}")
    else:
        st.info("Nenhuma sessão registrada ainda")

elif page == "➕ Novo Cliente":
    st.title("➕ Registrar Novo Cliente")

    with st.form("novo_cliente"):
        nome = st.text_input("Nome Completo *")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")

        submetido = st.form_submit_button("✅ Registrar Cliente")

        if submetido:
            if nome:
                db.add_client(nome, email, telefone)
                st.success(f"✅ Cliente '{nome}' registrado!")
                st.balloons()
            else:
                st.error("❌ Nome é obrigatório")

elif page == "➕ Nova Sessão":
    st.title("➕ Registrar Nova Sessão")

    clientes = db.get_active_clients()

    if not clientes.empty:
        with st.form("nova_sessao"):
            col1, col2 = st.columns(2)

            with col1:
                opcoes_clientes = dict(zip(clientes['name'], clientes['id']))
                cliente_selecionado = st.selectbox("Cliente *", options=list(opcoes_clientes.keys()))
                data_sessao = st.date_input("Data da Sessão *", value=datetime.now())

            with col2:
                valor = st.number_input("Valor (R$) *", min_value=0.0, value=150.0, step=10.0)
                metodo_pagamento = st.selectbox(
                    "Método de Pagamento",
                    ["Pix", "Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Transferência"]
                )

            notas = st.text_area("Notas (opcional)")

            submetido = st.form_submit_button("✅ Registrar Sessão")

            if submetido:
                id_cliente = opcoes_clientes[cliente_selecionado]
                db.add_session(
                    id_cliente,
                    data_sessao.strftime('%Y-%m-%d'),
                    valor,
                    metodo_pagamento,
                    notas
                )
                st.success(f"✅ Sessão registrada!")
                st.balloons()
    else:
        st.warning("⚠️ Nenhum cliente ativo disponível.")

st.sidebar.divider()
st.sidebar.caption("Gerenciador v2.0 - Google Sheets")
