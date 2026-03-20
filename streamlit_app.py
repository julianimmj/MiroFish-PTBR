# -*- coding: utf-8 -*-
"""
MiroFish - Portal Profissional
Motor de Inteligência Coletiva Universal
"""

import streamlit as st

# ===========================
# Configuração da Página
# ===========================
st.set_page_config(
    page_title="MiroFish — Motor de Inteligência Coletiva",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===========================
# CSS Customizado Premium
# ===========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    .stApp {
        background: #0A0A0A;
        color: #FFFFFF;
        font-family: 'Inter', -apple-system, system-ui, sans-serif;
    }

    .block-container {
        padding-top: 0 !important;
        max-width: 1200px;
    }

    .hero-box {
        text-align: center;
        padding: 80px 20px 60px;
        position: relative;
    }

    .hero-badge {
        display: inline-block;
        background: #FF4500;
        color: white;
        padding: 6px 16px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 24px;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -2px;
        margin-bottom: 24px;
        color: white;
    }

    .gradient-text {
        background: linear-gradient(135deg, #FF4500 0%, #FF8C00 50%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-sub {
        font-size: 1.15rem;
        color: #AAAAAA;
        max-width: 700px;
        margin: 0 auto 40px;
        line-height: 1.7;
    }

    .hero-link {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: #FF4500;
        color: white;
        padding: 14px 28px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 0.95rem;
        text-decoration: none;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }

    .hero-link:hover {
        background: #FF6A33;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(255, 69, 0, 0.3);
        color: white;
    }

    .stats-bar {
        display: flex;
        justify-content: center;
        gap: 60px;
        padding: 40px 0;
        border-top: 1px solid #2A2A2A;
        border-bottom: 1px solid #2A2A2A;
        margin: 0 20px 60px;
    }

    .stat-box { text-align: center; }

    .stat-val {
        font-family: 'JetBrains Mono', monospace;
        font-size: 2.2rem;
        font-weight: 800;
        color: #FF4500;
    }

    .stat-lbl {
        font-size: 0.8rem;
        color: #888888;
        margin-top: 4px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .sec-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #FF4500;
        letter-spacing: 3px;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 8px;
    }

    .sec-title {
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: -1px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    }

    .wf-card {
        background: #1A1A1A;
        border: 1px solid #2A2A2A;
        padding: 28px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
        border-left: 3px solid transparent;
    }

    .wf-card:hover {
        border-left-color: #FF4500;
        transform: translateX(4px);
    }

    .wf-step {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: #FF4500;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }

    .wf-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .wf-desc {
        font-size: 0.9rem;
        color: #888888;
        line-height: 1.6;
    }

    .feat-card {
        background: #111111;
        border: 1px solid #2A2A2A;
        padding: 32px 24px;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }

    .feat-card:hover {
        border-color: #FF4500;
    }

    .feat-icon {
        font-size: 2.5rem;
        margin-bottom: 16px;
    }

    .feat-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .feat-desc {
        font-size: 0.85rem;
        color: #888888;
        line-height: 1.6;
    }

    .setup-box {
        background: #1A1A1A;
        border: 1px solid #2A2A2A;
        padding: 32px;
        margin-bottom: 20px;
    }

    .setup-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1rem;
        font-weight: 700;
        color: white;
        margin-bottom: 20px;
    }

    .setup-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 16px;
    }

    .setup-num {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        color: #FF4500;
        font-size: 0.85rem;
        min-width: 24px;
    }

    .setup-txt {
        color: #AAAAAA;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .code-tag {
        font-family: 'JetBrains Mono', monospace;
        background: #0A0A0A;
        color: #FF4500;
        padding: 2px 6px;
        font-size: 0.8rem;
    }

    .footer-bar {
        text-align: center;
        padding: 40px 20px;
        border-top: 1px solid #2A2A2A;
        margin-top: 60px;
        color: #888888;
        font-size: 0.85rem;
    }

    .footer-bar a {
        color: #FF4500;
        text-decoration: none;
    }

    .footer-bar a:hover {
        text-decoration: underline;
    }

    @media (max-width: 768px) {
        .hero-title { font-size: 2.2rem; }
        .stats-bar { flex-direction: column; gap: 24px; }
    }
</style>
""", unsafe_allow_html=True)


# ===========================
# HERO
# ===========================
st.markdown("""
<div class="hero-box">
    <div class="hero-badge">MOTOR DE INTELIGÊNCIA COLETIVA</div>
    <h1 class="hero-title">
        Envie qualquer relatório.<br>
        <span class="gradient-text">Simule o futuro.</span>
    </h1>
    <p class="hero-sub">
        O MiroFish é um motor de previsão baseado em multi-agentes de IA que constrói 
        mundos digitais paralelos a partir de dados reais. Milhões de agentes inteligentes 
        interagem, evoluem e revelam tendências futuras com precisão.
    </p>
    <a href="https://github.com/666ghj/MiroFish" target="_blank" class="hero-link">
        EXPLORAR NO GITHUB →
    </a>
