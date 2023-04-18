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

// Handle form submission
form.addEventListener("submit", function(event) {
	event.preventDefault();

	// store values in variables
	const answers = {
		q1: document.getElementById("q1-slider").value,
		q2: document.getElementById("q2-slider").value,
		q3: document.getElementById("q3-slider").value,
		q4: document.getElementById("q4-slider").value,
		q5: document.getElementById("q5-slider").value,
		q6: document.getElementById("q6-slider").value,
        q7: document.getElementById("q7-slider").value,
		q8: document.getElementById("q8-slider").value,
        q9: document.querySelector('input[name="task"]:checked').value,
        q10: document.querySelector('input[name="time"]:checked').value,
	};

	// Displaying answer using log (can send to server later)
	console.log(answers);
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