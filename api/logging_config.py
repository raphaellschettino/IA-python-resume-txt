import logging

# Formato do log
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"

# Configurar logging global do sistema
logging.basicConfig(
    filename="app.log",         # arquivo gerado na raiz do projeto
    level=logging.INFO,         # pode trocar para DEBUG para mais detalhes
    format=LOG_FORMAT,
    encoding="utf-8"
)

logger = logging.getLogger("api_logger")