import asyncio
import json
from cryptography.fernet import Fernet

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.id = Fernet.generate_key().decode()
        self.peers = set()

    def to_json(self):
        return json.dumps({"host": self.host, "port": self.port, "id": self.id})

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        peer = cls(data["host"], data["port"])
        peer.id = data["id"]
        return peer

    def add_peer(self, peer):
        self.peers.add(peer)

    def remove_peer(self, peer):
        self.peers.discard(peer)