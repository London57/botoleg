const url = "http://localhost:8000/maps/card"

document.onclick = function(e) {
	res = click(e)
	if (res) {
		send_fetch_for_get_card_info(res)
	}
}

function click(e) {
	let s = e.target.className.split(' ')
	console.log("s:", s)
	let modal = document.querySelector(".modal")
	if (modal && s.length < 5) {
		modal.remove()
	}
	if (s[1] !== "leaflet-container") {
		console.log("pon")
		return [s[1], s[2]]
	}
}

function send_fetch_for_get_card_info(p) {
	fetch(`${url}?city=${p[0]}&biz=${p[1]}`, {
			method: "GET",
			headers: {
				'Content-Type': 'application/json',
	}}).then(response => {
		response.json().then((res) => {
			create_modal_window({
				title: "Информация о бизнесе",
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
	// modal_window.style.cssText = `
	// transition: opacity 3010 ms linear;
	// `
	function closeModal() {
		
		modal_window.remove()
	}

	for_sale ? 
	modal_window.innerHTML = `<div class="modal__main">
      <h3 class="modal__title">${title}</h2>
      
      <div class="modal__container">
        <p>businessman name: ${businessman_name}</p>
        <p>income: ${income}$/min</p>
      </div>

      <button class="modal__btn">buy</button>
      <button class="modal__close" ${onclick=closeModal()}>&#10006;</button>
    </div>`
	
	: modal_window.innerHTML = `<div class="modal__main">
      <h3 class="modal__title">${title}</h2>
      
      <div class="modal__container">
        <p>businessman name: ${businessman_name}</p>
        <p>income: ${income}$/min</p>
      </div>
      <button class="modal__close" ${onclick=closeModal()}>&#10006;</button>
    </div>`

	let map = document.querySelector(".folium-map")
	map.appendChild(modal_window)
	modal_window.style.display = "block"
}

function add_event_listeners_on_button() {}