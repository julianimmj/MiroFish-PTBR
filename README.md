<div align="center">

<img src="./static/image/MiroFish_logo_compressed.jpeg" alt="MiroFish Logo" width="75%"/>

Motor de Inteligência Coletiva Universal — Prevendo Qualquer Coisa
<br>
<em>A Simple and Universal Swarm Intelligence Engine, Predicting Anything</em>

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/MiroFish?style=flat-square&color=DAA520)](https://github.com/666ghj/MiroFish/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/MiroFish?style=flat-square)](https://github.com/666ghj/MiroFish/network)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)

[English](./README-EN.md) | [中文文档](./README-CN.md) | **Português (BR)**

</div>

## ⚡ Visão Geral do Projeto

**MiroFish** é um motor de previsão de IA de nova geração baseado em tecnologia multi-agente. Ao extrair informações-semente do mundo real (como notícias de última hora, rascunhos de políticas, sinais financeiros), ele constrói automaticamente mundos digitais paralelos de alta fidelidade. Neste espaço, milhares de agentes inteligentes com personalidades independentes, memória de longo prazo e lógica comportamental interagem livremente e evoluem socialmente. Você pode injetar variáveis dinamicamente através de uma "visão de Deus", simulando com precisão tendências futuras — **deixe o futuro ser ensaiado em uma sandbox digital, e vença as decisões após centenas de simulações**.

> Você só precisa: enviar material-semente (relatório de análise de dados ou uma história interessante), e descrever sua necessidade de previsão em linguagem natural
>
> O MiroFish retornará: um relatório detalhado de previsão e um mundo digital de alta fidelidade totalmente interativo

### Nossa Visão

O MiroFish se dedica a criar um espelho de inteligência coletiva que mapeia a realidade, capturando a emergência de grupo provocada por interações individuais, superando as limitações da previsão tradicional:

- **No Macro**: Somos o laboratório de ensaio dos tomadores de decisão, permitindo que políticas e relações públicas sejam testadas com risco zero
- **No Micro**: Somos a sandbox criativa do usuário individual, seja para simular o final de um romance ou explorar ideias — tudo ao alcance das mãos

De previsões sérias a simulações divertidas, tornamos cada "e se" visível em resultados, tornando possível prever qualquer coisa.

## 🌐 Demonstração Online
Bem-vindo à demonstração online, onde preparamos uma simulação de eventos de opinião pública: [mirofish-live-demo](https://666ghj.github.io/mirofish-demo/)

## 📸 Capturas de Tela do Sistema
<div align="center">
<table>
<tr>
<td><img src="./static/image/Screenshot/运行截图1.png" alt="Captura 1" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图2.png" alt="Captura 2" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图3.png" alt="Captura 3" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图4.png" alt="Captura 4" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图5.png" alt="Captura 5" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图6.png" alt="Captura 6" width="100%"/></td>
</tr>
</table>
</div>

## 🔄 Fluxo de Trabalho

1. **Construção do Grafo**: Extração de sementes reais & Injeção de memória individual e coletiva & Construção GraphRAG
2. **Configuração do Ambiente**: Extração de relações entre entidades & Geração de perfis & Injeção de parâmetros de simulação
3. **Iniciar Simulação**: Simulação paralela em duas plataformas & Análise automática de previsões & Atualização dinâmica de memória temporal
4. **Geração de Relatório**: O ReportAgent possui ferramentas avançadas para interação profunda com o ambiente pós-simulação
5. **Interação Profunda**: Converse com qualquer agente do mundo simulado & Dialogue com o ReportAgent

## 🚀 Início Rápido

### Opção 1: Deploy via Código-Fonte (Recomendado)

#### Pré-requisitos

| Ferramenta | Versão | Descrição | Verificação |
|------------|--------|-----------|-------------|
| **Node.js** | 18+ | Ambiente frontend, inclui npm | `node -v` |
| **Python** | ≥3.11, ≤3.12 | Ambiente backend | `python --version` |
| **uv** | Mais recente | Gerenciador de pacotes Python | `uv --version` |

#### 1. Configurar Variáveis de Ambiente

```bash
# Copiar arquivo de configuração de exemplo
cp .env.example .env

# Editar o arquivo .env e preencher as chaves de API necessárias
```

**Variáveis de ambiente obrigatórias:**

```env
# Configuração da API LLM (suporta qualquer API LLM no formato OpenAI SDK)
LLM_API_KEY=sua_chave_api
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# Configuração Zep Cloud
# A cota gratuita mensal é suficiente para uso simples: https://app.getzep.com/
ZEP_API_KEY=sua_chave_zep
```

#### 2. Instalar Dependências

```bash
# Instalação completa com um comando (raiz + frontend + backend)
npm run setup:all
```

Ou instale separadamente:

```bash
# Instalar dependências Node (raiz + frontend)
npm run setup

# Instalar dependências Python (backend, cria ambiente virtual automaticamente)
npm run setup:backend
```

#### 3. Iniciar Serviços

```bash
# Iniciar frontend e backend simultaneamente (executar na raiz do projeto)
npm run dev
```

**Endereços dos serviços:**
- Frontend: `http://localhost:3000`
- API Backend: `http://localhost:5001`

**Iniciar separadamente:**

```bash
npm run backend   # Apenas backend
npm run frontend  # Apenas frontend
```

### Opção 2: Deploy via Docker

```bash
# 1. Configurar variáveis de ambiente (mesmo processo do deploy por código)
cp .env.example .env

# 2. Puxar imagem e iniciar
docker compose up -d
```

Por padrão, lê o `.env` na raiz e mapeia as portas `3000 (frontend)/5001 (backend)`

### Opção 3: Deploy na Nuvem (Render / Web) - Recomendado

Para colocar o MiroFish completo no ar (frontend + backend via URL pública) gratuitamente:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/generate-deploy?repo=https://github.com/julianimmj/MiroFish-PTBR)

1. Crie uma conta no [Render.com](https://render.com) e conecte seu GitHub.
2. Clique no botão acima ou crie um novo **Web Service**.
3. Selecione seu repositório `MiroFish-PTBR`.
4. Defina as configurações:
   - **Environment:** `Docker` (Render vai ler o nosso `Dockerfile` automaticamente)
   - **Region:** A mais próxima (ex: Ohio)
   - **Branch:** `main`
5. Na seção **Environment Variables**, adicione suas chaves:
   - `LLM_API_KEY` = *sua-chave*
   - `LLM_BASE_URL` = *sua-url-se-diferente*
   - `LLM_MODEL_NAME` = *seu-modelo*
   - `ZEP_API_KEY` = *sua-chave-zep*
6. Clique em **Create Web Service**. O Render vai rodar o Build (pode demorar uns 5-10 minutos) e depois te dar um link público (ex: `mirofish.onrender.com`).

## 📬 Contato

Este é um fork em Português do projeto [MiroFish original](https://github.com/666ghj/MiroFish).

## 📄 Agradecimentos

**MiroFish recebeu apoio estratégico e incubação do Grupo Shanda!**

O motor de simulação do MiroFish é alimentado pelo **[OASIS](https://github.com/camel-ai/oasis)**, agradecemos sinceramente à equipe CAMEL-AI pela contribuição open-source!
