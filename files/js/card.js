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
			response.json().then(res=>console.log(res))
		}).catch(error => console.log(error))
}