import os
import aiohttp

from data import User


class RequestManager:
    def __init__(self, scheme: str = None, host: str = None, port: int = None) -> None:
        self.scheme = scheme or os.environ.get('SCHEME', 'http')
        self.host = host or os.environ.get('HOST', 'localhost')
        self.port = port or os.environ.get('PORT', 8000)

    async def auth(self, user: User):
        url = f'{self.scheme}://{self.host}:{self.port}/api/token/'
        payload = {'username': user.username, 'password': user.password}

        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.post(url, data=payload) as response:
                return await response.json(), response.status

    async def post(self, url: str, payload: dict = None, headers: dict = None):
        url = f'{self.scheme}://{self.host}:{self.port}/{url}'

        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.post(url, data=payload, headers=headers) as response:
                return await response.json(), response.status

    async def get(self, url: str, headers: dict = None):
        url = f'{self.scheme}://{self.host}:{self.port}/{url}'

        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(url, headers=headers) as response:
                return await response.json(), response.status
