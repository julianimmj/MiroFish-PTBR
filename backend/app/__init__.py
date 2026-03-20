"""
MiroFish Backend - Fábrica de Aplicação Flask
"""

import os
import warnings

# Suprimir avisos do multiprocessing resource_tracker
warnings.filterwarnings("ignore", message=".*resource_tracker.*")

from flask import Flask, request, send_from_directory
from flask_cors import CORS

from .config import Config
from .utils.logger import setup_logger, get_logger


def create_app(config_class=Config):
    """Função fábrica da aplicação Flask"""
    # Configurar para servir arquivos estáticos do frontend Vue
    frontend_dist = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'dist'))
    app = Flask(__name__, static_folder=frontend_dist, static_url_path='')
    
    app.config.from_object(config_class)
    
    # Configurar codificação JSON para exibir português diretamente
    if hasattr(app, 'json') and hasattr(app.json, 'ensure_ascii'):
        app.json.ensure_ascii = False
    
    # Configurar logs
    logger = setup_logger('mirofish')
    
    is_reloader_process = os.environ.get('WERKZEUG_RUN_MAIN') == 'true'
    debug_mode = app.config.get('DEBUG', False)
    should_log_startup = not debug_mode or is_reloader_process
    
    if should_log_startup:
        logger.info("=" * 50)
        logger.info("MiroFish Backend iniciando...")
        logger.info("=" * 50)
    
    # Habilitar CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Registrar função de limpeza de processos de simulação
    from .services.simulation_runner import SimulationRunner
    SimulationRunner.register_cleanup()
    if should_log_startup:
        logger.info("Função de limpeza de processos de simulação registrada")
    
    # Middleware de logs de requisição
    @app.before_request
    def log_request():
        logger = get_logger('mirofish.request')
        logger.debug(f"Requisição: {request.method} {request.path}")
        if request.content_type and 'json' in request.content_type:
            logger.debug(f"Corpo: {request.get_json(silent=True)}")
    
    @app.after_request
    def log_response(response):
        logger = get_logger('mirofish.request')
        logger.debug(f"Resposta: {response.status_code}")
        return response
    
    # Registrar Blueprints da API
    from .api import graph_bp, simulation_bp, report_bp
    app.register_blueprint(graph_bp, url_prefix='/api/graph')
    app.register_blueprint(simulation_bp, url_prefix='/api/simulation')
    app.register_blueprint(report_bp, url_prefix='/api/report')
    
    # Servir Frontend
    @app.route('/')
    def serve_vue():
        return send_from_directory(app.static_folder, 'index.html')

    # Roteamento Catch-all para o Vue Router
    @app.route('/<path:path>')
    def serve_catch_all(path):
        if path.startswith('api/'):
            return {"error": "Not Found"}, 404
        # Verificar se o arquivo existe na pasta dist (ex: js, css, imagens)
        if os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        # Caso contrário, retornar index.html (SPA)
        return send_from_directory(app.static_folder, 'index.html')

    # Status de Saúde
    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'MiroFish Backend PT-BR'}
    
    if should_log_startup:
        logger.info("MiroFish Backend iniciado com sucesso")
    
    return app

