---
layout: post
title: Ødelægger en slide-in konverteringsraten?
date: 2020-09-13 21:17:02
slug: slide-in-konverteringsrate
wordpress_id: 2485
categories:
  - Analytics
---

Slide-ins er geniale. Altså sådan nogle som danske <a href="https://sleeknote.com/">Sleeknote</a> laver. Eller sagt på godt gammeldags dansk: En <a href="https://trendsonline.dk/2014/06/10/twami-fusioneres-og-bliver-til-sleeknote/">twami</a> :)

De er geniale til at indsamle e-mail permission på et website. Og de er ikke så irriterende som pop-ups.

Eller er de?

Kan de være så irriterende at brugerne ikke konverterer og måske forlader sitet?

Det har jeg testet!

<h2>Indhold</h2>
<ul>
  <li><a href="#article-header-id-0">Byg en simpel slide-in</a></li>
    <ul><li><a href="#article-header-id-1">HTML</a></li>
    <li><a href="#article-header-id-2">CSS</a></li>
    <li><a href="#article-header-id-3">JavaScript</a></li></ul>
  <li><a href="#article-header-id-4">Hvornår skal den så vises?</a></li>
    <ul><li><a href="#article-header-id-5">Vis på et tilfældigt tidspunkt</a></li></ul>
  <li><a href="#article-header-id-6">Effekt på tilmelding til nyhedsbrev</a></li>
  <li><a href="#article-header-id-7">Effekt på læsning af blogindlæg</a></li>
    <ul><li><a href="#article-header-id-8">Læst 33%</a></li>
    <li><a href="#article-header-id-9">Læst 66%</a></li>
    <li><a href="#article-header-id-10">Læst 100%</a></li>
    <li><a href="#article-header-id-11">Læst 100% + 1 minut</a></li></ul>
  <li><a href="#article-header-id-12">Opsummering</a></li>
</ul>

<h2 id="article-header-id-0">Byg en simpel slide-in</h2>

Jeg lavede en simpel slide-in her på min blog.

<h3 id="article-header-id-1">HTML</h3>

Selve slide-in boxen er blot noget simpel HTML.

```html
<div class="slide-in-box">
    <a href="#" class="slide-in-box-close"></a>
    <h3>Få gratis tips og tricks i din indbakke!</h3>
    <form action="" method="post">
    ... input felter ...
    </form>
</div>
```

<h3 id="article-header-id-2">CSS</h3>

Den kan styles på mange måder, men det vigtigste er at den har <code>position: fixed</code> så den er låst i bunden af skærmen og <code>z-index: 99999</code> så den er "ovenpå" websitet. Derudover har den <code>bottom: -100%</code> som gør at den som standard er skjult "under" skærmen.

Når slide-in boxen skal vises, sætter jeg en <code>.open</code> class på den med JavaScript, som sætter <code>bottom: 5px</code> som gør at den bliver synlig 5px over bunden af skærmen.

<code>transition: .5s bottom ease-in-out</code> tilføjer en animation når værdien af <code>bottom</code> ændres, som gør at den "slider" op nedefra.

<pre><code class="language-sass">.slide-in-box  
  z-index: 99999  
  position: fixed 
  bottom: -100% 
  transition: .5s bottom ease-in-out

  &.open
    bottom: 5px
</code></pre>

Dermed har jeg en simpel slide-in box.

<figure><img src="{{ '/assets/images/2020/09/slide-in-box.jpg' | relative_url }}" alt="Den færdige slide-in box." width="447" height="450" class="size-full wp-image-2510 no-border" /><figcaption>Den færdige slide-in box.</figcaption></figure>

<h3 id="article-header-id-3">JavaScript</h3>

Det sidste er et stykke JavaScript til at vise boxen.

Slide-in boxen skal kunne åbne på forskellige tidspunkter, så jeg har lavet en funktion, som jeg kan kalde til at åbne den, som gør følgende.

<ol>
<li>Funktionen tager en parameter <code>randomPageState</code> som er tidspunktet hvor den skal åbne. Det kommer vi tilbage til lige om lidt.</li>
<li>Hvis personen tidligere har set og lukket en slide-in box, bliver det gemt i <code>localStorage</code>. Jeg tjekker om det er sket, så jeg ikke viser boxen igen til samme bruger.</li>
<li>Jeg sætter en <code>.open</code> class på boxen så den åbner.</li>
<li>Til sidst tracker jeg et event med at boxen er åbnet og tidspunktet den åbnede på.</li>
</ol>

<pre><code class="language-javascript">showSlideUpBox: function(randomPageState) {    
    var slideInOptOut = localStorage.getItem("slideInOptOut");
    var slideUpBox = document.querySelector(".slide-in-box");
    if (!slideInOptOut) {
      slideUpBox.classList.add("open");
      Tracking.trackSlideUpBox("open", randomPageState);
    }
}
</code></pre>

Sådan ser det ud når slide-in boxen bliver synlig.

