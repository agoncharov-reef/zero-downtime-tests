from fastapi import FastAPI, Response
from time import time
app = FastAPI()

return_502 = True


@app.get('/subsequent')
async def subsequent():
    global return_502
    return_502 = not return_502

    return Response(
        content='ok',
        media_type='text/html',
        status_code=502 if return_502 else 200,
    )


start_time = time()
warmup_time = 10


@app.get('/warmup')
async def warmup():
    elapsed = time() - start_time
    is_warmup = elapsed < warmup_time
    print(f'{elapsed=} {is_warmup=}')
    return Response(
        content='error' if is_warmup else 'ok',
        media_type='text/html',
        status_code=502 if is_warmup else 200,
    )
