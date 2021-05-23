from typing import  Optional
from urllib import parse
from instagrapi import Client


class ClientStorage:
    storage = {}

    def client(self, proxy: Optional[str] = ''):
        """Get new client (helper)
        """
        cl = Client(proxy=proxy)
        cl.request_timeout = 0.1
        return cl

    def get(self, sessionid: str) -> Client:
        """Get client settings
        """
        key = parse.unquote(sessionid.strip())
        return self.storage.get(key, None)

    def set(self, cl: Client) -> bool:
        """Set client settings
        """
        key = parse.unquote(cl.sessionid)
        self.storage[key] = cl
        return True
