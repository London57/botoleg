const url = "http://192.168.1.2:8000/maps/"
		
document.onclick = function(e) {
	res = click(e)
	if (res) {
	console.log(res)
		send_fetch_for_get_card_info(res)
	}
}

function click(e) {
	let target = e.target
	if (target.className.split(' ')[0] == 'fa-rotate-0') {
	  target = target.parentElement
	}
	
	let classes_list = target.className.split(' ')
	console.log(classes_list, target.className)
		let modal = document.querySelector(".modal")
	if (modal && !(target.className.startsWith("modal_"))) {
		modal.remove()
	}
	if (classes_list[1] !== "leaflet-container" && classes_list.length > 2) {
		return [classes_list[1], classes_list[2], classes_list[3]]
	}
}

function send_fetch_for_get_card_info(p) {
console.log("p:", p)
fetch(`${url}business_info?business_id=${p[2]}`, {method: "GET"})
.then(response => {
response.json().then((res) => {
console.log(res)
if (res) {
	create_modal_window({
		title: "gas station",
		modal_text: {
			for_sale: true,
			businessman_name: res.businessman_name,
			income: res.income,
		}
	})}
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
	
	<a href="https://t.me/Alex_Maximow_bot" target="_blank">a</a>
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