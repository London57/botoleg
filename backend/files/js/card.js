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
		return [classes_list[1], classes_list[2], classes_list[3]]
	}
}

function send_fetch_for_get_card_info(p) {
console.log("p:", p)
fetch(`${url}?business_id=${p[3]}`, {method: "GET"})
.then(response => {
response.json().then((res) => {
	create_modal_window({
		title: "gas station",
		modal_text: {
			for_sale: true,
			businessman_name: res.businessman_name,
			income: `${res.income}$/min`,
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