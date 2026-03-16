---
layout: post
title: Ødelægger en slide-in konverteringsraten?
date: 2020-09-13 21:17:02
slug: slide-in-konverteringsrate
categories:
  - Analytics
---

<p>Slide-ins er geniale. Altså sådan nogle som danske <a href="https://sleeknote.com/">Sleeknote</a> laver. Eller sagt på godt gammeldags dansk: En <a href="https://trendsonline.dk/2014/06/10/twami-fusioneres-og-bliver-til-sleeknote/">twami</a> :)</p>
<p>De er geniale til at indsamle e-mail permission på et website. Og de er ikke så irriterende som pop-ups.</p>
<p>Eller er de?</p>
<p>Kan de være så irriterende at brugerne ikke konverterer og måske forlader sitet?</p>
<p>Det har jeg testet!</p>
<h2>Indhold</h2>
<ul>
<li><a href="#article-header-id-0">Byg en simpel slide-in</a></li>
<ul>
<li><a href="#article-header-id-1">HTML</a></li>
<li><a href="#article-header-id-2">CSS</a></li>
<li><a href="#article-header-id-3">JavaScript</a></li>
</ul>
<li><a href="#article-header-id-4">Hvornår skal den så vises?</a></li>
<ul>
<li><a href="#article-header-id-5">Vis på et tilfældigt tidspunkt</a></li>
</ul>
<li><a href="#article-header-id-6">Effekt på tilmelding til nyhedsbrev</a></li>
<li><a href="#article-header-id-7">Effekt på læsning af blogindlæg</a></li>
<ul>
<li><a href="#article-header-id-8">Læst 33%</a></li>
<li><a href="#article-header-id-9">Læst 66%</a></li>
<li><a href="#article-header-id-10">Læst 100%</a></li>
<li><a href="#article-header-id-11">Læst 100% + 1 minut</a></li>
</ul>
<li><a href="#article-header-id-12">Opsummering</a></li>
</ul>
<h2 id="article-header-id-0">Byg en simpel slide-in</h2>
<p>Jeg lavede en simpel slide-in her på min blog.</p>
<h3 id="article-header-id-1">HTML</h3>
<p>Selve slide-in boxen er blot noget simpel HTML.</p>
<pre><code class="" data-line="">&lt;div class=&quot;slide-in-box&quot;&gt;
    &lt;a href=&quot;#&quot; class=&quot;slide-in-box-close&quot;&gt;&lt;/a&gt;
    &lt;h3&gt;Få gratis tips og tricks i din indbakke!&lt;/h3&gt;
    &lt;form action=&quot;&quot; method=&quot;post&quot;&gt;
    ... input felter ...
    &lt;/form&gt;
&lt;/div&gt;
</code></pre>
<h3 id="article-header-id-2">CSS</h3>
<p>Den kan styles på mange måder, men det vigtigste er at den har <code class="" data-line="">position: fixed</code> så den er låst i bunden af skærmen og <code class="" data-line="">z-index: 99999</code> så den er &#8220;ovenpå&#8221; websitet. Derudover har den <code class="" data-line="">bottom: -100%</code> som gør at den som standard er skjult &#8220;under&#8221; skærmen.</p>
<p>Når slide-in boxen skal vises, sætter jeg en <code class="" data-line="">.open</code> class på den med JavaScript, som sætter <code class="" data-line="">bottom: 5px</code> som gør at den bliver synlig 5px over bunden af skærmen.</p>
<p><code class="" data-line="">transition: .5s bottom ease-in-out</code> tilføjer en animation når værdien af <code class="" data-line="">bottom</code> ændres, som gør at den &#8220;slider&#8221; op nedefra.</p>
<pre><code class="" data-line="">.slide-in-box  
  z-index: 99999  
  position: fixed 
  bottom: -100% 
  transition: .5s bottom ease-in-out

  &amp;.open
    bottom: 5px
