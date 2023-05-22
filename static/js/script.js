const form = document.getElementById("question-form");
const sliders = document.querySelectorAll(".slider");

// Add event listeners to sliders to update values in real-time
sliders.forEach(function(slider) {
	const output = document.getElementById(slider.id + "-value");
	output.innerHTML = slider.value;

	slider.oninput = function() {
		output.innerHTML = this.value;
	};
});



// Add event listeners to fruit buttons
/*const fruitButtons = document.querySelectorAll(".fruit-button");
fruitButtons.forEach(function(button) {
  button.addEventListener("click", function() {
    const selectedFruit = this.id.slice(0, -7); // Get the fruit from the button ID
    document.getElementById("fruit-input").value = selectedFruit;
    document.getElementById("fruit-value").innerHTML = selectedFruit;
  });
});
*/