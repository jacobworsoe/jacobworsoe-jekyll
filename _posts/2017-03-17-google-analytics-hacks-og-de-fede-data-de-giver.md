---
layout: post
title: 6 Google Analytics hacks (og de fede data de giver)
date: 2017-03-17 20:50:11
slug: google-analytics-hacks-og-de-fede-data-de-giver
wordpress_id: 1031
categories:
  - Analytics
---

Google Analytics skal hackes. Punktum!

Google Analytics er et one-size-fits-all værktøj der skal kunne bruges på mange forskellige websites. Det har masser af fede features hvis man er en webshop, men hvis man ikke lige har et standard website, så skal der tænkes lidt kreativt, for at udnytte potentialet i Google Analytics.

Der er guld at hente ved at tilpasse værktøjet til det enkelte website og ikke bare nøjes med standardimplementeringen.

Man skal bare lige vide hvordan de forskellige dimensioner og metrics udregnes og påvirker hinanden, så kan man lave noget rigtig fedt.

På <a href="https://www.exchangemycoins.com/">ExchangeMyCoins.com</a> kan man veksle Bitcoins og andre digitale valuter og passer dermed ikke lige umiddelbart ned i standardrapporterne. Her vil jeg derfor vise dig hvordan vi har brugt Google Analytics kreativt og får en masse værdifuld viden om adfærden på websitet.

<h2>1. Tracking af CTR for dine Call-to-Actions</h2>

Vi bruger det fantastiske Enhanced Ecommerce i Universal Analytics til at tracke alle Call-to-Action knapper som Internal Promotions, så vi kan se hvor mange gange de er vist og klikket på, så vi får en CTR for hver knap. Det er guld værd og giver meget bedre data, end hvis vi blot tracker kliks som et Event uden at sammenholde det med antal visninger.

Visninger trackes sådan her, og sendes til Google Analytics med et Event. Husk at sætte det som non-interaction, så det ikke ødelægger din bounce-rate.

<pre class="prettyprint" rel="JavaScript"><code class="language-javascript">ga('require', 'ec');
ga('ec:addPromo', {
   'id': promotionName,
   'name': promotionName,
   'creative': promotionName,
   'position': '1'
});
ga('send', 'event', 'Internal Promotions', 'view', promotionName, {
   nonInteraction: true
});
</code></pre>

Kliks trackes næsten på samme måde, det skal bare aktiveres når man klikker på knappen/billedet. Se mere i <a href="https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce">Googles dokumentation her</a>.

Derved kan vi fx nemt se performance for vores primære Call-to-Action på forsiden, som ser således ud:

<a href="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta.png" alt="" width="869" height="425" class="alignnone size-full wp-image-1038" /></a>

I rapporten i Google Analytics hedder den "Start here" ligesom teksten på knappen og har en CTR på 34,96%. Godt at vide at den primære CTA bliver brugt ofte!

<a href="https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2.png" alt="" width="1267" height="543" class="alignnone size-full wp-image-1080" /></a>

Subscribe knappen i footeren bliver næsten ikke brugt og har kun en CTR på 0,09%. Som forventet vil jeg næsten sige, men det kræver data at få det bekræftet.

På kvitteringssiden opfordrer vi kunderne til at lave et review på facebook. Det er der cirka 2% der gør. Det har jeg skrevet meget mere om her: <a href="https://www.jacobworsoe.dk/skab-vaerdifulde-konverteringer-paa-kvitteringssiden/">Skab værdifulde konverteringer på kvitteringssiden</a>.

Breaking News var en nyheds-ribbon vi havde på forsiden med et tekstlink som linkede videre. Den har en CTR på 3% og dermed slet ikke samme CTR som vores CTA-knapper. "Start Exchange here >" er fx en CTA-knap på en landingpage og har en CTR på 18%. Igen er det ikke overraskende at knapper er bedre end tekstlinks, men det er bare så fedt at få noget data på det!

