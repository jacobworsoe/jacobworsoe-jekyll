(function() {
  var numberOfPeople = document.getElementById("numberOfPeople");
  if (!numberOfPeople) return;

  var resultTracked = false;
  var randomId = Math.random().toString(36).substring(2);
  var delay = (function() {
    var timer = 0;
    return function(callback, ms) {
      clearTimeout(timer);
      timer = setTimeout(callback, ms);
    };
  })();

  function updateOutput(id, value) {
    var el = document.getElementById(id);
    if (el) el.innerHTML = Math.ceil(value);
  }

  numberOfPeople.addEventListener("keyup", function() {
    var n = parseFloat(numberOfPeople.value) || 0;
    updateOutput("beerCases", n * 2.61842105 / 24);
    updateOutput("sodaCases", n * 2.97368421 / 24);
    updateOutput("ciderCases", n * 1.31578947 / 24);
    updateOutput("welcomeWine", n * 0.144736842);
    updateOutput("whiteWine", n * 0.342105263);
    updateOutput("redWine", n * 0.434210526);
    updateOutput("dessertWine", n * 0.098684211);
    updateOutput("shotBottles", n * 5.6828947368 / 35);

    var result = document.getElementById("drinksCalculatorResult");
    if (result) {
      result.style.display = "block";
      result.style.opacity = 1;
    }

    delay(function() {
      if (!resultTracked) {
        window.dataLayer = window.dataLayer || [];
        dataLayer.push({
          event: "drinksCalculated",
          numberOfPeople: numberOfPeople.value,
          randomId: randomId
        });
        resultTracked = true;
      }
    }, 5000);
  });
})();
