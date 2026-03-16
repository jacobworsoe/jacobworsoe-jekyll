---
layout: post
title: Tracking af cola med Google Analytics og Flic buttons
date: 2018-07-29 23:50:27
slug: cola-google-analytics-flic-buttons
categories:
  - Analytics
---

Measurement Protocol som kom i Universal Analytics er super fedt, fordi det giver mulighed for at tracke ting som ikke sker på dit website.

Her vil jeg vise dig hvordan man kan bruge det til at tracke "offline" events, som fx når man tager en sodavand i køleskabet.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg" alt="" width="900" height="615" class="alignnone size-full wp-image-1389" /></a>

<h2>Indhold</h2>

<ul>
<li><a href="#article-header-id-0"> 1) Flic knapper kan sende data til Google Analytics</a>

<ul>
<li><a href="#article-header-id-1"> Flic kan kalde en given URL = uendelige muligheder</a></li>
</ul></li>
<li><a href="#article-header-id-2"> 2) Byg Measurement Protocol URL'en som sender data</a></li>
<li><a href="#article-header-id-3"> 3) Validering af den endelige URL</a>

<ul>
<li><a href="#article-header-id-4"> Opsæt Flic knappen til at kalde URL'en</a></li>
<li><a href="#article-header-id-5"> Test af knappen i Real-time Analytics</a></li>
<li><a href="#article-header-id-6"> Se de nye data i Google Analytics</a></li>
</ul></li>
<li><a href="#article-header-id-7"> 4) Dashboard i Data Studio</a>

<ul>
<li><a href="#article-header-id-8"> Der bliver drukket mest cola i weekenden</a></li>
<li><a href="#article-header-id-9"> Kl. 20 er Prime Time for cola</a></li>
<li><a href="#article-header-id-10"> Flic button ved puslebordet?</a></li>
</ul></li>
<li><a href="#article-header-id-11"> Hvor kan man købe Flic buttons?</a></li>
</ul>

For at kunne tracke når nogen tager en sodavand i Google Analytics via deres API, skal der bruges 4 ting:

<ol>
<li>En knap som man trykker på, når man tager en sodavand</li>
<li>En række event data som skal sendes til Google Analytics</li>
<li>En URL man kan kalde, der sender dataene til Google Analytics</li>
<li>En måde at visualisere de opsamlede data på</li>
</ol>

<h2 id="article-header-id-0">1) Flic knapper kan sende data til Google Analytics</h2>

Jeg fik for nyligt en <a href="https://flic.io/flic-hub-3-flics">Flic Hub</a> ind af døren, som seneste nye gadget i mit Smart Home. Med <a href="https://flic.io/">Flic</a> har jeg <a href="https://flic.io/shop/flic-4pack">små knapper</a> rundt omkring i huset til at styre forskellige "smart" dimser, fx mit Philips Hue lys.

