import socket
from abc import ABC, abstractmethod


class Connection(ABC):

    def __init__(self, api_endpoint=None):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.endpoint = api_endpoint

    def set_endpoint(self, api_endpoint):
        self.endpoint = api_endpoint

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
