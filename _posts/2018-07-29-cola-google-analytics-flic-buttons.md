---
layout: post
title: Tracking af cola med Google Analytics og Flic buttons
date: 2018-07-29 23:50:27
slug: cola-google-analytics-flic-buttons
categories:
  - Analytics
---

<p>Measurement Protocol som kom i Universal Analytics er super fedt, fordi det giver mulighed for at tracke ting som ikke sker på dit website.</p>
<p>Her vil jeg vise dig hvordan man kan bruge det til at tracke &#8220;offline&#8221; events, som fx når man tager en sodavand i køleskabet.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg" alt="" width="900" height="615" class="alignnone size-full wp-image-1389" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg 900w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-690x472.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-768x525.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-725x495.jpg 725w" sizes="auto, (max-width: 900px) 100vw, 900px" /></a></p>
<h2>Indhold</h2>
<ul>
<li><a href="#article-header-id-0"> 1) Flic knapper kan sende data til Google Analytics</a>
<ul>
<li><a href="#article-header-id-1"> Flic kan kalde en given URL = uendelige muligheder</a></li>
</ul>
</li>
<li><a href="#article-header-id-2"> 2) Byg Measurement Protocol URL&#8217;en som sender data</a></li>
<li><a href="#article-header-id-3"> 3) Validering af den endelige URL</a>
<ul>
<li><a href="#article-header-id-4"> Opsæt Flic knappen til at kalde URL&#8217;en</a></li>
<li><a href="#article-header-id-5"> Test af knappen i Real-time Analytics</a></li>
<li><a href="#article-header-id-6"> Se de nye data i Google Analytics</a></li>
</ul>
</li>
<li><a href="#article-header-id-7"> 4) Dashboard i Data Studio</a>
<ul>
<li><a href="#article-header-id-8"> Der bliver drukket mest cola i weekenden</a></li>
<li><a href="#article-header-id-9"> Kl. 20 er Prime Time for cola</a></li>
<li><a href="#article-header-id-10"> Flic button ved puslebordet?</a></li>
</ul>
</li>
<li><a href="#article-header-id-11"> Hvor kan man købe Flic buttons?</a></li>
</ul>
<p>For at kunne tracke når nogen tager en sodavand i Google Analytics via deres API, skal der bruges 4 ting:</p>
<ol>
<li>En knap som man trykker på, når man tager en sodavand</li>
<li>En række event data som skal sendes til Google Analytics</li>
<li>En URL man kan kalde, der sender dataene til Google Analytics</li>
<li>En måde at visualisere de opsamlede data på</li>
</ol>
<h2 id="article-header-id-0">1) Flic knapper kan sende data til Google Analytics</h2>
<p>Jeg fik for nyligt en <a href="https://flic.io/flic-hub-3-flics">Flic Hub</a> ind af døren, som seneste nye gadget i mit Smart Home. Med <a href="https://flic.io/">Flic</a> har jeg <a href="https://flic.io/shop/flic-4pack">små knapper</a> rundt omkring i huset til at styre forskellige &#8220;smart&#8221; dimser, fx mit Philips Hue lys.</p>
<div id="attachment_1364" style="width: 630px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-hub.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1364" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-hub.jpg" alt="Billede fra: flic.io" width="620" height="350" class="size-full wp-image-1364" /></a><p id="caption-attachment-1364" class="wp-caption-text">Flic Hub &#8211; billede fra: flic.io</p></div>
<p>Vi har en lille knap under sofabordet som kan tænde alle Philips Hue lamper i stuen i forskellige indstillinger, fx dæmpet varmt lys, når der skal ses film.</p>
<div id="attachment_1365" style="width: 510px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic_turquoise.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1365" src="https://www.jacobworsoe.dk/wp-content/uploads/flic_turquoise.png" alt="Billede fra: flic.io" width="500" height="500" class="size-full wp-image-1365" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic_turquoise.png 500w, https://www.jacobworsoe.dk/wp-content/uploads/flic_turquoise-300x300.png 300w" sizes="auto, (max-width: 500px) 100vw, 500px" /></a><p id="caption-attachment-1365" class="wp-caption-text">Flic button &#8211; billede fra: flic.io</p></div>
<p>Knappen kan tre ting: 1 klik, 2 klik og langt klik.</p>
<div id="attachment_1372" style="width: 700px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1372" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-690x755.png" alt="1 klik, 2 klik og langt klik - simpelt og nemt." width="690" height="755" class="size-medium wp-image-1372" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-690x755.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-725x794.png 725w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events.png 750w" sizes="auto, (max-width: 690px) 100vw, 690px" /></a><p id="caption-attachment-1372" class="wp-caption-text">1 klik, 2 klik og langt klik &#8211; simpelt og nemt.</p></div>
<p>Hvert klik kan indstilles til at gøre en bestemt ting. Alt fra Spotify, Philips Hue, IFTTT, Slack, Zapier, Chromecast, etc.</p>
<p>Dvs. snakke sammen med en masse forudbestemte services.</p>
<h3 id="article-header-id-1">Flic kan kalde en given URL = uendelige muligheder</h3>
<p>Flic har også muligheden for at kalde en given URL og dermed kan du kalde et hvilket som helst API eller lave dine egne endpoints som kan udføre en hvilken som helst handling &#8211; kun fantasien sætter grænser.</p>
<div id="attachment_1366" style="width: 700px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1366" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request-690x1058.png" alt="Flic kan kalde en URL når man trykker på knappen." width="690" height="1058" class="size-medium wp-image-1366" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request-690x1058.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request-725x1112.png 725w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-internet-request.png 750w" sizes="auto, (max-width: 690px) 100vw, 690px" /></a><p id="caption-attachment-1366" class="wp-caption-text">Flic kan kalde en URL når man trykker på knappen.</p></div>
<p>Et eksempel på en URL man kan kalde er Google Analytics API &#8211; Measurement Protocol &#8211; og dermed sende hits til Google Analytics når man klikker på knappen.</p>
<h2 id="article-header-id-2">2) Byg Measurement Protocol URL&#8217;en som sender data</h2>
<p>Google Analytics har en super smart <a href="https://ga-dev-tools.appspot.com/hit-builder/">Hit Builder</a> hvor man kan bygge den URL der skal kaldes.</p>
<p>Der findes også en <a href="https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide#commonhits">række eksempler</a> på data man typisk sender, som man kan bruge som udgangspunkt. Her vil jeg sende et Event til Google, når nogen tager en cola.</p>
<div id="attachment_1367" style="width: 677px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-build.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1367" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-build.png" alt="Eventet bygges nemt i Hit Builder." width="667" height="591" class="size-full wp-image-1367" /></a><p id="caption-attachment-1367" class="wp-caption-text">Eventet bygges nemt i Hit Builder.</p></div>
<p>Der er en række parametre der skal sættes:</p>
<ul>
<li><strong>TID</strong> er mit Google Analytics property ID</li>
<li><strong>CID</strong> er brugerens cookie ID, hvis eventet skal kobles sammen med noget tidligere online adfærd på websitet. Fx trafikkilde eller landingpage. Her auto-genererer jeg bare et random ID</li>
<li><strong>ec</strong> er Event Category og sættes til &#8220;Køleskab&#8221;</li>
<li><strong>ea</strong> er Event Action og sættes til det man tager i køleskabet</li>
<li><strong>el</strong> er Event Label og sættes til personen der tager noget i køleskabet</li>
<li><strong>ev</strong> er Event Value og sættes her til 330ml i en dåsecola.</li>
</ul>
<h2 id="article-header-id-3">3) Validering af den endelige URL</h2>
<p>Hit Builder kan validere den endelige URL og tjekke om alle værdier er udfyldt korrekt.</p>
<div id="attachment_1371" style="width: 939px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1371" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit.png" alt="Hit Builder gør det nemt at tjekke om et hit indeholder de korrekte værdier." width="929" height="507" class="size-full wp-image-1371" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit.png 929w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit-690x377.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit-768x419.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-event-validate-hit-725x396.png 725w" sizes="auto, (max-width: 929px) 100vw, 929px" /></a><p id="caption-attachment-1371" class="wp-caption-text">Hit Builder gør det nemt at tjekke om et hit indeholder de korrekte værdier.</p></div>
<p>Den endelige URL som skal kaldes fåes ved at sætte <code class="" data-line="">https://www.google-analytics.com/collect?</code> foran den URL (Hit Payload) som Hit Builder genererer.</p>
<p>Dermed fås denne URL:<br />
<code class="" data-line="">https://www.google-analytics.com/collect?v=1&amp;t=event&amp;tid=UA-12345-1&amp;cid=5b3393c6-dbf2-4e60-a912-c30d7df10f0e&amp;ec=K%C3%B8leskab&amp;ea=Pepsi%20Max&amp;el=Jacob&amp;ev=330</code></p>
<h3 id="article-header-id-4">Opsæt Flic knappen til at kalde URL&#8217;en</h3>
<p>Jeg laver i alt tre URL&#8217;er til de tre ting knappen kan:</p>
<ul>
<li><strong>1 klik:</strong> Tina tager en cola</li>
<li><strong>2 klik:</strong> Jacob tager en cola</li>
<li><strong>Langt klik:</strong> Fælles cola til deling</li>
</ul>
<p>Inde i app&#8217;en sætter jeg de tre URL&#8217;er:</p>
<div id="attachment_1373" style="width: 700px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1373" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured-690x1045.png" alt="Hver type klik kalder en bestemt URL, som sender de korrekte event data." width="690" height="1045" class="size-medium wp-image-1373" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured-690x1045.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured-725x1098.png 725w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-three-button-events-configured.png 750w" sizes="auto, (max-width: 690px) 100vw, 690px" /></a><p id="caption-attachment-1373" class="wp-caption-text">Hver type klik kalder en bestemt URL, som sender de korrekte event data.</p></div>
<h3 id="article-header-id-5">Test af knappen i Real-time Analytics</h3>
<p>Så skal der testes!</p>
<div class="videoWrapper">
<iframe loading="lazy" width="560" height="315" src="https://www.youtube.com/embed/T5jUCwHyr1U" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>
<p>1 klik, 2 klik, langt klik.</p>
<p>Og så skal knappen bare monteres, så man husker at trykke, når man tager en sodavand.</p>
<div id="attachment_1375" style="width: 910px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1375" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab.jpg" alt="Flic knappen er rimelig diskret og kan let placeres alle mulige steder." width="900" height="615" class="size-full wp-image-1375" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab.jpg 900w, https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab-690x472.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab-768x525.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-button-koeleskab-725x495.jpg 725w" sizes="auto, (max-width: 900px) 100vw, 900px" /></a><p id="caption-attachment-1375" class="wp-caption-text">Flic knappen er rimelig diskret og kan let placeres alle mulige steder.</p></div>
<h3 id="article-header-id-6">Se de nye data i Google Analytics</h3>
<p>Derefter kan følgende data ses i Google Analytics.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report.png" alt="" width="1352" height="378" class="alignnone size-full wp-image-1359" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report.png 1352w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report-690x193.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report-768x215.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-google-analytics-event-report-725x203.png 725w" sizes="auto, (max-width: 1352px) 100vw, 1352px" /></a></p>
<p>Meget sjovt, men lidt federe hvis vi tilføjer lidt grafer.</p>
<h2 id="article-header-id-7">4) Dashboard i Data Studio</h2>
<p>Ved at udnytte de indbyggede dimensioner i Google Analytics til at bryde Events op på timer og dage, kan man se hvornår på ugen og døgnet vi er mest tilbøjelige til at snuppe en kold cola.</p>
<div id="attachment_1376" style="width: 289px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-data-studio-dimensions-metrics-sorting.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1376" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-data-studio-dimensions-metrics-sorting.png" alt="Dimensioner, metrics og sortering i Data Studio." width="279" height="532" class="size-full wp-image-1376" /></a><p id="caption-attachment-1376" class="wp-caption-text">Dimensioner, metrics og sortering i Data Studio.</p></div>
<p>Bemærk at &#8220;Total events&#8221; på engelsk hedder &#8220;Al aktivitet&#8221; på dansk. Ikke den bedste oversættelse.</p>
<h3 id="article-header-id-8">Der bliver drukket mest cola i weekenden</h3>
<p>Men der har været sommerferie, så grafen er ikke helt retvisende endnu &#8211; men den opdateres automatisk med nye data, så kig endelig forbi igen om et par uger.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage.png" alt="" width="1371" height="820" class="alignnone size-full wp-image-1914" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage.png 1371w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage-690x413.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage-768x459.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-ugedage-725x434.png 725w" sizes="auto, (max-width: 1371px) 100vw, 1371px" /></a></p>
<h3 id="article-header-id-9">Kl. 20 er Prime Time for cola</h3>
<p>Det er tydeligt at behovet for en kold cola peaker når vores datter er puttet og der skal slappes af i sofaen.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet.png" alt="" width="1377" height="845" class="alignnone size-full wp-image-1913" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet.png 1377w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet-690x423.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet-768x471.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-cola-fordelt-på-døgnet-725x445.png 725w" sizes="auto, (max-width: 1377px) 100vw, 1377px" /></a></p>
<p>Og hvad skal man så se i fjernsynet, når man ligger på sofaen? Man kunne jo Chromecaste dashboardet fra Data Studio til TV&#8217;et.</p>
<div id="attachment_1363" style="width: 910px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1363" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard.jpg" alt="Data Studio dashboard på TV via Google Chromecast." width="900" height="506" class="size-full wp-image-1363" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard.jpg 900w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard-690x388.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard-768x432.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-chromecast-dashboard-725x408.jpg 725w" sizes="auto, (max-width: 900px) 100vw, 900px" /></a><p id="caption-attachment-1363" class="wp-caption-text">Data Studio dashboard på TV via Google Chromecast.</p></div>
<h3 id="article-header-id-10">Flic button ved puslebordet?</h3>
<p>Jeg elsker at indsamle data til at træffe beslutninger (eller afgøre væddemål). Derfor har vi naturligvis også en Flic button ved puslebordet.</p>
<div id="attachment_1378" style="width: 910px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1378" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord.jpg" alt="Flic button ved puslebordet." width="900" height="506" class="size-full wp-image-1378" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord.jpg 900w, https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord-690x388.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord-768x432.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-button-puslebord-725x408.jpg 725w" sizes="auto, (max-width: 900px) 100vw, 900px" /></a><p id="caption-attachment-1378" class="wp-caption-text">Flic button ved puslebordet.</p></div>
<p>Så skulle den diskussion være afgjort &#8211; desværre ikke til min fordel :)</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner.png" alt="" width="1382" height="830" class="alignnone size-full wp-image-1912" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner.png 1382w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner-690x414.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner-768x461.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2018/07/Google-data-studio-bleskift-fordelt-på-personner-725x435.png 725w" sizes="auto, (max-width: 1382px) 100vw, 1382px" /></a></p>
<h2 id="article-header-id-11">Hvor kan man købe Flic buttons?</h2>
<p>Flic knapper <a href="https://www.partner-ads.com/dk/klikbanner.php?partnerid=16938&#038;bannerid=48783&#038;htmlurl=https://wifi-butikken.dk/produkt-kategori/flic/">kan købes separat</a> og skal kobles sammen med din telefon eller tablet via Bluetooth for at sende data. Det giver nogle udfordringer som <a href="http://www.gizmodo.co.uk/2018/05/flic-hub-fixes-the-one-big-problem-with-the-original-flic-buttons/">Gizmodo har beskrevet her</a> &#8211; fx kræver det at din telefon altid er i nærheden, hvilket ikke er så smart i et privat hjem. Flic har derfor lanceret en Flic Hub, som knapperne kobles sammen med, så det ikke er afhængigt af at din telefon er i nærheden. Jeg købte min Flic Hub gennem en <a href="https://www.indiegogo.com/projects/flic-hub-simplify-home-control-with-smart-buttons#/">Indiegogo kampagne</a> og så vidt jeg kan se kan Flic Hub ikke købes i danske webshops endnu, men kun via <a href="https://flic.io/flic-hub-3-flics">Flics egen webshop</a>.</p>
<p>Bonus: Jeg har tidligere skrevet om hvordan man kan bruge Measurement Protocol til at <a href="https://www.jacobworsoe.dk/6-google-analytics-hacks-og-de-fede-data-de-giver/#send-data-forsinket">tracke transaktioner efter brugerne har forladt sitet</a> og til at <a href="https://www.jacobworsoe.dk/6-google-analytics-hacks-og-de-fede-data-de-giver/#send-hemmelige-data">sende hemmelige data (fx din avance)</a> til Google Analytics, uden at brugerne kan se din avance.</p>

