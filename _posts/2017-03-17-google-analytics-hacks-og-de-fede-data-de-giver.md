---
layout: post
title: 6 Google Analytics hacks (og de fede data de giver)
date: 2017-03-17 20:50:11
slug: google-analytics-hacks-og-de-fede-data-de-giver
categories:
  - Analytics
---

<p>Google Analytics skal hackes. Punktum!</p>
<p>Google Analytics er et one-size-fits-all værktøj der skal kunne bruges på mange forskellige websites. Det har masser af fede features hvis man er en webshop, men hvis man ikke lige har et standard website, så skal der tænkes lidt kreativt, for at udnytte potentialet i Google Analytics.</p>
<p>Der er guld at hente ved at tilpasse værktøjet til det enkelte website og ikke bare nøjes med standardimplementeringen.</p>
<p>Man skal bare lige vide hvordan de forskellige dimensioner og metrics udregnes og påvirker hinanden, så kan man lave noget rigtig fedt.</p>
<p>På <a href="https://www.exchangemycoins.com/">ExchangeMyCoins.com</a> kan man veksle Bitcoins og andre digitale valuter og passer dermed ikke lige umiddelbart ned i standardrapporterne. Her vil jeg derfor vise dig hvordan vi har brugt Google Analytics kreativt og får en masse værdifuld viden om adfærden på websitet.</p>
<h2>1. Tracking af CTR for dine Call-to-Actions</h2>
<p>Vi bruger det fantastiske Enhanced Ecommerce i Universal Analytics til at tracke alle Call-to-Action knapper som Internal Promotions, så vi kan se hvor mange gange de er vist og klikket på, så vi får en CTR for hver knap. Det er guld værd og giver meget bedre data, end hvis vi blot tracker kliks som et Event uden at sammenholde det med antal visninger.</p>
<p>Visninger trackes sådan her, og sendes til Google Analytics med et Event. Husk at sætte det som non-interaction, så det ikke ødelægger din bounce-rate.</p>
<pre class="prettyprint" rel="JavaScript"><code class="" data-line="">ga(&#039;require&#039;, &#039;ec&#039;);
ga(&#039;ec:addPromo&#039;, {
   &#039;id&#039;: promotionName,
   &#039;name&#039;: promotionName,
   &#039;creative&#039;: promotionName,
   &#039;position&#039;: &#039;1&#039;
});
ga(&#039;send&#039;, &#039;event&#039;, &#039;Internal Promotions&#039;, &#039;view&#039;, promotionName, {
   nonInteraction: true
});
</code></pre>
<p>Kliks trackes næsten på samme måde, det skal bare aktiveres når man klikker på knappen/billedet. Se mere i <a href="https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce">Googles dokumentation her</a>.</p>
<p>Derved kan vi fx nemt se performance for vores primære Call-to-Action på forsiden, som ser således ud:</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta.png" alt="" width="869" height="425" class="alignnone size-full wp-image-1038" srcset="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta.png 869w, https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta-690x337.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta-768x376.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-start-here-cta-725x355.png 725w" sizes="auto, (max-width: 869px) 100vw, 869px" /></a></p>
<p>I rapporten i Google Analytics hedder den &#8220;Start here&#8221; ligesom teksten på knappen og har en CTR på 34,96%. Godt at vide at den primære CTA bliver brugt ofte!</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2.png" alt="" width="1267" height="543" class="alignnone size-full wp-image-1080" srcset="https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2.png 1267w, https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2-690x296.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2-768x329.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/internal-promotions-report-v2-725x311.png 725w" sizes="auto, (max-width: 1267px) 100vw, 1267px" /></a></p>
<p>Subscribe knappen i footeren bliver næsten ikke brugt og har kun en CTR på 0,09%. Som forventet vil jeg næsten sige, men det kræver data at få det bekræftet.</p>
<p>På kvitteringssiden opfordrer vi kunderne til at lave et review på facebook. Det er der cirka 2% der gør. Det har jeg skrevet meget mere om her: <a href="https://www.jacobworsoe.dk/skab-vaerdifulde-konverteringer-paa-kvitteringssiden/">Skab værdifulde konverteringer på kvitteringssiden</a>.</p>
<p>Breaking News var en nyheds-ribbon vi havde på forsiden med et tekstlink som linkede videre. Den har en CTR på 3% og dermed slet ikke samme CTR som vores CTA-knapper. &#8220;Start Exchange here >&#8221; er fx en CTA-knap på en landingpage og har en CTR på 18%. Igen er det ikke overraskende at knapper er bedre end tekstlinks, men det er bare så fedt at få noget data på det!</p>
<p>Vi har Call-to-Actions på alle vores landingpages som fx <a href="https://www.exchangemycoins.com/pages/buy-bitcoins-with-usd">den her</a> eller <a href="https://www.exchangemycoins.com/pages/exchange-bitcoins-paypal">den her</a>.</p>
<p>Med disse data kan vi også nemt se hvor godt de performer og CTR gør det super nemt at sammenligne sider med vidt forskellige antal visninger og kliks.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance.png" alt="" width="1236" height="307" class="alignnone size-full wp-image-1047" srcset="https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance.png 1236w, https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance-690x171.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance-768x191.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/landingpage-cta-performance-725x180.png 725w" sizes="auto, (max-width: 1236px) 100vw, 1236px" /></a></p>
<h2 id="send-data-forsinket">2. Send data forsinket</h2>
<p>Med Universal Analytics lancerede Google også et API til Google Analytics, kaldet Measurement Protocol, som kan bruges til at sende data til Google Analytics, direkte fra serveren. Mulighederne er mange, men i vores tilfælde giver det primært to fordele: Hemmelige data og forsinket data.</p>
<p>Når man veksler Bitcoins, kan der gå op til 60 minutter før vekslingen er endelig bekræftet og ikke kan annulleres &#8211; sådan er det med Bitcoin, men det giver en tydelig udfordring med tracking af vekslingen.</p>
<p>Hvis brugeren ikke længere er aktiv på sitet eller har forladt sitet, vil vekslingen stadig blive gennemført, men vi har ikke længere brugerens browser til at sende data til Google Analytics for os.</p>
<p>Men med Measurement Protocol er vi ikke afhængig af at brugeren udfører en handling på websitet, for at kunne tracke det. Når vekslingen er færdig sender serveren selv data direkte til Google.</p>
<p>Vi gemmer værdien af brugerens Google Analytics cookie når de starter vekslingen, så vi kan sende den med, når vi sender data til Google. Dermed bliver transaktionen koblet sammen med brugerens session og vi kan dermed stadig se trafikkilden og lignende, præcis som hvis brugerens browser havde sendt transaktionen til Google. Skide smart!</p>
<h2 id="send-hemmelige-data">3. Send hemmelige data til Google Analytics</h2>
<p>Normalt bliver alle data sendt til Google Analytics via JavaScript som kører på klienten. Dvs. alt hvad du sender til Google Analytics har brugeren i princippet mulighed for at se. Når man sender data direkte fra serveren til Google, kan brugeren ikke se de data man sender. Og dermed kan man sende hemmelige forretningsdata til Google Analytics.</p>
<p>Fx avance på ordre, så du kan udregne en mere præcis fortjeneste på dine Adwords kampagner, direkte i Google Analytics.</p>
<p>Som sagt så skal Google Analytics hackes. Google Analytics har ikke et datafelt til at gemme avance, men de har en felt til moms. Vi regner ikke med moms, så det felt kan vi passende bruge til at tracke avance.</p>
<h2>4. Udregn din avanceprocent direkte i Google Analytics</h2>
<p>Vi bruger Calculated Metrics til at udregne vores avanceprocent direkte i Google Analytics.</p>
<p><strong>Pro tip:</strong> Vidste du at Calculated Metrics også virker på historiske data? Ikke kun fremadrettet.</p>
<p>Vi har lavet en Calculated Metric som udregner vores avanceprocent med denne udregning: <em>{{Tax}} / {{Revenue}}</em></p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/calculated-metric-profit-rate.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/calculated-metric-profit-rate.png" alt="" width="402" height="500" class="alignnone size-full wp-image-1041" /></a></p>
<p>Dermed kan vi nemt få et overblik over hvordan vores avanceprocent udvikler sig over tid. Og ved at have det i Google Analytics, kan vi nemt segmentere det på trafikkilde, landingpages, etc.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph.png" alt="" width="1517" height="307" class="alignnone size-full wp-image-1095" srcset="https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph.png 1517w, https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph-690x140.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph-768x155.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/profit-rate-graph-725x147.png 725w" sizes="auto, (max-width: 1517px) 100vw, 1517px" /></a></p>
<h2>5. Hvilke produkter performer bedst?</h2>
<p>Kunderne kan veksle mellem flere forskellige digitale valutaer, så vi bruger Enhanced Ecommerce til at få et unikt indblik i hvilke der oftest bliver kigget på, samt hvilke kunderne oftest veksler.</p>
<p>Når en bruger vælger to valutaer i formularen på forsiden, viser vi kursen mellem de to valutaer:</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/bitcoin-to-litecoin-exchange-dropdown.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/bitcoin-to-litecoin-exchange-dropdown.png" alt="" width="729" height="222" class="alignnone size-full wp-image-1050" /></a></p>
<p>Dette tracker vi som en produktdetaljevisning, altså det der svarer til at brugeren ser en produktside på en webshop. Dette gøres med følgende JavaScript:</p>
<pre class="prettyprint" rel="JavaScript"><code class="" data-line="">ga(&#039;require&#039;, &#039;ec&#039;);

ga(&#039;ec:addProduct&#039;, {
   &#039;id&#039;: ga_ProductName,
   &#039;name&#039;: ga_ProductName,
   &#039;category&#039;: ga_Category,
   &#039;brand&#039;: &#039;&#039;,
   &#039;variant&#039;: &#039;&#039;
});

