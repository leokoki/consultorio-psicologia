# 🧠 Consultório de Psicologia – Dashboard em Streamlit

Aplicação web para gerenciamento simples de um consultório de psicologia, construída em **Python + Streamlit** usando **Google Sheets** como banco de dados.  
Permite cadastrar clientes, registrar sessões, acompanhar faturamento mensal e visualizar métricas do consultório de forma prática.

---

## 📌 Funcionalidades

- 👥 **Cadastro de clientes**
  - Nome, e‑mail, telefone, status (ativo/inativo)
- 🗓️ **Registro de sessões**
  - Cliente, data, valor, forma de pagamento, observações
- 💰 **Dashboard financeiro**
  - Receita total
  - Receita por mês
  - Número de sessões por mês
  - Número de clientes ativos por mês
- 🔐 **Acesso protegido por senha**
  Senha armazenada em `st.secrets` (não vai para o Git)
- ☁️ **Persistência em Google Sheets**
  - Planilha usada como “banco de dados”
  - Abas recomendadas:
    - `clients`
    - `sessions`

---

## 🏗️ Arquitetura do Projeto

Estrutura básica do repositório:

text . ├── app.py # Código principal do Streamlit (interface e dashboard) ├── database.py # Funções de acesso e escrita no Google Sheets (gspread) ├── requirements.txt # Dependências Python ├── README.md # Este arquivo └── .streamlit/ └── config.toml # (opcional) Configuração de tema/servidor do Streamlit

> **Importante:**  
> Arquivos com credenciais **NÃO** devem ir para o Git (`service_account.json`, `secrets.toml`, `.env`, etc.).  
> Use o painel de **Secrets** do Streamlit Cloud para isso.

---

## 🧬 Tecnologias Utilizadas

