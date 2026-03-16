var numberOfPeople = document.getElementById("numberOfPeople");

if (typeof(numberOfPeople) != 'undefined' && numberOfPeople != null)
{
	// Drinks calculator
	var randomId = Math.random()
		.toString(36)
		.substring(2);


	var resultTracked = false;

	var delay = (function() {
		var timer = 0;
		return function(callback, ms) {
			clearTimeout(timer);
			timer = setTimeout(callback, ms);
		};
	})();


	numberOfPeople.addEventListener("keyup", function() {
		document.getElementById("beerCases").innerHTML = Math.ceil(
			numberOfPeople.value * 2.61842105 / 24
		);
		document.getElementById("sodaCases").innerHTML = Math.ceil(
			numberOfPeople.value * 2.97368421 / 24
		);
		document.getElementById("ciderCases").innerHTML = Math.ceil(
			numberOfPeople.value * 1.31578947 / 24
		);
		document.getElementById("welcomeWine").innerHTML = Math.ceil(
			numberOfPeople.value * 0.144736842
		);
		document.getElementById("whiteWine").innerHTML = Math.ceil(
			numberOfPeople.value * 0.342105263
		);
		document.getElementById("redWine").innerHTML = Math.ceil(
			numberOfPeople.value * 0.434210526
		);
		document.getElementById("dessertWine").innerHTML = Math.ceil(
			numberOfPeople.value * 0.098684211
		);
		document.getElementById("shotBottles").innerHTML = Math.ceil(
			numberOfPeople.value * 5.6828947368 / 35
		);		

		// Show result
		var drinksCalculatorResult = document.getElementById(
			"drinksCalculatorResult"
		);
		drinksCalculatorResult.style.display = "block";
		drinksCalculatorResult.style.opacity = 1;

		delay(function() {
			if (!resultTracked) {
				window.dataLayer = window.dataLayer || [];
				dataLayer.push({
					event: "drinksCalculated",
					numberOfPeople: numberOfPeople.value,
					randomId: randomId
				});
			}
			resultTracked = true;
		}, 5000);
	});
}

if (document.querySelector(".drinksCalculatorButton") !== null) {
	drinksCalculatorButton.addEventListener("click", function() {
		document
			.getElementById("drinksCalculatorResult")
			.classList.remove("show");
		document.getElementById("drinksCalculatorResult").classList.add("hide");
		document
			.getElementById("drinksCalculatorResult")
			.classList.remove("hide");
		document.getElementById("drinksCalculatorResult").classList.add("show");
	});
}