ga(&#039;ec:setAction&#039;, &#039;detail&#039;);
ga(&#039;send&#039;, &#039;event&#039;, &#039;Ecommerce&#039;, &#039;Product view&#039;, ga_ProductName);
</code></pre>
<p>Når brugeren går igang med vekslingen, tracker vi at produktet er lagt i kurven.</p>
<p>Og når brugeren gennemfører vekslingen, registrerer vi at produktet er købt. Det er det vi gør server-side, som beskrevet ovenfor.</p>
<p>Derved har vi et fuldt overblik over produkterne, hele vejen gennem websitet:</p>
<div id="attachment_1085" style="width: 1724px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1085" src="https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance.png" alt="Se også de to sidste kolonner med rates som gør produkterne sammenlignelige!" width="1714" height="728" class="size-full wp-image-1085" srcset="https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance.png 1714w, https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance-690x293.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance-768x326.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/ga-product-performance-725x308.png 725w" sizes="auto, (max-width: 1714px) 100vw, 1714px" /></a><p id="caption-attachment-1085" class="wp-caption-text">Se også de to sidste kolonner med rates som gør produkterne sammenlignelige!</p></div>
<p>Bemærk især de to sidste kolonner herover, som viser hvor tit produkterne lægges i kurv og købes i forhold til hvor tit de bliver set ude på forsiden. Med de to tal, kan vi meget nemt se hvilke produkter vi har en god og mindre god vekselkurs på.</p>
<p>Vi får også en overskuelig oversigt over frafaldet på hvert trin i købsrejsen gennem sitet:</p>
<div id="attachment_1158" style="width: 847px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1158" src="https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior.png" alt="39% af alle besøg ser produkter og 25% af dem lægger et produkt i kurven." width="837" height="481" class="size-full wp-image-1158" srcset="https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior.png 837w, https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior-690x397.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior-768x441.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/EMC-shopping-behavior-725x417.png 725w" sizes="auto, (max-width: 837px) 100vw, 837px" /></a><p id="caption-attachment-1158" class="wp-caption-text">39% af alle besøg ser produkter og 25% af dem lægger et produkt i kurven.</p></div>
<h2>6. Mest populære FAQ spørgsmål</h2>
<p>Fra starten har vi haft fokus på at lave alting så automatisk som muligt. Hver gang vi modtager et generelt spørgsmål på vores supportmail, opretter vi en FAQ på spørgsmålet, så vi ikke skal bruge tid på at svare på de samme spørgsmål igen og igen. Vi har derfor en grundig FAQ sektion og vi tracker selvfølgelig hvilke FAQ spørgsmål der er mest populære.</p>
<div id="attachment_1076" style="width: 1007px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1076" src="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq.png" alt="En del af FAQ sektionen på sitet." width="997" height="653" class="size-full wp-image-1076" srcset="https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq.png 997w, https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq-690x452.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq-768x503.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/exchangemycoins-faq-725x475.png 725w" sizes="auto, (max-width: 997px) 100vw, 997px" /></a><p id="caption-attachment-1076" class="wp-caption-text">En del af FAQ sektionen på sitet.</p></div>
<p>Med følgende simple kode tracker vi automatisk alle klik på FAQ spørgsmål. Koden tager ankerteksten og sender som Event til Google Analytics.</p>
<pre class="prettyprint" rel="JavaScript"><code class="" data-line="">$(&quot;a[href^=&#039;#faq-&#039;]&quot;).on(&quot;click&quot;, function () {
        var anchorText = $(this).text();
        ga(&#039;send&#039;, &#039;event&#039;, &#039;FAQ click&#039;, anchorText);
    });
</code></pre>
<p>Voila!</p>
<div id="attachment_1074" style="width: 1077px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1074" src="https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq.png" alt="De mest populære FAQ spørgsmål på sitet." width="1067" height="554" class="size-full wp-image-1074" srcset="https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq.png 1067w, https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq-690x358.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq-768x399.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/ga-event-most-clicked-faq-725x376.png 725w" sizes="auto, (max-width: 1067px) 100vw, 1067px" /></a><p id="caption-attachment-1074" class="wp-caption-text">De mest populære FAQ spørgsmål på sitet.</p></div>
<p>Så standardrapporterne kan sagtens bruges, selvom man ikke er en webshop! De skal bare hackes lidt.</p>

