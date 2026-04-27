---
layout: post
title: Visualisering af data med Google Tag Manager og ChartJS
date: 2017-06-14 21:29:04
slug: visualisering-data-google-tag-manager-chartjs
wordpress_id: 1138
categories:
  - Analytics
---

Tag Managers er mega kraftfulde og kan meget mere end bare styre tracking scripts.

Når man har mulighed for at skyde JavaScript ind på et website, kan man nemlig også indsætte HTML og CSS. Dvs. alle de tre byggesten som et website er opbygget af.

Det har jeg for nyligt brugt til at visualisere data på et website, ved at indsætte grafer som denne kun ved brug af Google Tag Manager.

Grafen viser udviklingen af Bitcoins værdi de sidste 90 dage og opdateres dagligt med nyeste data. Og det fede er, at grafen slet ikke findes i kildekoden. Alt der skal bruges - både koden som laver grafen og de data der vises - hentes asynkront med Google Tag Manager og indsættes på siden, når det hele er hentet og klar. Og det kan indsættes et vilkårligt sted på alle sites på 5-10 minutter!

<div class="attention">
<strong>Opdatering 2026:</strong> Grafen herunder var oprindeligt indsat via GTM. Den er nu bygget direkte ind i sitet — den oprindelige guide nedenfor står urørt af historiske grunde.
</div>

<div class="bitcoin-chart-wrapper">
  <div class="bitcoin-chart-skeleton" aria-hidden="true"></div>
  <canvas id="bitcoinChart" aria-label="Linjegraf over Bitcoin værdi i USD det sidste år" role="img"></canvas>
  <table class="visually-hidden bitcoin-chart-data"><caption>Bitcoin værdi i USD per dag</caption><thead><tr><th>Dato</th><th>Værdi (USD)</th></tr></thead><tbody></tbody></table>
</div>

<h2>Opskriften</h2>

Der skal bruges tre ting:

<ul>
<li><a href="http://www.chartjs.org">ChartJS</a> til at visualisere data</li>
<li><a href="https://momentjs.com">MomentJS</a> til pæn formattering af datoer</li>
<li><a href="https://blockchain.info/api/charts_api">Data</a> der skal visualiseres</li>
</ul>

De første to ting er eksterne JavaScript filer som skal indlæses på siden. Dataene er tilgængelige via et JSON API, som skal hentes og indsættes i grafen og derefter skal det hele indsættes på siden.

<h2>Indlæs eksterne filer i GTM</h2>

Inde fra GTM kan man hente eksterne filer. Det gøres asynkront via AJAX, og det kører dermed i baggrunden, men det er stadig vigtigt at det kører så hurtigt som muligt.

Når ting hentes asynkront kan man ikke være sikker på at filerne bliver hentet i den rækkefølge man skriver dem i koden. Filer kan variere i størrelse og der kan være ventetid på den server de hentes fra. Det kan derfor sagtens være at det er den sidste fil, der bliver færdig først. Så man er nødt til at holde øje med hvornår <em>alle</em> filerne er hentet, inden resten af koden eksekveres.

Her er Promises i JavaScript genialt.

Med Promises kan man sætte alle filerne - både de eksterne filer og dataene der skal vises - igang med at downloade på én gang - asynkront - og derefter gå videre med at indlæse siden, så brugeren ikke skal vente. Ligeså snart alle filerne er downloadet og klar, kan jeg indsætte grafen på siden. Jeg bruger i øvrigt jQuery som gør det super nemt at arbejde med Promises.

<pre><code class="language-javascript">// De to eksterne filer, samt data i JSON format hentes
var chartJsPromise = $.getScript("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.min.js");
var momentJsPromise = $.getScript("https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js");
var dataPromise = $.getJSON("https://api.blockchain.info/charts/market-price?timespan=31days&amp;rollingAverage=24hours&amp;format=json&amp;cors=true");

// $.when metoden holder øje med hvornår alle filer er hentet
$.when(chartJsPromise, momentJsPromise, dataPromise).done(function(chartJsData, momentJsData, dataData) { 

    // Kør koden der indsætter grafen på siden

});
</code></pre>