Vi har Call-to-Actions på alle vores landingpages som fx <a href="https://www.exchangemycoins.com/pages/buy-bitcoins-with-usd">den her</a> eller <a href="https://www.exchangemycoins.com/pages/exchange-bitcoins-paypal">den her</a>.

Med disse data kan vi også nemt se hvor godt de performer og CTR gør det super nemt at sammenligne sider med vidt forskellige antal visninger og kliks.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance.png" alt="" width="1236" height="307" class="alignnone size-full wp-image-1047" /></a>

<h2 id="send-data-forsinket">2. Send data forsinket</h2>

Med Universal Analytics lancerede Google også et API til Google Analytics, kaldet Measurement Protocol, som kan bruges til at sende data til Google Analytics, direkte fra serveren. Mulighederne er mange, men i vores tilfælde giver det primært to fordele: Hemmelige data og forsinket data.

Når man veksler Bitcoins, kan der gå op til 60 minutter før vekslingen er endelig bekræftet og ikke kan annulleres - sådan er det med Bitcoin, men det giver en tydelig udfordring med tracking af vekslingen.

Hvis brugeren ikke længere er aktiv på sitet eller har forladt sitet, vil vekslingen stadig blive gennemført, men vi har ikke længere brugerens browser til at sende data til Google Analytics for os.

Men med Measurement Protocol er vi ikke afhængig af at brugeren udfører en handling på websitet, for at kunne tracke det. Når vekslingen er færdig sender serveren selv data direkte til Google.

Vi gemmer værdien af brugerens Google Analytics cookie når de starter vekslingen, så vi kan sende den med, når vi sender data til Google. Dermed bliver transaktionen koblet sammen med brugerens session og vi kan dermed stadig se trafikkilden og lignende, præcis som hvis brugerens browser havde sendt transaktionen til Google. Skide smart!

<h2 id="send-hemmelige-data">3. Send hemmelige data til Google Analytics</h2>

Normalt bliver alle data sendt til Google Analytics via JavaScript som kører på klienten. Dvs. alt hvad du sender til Google Analytics har brugeren i princippet mulighed for at se. Når man sender data direkte fra serveren til Google, kan brugeren ikke se de data man sender. Og dermed kan man sende hemmelige forretningsdata til Google Analytics.

Fx avance på ordre, så du kan udregne en mere præcis fortjeneste på dine Adwords kampagner, direkte i Google Analytics.

Som sagt så skal Google Analytics hackes. Google Analytics har ikke et datafelt til at gemme avance, men de har en felt til moms. Vi regner ikke med moms, så det felt kan vi passende bruge til at tracke avance.

<h2>4. Udregn din avanceprocent direkte i Google Analytics</h2>

Vi bruger Calculated Metrics til at udregne vores avanceprocent direkte i Google Analytics.

<strong>Pro tip:</strong> Vidste du at Calculated Metrics også virker på historiske data? Ikke kun fremadrettet.

Vi har lavet en Calculated Metric som udregner vores avanceprocent med denne udregning: <em>&#123;&#123;Tax&#125;&#125; / &#123;&#123;Revenue&#125;&#125;</em>

<a href="https://www.jacobworsoe.dk/wp-content/uploads/calculated-metric-profit-rate.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/calculated-metric-profit-rate.png" alt="" width="402" height="500" class="alignnone size-full wp-image-1041" /></a>

Dermed kan vi nemt få et overblik over hvordan vores avanceprocent udvikler sig over tid. Og ved at have det i Google Analytics, kan vi nemt segmentere det på trafikkilde, landingpages, etc.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph.png" alt="" width="1517" height="307" class="alignnone size-full wp-image-1095" /></a>

<h2>5. Hvilke produkter performer bedst?</h2>

Kunderne kan veksle mellem flere forskellige digitale valutaer, så vi bruger Enhanced Ecommerce til at få et unikt indblik i hvilke der oftest bliver kigget på, samt hvilke kunderne oftest veksler.

