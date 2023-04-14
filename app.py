import fastapi
from fastapi import HTTPException
import numpy as np
import random
import asyncio

app = fastapi.FastAPI()

@app.get("/GetBigNumber")
def get_big_number():
    big_array = np.random.rand(1000,1000,60)
    big_array_mins = big_array.argmin(0)
    big_array_mins = big_array_mins.ravel()
    result = big_array_mins.sum()
    result = int(result)
    maybe = asyncio.run(maybe_error())
    if maybe:
        raise HTTPException(404, "Bad roll bud")
        # return result
    else:
        return result

async def maybe_error():
    if random.random() < 0.1:
        return True