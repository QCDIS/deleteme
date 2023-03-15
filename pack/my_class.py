import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class WorkflowParser:
    logger = logging.getLogger(__name__)
    nodes: dict

    def __init__(self, nodes):
        self.nodes = nodes

    def do_stuf(self, name):
        secret = os.environ('SECRET')
        if not secret:
            raise Exception('Environment variable: SECRET not set')
        self.nodes[name] = name