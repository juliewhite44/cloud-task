from typing import Literal
from .metaclasses import Singleton


class Env(metaclass=Singleton):

    def __init__(self):
        self.current_env: Literal['UNKNOWN', 'DOCKER', 'K8S'] = 'UNKNOWN'

    def is_docker(self):
        if self.current_env == 'DOCKER':
            return True
        return False

    def is_k8s(self):
        if self.current_env == 'K8S':
            return True
        return False

    def set(self, env: Literal['k8s', 'docker']):
        if env == 'docker':
            self.current_env = 'DOCKER'
        elif env == 'k8s':
            self.current_env = 'K8S'
        else:
            raise ValueError("Wrong param provided. Must be one of ['k8s', 'docker']")

    def reset(self):
        self.current_env = 'UNKNOWN'