<figure><img src="{{ '/assets/images/2020/09/Slide-in-16c-lossy0.gif' | relative_url }}" alt="Slide-in boxen bliver synlig." width="830" height="467" class="size-full wp-image-2511" /><figcaption>Slide-in boxen bliver synlig.</figcaption></figure>

<h2 id="article-header-id-4">Hvornår skal den så vises?</h2>

Jeg tracker detaljeret hvor meget der bliver læst af mine blogindlæg ved at sende et event på følgende tidspunkter.

<ol>
<li>Når brugeren lander på et blogindlæg (detail view)</li>
<li>Når brugeren begynder at scrolle (add to cart).</li>
<li>Når brugeren har scrollet 33% af indlæggets længde (checkout step 1).</li>
<li>Når brugeren har scrollet 66% af indlæggets længde (checkout step 2).</li>
<li>Når brugeren har scrollet 100% af indlæggets længde (checkout step 3).</li>
<li>Når brugeren har scrollet 100% af indlæggets længde og været på siden mindst et minut (purchase).</li>
</ol>

Jeg tracker de events med <a href="{{ '/indhold-enhanced-ecommerce/' | relative_url }}">Enhanced Ecommerce hvis du vil læse mere om det</a>.

Jeg vil gerne tracke det optimale tidspunkt at vise en slide-in på af de 6 ovenstående tidspunkter. Både for at øge konverteringen og få flest mulige tilmeldinger til mit <a href="{{ '/nyhedsbrev/' | relative_url }}">nyhedsbrev</a>. Men også for at undgå at irritere brugeren, så de forlader siden uden at læse indlægget færdigt.

<h3 id="article-header-id-5">Vis på et tilfældigt tidspunkt</h3>

Ud af de 6 ovenstående tidspunkter jeg kan vise en slide-in på, vil jeg dog ikke vise den med det samme når brugeren lander på siden, så jeg vil teste de andre 5 tidspunkter.

Jeg har lavet et array med de 5 tidspunkter:

<pre><code class="language-javascript">var randomPageStates = ["scroller","oneThird","twoThirds","endContent","purchase"];
</code></pre>

Når brugeren lander på et blogindlæg bruger jeg JavaScript til at generere et tilfældigt tal mellem 0-4.

<pre><code class="language-javascript">var randomPageState = Math.floor(Math.random() * 5);
</code></pre>

Dette tal bruger jeg så til at vælge et af de 5 tidspunkter. Arrays i JavaScript er 0-indexeret, så den første plads er index 0, op til index 4.

Jeg bruger det tilfældige tal til at vælge et tilfældigt index i array'et, som styrer hvornår min slide-in vises på siden. Jeg tracker også værdien i en Hit-scoped custom dimension, så jeg kan sammenholde det med konvertering og frafald.

Lad os starte med konverteringer.

<h2 id="article-header-id-6">Effekt på tilmelding til nyhedsbrev</h2>

Okay, vi kan lige så godt tage den med det samme. Min slide-in konverterer ikke. Slet ikke.

<figure><img src="{{ '/assets/images/2020/09/Slide-in-conversion-events-dark-860x435.jpg' | relative_url }}" alt="22.161 visninger af slide-in og kun 29 tilmeldinger." width="860" height="435" class="size-large wp-image-2540" /><figcaption>22.161 visninger af slide-in og kun 29 tilmeldinger.</figcaption></figure>

Slide-in boxen er i alt blevet vist 22.161 gange og den er blevet lukket 15.490 gange. Men den har kun fået 29 tilmeldinger.

29!

Det er en konverteringsrate på 0,13%.

Men det er også min egen skyld. Jeg sælger slet ikke den tilmelding godt nok. Det er ikke nok bare at give mulighed for at få en mail ved nye blogindlæg.

Det virker meget bedre med en <a href="http://pottercut.dk/emil-kristensen/faa-flere-tilmeldinger-din-nyhedsmail/">Content Upgrade</a>.

Nåh, men det var heller ikke det vi skulle snakke om!

<h2 id="article-header-id-7">Effekt på læsning af blogindlæg</h2>

Jeg vil gerne undersøge om brugerne er mere tilbøjelige til at forlade sitet når min slide-in bliver vist.

I det efterfølgende kigger jeg på konverteringsraten for de enkelte events ned gennem et blogindlæg sammenlignet med detail views som er det samme som sidevisninger på blogindlægget.

Det første jeg kigger på er Add to Cart konverteringsraten, dvs. hvor mange der begynder at scrolle.

Denne er lidt ligeyldig fordi min slide-in tidligst bliver vist på det tidspunkt hvor de rammer Add to Cart. Så den kan faktisk ikke nå at påvirke, men den er god at have med som kontrol.

De fem søjler er de fem tidspunkter slide-in boxen bliver vist på. Ikke overraskende er konverteringsraten næsten den samme for alle grupper.

