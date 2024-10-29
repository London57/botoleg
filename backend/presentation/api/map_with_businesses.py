from fastapi import Request, APIRouter, Query
from fastapi.templating import Jinja2Templates

from typing import Annotated

from pydantic import BaseModel

from infrastructure.map import m

from files.consts import STATIC_ROOT

templates = Jinja2Templates(directory=STATIC_ROOT)

router = APIRouter(
	prefix="/maps"
)

#TODO убрать
class CardDTO(BaseModel):
	city: str
	biz: str

#TODO убрать
@router.get("/card")
async def card(card: Annotated[CardDTO, Query()]):
	return {"name": 'Олег', 'city': card.city, 'biz': card.biz}

@router.get('')
async def get_map(user_id, request: Request):
	m.save(f'{STATIC_ROOT}/{user_id}.html')

	with open(f"{STATIC_ROOT}/{user_id}.html", "r") as file:
		s = file.readlines()
	with open(f"{STATIC_ROOT}/{user_id}.html", "w") as file:
		s[2] += f'<link rel="stylesheet" href="{STATIC_ROOT}/css/modal.css">'
		s[-2] += """<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>"""
		s[-2] += """
<script>
		const url = "http://192.168.1.2:8000/maps/card"
		
		document.onclick = function(e) {
			res = click(e)
			if (res) {
			console.log(res)
				send_fetch_for_get_card_info(res)
			}
		}

		function click(e) {
		console.log(e)
			let classes_list = e.target.className.split(' ')
			console.log(classes_list, e.target)
				let modal = document.querySelector(".modal")
			if (modal && !(e.target.className.startsWith("modal_"))) {
				modal.remove()
			}
			if (classes_list[1] !== "leaflet-container" && classes_list.length > 2) {
			console.log("pon")
				return [classes_list[1], classes_list[2]]
			}
		}

function send_fetch_for_get_card_info(p) {
	console.log("p:", p)
	console.log(url)
	fetch(`${url}?city=${p[0]}&biz=${p[1]}`, {method: "GET"})
		.then(response => {
		response.json().then((res) => {
			create_modal_window({
				title: "gas station",
				modal_text: {
					for_sale: true,
					businessman_name: "Oleg",
					income: `400$/min`,
				}
			})
		})
	}).catch(error => console.log(error))
}


function create_modal_window({title, modal_text: {for_sale, businessman_name, income}}) {
	let modal_window = document.createElement("div")
	modal_window.className = "modal"
	function closeModal() {
		modal_window.remove()
	}

	for_sale ? 
	modal_window.innerHTML = `<div class="modal__main">
      <h3 class="modal__title">${title}</h2>
      
      <div class="modal__container">
        <p class="modal_p">businessman name: ${businessman_name}</p>
        <p class="modal_p">income: ${income}$/min</p>
      </div>

      <button class="modal__btn">buy</button>
      <button class="modal__close" >&#10006;</button>
    </div>`
	
	: modal_window.innerHTML = `<div class="modal__main">
      <h3 class="modal__title">${title}</h2>
      
      <div class="modal__container">
        <p class="modal_p">businessman name: ${businessman_name}</p>
        <p class="modal_p">income: ${income}$/min</p>
      </div>
      <button class="modal__close" >&#10006;</button>
    </div>
	`
	const closeButton = modal_window.querySelector('.modal__close')
	closeButton.addEventListener('click', closeModal)
	let map = document.querySelector(".folium-map")
	map.appendChild(modal_window)
	modal_window.style.display = "block"
}
		</script>
		"""
		file.writelines(s)
	return templates.TemplateResponse(f'{user_id}.html', {'request': request})
