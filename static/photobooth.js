let cache = []

function refresh() {
	fetch('latest.json').then(response => response.json()).then(({ photos }) => {
		let update = false
		for (var i = photos.length - 1; i >= 0; i--) {
			if (cache.indexOf(photos[i]) === -1) {
				update = true
				cache.unshift(photos[i])
			}
		}
		if (!update) return

		document.querySelector('#photos').innerHTML = cache.map(url => `<img src='${url}' />`).join('')
	})
}

setInterval(refresh, 5000)
window.onload = refresh