<figure><img src="{{ '/assets/images/2020/09/Add-to-Cart-konvertering.jpg' | relative_url }}" alt="Ikke overraskende er konverteringsraten næsten den samme for alle grupper." width="1035" height="578" class="size-full wp-image-2530" /><figcaption>Ikke overraskende er konverteringsraten næsten den samme for alle grupper.</figcaption></figure>

<h3 id="article-header-id-8">Læst 33%</h3>

Det næste event er dem som har scrollet 33% af indlægget og her vil den første gruppe altså have set slide-in boxen, mens de andre ikke har set den endnu.

<figure><img src="{{ '/assets/images/2020/09/Laest-33p-konvertering.jpg' | relative_url }}" alt="Ikke den store forskel på dem der har set slide-in boxen." width="1033" height="580" class="size-full wp-image-2531" /><figcaption>Ikke den store forskel på dem der har set slide-in boxen.</figcaption></figure>

Add to Cart har en anelse lavere konverteringsrate end Læst 33% men forskellen er meget lille og med en p-værdi på 0,1572 er den ikke signifikant.

<figure><a href="https://www.surveymonkey.com/mp/ab-testing-significance-calculator/"><img src="{{ '/assets/images/2020/09/significance-test-860x413.jpg' | relative_url }}" alt="SurveyMonkey: A/B-test signifikansberegner (skærmbillede)" width="860" height="413" class="size-large wp-image-2543" /></a><figcaption><a href="https://www.surveymonkey.com/mp/ab-testing-significance-calculator/">SurveyMonkey</a> har en god signifikans test.</figcaption></figure>

Man kan også se at Læst 100% har en konverteringsrate der er endnu lavere end Add to Cart og Læst 100% har altså ikke set slide-in boxen endnu, så det er bare naturlig varians.

Indtil videre påvirker det altså ikke konverteringsraten.

<h3 id="article-header-id-9">Læst 66%</h3>

Ved 66% læst er der heller ingen markant forskel og faktisk er det de to øverste grupper (som på dette tidspunkt har set slide-in boxen) der har den højeste konvertering.

<figure><img src="{{ '/assets/images/2020/09/Laest-66p-konvertering.jpg' | relative_url }}" alt="Ved 66% læst er der heller ikke forskel." width="1032" height="578" class="size-full wp-image-2532" /><figcaption>Ved 66% læst er der heller ikke forskel.</figcaption></figure>

Så stadig ingen påvirkning.

<h3 id="article-header-id-10">Læst 100%</h3>

Ved 100% læst er det dermed de øverste 3 grupper der har fået vist slide-in boxen - men det har stadig ingen betydning.

<figure><img src="{{ '/assets/images/2020/09/Laest-100p-konvertering.jpg' | relative_url }}" alt="Samme billede ved 100% læst." width="1030" height="577" class="size-full wp-image-2533" /><figcaption>Samme billede ved 100% læst.</figcaption></figure>

Videre til sidste event.

<h3 id="article-header-id-11">Læst 100% + 1 minut</h3>

Det sidste event er dem som har scrollet 100% og været på siden mindst 1 minut - det er dem hvor jeg antager at de faktisk har læst hele blogindlægget (<a href="{{ '/indhold-enhanced-ecommerce/' | relative_url }}">og dem jeg tracker som et transaktion i Enhanced Ecommerce</a>).

<figure><img src="{{ '/assets/images/2020/09/Laest-100p-1-minut-konvertering.jpg' | relative_url }}" alt="Heller ikke ved 100% læst + 1 minut på siden er der nogen entydig forskel." width="1030" height="577" class="size-full wp-image-2534" /><figcaption>Heller ikke ved 100% læst + 1 minut på siden er der nogen entydig forskel.</figcaption></figure>

Men heller ikke her er der nogen entydig forskel som skulle indikere at brugerne bliver irriteret af en slide-in og dermed er mere tilbøjelige til at forlade sitet eller mindre tilbøjelige til at læse blogindlægget færdig.

Konklusionen er derfor at min slide-in ikke er irriterende for brugerne - i hvert fald ikke så meget at de ikke gider læse blogindlægget færdigt.

<h2 id="article-header-id-12">Opsummering</h2>

I dette blogindlæg har jeg brugt Google Analytics og Google Tag Manager til at indsamle det nødvendige data til at teste hypotesen om at slide-ins ødelægger konverteringsraten. Min konklusion gælder ikke for alle sites og alle brancher - sådan noget skal altid testes på det enkelte site. Men jeg håber at ovenstående kan give noget inspiration til hvordan man kan opstille en hypotese, indsamle den nødvendige data og analysere det, så der kan træffes en beslutning på baggrund af data.

Tilbage er der blot at få lavet en ordentlig content upgrade, så jeg kan lave en slide-in der faktisk kan give nogle tilmeldinger til mit <a href="{{ '/nyhedsbrev/' | relative_url }}">nyhedsbrev</a>.