function changeImage(imgname)
{
	var img = document.getElementById("bigimg");
	var path = "../static/images/".concat(imgname);
	img.src = path;
}

function imgOne()
{
	changeImage("84bykpsrir1a1.jpg");
}

function imgTwo()
{
	changeImage("9fdeudnyny6a1.jpg");
}

function imgThree()
{
	changeImage("ezOgN0q.jpg");
}