Når en bruger vælger to valutaer i formularen på forsiden, viser vi kursen mellem de to valutaer:

<a href="https://www.jacobworsoe.dk/wp-content/uploads/bitcoin-to-litecoin-exchange-dropdown.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/bitcoin-to-litecoin-exchange-dropdown.png" alt="" width="729" height="222" class="alignnone size-full wp-image-1050" /></a>

Dette tracker vi som en produktdetaljevisning, altså det der svarer til at brugeren ser en produktside på en webshop. Dette gøres med følgende JavaScript:

<pre class="prettyprint" rel="JavaScript"><code class="language-javascript">ga('require', 'ec');

ga('ec:addProduct', {
   'id': ga_ProductName,
   'name': ga_ProductName,
   'category': ga_Category,
   'brand': '',
   'variant': ''
});

ga('ec:setAction', 'detail');
ga('send', 'event', 'Ecommerce', 'Product view', ga_ProductName);
</code></pre>

Når brugeren går igang med vekslingen, tracker vi at produktet er lagt i kurven.

Og når brugeren gennemfører vekslingen, registrerer vi at produktet er købt. Det er det vi gør server-side, som beskrevet ovenfor.

Derved har vi et fuldt overblik over produkterne, hele vejen gennem websitet:

[caption id="attachment_1085" align="alignnone" width="1714"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance.png" alt="Se også de to sidste kolonner med rates som gør produkterne sammenlignelige!" width="1714" height="728" class="size-full wp-image-1085" /></a> Se også de to sidste kolonner med rates som gør produkterne sammenlignelige![/caption]

Bemærk især de to sidste kolonner herover, som viser hvor tit produkterne lægges i kurv og købes i forhold til hvor tit de bliver set ude på forsiden. Med de to tal, kan vi meget nemt se hvilke produkter vi har en god og mindre god vekselkurs på.

Vi får også en overskuelig oversigt over frafaldet på hvert trin i købsrejsen gennem sitet:

[caption id="attachment_1158" align="alignnone" width="837"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior.png" alt="39% af alle besøg ser produkter og 25% af dem lægger et produkt i kurven." width="837" height="481" class="size-full wp-image-1158" /></a> 39% af alle besøg ser produkter og 25% af dem lægger et produkt i kurven.[/caption]

<h2>6. Mest populære FAQ spørgsmål</h2>

Fra starten har vi haft fokus på at lave alting så automatisk som muligt. Hver gang vi modtager et generelt spørgsmål på vores supportmail, opretter vi en FAQ på spørgsmålet, så vi ikke skal bruge tid på at svare på de samme spørgsmål igen og igen. Vi har derfor en grundig FAQ sektion og vi tracker selvfølgelig hvilke FAQ spørgsmål der er mest populære.

[caption id="attachment_1076" align="alignnone" width="997"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq.png" alt="En del af FAQ sektionen på sitet." width="997" height="653" class="size-full wp-image-1076" /></a> En del af FAQ sektionen på sitet.[/caption]

Med følgende simple kode tracker vi automatisk alle klik på FAQ spørgsmål. Koden tager ankerteksten og sender som Event til Google Analytics.

<pre class="prettyprint" rel="JavaScript"><code class="language-javascript">$("a[href^='#faq-']").on("click", function () {
        var anchorText = $(this).text();
        ga('send', 'event', 'FAQ click', anchorText);
    });
</code></pre>

Voila!

[caption id="attachment_1074" align="alignnone" width="1067"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq.png" alt="De mest populære FAQ spørgsmål på sitet." width="1067" height="554" class="size-full wp-image-1074" /></a> De mest populære FAQ spørgsmål på sitet.[/caption]

Så standardrapporterne kan sagtens bruges, selvom man ikke er en webshop! De skal bare hackes lidt.