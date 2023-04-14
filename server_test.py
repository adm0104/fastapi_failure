import aiohttp
import asyncio

class ServerTest():
    def __init__(self):
        self.server = 'http://localhost:8000'
        self.responses = 0

    async def batch_call(self, calls: int = 10):
        async with aiohttp.ClientSession() as session:
            tasks = [self.single_server_call(session) for _ in range(calls)]
            results = await asyncio.gather(*tasks)
            return results

    async def single_server_call(self, session: aiohttp.ClientSession = None):
        url = self.server + "/GetBigNumber"
        async with session.get(url) as response:
            self.responses += 1
            print(f"Total responses: {self.responses}")
            if response.status == 200:
                return True
            else:
                print(f"Bad response: {response.status}, {response.reason}")
                return False

