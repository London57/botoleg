from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates

from map import m
import uvicorn

templates = Jinja2Templates(directory="files")

router = APIRouter(
	prefix='/maps'
)

@router.get('')
async def get_map(user_id, request: Request):
	m.save(f'files/{user_id}.html')
	return templates.TemplateResponse(f'{user_id}.html', {'request': request})

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
	uvicorn.run('main:app', reload=True)
