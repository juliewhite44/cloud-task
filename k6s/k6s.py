import os
import yaml
from flask import Flask
from .env import Env
from .resources import Instructions




class K6s:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as config_file:
            self.config = yaml.safe_load(config_file)
        self.host = self.config['host']
        self.port = self.config['port']
        self.env = Env()
        if os.path.isdir("/var/run/secrets/kubernetes.io"):
            self.env.set('k8s')
        elif os.path.exists('/.dockerenv'):
            self.env.set('docker')
        else:
            self.env.reset()
        self.app = Flask(__name__, template_folder="./templates")
        Instructions.register(self.app, route_base='/')

    def run(self):
        self.app.run(host=self.host, port=self.port)

