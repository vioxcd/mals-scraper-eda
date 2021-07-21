clear()

const extractLink = () => {
	const list = document.querySelectorAll('.picSurround')

	list.forEach(div => {
		console.log(div.firstChild.href)
	})
}

extractLink()