</div>
""", unsafe_allow_html=True)


# ===========================
# STATS
# ===========================
st.markdown("""
<div class="stats-bar">
    <div class="stat-box">
        <div class="stat-val">1M+</div>
        <div class="stat-lbl">Agentes Simulados</div>
    </div>
    <div class="stat-box">
        <div class="stat-val">~US$5</div>
        <div class="stat-lbl">Custo por Simulação</div>
    </div>
    <div class="stat-box">
        <div class="stat-val">5</div>
        <div class="stat-lbl">Etapas do Fluxo</div>
    </div>
    <div class="stat-box">
        <div class="stat-val">AGPL-3.0</div>
        <div class="stat-lbl">Open Source</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ===========================
# WORKFLOW
# ===========================
st.markdown('<div class="sec-tag">◇ FLUXO DE TRABALHO</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Como Funciona</div>', unsafe_allow_html=True)

workflow_steps = [
    ("ETAPA 01", "🔗 Construção do Grafo", "Extração de sementes reais, injeção de memória individual e coletiva, e construção de grafo de conhecimento via GraphRAG."),
    ("ETAPA 02", "⚙️ Configuração do Ambiente", "Extração de relações entre entidades, geração automática de perfis e injeção de parâmetros de simulação."),
    ("ETAPA 03", "▶️ Simulação", "Simulação paralela em duas plataformas com análise automática de previsões e atualização dinâmica de memória temporal."),
    ("ETAPA 04", "📊 Relatório de Previsão", "O ReportAgent utiliza ferramentas avançadas para interação profunda com o ambiente pós-simulação."),
    ("ETAPA 05", "💬 Interação Profunda", "Converse com qualquer agente do mundo simulado ou dialogue diretamente com o ReportAgent."),
]

for step_num, title, desc in workflow_steps:
    st.markdown(f"""
    <div class="wf-card">
        <div class="wf-step">{step_num}</div>
        <div class="wf-title">{title}</div>
        <div class="wf-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)


# ===========================
# FEATURES
# ===========================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="sec-tag">★ RECURSOS</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Por que MiroFish?</div>', unsafe_allow_html=True)

features = [
    ("🧠", "Multi-Agentes Inteligentes", "Agentes com personalidades únicas, memória de longo prazo e lógica comportamental independente."),
    ("🌐", "Mundos Paralelos", "Construção automática de mundos digitais de alta fidelidade a partir de dados do mundo real."),
    ("📈", "Previsão Precisa", "Injete variáveis em tempo real e encontre soluções ótimas em cenários complexos."),
    ("💰", "Custo Acessível", "Simulações completas por ~US$5 com suporte a qualquer API LLM no formato OpenAI SDK."),
    ("🔓", "Código Aberto", "Licença AGPL-3.0. Totalmente aberto, personalizável e extensível."),
    ("🐳", "Deploy Simples", "Deploy via código-fonte ou Docker com um único comando em minutos."),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="feat-card">
            <div class="feat-icon">{icon}</div>
            <div class="feat-title">{title}</div>
            <div class="feat-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)


# ===========================
# QUICK START
# ===========================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="sec-tag">🚀 INÍCIO RÁPIDO</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Comece em Minutos</div>', unsafe_allow_html=True)

st.markdown("""
<div class="setup-box">
    <div class="setup-title">> Deploy via Código-Fonte</div>
    <div class="setup-item">
        <span class="setup-num">01</span>
        <span class="setup-txt">Clone o repositório: <span class="code-tag">git clone https://github.com/666ghj/MiroFish.git</span></span>
    </div>
    <div class="setup-item">
        <span class="setup-num">02</span>
        <span class="setup-txt">Configure as variáveis: <span class="code-tag">cp .env.example .env</span> e preencha suas chaves de API</span>
    </div>
    <div class="setup-item">
        <span class="setup-num">03</span>
        <span class="setup-txt">Instale dependências: <span class="code-tag">npm run setup:all</span></span>
    </div>
    <div class="setup-item">
        <span class="setup-num">04</span>
        <span class="setup-txt">Inicie: <span class="code-tag">npm run dev</span> — Frontend em <span class="code-tag">localhost:3000</span> | Backend em <span class="code-tag">localhost:5001</span></span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="setup-box">
    <div class="setup-title">> Deploy via Docker</div>
    <div class="setup-item">
        <span class="setup-num">01</span>
        <span class="setup-txt">Configure o <span class="code-tag">.env</span> com suas chaves de API</span>
    </div>
    <div class="setup-item">
        <span class="setup-num">02</span>
        <span class="setup-txt">Execute: <span class="code-tag">docker compose up -d</span></span>
    </div>
</div>
""", unsafe_allow_html=True)


# ===========================
# FOOTER
# ===========================
st.markdown("""
<div class="footer-bar">
    🐟 MiroFish — Motor de Inteligência Coletiva Universal<br>
    Fork em Português do <a href="https://github.com/666ghj/MiroFish" target="_blank">projeto original</a> 
    | Motor de simulação: <a href="https://github.com/camel-ai/oasis" target="_blank">OASIS</a>
    | Licença AGPL-3.0
</div>
""", unsafe_allow_html=True)
