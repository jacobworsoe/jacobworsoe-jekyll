---
layout: post
title: Visualisering af data med Google Tag Manager og ChartJS
date: 2017-06-14 21:29:04
slug: visualisering-data-google-tag-manager-chartjs
categories:
  - Analytics
---

<p>Tag Managers er mega kraftfulde og kan meget mere end bare styre tracking scripts.</p>
<p>Når man har mulighed for at skyde JavaScript ind på et website, kan man nemlig også indsætte HTML og CSS. Dvs. alle de tre byggesten som et website er opbygget af.</p>
<p>Det har jeg for nyligt brugt til at visualisere data på et website, ved at indsætte grafer som denne kun ved brug af Google Tag Manager.</p>
<p>Grafen viser udviklingen af Bitcoins værdi de sidste 90 dage og opdateres dagligt med nyeste data. Og det fede er, at grafen slet ikke findes i kildekoden. Alt der skal bruges &#8211; både koden som laver grafen og de data der vises &#8211; hentes asynkront med Google Tag Manager og indsættes på siden, når det hele er hentet og klar. Og det kan indsættes et vilkårligt sted på alle sites på 5-10 minutter!</p>
<h2>Opskriften</h2>
<p>Der skal bruges tre ting:</p>
<ul>
<li><a href="http://www.chartjs.org">ChartJS</a> til at visualisere data</li>
<li><a href="https://momentjs.com">MomentJS</a> til pæn formattering af datoer</li>
<li><a href="https://blockchain.info/api/charts_api">Data</a> der skal visualiseres</li>
</ul>
<p>De første to ting er eksterne JavaScript filer som skal indlæses på siden. Dataene er tilgængelige via et JSON API, som skal hentes og indsættes i grafen og derefter skal det hele indsættes på siden.</p>
<h2>Indlæs eksterne filer i GTM</h2>
<p>Inde fra GTM kan man hente eksterne filer. Det gøres asynkront via AJAX, og det kører dermed i baggrunden, men det er stadig vigtigt at det kører så hurtigt som muligt.</p>
<p>Når ting hentes asynkront kan man ikke være sikker på at filerne bliver hentet i den rækkefølge man skriver dem i koden. Filer kan variere i størrelse og der kan være ventetid på den server de hentes fra. Det kan derfor sagtens være at det er den sidste fil, der bliver færdig først. Så man er nødt til at holde øje med hvornår <em>alle</em> filerne er hentet, inden resten af koden eksekveres.</p>
<p>Her er Promises i JavaScript genialt.</p>
<p>Med Promises kan man sætte alle filerne &#8211; både de eksterne filer og dataene der skal vises &#8211; igang med at downloade på én gang &#8211; asynkront &#8211; og derefter gå videre med at indlæse siden, så brugeren ikke skal vente. Ligeså snart alle filerne er downloadet og klar, kan jeg indsætte grafen på siden. Jeg bruger i øvrigt jQuery som gør det super nemt at arbejde med Promises.</p>
<pre><code class="" data-line="">// De to eksterne filer, samt data i JSON format hentes
var chartJsPromise = $.getScript(&quot;https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.min.js&quot;);
var momentJsPromise = $.getScript(&quot;https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js&quot;);
var dataPromise = $.getJSON(&quot;https://api.blockchain.info/charts/market-price?timespan=31days&amp;rollingAverage=24hours&amp;format=json&amp;cors=true&quot;);

// $.when metoden holder øje med hvornår alle filer er hentet
$.when(chartJsPromise, momentJsPromise, dataPromise).done(function(chartJsData, momentJsData, dataData) { 

    // Kør koden der indsætter grafen på siden

});
</code></pre>
<h2>Indsættelse af grafen på siden</h2>
<p>For at indsætte grafen på siden skal der gøres følgende:</p>
<ul>
<li>Find det sted på siden hvor grafen skal indsættes, dvs. find det HTML element som grafen enten skal indsættes før eller efter.</li>
<li>Det HTML som skal indsættes på siden, i dette tilfælde et canvas element.</li>
<li>CSS til styling af grafen og andre ting, så det hele ser pænt ud.</li>
</ul>
<p>Grafen kan indsættes alle steder på siden, fx mellem det 3. og 4. afsnit som det er gjort her i indlægget.</p>
<p>Koden herunder finder først et element med ID&#8217;et #post-content og derefter alle p-elementer deri. Derefter findes det 3. p-element med eq(2) og indsætter canvas elementet som indeholder grafen lige efter dét p-element i koden med .after. Det er fedt med fuld fleksibilitet til at indsætte nye ting alle steder på siden. Til sidst har jeg tilføjet lidt inline CSS styling for at give grafen lidt luft.</p>
<pre><code class="" data-line="">$(&quot;#post-content p&quot;).eq(2).after(&quot;&lt;canvas id=\&quot;myChart\&quot; width=\&quot;400\&quot; height=\&quot;200\&quot; style=\&quot;margin: 50px 0 25px;\&quot;&gt;&lt;/canvas&gt;&quot;);
</code></pre>
<h2>Klargøring af data til grafen</h2>
<p>Dataene kommer fra et JSON API og for at dataene kan bruges i ChartJS skal de formatteres i to arrays. Et array med alle værdierne for X-aksen og et med alle værdierne som skal plottes på Y-aksen. I dette tilfælde er det datoer på X-aksen og den daglige værdi af Bitcoin på Y-aksen.</p>
<p>Der skal derfor gøres følgende:</p>
<ul>
<li>Lav de to arrays.</li>
<li>Loop igennem alle rækkerne i det JSON data der kommer retur fra API&#8217;et.</li>
<li>Lav en pæn formattering af datoen baseret på det UNIX timestamp som kommer fra API&#8217;et.</li>
<li>Fyld alle værdierne i de to arrays.</li>
</ul>
<pre><code class="" data-line="">// De to arrays laves
  var dates = [],
  values = [];  

  // Loop igennem alle JSON rækkerne
  for (var i = 0; i &lt; dataData[0].values.length; i++) {

    // Lav en pæn dato formattering baseret på timestamp med MomentJS
    var prettyDate = moment(dataData[0].values[i].x*1000).format(&quot;DD/MM&quot;);

    // For hver række pushes værdierne for X og Y-aksen ind i de to arrays
    dates.push(prettyDate);
    values.push(dataData[0].values[i].y);     
  }
</code></pre>
<h2>Opsætning og opdatering af grafen</h2>
<p>Canvas elementet er indsat på siden, så nu skal grafen bare bygges og indsættes i canvas elementet. Alt det klarer ChartJS med lidt simpel opsætning</p>
<pre><code class="" data-line="">// Først findes canvas elementet med ID&#039;et myChart    
  var ctx = document.getElementById(&quot;myChart&quot;).getContext(&#039;2d&#039;);

  // Grafen konfigureres ved at angive de to arrays med X og Y-værdierne, samt vælge lidt farver for grafen, så den passer ind i det øvrige design på sitet
  var myChart = new Chart(ctx, {    
    type: &#039;line&#039;,
    data: {
      labels: dates,
      datasets: [{
        label: &#039;Bitcoin værdi i USD&#039;,
        backgroundColor: &#039;rgba(88, 147, 178, 0.3)&#039;,
        borderColor: &#039;rgb(88, 147, 178)&#039;,
        data: values        
      }]
    }      
  });
});
</code></pre>
<p>Den samlede kode som skal indsættes på sitet via GTM ser sådan ud:</p>
<pre><code class="" data-line="">&lt;script&gt;
// De to eksterne filer, samt data i JSON format hentes
var chartJsPromise = $.getScript(&quot;https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.min.js&quot;);
var momentJsPromise = $.getScript(&quot;https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js&quot;);
var dataPromise = $.getJSON(&quot;https://api.blockchain.info/charts/market-price?timespan=31days&amp;rollingAverage=24hours&amp;format=json&amp;cors=true&quot;);

// $.when metoden holder øje med hvornår alle filer er hentet
$.when(chartJsPromise, momentJsPromise, dataPromise).done(function(chartJsData, momentJsData, dataData) {

  $(&quot;#post-content p&quot;).eq(2).after(&quot;&lt;canvas id=\&quot;myChart\&quot; width=\&quot;400\&quot; height=\&quot;200\&quot; style=\&quot;margin: 50px 0 25px;\&quot;&gt;&lt;/canvas&gt;&quot;);

  // De to arrays laves
  var dates = [],
  values = [];  

  // Loop igennem alle JSON rækkerne
  for (var i = 0; i &lt; dataData[0].values.length; i++) {

    // Lav en pæn dato formattering baseret på timestamp med MomentJS
    var prettyDate = moment(dataData[0].values[i].x*1000).format(&quot;DD/MM&quot;);

    // For hver række pushes værdierne for X og Y-aksen ind i de to arrays
    dates.push(prettyDate);
    values.push(dataData[0].values[i].y);     
  }

  // Først findes canvas elementet med ID&#039;et myChart    
  var ctx = document.getElementById(&quot;myChart&quot;).getContext(&#039;2d&#039;);

  // Grafen konfigureres ved at angive de to arrays med X og Y-værdierne, samt vælge lidt farver for grafen, så den passer ind i det øvrige design på sitet
  var myChart = new Chart(ctx, {    
    type: &#039;line&#039;,
    data: {
      labels: dates,
      datasets: [{
        label: &#039;Bitcoin værdi i USD&#039;,
        backgroundColor: &#039;rgba(88, 147, 178, 0.3)&#039;,
        borderColor: &#039;rgb(88, 147, 178)&#039;,
        data: values        
      }]
    }      
  });
});
&lt;/script&gt;
</code></pre>
<h2>Indsæt koden på sitet via GTM</h2>
<p>I Google Tag Manager indsættes koden via et Custom HTML Tag.</p>
<div id="attachment_1142" style="width: 939px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-custom-html.tag_.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1142" src="https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-custom-html.tag_.png" alt="Custom HTML Tag med alt koden." width="929" height="692" class="size-full wp-image-1142" srcset="https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-custom-html.tag_.png 929w, https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-custom-html.tag_-690x514.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-custom-html.tag_-768x572.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-custom-html.tag_-725x540.png 725w" sizes="auto, (max-width: 929px) 100vw, 929px" /></a><p id="caption-attachment-1142" class="wp-caption-text">Custom HTML Tag med alt koden.</p></div>
<p>Som trigger vælges den side grafen skal indsættes på, så koden og de eksterne filer kun indlæses på den ene side, og ikke sløver hele sitet.</p>
<p>Jeg har derfor lavet en trigger med URL&#8217;en for denne side: <strong>/visualisering-data-google-tag-manager-chartjs</strong></p>
<div id="attachment_1148" style="width: 1391px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-trigger.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1148" src="https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-trigger.png" alt="Trigger i GTM som kun affyrer koden på denne side." width="1381" height="546" class="size-full wp-image-1148" srcset="https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-trigger.png 1381w, https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-trigger-690x273.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-trigger-768x304.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/gtm-chartjs-trigger-725x287.png 725w" sizes="auto, (max-width: 1381px) 100vw, 1381px" /></a><p id="caption-attachment-1148" class="wp-caption-text">Trigger i GTM som kun affyrer koden på denne side.</p></div>
<p>Bemærk at triggeren kører på DOM ready og ikke når siden indlæses. GTM scriptet bliver indlæst i toppen af siden, så hvis triggeren kører når siden indlæses er det ikke sikkert at HTML elementet som grafen skal indsættes efter findes endnu og så vil koden fejle. Når triggeren kører på DOM ready er man sikker på at hele DOM&#8217;en er indlæst og HTML elementet er tilstede i koden.</p>
<h2>Det er ikke super robust</h2>
<p>Ovenstående er et glimrende eksempel på hvor meget fedt man kan lave på et website. Det kræver blot Google Tag Manager og et API som kan levere data, så kan det indsættes på siden med JavaScript. Og det kan laves på meget kort tid og være live på website med det samme.</p>
<p>Ulempen ved at indsætte ting på sitet på denne måde, er at det er meget sårbart overfor ændringer på sitet. Hvis HTML koden på sitet ændres, kan man måske ikke længere finde det element som grafen skal indsættes efter. Det kan også være URL&#8217;en til API&#8217;et ændres. Eller formatet i JSON filen kan ændres og så virker dataene ikke længere. Så det er ofte noget jeg vil anbefale som et quick fix, men så længe man er opmærksom på det, kan man også hurtigt tilpasse koden i GTM og være live igen på få minutter.</p>