[caption id="attachment_1364" align="alignnone" width="620"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-hub.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-hub.jpg" alt="Billede fra: flic.io" width="620" height="350" class="size-full wp-image-1364" /></a> Flic Hub - billede fra: flic.io[/caption]

Vi har en lille knap under sofabordet som kan tænde alle Philips Hue lamper i stuen i forskellige indstillinger, fx dæmpet varmt lys, når der skal ses film.

[caption id="attachment_1365" align="alignnone" width="500"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic_turquoise.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic_turquoise.png" alt="Billede fra: flic.io" width="500" height="500" class="size-full wp-image-1365" /></a> Flic button - billede fra: flic.io[/caption]

Knappen kan tre ting: 1 klik, 2 klik og langt klik.

[caption id="attachment_1372" align="alignnone" width="690"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-690x755.png" alt="1 klik, 2 klik og langt klik - simpelt og nemt." width="690" height="755" class="size-medium wp-image-1372" /></a> 1 klik, 2 klik og langt klik - simpelt og nemt.[/caption]

Hvert klik kan indstilles til at gøre en bestemt ting. Alt fra Spotify, Philips Hue, IFTTT, Slack, Zapier, Chromecast, etc.

Dvs. snakke sammen med en masse forudbestemte services.

<h3 id="article-header-id-1">Flic kan kalde en given URL = uendelige muligheder</h3>

Flic har også muligheden for at kalde en given URL og dermed kan du kalde et hvilket som helst API eller lave dine egne endpoints som kan udføre en hvilken som helst handling - kun fantasien sætter grænser.

[caption id="attachment_1366" align="alignnone" width="690"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request-690x1058.png" alt="Flic kan kalde en URL når man trykker på knappen." width="690" height="1058" class="size-medium wp-image-1366" /></a> Flic kan kalde en URL når man trykker på knappen.[/caption]

Et eksempel på en URL man kan kalde er Google Analytics API - Measurement Protocol - og dermed sende hits til Google Analytics når man klikker på knappen.

<h2 id="article-header-id-2">2) Byg Measurement Protocol URL'en som sender data</h2>

Google Analytics har en super smart <a href="https://ga-dev-tools.appspot.com/hit-builder/">Hit Builder</a> hvor man kan bygge den URL der skal kaldes.

Der findes også en <a href="https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide#commonhits">række eksempler</a> på data man typisk sender, som man kan bruge som udgangspunkt. Her vil jeg sende et Event til Google, når nogen tager en cola.

[caption id="attachment_1367" align="alignnone" width="667"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-build.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-build.png" alt="Eventet bygges nemt i Hit Builder." width="667" height="591" class="size-full wp-image-1367" /></a> Eventet bygges nemt i Hit Builder.[/caption]

Der er en række parametre der skal sættes:

<ul>
<li><strong>TID</strong> er mit Google Analytics property ID</li>
<li><strong>CID</strong> er brugerens cookie ID, hvis eventet skal kobles sammen med noget tidligere online adfærd på websitet. Fx trafikkilde eller landingpage. Her auto-genererer jeg bare et random ID</li>
<li><strong>ec</strong> er Event Category og sættes til "Køleskab"</li>
<li><strong>ea</strong> er Event Action og sættes til det man tager i køleskabet</li>
<li><strong>el</strong> er Event Label og sættes til personen der tager noget i køleskabet</li>
<li><strong>ev</strong> er Event Value og sættes her til 330ml i en dåsecola.</li>
</ul>

<h2 id="article-header-id-3">3) Validering af den endelige URL</h2>

Hit Builder kan validere den endelige URL og tjekke om alle værdier er udfyldt korrekt.

[caption id="attachment_1371" align="alignnone" width="929"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit.png" alt="Hit Builder gør det nemt at tjekke om et hit indeholder de korrekte værdier." width="929" height="507" class="size-full wp-image-1371" /></a> Hit Builder gør det nemt at tjekke om et hit indeholder de korrekte værdier.[/caption]

Den endelige URL som skal kaldes fåes ved at sætte <code>https://www.google-analytics.com/collect?</code> foran den URL (Hit Payload) som Hit Builder genererer.

Dermed fås denne URL:
<code>https://www.google-analytics.com/collect?v=1&amp;t=event&amp;tid=UA-12345-1&amp;cid=5b3393c6-dbf2-4e60-a912-c30d7df10f0e&amp;ec=K%C3%B8leskab&amp;ea=Pepsi%20Max&amp;el=Jacob&amp;ev=330</code>

<h3 id="article-header-id-4">Opsæt Flic knappen til at kalde URL'en</h3>

Jeg laver i alt tre URL'er til de tre ting knappen kan:

<ul>
<li><strong>1 klik:</strong> Tina tager en cola</li>
<li><strong>2 klik:</strong> Jacob tager en cola</li>
<li><strong>Langt klik:</strong> Fælles cola til deling</li>
</ul>

Inde i app'en sætter jeg de tre URL'er:

[caption id="attachment_1373" align="alignnone" width="690"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured-690x1045.png" alt="Hver type klik kalder en bestemt URL, som sender de korrekte event data." width="690" height="1045" class="size-medium wp-image-1373" /></a> Hver type klik kalder en bestemt URL, som sender de korrekte event data.[/caption]

<h3 id="article-header-id-5">Test af knappen i Real-time Analytics</h3>

Så skal der testes!

<div class="videoWrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/T5jUCwHyr1U" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

1 klik, 2 klik, langt klik.

Og så skal knappen bare monteres, så man husker at trykke, når man tager en sodavand.

[caption id="attachment_1375" align="alignnone" width="900"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab.jpg" alt="Flic knappen er rimelig diskret og kan let placeres alle mulige steder." width="900" height="615" class="size-full wp-image-1375" /></a> Flic knappen er rimelig diskret og kan let placeres alle mulige steder.[/caption]

<h3 id="article-header-id-6">Se de nye data i Google Analytics</h3>

Derefter kan følgende data ses i Google Analytics.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report.png" alt="" width="1352" height="378" class="alignnone size-full wp-image-1359" /></a>

Meget sjovt, men lidt federe hvis vi tilføjer lidt grafer.

<h2 id="article-header-id-7">4) Dashboard i Data Studio</h2>

Ved at udnytte de indbyggede dimensioner i Google Analytics til at bryde Events op på timer og dage, kan man se hvornår på ugen og døgnet vi er mest tilbøjelige til at snuppe en kold cola.

[caption id="attachment_1376" align="alignnone" width="279"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-data-studio-dimensions-metrics-sorting.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-data-studio-dimensions-metrics-sorting.png" alt="Dimensioner, metrics og sortering i Data Studio." width="279" height="532" class="size-full wp-image-1376" /></a> Dimensioner, metrics og sortering i Data Studio.[/caption]

Bemærk at "Total events" på engelsk hedder "Al aktivitet" på dansk. Ikke den bedste oversættelse.

<h3 id="article-header-id-8">Der bliver drukket mest cola i weekenden</h3>

Men der har været sommerferie, så grafen er ikke helt retvisende endnu - men den opdateres automatisk med nye data, så kig endelig forbi igen om et par uger.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage.png" alt="" width="1371" height="820" class="alignnone size-full wp-image-1914" /></a>

<h3 id="article-header-id-9">Kl. 20 er Prime Time for cola</h3>

Det er tydeligt at behovet for en kold cola peaker når vores datter er puttet og der skal slappes af i sofaen.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet.png" alt="" width="1377" height="845" class="alignnone size-full wp-image-1913" /></a>

Og hvad skal man så se i fjernsynet, når man ligger på sofaen? Man kunne jo Chromecaste dashboardet fra Data Studio til TV'et.

[caption id="attachment_1363" align="alignnone" width="900"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard.jpg" alt="Data Studio dashboard på TV via Google Chromecast." width="900" height="506" class="size-full wp-image-1363" /></a> Data Studio dashboard på TV via Google Chromecast.[/caption]

<h3 id="article-header-id-10">Flic button ved puslebordet?</h3>

Jeg elsker at indsamle data til at træffe beslutninger (eller afgøre væddemål). Derfor har vi naturligvis også en Flic button ved puslebordet.

[caption id="attachment_1378" align="alignnone" width="900"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord.jpg" alt="Flic button ved puslebordet." width="900" height="506" class="size-full wp-image-1378" /></a> Flic button ved puslebordet.[/caption]

Så skulle den diskussion være afgjort - desværre ikke til min fordel :)

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner.png" alt="" width="1382" height="830" class="alignnone size-full wp-image-1912" /></a>

<h2 id="article-header-id-11">Hvor kan man købe Flic buttons?</h2>

Flic knapper <a href="https://www.partner-ads.com/dk/klikbanner.php?partnerid=16938&bannerid=48783&htmlurl=https://wifi-butikken.dk/produkt-kategori/flic/">kan købes separat</a> og skal kobles sammen med din telefon eller tablet via Bluetooth for at sende data. Det giver nogle udfordringer som <a href="http://www.gizmodo.co.uk/2018/05/flic-hub-fixes-the-one-big-problem-with-the-original-flic-buttons/">Gizmodo har beskrevet her</a> - fx kræver det at din telefon altid er i nærheden, hvilket ikke er så smart i et privat hjem. Flic har derfor lanceret en Flic Hub, som knapperne kobles sammen med, så det ikke er afhængigt af at din telefon er i nærheden. Jeg købte min Flic Hub gennem en <a href="https://www.indiegogo.com/projects/flic-hub-simplify-home-control-with-smart-buttons#/">Indiegogo kampagne</a> og så vidt jeg kan se kan Flic Hub ikke købes i danske webshops endnu, men kun via <a href="https://flic.io/flic-hub-3-flics">Flics egen webshop</a>.

Bonus: Jeg har tidligere skrevet om hvordan man kan bruge Measurement Protocol til at <a href="https://www.jacobworsoe.dk/6-google-analytics-hacks-og-de-fede-data-de-giver/#send-data-forsinket">tracke transaktioner efter brugerne har forladt sitet</a> og til at <a href="https://www.jacobworsoe.dk/6-google-analytics-hacks-og-de-fede-data-de-giver/#send-hemmelige-data">sende hemmelige data (fx din avance)</a> til Google Analytics, uden at brugerne kan se din avance.