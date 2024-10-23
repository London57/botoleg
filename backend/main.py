from fastapi import FastAPI, APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated

from pydantic import BaseModel
from map import m
import uvicorn

templates = Jinja2Templates(directory="files")

router = APIRouter(
	prefix='/maps'
)

@router.get('')
async def get_map(user_id, request: Request):
	m.save(f'files/{user_id}.html')

	with open(f"files/{user_id}.html", "r") as file:
		s = file.readlines()
	with open(f"files/{user_id}.html", "w") as file:
		s[-2] += """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>"""
		s[-2] += """
<script>
		const url = "http://localhost:8000/maps/card"
		let map = document.querySelector(".folium-map")
		
		let modalDiv = document.createElement("div");
		modalDiv.className = "modal-dialog modal-dialog-centered";
		modalDiv.textContent = 'r'
		map.appendChild(modalDiv);
		document.onclick = function(e) {
			res = click(e)
			if (res) {
				send_fetch_for_get_card_info(res)
			}
		}

		function click(e) {
			let s = e.target.className.split(' ')
			if (s[1] !== "leaflet-container") {
				return [s[1], s[2]]
			}
		}

		function send_fetch_for_get_card_info(p) {
			fetch(`${url}?city=${p[0]}&biz=${p[1]}`, {
					method: "GET",
					headers: {
						'Content-Type': 'application/json',
				}}).then(response => {
					response.json().then(res=>{
						console.log(res)
						let modal = document.querySelector(".modal-dialog")
						console.log(modal)
						modal.classList.add('show')
						modal.style.display = "block"
					})

				}).catch(error => console.log(error))
		}
		</script>
		"""
		file.writelines(s)
	return templates.TemplateResponse(f'{user_id}.html', {'request': request})


class CardDTO(BaseModel):
	city: str
	biz: str

@router.get("/card")
async def card(card: Annotated[CardDTO, Query()]):
	return {"name": 'Олег', 'city': card.city, 'biz': card.biz}

app = FastAPI()
app.include_router(router)
#CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://192.168.1.2:8000'],
    allow_credentials=True,
    allow_methods=['*'], 
    # allow_headers=['Access-Control-Allow-Origin', 'Access-Control-Allow-Headers', 'Cookie', 'Authorization'],
    allow_headers=['*'],
)

if __name__ == '__main__':
	uvicorn.run('main:app', reload=True, host="0.0.0.0", port=8000)
