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
