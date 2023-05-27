function changeImage(imgname, imgdesc)
{
	var img = document.getElementById("bigimg");
	var path = "../static/images/".concat(imgname);
	var desc = imgdesc;
	img.src = path;
	img.alt = desc;
}

function imgOne()
{
	changeImage("ezOgN0q.jpg", "Sunset-ish");
}

function imgTwo()
{
	changeImage("9fdeudnyny6a1.jpg", "Makima");
}

function imgThree()
{
	changeImage("84bykpsrir1a1.jpg", "Spider-Man: Into the Spider-Verse");
}
