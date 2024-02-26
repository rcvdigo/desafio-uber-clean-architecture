import logging
import asyncio


def logging_settings():
    # Configuração do nível de log para 'warning' ou superior
    logging.basicConfig(level=logging.WARNING)

    # Desativa o modo de depuração do loop assíncrono
    asyncio.get_event_loop().set_debug(False)

    # Configuração do nível de log do asyncio para 'warning'
    asyncio_logger = logging.getLogger('asyncio')
    asyncio_logger.setLevel(logging.WARNING)

    # Configuração do nível de log do Hypercorn e Quart para 'warning'
    hypercorn_logger = logging.getLogger('hypercorn')
    hypercorn_logger.setLevel(logging.WARNING)

    # Configuração do nível de log do Hypercorn e Quart para 'warning'
    quart_logger = logging.getLogger('quart')
    quart_logger.setLevel(logging.WARNING)
