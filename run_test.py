from server_test import ServerTest
import asyncio

if __name__ == "__main__":
    server = ServerTest()
    asyncio.run(server.batch_call(100))