- [Python](https://www.python.org/) (3.10+ recomendado)
- [Streamlit](https://streamlit.io/)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/googleapis/oauth2client)
- Google Sheets + Google Drive APIs

---

## 📊 Estrutura da Planilha (Google Sheets)

A aplicação usa uma planilha do Google como base de dados.  
Exemplo de planilha **“Consultório Psicologia”**

### Aba `clients`

| id | name            | email                  | phone         | created_at | status   |
|----|-----------------|------------------------|---------------|-----------|---------|
| 1  | Maria Silva     | maria.silva@email.com  | 11 98765-4321 | 2024-01-15 | active  |
| 2  | João Pereira    | joao.p@gmail.com       | 11 91234-5678 | 2024-01-18 | active  |
| …  | …               | …                      | …             | …         | …       |

### Aba `sessions`

| id | client_id | session_date | amount | payment_method   | notes             |
|----|-----------|--------------|--------|------------------|-------------------|
| 1  | 1         | 2025-01-03   | 150    | Pix              | Retorno           |
| 2  | 2         | 2025-01-05   | 150    | Cartão de Débito | -                 |
| …  | …         | …            | …      | …                | …                 |

- `client_id` faz referência ao `id` da aba `clients`.
- Datas no formato `YYYY-MM-DD`.

---

## 🔐 Segurança e Segredos

### 1. Senha do App

A senha de acesso ao dashboard é lida de `st.secrets`:

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">python</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-ulr3zxog3" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-python" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:rgb(127, 219, 202)">import</span><span> streamlit </span><span class="token" style="color:rgb(127, 219, 202)">as</span><span> stst</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>set_page_config</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span>
</span><span>    page_title</span><span class="token" style="color:rgb(127, 219, 202)">=</span><span class="token" style="color:rgb(173, 219, 103)">&quot;Consultório – Gerenciador&quot;</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span>
</span><span>    page_icon</span><span class="token" style="color:rgb(127, 219, 202)">=</span><span class="token" style="color:rgb(173, 219, 103)">&quot;🧠&quot;</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span>
</span><span>    layout</span><span class="token" style="color:rgb(127, 219, 202)">=</span><span class="token" style="color:rgb(173, 219, 103)">&quot;wide&quot;</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span>
</span><span></span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span>
<span>PASSWORD </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>secrets</span><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token" style="color:rgb(173, 219, 103)">&quot;app&quot;</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token" style="color:rgb(173, 219, 103)">&quot;password&quot;</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span>
</span>
<span></span><span class="token" style="color:rgb(127, 219, 202)">if</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;autenticado&quot;</span><span> </span><span class="token" style="color:rgb(127, 219, 202)">not</span><span> </span><span class="token" style="color:rgb(127, 219, 202)">in</span><span> st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>session_state</span><span class="token" style="color:rgb(199, 146, 234)">:</span><span>
</span><span>    st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>session_state</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>autenticado </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> </span><span class="token" style="color:rgb(255, 88, 116)">False</span><span>
</span>
<span></span><span class="token" style="color:rgb(127, 219, 202)">if</span><span> </span><span class="token" style="color:rgb(127, 219, 202)">not</span><span> st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>session_state</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>autenticado</span><span class="token" style="color:rgb(199, 146, 234)">:</span><span>
</span><span>    st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>markdown</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(173, 219, 103)">&quot;### 🔐 Acesso Restrito&quot;</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>    senha_input </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>text_input</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(173, 219, 103)">&quot;Digite a senha para acessar o sistema:&quot;</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span> </span><span class="token" style="color:rgb(130, 170, 255)">type</span><span class="token" style="color:rgb(127, 219, 202)">=</span><span class="token" style="color:rgb(173, 219, 103)">&quot;password&quot;</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>    </span><span class="token" style="color:rgb(127, 219, 202)">if</span><span> st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>button</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(173, 219, 103)">&quot;Entrar&quot;</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span class="token" style="color:rgb(199, 146, 234)">:</span><span>
</span><span>        </span><span class="token" style="color:rgb(127, 219, 202)">if</span><span> senha_input </span><span class="token" style="color:rgb(127, 219, 202)">==</span><span> PASSWORD</span><span class="token" style="color:rgb(199, 146, 234)">:</span><span>
</span><span>            st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>session_state</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>autenticado </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> </span><span class="token" style="color:rgb(255, 88, 116)">True</span><span>
</span><span>            st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>rerun</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>        </span><span class="token" style="color:rgb(127, 219, 202)">else</span><span class="token" style="color:rgb(199, 146, 234)">:</span><span>
</span><span>            st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>error</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(173, 219, 103)">&quot;❌ Senha incorreta!&quot;</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>    st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>stop</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span></code></pre></div>

### 2. Credenciais do Google (Service Account)

No **Streamlit Cloud**, as credenciais vão em **Settings → Secrets**, por exemplo:

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">toml</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-4yv3lk3mw" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-toml" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token table" style="color:rgb(255, 203, 139)">app</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">password</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;suaSenhaSeguraAqui&quot;</span><span>
</span>
<span></span><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token table" style="color:rgb(255, 203, 139)">gcp_service_account</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">type</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;service_account&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">project_id</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;consultorio-psicologia-xxxxx&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">private_key_id</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;...&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">private_key</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;&quot;&quot;-----BEGIN PRIVATE KEY-----
</span><span class="token" style="color:rgb(173, 219, 103)">...
</span><span class="token" style="color:rgb(173, 219, 103)">-----END PRIVATE KEY-----
</span><span class="token" style="color:rgb(173, 219, 103)">&quot;&quot;&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">client_email</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;consultorio-app@consultorio-psicologia-xxxxx.iam.gserviceaccount.com&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">client_id</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;...&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">auth_uri</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;https://accounts.google.com/o/oauth2/auth&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">token_uri</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;https://oauth2.googleapis.com/token&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">auth_provider_x509_cert_url</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;https://www.googleapis.com/oauth2/v1/certs&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">client_x509_cert</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;https://www.googleapis.com/robot/v1/metadata/x509/consultorio-app%40consultorio-psicologia-xxxxx.iam.gserviceaccount.com&quot;</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">universe_domain</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;googleapis.com&quot;</span><span>
</span></code></pre></div>

No código (`database.py`), elas são usadas assim:

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">python</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-w8n0kb8w4" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-python" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:rgb(127, 219, 202)">import</span><span> streamlit </span><span class="token" style="color:rgb(127, 219, 202)">as</span><span> st
</span><span></span><span class="token" style="color:rgb(127, 219, 202)">import</span><span> gspread
</span><span></span><span class="token" style="color:rgb(127, 219, 202)">from</span><span> oauth2client</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>service_account </span><span class="token" style="color:rgb(127, 219, 202)">import</span><span> ServiceAccountCredentials
</span>
<span></span><span class="token" style="color:rgb(127, 219, 202)">def</span><span> </span><span class="token" style="color:rgb(130, 170, 255)">get_spreadsheet</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span class="token" style="color:rgb(199, 146, 234)">:</span><span>
</span><span>    scopes </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">[</span><span>
</span><span>        </span><span class="token" style="color:rgb(173, 219, 103)">&quot;https://www.googleapis.com/auth/spreadsheets&quot;</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span>
</span><span>        </span><span class="token" style="color:rgb(173, 219, 103)">&quot;https://www.googleapis.com/auth/drive&quot;</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span>
</span><span>    </span><span class="token" style="color:rgb(199, 146, 234)">]</span><span>
</span><span>    creds_dict </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> </span><span class="token" style="color:rgb(130, 170, 255)">dict</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span>st</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>secrets</span><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token" style="color:rgb(173, 219, 103)">&quot;gcp_service_account&quot;</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>    creds </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> ServiceAccountCredentials</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>from_json_keyfile_dict</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span>creds_dict</span><span class="token" style="color:rgb(199, 146, 234)">,</span><span> scopes</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>    client </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> gspread</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>authorize</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span>creds</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span>
<span>    </span><span class="token" style="color:rgb(99, 119, 119);font-style:italic"># Substitua pelo ID real da sua planilha</span><span>
</span><span>    sheet </span><span class="token" style="color:rgb(127, 219, 202)">=</span><span> client</span><span class="token" style="color:rgb(199, 146, 234)">.</span><span>open_by_key</span><span class="token" style="color:rgb(199, 146, 234)">(</span><span class="token" style="color:rgb(173, 219, 103)">&quot;SEU_SHEET_ID_AQUI&quot;</span><span class="token" style="color:rgb(199, 146, 234)">)</span><span>
</span><span>    </span><span class="token" style="color:rgb(127, 219, 202)">return</span><span> sheet
</span></code></pre></div>

---

## ▶️ Como Rodar Localmente

1. **Clonar o repositório:**

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-4zwwyqzi5" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:rgb(130, 170, 255)">git</span><span> clone https://github.com/SEU_USUARIO/consultorio-psicologia.git
</span><span></span><span class="token" style="color:rgb(255, 203, 139)">cd</span><span> consultorio-psicologia
</span></code></pre></div>

2. **Criar e ativar ambiente virtual (opcional, mas recomendado):**

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-vlmkj52nl" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pythonm venv venv
</span><span></span><span class="token" style="color:rgb(255, 203, 139)">source</span><span> venv/bin/activate  </span><span class="token" style="color:rgb(99, 119, 119);font-style:italic"># Linux/Mac</span><span>
</span><span>venv</span><span class="token" style="color:rgb(199, 146, 234)">\</span><span>Scripts</span><span class="token" style="color:rgb(199, 146, 234)">\</span><span>activate     </span><span class="token" style="color:rgb(99, 119, 119);font-style:italic"># Windows</span><span>
</span></code></pre></div>

3. **Instalar dependências:**

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-xst8hlovm" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip </span><span class="token" style="color:rgb(130, 170, 255)">install</span><span> </span><span class="token parameter" style="color:rgb(214, 222, 235)">-r</span><span> requirements.txt
</span></code></pre></div>

4. **Configurar segredos localmente (opção simples)**

Crie um arquivo `.streamlit/secrets.toml` (e NÃO envie para o Git):

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">toml</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-a3ue3xz5m" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-toml" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token table" style="color:rgb(255, 203, 139)">app</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span>
</span><span></span><span class="token key" style="color:rgb(128, 203, 196)">password</span><span> </span><span class="token" style="color:rgb(199, 146, 234)">=</span><span> </span><span class="token" style="color:rgb(173, 219, 103)">&quot;suaSenhaSeguraAqui&quot;</span><span>
</span>
<span></span><span class="token" style="color:rgb(199, 146, 234)">[</span><span class="token table" style="color:rgb(255, 203, 139)">gcp_service_account</span><span class="token" style="color:rgb(199, 146, 234)">]</span><span>
</span><span></span><span class="token" style="color:rgb(99, 119, 119);font-style:italic"># cole aqui o conteúdo do JSON do service account convertido para TOML</span><span>
</span></code></pre></div>

5. **Rodar o app:**

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">bash</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-fe0xt1gwo" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-bash" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>streamlit run app.py
</span></code></pre></div>

O app ficará disponível em:
- http://localhost:8501

---

## ☁️ Deploy no Streamlit Cloud

1. Faça push do repositório para o GitHub (repositório público no plano gratuito).
2. Acesse: https://share.streamlit.io
3. Clique em **“New app”** e escolha o repositório e o arquivo principal (`app.py`).
4. Em **Settings → Secrets**, cole suas configurações (senha + gcp_service_account).
5. Salve e aguarde o deploy.

Opcionalmente, configure:
- Tema / Layout em `.streamlit/config.toml`
- Ícone e título via `st.set_page_config(...)` no início do `app.py`

---

## 🧪 Massa de Testes

A planilha pode ser preenchida com massa de testes para o ano inteiro (2025), com- Vários clientes
- Sessões distribuídas por mês
- Valores e formas de pagamento variados

Isso permite visualizar:
- Receita mensal
- Sazonalidade
- Número de clientes ativos ao longo do ano

*(Opcional: aqui você pode colar um trecho resumido ou link para um `tests_data.md` se criar um.)*

---

## ⚠️ Cuidados com Segurança

- **Nunca** envie:
  - `service_account.json`
  - `secrets.toml`
  - Tokens, senhas ou chaves
- Adicione estes arquivos ao `.gitignore`:

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">gitignore</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-rbf09qdo3" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-gitignore" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span class="token" style="color:rgb(99, 119, 119);font-style:italic"># Credenciais / segredos</span><span>
</span><span></span><span class="token entry" style="color:rgb(173, 219, 103)">secrets.toml</span><span>
</span><span></span><span class="token entry" style="color:rgb(173, 219, 103)">service_account.json</span><span>
</span><span></span><span class="token entry" style="color:rgb(173, 219, 103)">.env</span><span>
</span><span></span><span class="token entry" style="color:rgb(173, 219, 103)">config.toml</span><span>
</span></code></pre></div>

- Se alguma chave sensível já foi commitada:
  - Rev/exclua a chave no Google Cloud
  - Gere uma nova
  - Atualize os Secrets
  - (Opcional) Limpe o histórico do Git com BFG ou `git filter-branch`

---

## 📄 Licença

Defina aqui a licença do seu projeto, por exemplo:

- MIT
- Apache 2.0
- Uso pessoal / privado

Exemplo (MIT):

<div class="widget code-container remove-before-copy"><div class="code-header non-draggable"><span class="iaf s13 w700 code-language-placeholder">text</span><div class="code-copy-button"><span class="iaf s13 w500 code-copy-placeholder">Copiar</span><img class="code-copy-icon" src="data:image/svg+xml;utf8,%0A%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%3E%0A%20%20%3Cpath%20d%3D%22M10.8%208.63V11.57C10.8%2014.02%209.82%2015%207.37%2015H4.43C1.98%2015%201%2014.02%201%2011.57V8.63C1%206.18%201.98%205.2%204.43%205.2H7.37C9.82%205.2%2010.8%206.18%2010.8%208.63Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%20%20%3Cpath%20d%3D%22M15%204.42999V7.36999C15%209.81999%2014.02%2010.8%2011.57%2010.8H10.8V8.62999C10.8%206.17999%209.81995%205.19999%207.36995%205.19999H5.19995V4.42999C5.19995%201.97999%206.17995%200.999992%208.62995%200.999992H11.57C14.02%200.999992%2015%201.97999%2015%204.42999Z%22%20stroke%3D%22%23717C92%22%20stroke-width%3D%221.05%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%2F%3E%0A%3C%2Fsvg%3E%0A" /></div></div><pre id="code-lnnyp8h32" style="color:white;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:8px;margin:8px;overflow:auto;background:#011627;width:calc(100% - 8px);border-radius:8px;box-shadow:0px 8px 18px 0px rgba(120, 120, 143, 0.10), 2px 2px 10px 0px rgba(255, 255, 255, 0.30) inset"><code class="language-text" style="white-space:pre;color:#d6deeb;font-family:Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace;text-align:left;word-spacing:normal;word-break:normal;word-wrap:normal;line-height:1.5;font-size:1em;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>Este projeto é disponibilizado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
</span></code></pre></div>

---

## 🙋‍♀️ Contato

Se você quiser adaptar este dashboard para outro tipo de consultório ou integrar com outros sistemas (ex.: emissão de notas, agenda online), basta ajustar:

- As colunas da planilha
- As funções em `database.py`
- Os gráficos/tabelas em `app.py`