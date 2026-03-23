# Estágio 1: Build do Frontend (Node.js)
FROM node:22-alpine as frontend-builder
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend ./
RUN npm run build

# Estágio 2: Setup do Backend e Servidor (Python)
FROM python:3.11-slim
WORKDIR /app

# Instalar 'uv' para dependências rápidas
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/

# Copiar arquivos de descrição e o backend
COPY backend/pyproject.toml backend/uv.lock ./backend/
RUN cd backend && uv sync --frozen && /uv pip install gunicorn

# Copiar o restante do código backend
COPY backend ./backend
COPY .env.example .env

# O frontend compilado precisa ficar um nível acima do backend,
# conforme static_folder definido no __init__.py (../../frontend/dist)
# A estrutura final será /app/frontend/dist e /app/backend
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Expor apenas a porta 5001 (Render usa a porta definida pelo processo ou PORT env var)
# Ajustar para pegar a porta automática via variável de ambiente, padrão 5001
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5001
EXPOSE ${FLASK_PORT}

# Comando para rodar apenas o backend com servidor WSGI de Produção (Gunicorn)
CMD ["/app/backend/.venv/bin/gunicorn", "--chdir", "backend", "--bind", "0.0.0.0:5001", "--workers", "1", "--threads", "4", "--timeout", "300", "app:create_app()"]