</code></pre>
<p>Dermed har jeg en simpel slide-in box.</p>
<div id="attachment_2510" style="width: 457px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2510" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/slide-in-box.jpg" alt="Den færdige slide-in box." width="447" height="450" class="size-full wp-image-2510 no-border" /><p id="caption-attachment-2510" class="wp-caption-text">Den færdige slide-in box.</p></div>
<h3 id="article-header-id-3">JavaScript</h3>
<p>Det sidste er et stykke JavaScript til at vise boxen.</p>
<p>Slide-in boxen skal kunne åbne på forskellige tidspunkter, så jeg har lavet en funktion, som jeg kan kalde til at åbne den, som gør følgende.</p>
<ol>
<li>Funktionen tager en parameter <code class="" data-line="">randomPageState</code> som er tidspunktet hvor den skal åbne. Det kommer vi tilbage til lige om lidt.</li>
<li>Hvis personen tidligere har set og lukket en slide-in box, bliver det gemt i <code class="" data-line="">localStorage</code>. Jeg tjekker om det er sket, så jeg ikke viser boxen igen til samme bruger.</li>
<li>Jeg sætter en <code class="" data-line="">.open</code> class på boxen så den åbner.</li>
<li>Til sidst tracker jeg et event med at boxen er åbnet og tidspunktet den åbnede på.</li>
</ol>
<pre><code class="" data-line="">showSlideUpBox: function(randomPageState) {    
    var slideInOptOut = localStorage.getItem(&quot;slideInOptOut&quot;);
    var slideUpBox = document.querySelector(&quot;.slide-in-box&quot;);
    if (!slideInOptOut) {
      slideUpBox.classList.add(&quot;open&quot;);
      Tracking.trackSlideUpBox(&quot;open&quot;, randomPageState);
    }
}
</code></pre>
<p>Sådan ser det ud når slide-in boxen bliver synlig.</p>
<div id="attachment_2511" style="width: 840px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2511" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Slide-in-16c-lossy0.gif" alt="Slide-in boxen bliver synlig." width="830" height="467" class="size-full wp-image-2511" /><p id="caption-attachment-2511" class="wp-caption-text">Slide-in boxen bliver synlig.</p></div>
<h2 id="article-header-id-4">Hvornår skal den så vises?</h2>
<p>Jeg tracker detaljeret hvor meget der bliver læst af mine blogindlæg ved at sende et event på følgende tidspunkter.</p>
<ol>
<li>Når brugeren lander på et blogindlæg (detail view)</li>
<li>Når brugeren begynder at scrolle (add to cart).</li>
<li>Når brugeren har scrollet 33% af indlæggets længde (checkout step 1).</li>
<li>Når brugeren har scrollet 66% af indlæggets længde (checkout step 2).</li>
<li>Når brugeren har scrollet 100% af indlæggets længde (checkout step 3).</li>
<li>Når brugeren har scrollet 100% af indlæggets længde og været på siden mindst et minut (purchase).</li>
</ol>
<p>Jeg tracker de events med <a href="https://www.jacobworsoe.dk/indhold-enhanced-ecommerce/">Enhanced Ecommerce hvis du vil læse mere om det</a>.</p>
<p>Jeg vil gerne tracke det optimale tidspunkt at vise en slide-in på af de 6 ovenstående tidspunkter. Både for at øge konverteringen og få flest mulige tilmeldinger til mit <a href="https://www.jacobworsoe.dk/nyhedsbrev/">nyhedsbrev</a>. Men også for at undgå at irritere brugeren, så de forlader siden uden at læse indlægget færdigt.</p>
<h3 id="article-header-id-5">Vis på et tilfældigt tidspunkt</h3>
<p>Ud af de 6 ovenstående tidspunkter jeg kan vise en slide-in på, vil jeg dog ikke vise den med det samme når brugeren lander på siden, så jeg vil teste de andre 5 tidspunkter.</p>
<p>Jeg har lavet et array med de 5 tidspunkter:</p>
<pre><code class="" data-line="">var randomPageStates = [&quot;scroller&quot;,&quot;oneThird&quot;,&quot;twoThirds&quot;,&quot;endContent&quot;,&quot;purchase&quot;];
</code></pre>
<p>Når brugeren lander på et blogindlæg bruger jeg JavaScript til at generere et tilfældigt tal mellem 0-4.</p>
<pre><code class="" data-line="">var randomPageState = Math.floor(Math.random() * 5);
</code></pre>
<p>Dette tal bruger jeg så til at vælge et af de 5 tidspunkter. Arrays i JavaScript er 0-indexeret, så den første plads er index 0, op til index 4.</p>
<p>Jeg bruger det tilfældige tal til at vælge et tilfældigt index i array&#8217;et, som styrer hvornår min slide-in vises på siden. Jeg tracker også værdien i en Hit-scoped custom dimension, så jeg kan sammenholde det med konvertering og frafald.</p>
<p>Lad os starte med konverteringer.</p>
<h2 id="article-header-id-6">Effekt på tilmelding til nyhedsbrev</h2>
<p>Okay, vi kan lige så godt tage den med det samme. Min slide-in konverterer ikke. Slet ikke.</p>
<div id="attachment_2540" style="width: 870px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2540" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Slide-in-conversion-events-dark-860x435.jpg" alt="22.161 visninger af slide-in og kun 29 tilmeldinger." width="860" height="435" class="size-large wp-image-2540" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Slide-in-conversion-events-dark-860x435.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Slide-in-conversion-events-dark-690x349.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Slide-in-conversion-events-dark-768x389.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Slide-in-conversion-events-dark.jpg 1031w" sizes="auto, (max-width: 860px) 100vw, 860px" /><p id="caption-attachment-2540" class="wp-caption-text">22.161 visninger af slide-in og kun 29 tilmeldinger.</p></div>
<p>Slide-in boxen er i alt blevet vist 22.161 gange og den er blevet lukket 15.490 gange. Men den har kun fået 29 tilmeldinger.</p>
<p>29!</p>
<p>Det er en konverteringsrate på 0,13%.</p>
<p>Men det er også min egen skyld. Jeg sælger slet ikke den tilmelding godt nok. Det er ikke nok bare at give mulighed for at få en mail ved nye blogindlæg.</p>
<p>Det virker meget bedre med en <a href="http://pottercut.dk/emil-kristensen/faa-flere-tilmeldinger-din-nyhedsmail/">Content Upgrade</a>.</p>
<p>Nåh, men det var heller ikke det vi skulle snakke om!</p>
<h2 id="article-header-id-7">Effekt på læsning af blogindlæg</h2>
<p>Jeg vil gerne undersøge om brugerne er mere tilbøjelige til at forlade sitet når min slide-in bliver vist.</p>
<p>I det efterfølgende kigger jeg på konverteringsraten for de enkelte events ned gennem et blogindlæg sammenlignet med detail views som er det samme som sidevisninger på blogindlægget.</p>
<p>Det første jeg kigger på er Add to Cart konverteringsraten, dvs. hvor mange der begynder at scrolle.</p>
<p>Denne er lidt ligeyldig fordi min slide-in tidligst bliver vist på det tidspunkt hvor de rammer Add to Cart. Så den kan faktisk ikke nå at påvirke, men den er god at have med som kontrol.</p>
<p>De fem søjler er de fem tidspunkter slide-in boxen bliver vist på. Ikke overraskende er konverteringsraten næsten den samme for alle grupper.</p>
<div id="attachment_2530" style="width: 1045px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2530" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Add-to-Cart-konvertering.jpg" alt="Ikke overraskende er konverteringsraten næsten den samme for alle grupper." width="1035" height="578" class="size-full wp-image-2530" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Add-to-Cart-konvertering.jpg 1035w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Add-to-Cart-konvertering-690x385.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Add-to-Cart-konvertering-860x480.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Add-to-Cart-konvertering-768x429.jpg 768w" sizes="auto, (max-width: 1035px) 100vw, 1035px" /><p id="caption-attachment-2530" class="wp-caption-text">Ikke overraskende er konverteringsraten næsten den samme for alle grupper.</p></div>
<h3 id="article-header-id-8">Læst 33%</h3>
<p>Det næste event er dem som har scrollet 33% af indlægget og her vil den første gruppe altså have set slide-in boxen, mens de andre ikke har set den endnu.</p>
<div id="attachment_2531" style="width: 1043px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2531" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-33p-konvertering.jpg" alt="Ikke den store forskel på dem der har set slide-in boxen." width="1033" height="580" class="size-full wp-image-2531" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-33p-konvertering.jpg 1033w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-33p-konvertering-690x387.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-33p-konvertering-860x483.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-33p-konvertering-768x431.jpg 768w" sizes="auto, (max-width: 1033px) 100vw, 1033px" /><p id="caption-attachment-2531" class="wp-caption-text">Ikke den store forskel på dem der har set slide-in boxen.</p></div>
<p>Add to Cart har en anelse lavere konverteringsrate end Læst 33% men forskellen er meget lille og med en p-værdi på 0,1572 er den ikke signifikant.</p>
<div id="attachment_2543" style="width: 870px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2543" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/significance-test-860x413.jpg" alt="&lt;a href=&quot;https://www.surveymonkey.com/mp/ab-testing-significance-calculator/&quot;&gt;SurveyMonkey&lt;/a&gt; har en god signifikans test." width="860" height="413" class="size-large wp-image-2543" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/significance-test-860x413.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/significance-test-690x331.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/significance-test-768x368.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/significance-test.jpg 1230w" sizes="auto, (max-width: 860px) 100vw, 860px" /><p id="caption-attachment-2543" class="wp-caption-text"><a href="https://www.surveymonkey.com/mp/ab-testing-significance-calculator/">SurveyMonkey</a> har en god signifikans test.</p></div>
<p>Man kan også se at Læst 100% har en konverteringsrate der er endnu lavere end Add to Cart og Læst 100% har altså ikke set slide-in boxen endnu, så det er bare naturlig varians.</p>
<p>Indtil videre påvirker det altså ikke konverteringsraten.</p>
<h3 id="article-header-id-9">Læst 66%</h3>
<p>Ved 66% læst er der heller ingen markant forskel og faktisk er det de to øverste grupper (som på dette tidspunkt har set slide-in boxen) der har den højeste konvertering.</p>
<div id="attachment_2532" style="width: 1042px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2532" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-66p-konvertering.jpg" alt="Ved 66% læst er der heller ikke forskel." width="1032" height="578" class="size-full wp-image-2532" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-66p-konvertering.jpg 1032w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-66p-konvertering-690x386.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-66p-konvertering-860x482.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-66p-konvertering-768x430.jpg 768w" sizes="auto, (max-width: 1032px) 100vw, 1032px" /><p id="caption-attachment-2532" class="wp-caption-text">Ved 66% læst er der heller ikke forskel.</p></div>
<p>Så stadig ingen påvirkning.</p>
<h3 id="article-header-id-10">Læst 100%</h3>
<p>Ved 100% læst er det dermed de øverste 3 grupper der har fået vist slide-in boxen &#8211; men det har stadig ingen betydning.</p>
<div id="attachment_2533" style="width: 1040px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2533" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-konvertering.jpg" alt="Samme billede ved 100% læst." width="1030" height="577" class="size-full wp-image-2533" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-konvertering.jpg 1030w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-konvertering-690x387.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-konvertering-860x482.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-konvertering-768x430.jpg 768w" sizes="auto, (max-width: 1030px) 100vw, 1030px" /><p id="caption-attachment-2533" class="wp-caption-text">Samme billede ved 100% læst.</p></div>
<p>Videre til sidste event.</p>
<h3 id="article-header-id-11">Læst 100% + 1 minut</h3>
<p>Det sidste event er dem som har scrollet 100% og været på siden mindst 1 minut &#8211; det er dem hvor jeg antager at de faktisk har læst hele blogindlægget (<a href="https://www.jacobworsoe.dk/indhold-enhanced-ecommerce/">og dem jeg tracker som et transaktion i Enhanced Ecommerce</a>).</p>
<div id="attachment_2534" style="width: 1040px" class="wp-caption aligncenter"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2534" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-1-minut-konvertering.jpg" alt="Heller ikke ved 100% læst + 1 minut på siden er der nogen entydig forskel." width="1030" height="577" class="size-full wp-image-2534" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-1-minut-konvertering.jpg 1030w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-1-minut-konvertering-690x387.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-1-minut-konvertering-860x482.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/09/Laest-100p-1-minut-konvertering-768x430.jpg 768w" sizes="auto, (max-width: 1030px) 100vw, 1030px" /><p id="caption-attachment-2534" class="wp-caption-text">Heller ikke ved 100% læst + 1 minut på siden er der nogen entydig forskel.</p></div>
<p>Men heller ikke her er der nogen entydig forskel som skulle indikere at brugerne bliver irriteret af en slide-in og dermed er mere tilbøjelige til at forlade sitet eller mindre tilbøjelige til at læse blogindlægget færdig.</p>
<p>Konklusionen er derfor at min slide-in ikke er irriterende for brugerne &#8211; i hvert fald ikke så meget at de ikke gider læse blogindlægget færdigt.</p>
<h2 id="article-header-id-12">Opsummering</h2>
<p>I dette blogindlæg har jeg brugt Google Analytics og Google Tag Manager til at indsamle det nødvendige data til at teste hypotesen om at slide-ins ødelægger konverteringsraten. Min konklusion gælder ikke for alle sites og alle brancher &#8211; sådan noget skal altid testes på det enkelte site. Men jeg håber at ovenstående kan give noget inspiration til hvordan man kan opstille en hypotese, indsamle den nødvendige data og analysere det, så der kan træffes en beslutning på baggrund af data.</p>
<p>Tilbage er der blot at få lavet en ordentlig content upgrade, så jeg kan lave en slide-in der faktisk kan give nogle tilmeldinger til mit <a href="https://www.jacobworsoe.dk/nyhedsbrev/">nyhedsbrev</a>.</p>