<h2>Indsættelse af grafen på siden</h2>

For at indsætte grafen på siden skal der gøres følgende:

<ul>
<li>Find det sted på siden hvor grafen skal indsættes, dvs. find det HTML element som grafen enten skal indsættes før eller efter.</li>
<li>Det HTML som skal indsættes på siden, i dette tilfælde et canvas element.</li>
<li>CSS til styling af grafen og andre ting, så det hele ser pænt ud.</li>
</ul>

Grafen kan indsættes alle steder på siden, fx mellem det 3. og 4. afsnit som det er gjort her i indlægget.

Koden herunder finder først et element med ID'et #post-content og derefter alle p-elementer deri. Derefter findes det 3. p-element med eq(2) og indsætter canvas elementet som indeholder grafen lige efter dét p-element i koden med .after. Det er fedt med fuld fleksibilitet til at indsætte nye ting alle steder på siden. Til sidst har jeg tilføjet lidt inline CSS styling for at give grafen lidt luft.

<pre><code class="language-javascript">$("#post-content p").eq(2).after("&lt;canvas id=\"myChart\" width=\"400\" height=\"200\" style=\"margin: 50px 0 25px;\"&gt;&lt;/canvas&gt;");
</code></pre>

<h2>Klargøring af data til grafen</h2>

Dataene kommer fra et JSON API og for at dataene kan bruges i ChartJS skal de formatteres i to arrays. Et array med alle værdierne for X-aksen og et med alle værdierne som skal plottes på Y-aksen. I dette tilfælde er det datoer på X-aksen og den daglige værdi af Bitcoin på Y-aksen.

Der skal derfor gøres følgende:

<ul>
<li>Lav de to arrays.</li>
<li>Loop igennem alle rækkerne i det JSON data der kommer retur fra API'et.</li>
<li>Lav en pæn formattering af datoen baseret på det UNIX timestamp som kommer fra API'et.</li>
<li>Fyld alle værdierne i de to arrays.</li>
</ul>

<pre><code class="language-javascript">// De to arrays laves
  var dates = [],
  values = [];  

  // Loop igennem alle JSON rækkerne
  for (var i = 0; i &lt; dataData[0].values.length; i++) {

    // Lav en pæn dato formattering baseret på timestamp med MomentJS
    var prettyDate = moment(dataData[0].values[i].x*1000).format("DD/MM");

    // For hver række pushes værdierne for X og Y-aksen ind i de to arrays
    dates.push(prettyDate);
    values.push(dataData[0].values[i].y);     
  }
</code></pre>

<h2>Opsætning og opdatering af grafen</h2>

Canvas elementet er indsat på siden, så nu skal grafen bare bygges og indsættes i canvas elementet. Alt det klarer ChartJS med lidt simpel opsætning

<pre><code class="language-javascript">// Først findes canvas elementet med ID'et myChart    
  var ctx = document.getElementById("myChart").getContext('2d');

  // Grafen konfigureres ved at angive de to arrays med X og Y-værdierne, samt vælge lidt farver for grafen, så den passer ind i det øvrige design på sitet
  var myChart = new Chart(ctx, {    
    type: 'line',
    data: {
      labels: dates,
      datasets: [{
        label: 'Bitcoin værdi i USD',
        backgroundColor: 'rgba(88, 147, 178, 0.3)',
        borderColor: 'rgb(88, 147, 178)',
        data: values        
      }]
    }      
  });
});
</code></pre>

Den samlede kode som skal indsættes på sitet via GTM ser sådan ud:

```javascript
<script>
// De to eksterne filer, samt data i JSON format hentes
var chartJsPromise = $.getScript("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.min.js");
var momentJsPromise = $.getScript("https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js");
var dataPromise = $.getJSON("https://api.blockchain.info/charts/market-price?timespan=31days&amp;rollingAverage=24hours&amp;format=json&amp;cors=true");

// $.when metoden holder øje med hvornår alle filer er hentet
$.when(chartJsPromise, momentJsPromise, dataPromise).done(function(chartJsData, momentJsData, dataData) {

  $("#post-content p").eq(2).after("&lt;canvas id=\"myChart\" width=\"400\" height=\"200\" style=\"margin: 50px 0 25px;\"&gt;&lt;/canvas&gt;");

  // De to arrays laves
  var dates = [],
  values = [];  

  // Loop igennem alle JSON rækkerne
  for (var i = 0; i &lt; dataData[0].values.length; i++) {

    // Lav en pæn dato formattering baseret på timestamp med MomentJS
    var prettyDate = moment(dataData[0].values[i].x*1000).format("DD/MM");

    // For hver række pushes værdierne for X og Y-aksen ind i de to arrays
    dates.push(prettyDate);
    values.push(dataData[0].values[i].y);     
  }

  // Først findes canvas elementet med ID'et myChart    
  var ctx = document.getElementById("myChart").getContext('2d');

  // Grafen konfigureres ved at angive de to arrays med X og Y-værdierne, samt vælge lidt farver for grafen, så den passer ind i det øvrige design på sitet
  var myChart = new Chart(ctx, {    
    type: 'line',
    data: {
      labels: dates,
      datasets: [{
        label: 'Bitcoin værdi i USD',
        backgroundColor: 'rgba(88, 147, 178, 0.3)',
        borderColor: 'rgb(88, 147, 178)',
        data: values        
      }]
    }      
  });
});
</script>
```

<h2>Indsæt koden på sitet via GTM</h2>

I Google Tag Manager indsættes koden via et Custom HTML Tag.

<figure><a href="{{ '/assets/images/gtm-chartjs-custom-html.tag_.png' | relative_url }}"><img src="{{ '/assets/images/gtm-chartjs-custom-html.tag_.png' | relative_url }}" alt="Custom HTML Tag med alt koden." width="929" height="692" class="size-full wp-image-1142" /></a><figcaption>Custom HTML Tag med alt koden.</figcaption></figure>

Som trigger vælges den side grafen skal indsættes på, så koden og de eksterne filer kun indlæses på den ene side, og ikke sløver hele sitet.

Jeg har derfor lavet en trigger med URL'en for denne side: <strong>/visualisering-data-google-tag-manager-chartjs</strong>

<figure><a href="{{ '/assets/images/gtm-chartjs-trigger.png' | relative_url }}"><img src="{{ '/assets/images/gtm-chartjs-trigger.png' | relative_url }}" alt="Trigger i GTM som kun affyrer koden på denne side." width="1381" height="546" class="size-full wp-image-1148" /></a><figcaption>Trigger i GTM som kun affyrer koden på denne side.</figcaption></figure>

Bemærk at triggeren kører på DOM ready og ikke når siden indlæses. GTM scriptet bliver indlæst i toppen af siden, så hvis triggeren kører når siden indlæses er det ikke sikkert at HTML elementet som grafen skal indsættes efter findes endnu og så vil koden fejle. Når triggeren kører på DOM ready er man sikker på at hele DOM'en er indlæst og HTML elementet er tilstede i koden.

<h2>Det er ikke super robust</h2>

Ovenstående er et glimrende eksempel på hvor meget fedt man kan lave på et website. Det kræver blot Google Tag Manager og et API som kan levere data, så kan det indsættes på siden med JavaScript. Og det kan laves på meget kort tid og være live på website med det samme.

Ulempen ved at indsætte ting på sitet på denne måde, er at det er meget sårbart overfor ændringer på sitet. Hvis HTML koden på sitet ændres, kan man måske ikke længere finde det element som grafen skal indsættes efter. Det kan også være URL'en til API'et ændres. Eller formatet i JSON filen kan ændres og så virker dataene ikke længere. Så det er ofte noget jeg vil anbefale som et quick fix, men så længe man er opmærksom på det, kan man også hurtigt tilpasse koden i GTM og være live igen på få minutter.