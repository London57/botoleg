from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uvicorn
from files.consts import STATIC_ROOT
from presentation.api.routers import routers


app = FastAPI()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    # allow_headers=['Access-Control-Allow-Origin', 'Access-Control-Allow-Headers', 'Cookie', 'Authorization'],
    allow_headers=['*'],
)

app.mount(f"/{STATIC_ROOT}", StaticFiles(directory=STATIC_ROOT))

for router in routers:
	app.include_router(router)

if __name__ == '__main__':
	uvicorn.run('main:app', reload=True, host="0.0.0.0", port=8000)
