---
layout: post
title: Tracking af returvarer i Google Analytics
date: 2019-10-27 00:10:19
slug: returvarer-google-analytics
wordpress_id: 1597
categories:
  - Analytics
---

Tracker du returvarer i Google Analytics? Nej? Bare rolig, du er ikke den eneste.

Jeg har arbejdet med Google Analytics for mere end 100 webshops, og jeg kender mindre end 5 webshops der tracker returvarer i Google Analytics.

Og når returvarer i nogle brancher udgør 25% eller mere er det ofte den største årsag til forskellen mellem tallene i Google Analytics og de rigtige tal i ERP systemet.

Så hvis du arbejder med Google Analytics på en webshop, bør du overveje at implementere det. Og her viser jeg dig hvordan du gør, samt hvordan det påvirker dine data - det er nemlig ikke helt som man forventer, men mere om det senere.

<h2>Indhold</h2>

<ul>
<li><a href="#article-header-id-0">Track ordre med negativ omsætning og antal</a></li>
<li><a href="#article-header-id-1">Enhanced Ecommerce refunds</a>

<ul>
<li><a href="#article-header-id-2">Returnering af hele ordren</a></li>
<li><a href="#article-header-id-3">Hvornår registreres returneringer?</a></li>
<li><a href="#article-header-id-4">Returnering af dele af ordren</a></li>
</ul></li>
<li><a href="#article-header-id-5">Tracking af returneringen</a>

<ul>
<li><a href="#article-header-id-6">Track returneringen med JavaScript</a></li>
<li><a href="#article-header-id-7">Send data med Measurement Protocol</a></li>
<li><a href="#article-header-id-8">Upload returneringer med Data Import</a></li>
</ul></li>
<li><a href="#article-header-id-9">Analyse af Refund data</a>

<ul>
<li><a href="#article-header-id-10">Udregn de rigtige tal med Calculated Metrics</a></li>
<li><a href="#article-header-id-11">Den korrekte konverteringsrate</a></li>
<li><a href="#article-header-id-12">Find produkter der ofte bliver sendt retur</a></li>
<li><a href="#article-header-id-13">Pas på med trafikkilder!</a></li>
</ul></li>
<li><a href="#article-header-id-14">Opsummering</a></li>
</ul>

Lad os først kigge på hvordan du sætter det op.

Jeg vil gennemgå fire forskellige måder at gøre det på, samt vise fordele/ulemper ved dem.

<h3>Eksempler med Google Tag Manager</h3>

Herunder bruger jeg <a href="http://tagmanager.google.com/" rel="noopener noreferrer" target="_blank">Google Tag Manager</a> og et <code>dataLayer</code> til eksemplerne, men alle eksemplerne er også mulige, hvis du har Google Analytics hardcoded på sitet.

Du kan finde de tilsvarende hardcodede kode eksempler i <a href="https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce#measuring-refunds">Google Analytics dokumentationen her</a>.

<h3>Først skal vi have en ordre der kan returneres</h3>

Som gennemgående eksempel bruger jeg denne ordre.

<ul>
<li>To produkter til i alt 1000,- kroner</li>
<li>Fragt på 50,- kroner</li>
<li>En totalomsætning på 1050,- kroner</li>
<li>Og til sidst moms af hele balladen på 210,- kroner (der er <a href="https://dinero.dk/support/salg-af-fragt-hvordan-fakturerer-jeg-fragt/" rel="noopener noreferrer" target="_blank">moms på fragt</a>)</li>
</ul>

<pre><code class="language-javascript">dataLayer.push({
    'event': 'purchase',
    'ecommerce': {
    'purchase': {
      'actionField': {
        'id': '12345',
        'affiliation': '',
        'revenue': '1050',
        'tax':'210',
        'shipping': '50',
        'coupon': ''
      },
      'products': [{
        'name': 'T-Shirt',
        'id': '123',
        'price': '300',
        'brand': '',
        'category': '',
        'variant': '',
        'quantity': 1
       },
       {
        'name': 'Jeans',
        'id': '456',
        'price': '700',
        'brand': '',
        'category': '',
        'variant': '',
        'quantity': 1
       }]
    }
  }
});
</code></pre>

Dermed har vi disse tal i ecommerce overview:

<figure><a href="{{ '/assets/images/2019/08/test-ordre-ecommerce-overview.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/test-ordre-ecommerce-overview.png' | relative_url }}" alt="Test ordren i Ecommerce overview." width="1452" height="620" class="size-full wp-image-1854" /></a><figcaption>Test ordren i Ecommerce overview.</figcaption></figure>

Den specfikke ordre ser således ud:

<figure><a href="{{ '/assets/images/2019/08/test-ordre-sales-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/test-ordre-sales-performance.png' | relative_url }}" alt="De detaljerede tal for ordren." width="1473" height="308" class="size-full wp-image-1855" /></a><figcaption>De detaljerede tal for ordren.</figcaption></figure>

Og produkterne ser således ud:

<figure><a href="{{ '/assets/images/2019/08/test-ordre-product-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/test-ordre-product-performance.png' | relative_url }}" alt="Produkterne i test ordren." width="1267" height="481" class="size-full wp-image-1856" /></a><figcaption>Produkterne i test ordren.</figcaption></figure>

<h2 id="article-header-id-0">Track ordren med negativ omsætning og antal</h2>

Det her er faktisk et gammelt trick fra før Enhanced Ecommerce blev <a href="https://analytics.googleblog.com/2014/05/google-analytics-summit-2014-whats-next.html">introduceret tilbage i 2014</a>.

Det er ikke muligt at fjerne en ordre fra Google Analytics, men man kan fjerne omsætningen, ved at tracke den samme ordre igen, bare med negativ omsætning.

Dvs. hvis der er blevet returneret en ordre på 1050,- kroner, så tracker du en ny ordre hvor omsætningen er -1050,- kroner. Smart ik?

Produkterne bliver tracket med deres normale positive pris, men derimod er mængden -1. Dermed fjernes både mængden og produktomsætningen, fordi mængden ganges med prisen og dermed bliver prisen negativ.

<pre><code class="language-javascript">dataLayer.push({
    'event': 'purchase',
    'ecommerce': {
    'purchase': {
      'actionField': {
        'id': '12345',
        'affiliation': '',
        'revenue': '-1050', // negativt beløb
        'tax':'-210', // negativt beløb
        'shipping': '-50', // negativt beløb
        'coupon': ''
      },
      'products': [{
        'name': 'T-Shirt',
        'id': '123',
        'price': '300',
        'brand': '',
        'category': '',
        'variant': '',
        'quantity': -1 // negativ mængde
       },
       {
        'name': 'Jeans',
        'id': '456',
        'price': '700',
        'brand': '',
        'category': '',
        'variant': '',
        'quantity': -1 // negativ mængde
       }]
    }
  }
});
</code></pre>

Ordren med negativ omsætning ser sådan ud i Google Analytics - bemærk negativ omsætning og negativ mængde:

<figure><a href="{{ '/assets/images/2019/07/negative-purchase-order.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/negative-purchase-order.png' | relative_url }}" alt="Ordre med negativ omsætning og antal produkter." width="1716" height="271" class="size-full wp-image-1726" /></a><figcaption>Ordre med negativ omsætning og antal produkter.</figcaption></figure>

Hvis man kigger på hele perioden hvor både den normale ordre blev lavet, samt 4 dage senere hvor den negative ordre blev registreret, ser produkterne ud som herunder.

Bemærk at <code>Product Revenue</code> bliver negativ, når mængden er negativ. Resultatet af de to ordre tilsammen ses i øverste linje hvor den totale <code>Product Revenue</code> er 0,00 og den totale købte mængde er 0.

Derimod er <code>Unique Purchases</code> nu blevet til 4, fordi produkterne tæller med her selvom de er negative, fordi den blot tæller hvor mange ordre der findes med de pågældende produkter - også selvom mængden har været negativ.

<figure><a href="{{ '/assets/images/2019/07/negative-purchase-products.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/negative-purchase-products.png' | relative_url }}" alt="Produktoversigt med de negative produkter samt de normale købte produkter." width="1737" height="548" class="size-full wp-image-1728" /></a><figcaption>Produktoversigt med de negative produkter samt de normale købte produkter.</figcaption></figure>

Og når man ser resultatet af både den første ordre og den negative ordre, ser det således ud, dvs. der er nu 2 ordre, men omsætningen er korrekt.

<figure><a href="{{ '/assets/images/2019/07/negative-purchase-sales-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/negative-purchase-sales-performance.png' | relative_url }}" alt="Resultatet af begge ordre er at omsætning, moms, fragt og antal går i 0." width="1744" height="685" class="size-full wp-image-1730" /></a><figcaption>Resultatet af begge ordre er at omsætning, moms, fragt og antal går i 0.</figcaption></figure>

Ulempen ved denne metode er altså at man tracker en ordre mere, så antal ordre bliver for højt, hvilket påvirker konverteringsraten. Især hvis der returneres mange ordre.

Men omsætningen kommer til at passe. Så det er en vurdering man er nødt til at lave.

<figure><a href="{{ '/assets/images/2019/07/negative-purchase-2-transactions.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/negative-purchase-2-transactions.png' | relative_url }}" alt="Den negative ordre tæller som en ny ordre og dermed er der nu to ordre." width="1446" height="491" class="size-full wp-image-1732" /></a><figcaption>Den negative ordre tæller som en ny ordre og dermed er der nu to ordre.</figcaption></figure>

<h2 id="article-header-id-1">Enhanced Ecommerce refunds</h2>

Med <a href="https://support.google.com/analytics/answer/6014841?hl=en" rel="noopener noreferrer" target="_blank">Enhanced Ecommerce</a> kom også muligheden for at tracke returneringer. Både hele ordren, men også enkelte ordrelinjer.

<h3 id="article-header-id-2">Returnering af hele ordren</h3>

For at tracke en returnering af en komplet ordre skal der blot sendes en Refund action med ordrenummeret. Mega simpelt.

<pre><code class="language-javascript">dataLayer.push({
  'event': 'refund',
  'ecommerce': {
    'refund': {
      'actionField': {'id': '12345'}
    }
  }
});
</code></pre>

Men det der sker med dine data er ikke så simpelt.

Man forventer måske at den pågældende ordre nu blot bliver slettet i datasættet og dermed ikke findes mere. Men det gør den ikke. Den originale ordre bliver liggende i datasættet.

Sådan fungerer Google Analytics i øvrigt altid. Når først data er sendt og behandlet kan de ikke ændres.

Det der istedet sker er at der bliver registreret en <em>returnering</em> af den ordre, hvor Google Analytics bruger det ordrenummer der er sendt med i ovenstående <code>Refund</code>action til at finde alle informationerne om ordren og registerer en returnering med dem.

<p class="attention"><strong>Bemærk!</strong> Google Analytics kigger kun på ordre de sidste 6 måneder tilbage. Hvis der ikke findes en ordre med det pågældende ordre ID indenfor de sidste 6 måneder, bliver der ikke tracket en returnering.</p>

Returneringen kan du derefter finde under Conversions -> E-commerce -> Sales performance hvor det returnerede beløb fremgår ud for ordren i kolonnen <code>Refund Amount</code>.

<figure><a href="{{ '/assets/images/2019/07/eec-refund-sales-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/eec-refund-sales-performance.png' | relative_url }}" alt="Conversions -&gt; E-commerce -&gt; Sales performance" width="1473" height="216" class="size-full wp-image-1734" /></a><figcaption>Conversions -> E-commerce -> Sales performance</figcaption></figure>

Her er <code>Refund Amount</code> nu sat til 1050,-

Bemærk at omsætningen stadig er den samme.

<p class="attention"><strong>Bemærk!</strong> Hvis der er flere ordre med samme transaktions ID, så vil Google Analytics tage beløbet og produkterne fra den seneste ordre.</p>

Omsætningen er også uændret i dit E-commerce overview, både for ordren og produkterne. Det samme gælder alle andre steder i Google Analytics rapporter, hvor du kigger på omsætningen, fx trafikkilder og landingpages.

<figure><a href="{{ '/assets/images/2019/07/eec-refund-ecommerce-overview.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/eec-refund-ecommerce-overview.png' | relative_url }}" alt="Omsætning og produktsalg er uændret." width="1452" height="631" class="size-full wp-image-1735" /></a><figcaption>Omsætning og produktsalg er uændret.</figcaption></figure>

Det samme gælder hvis man kigger på de enkelte produkter under <code>Product Performance</code> men det returnerede beløb fremgår i <code>Product Refund Amount</code>.

<figure><a href="{{ '/assets/images/2019/07/eec-refund-product-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/eec-refund-product-performance.png' | relative_url }}" alt="Produkter har fået registreret et refunderet beløb." width="1295" height="386" class="size-full wp-image-1736" /></a><figcaption>Produkter har fået registreret et refunderet beløb.</figcaption></figure>

<p class="attention"><strong>Bemærk!</strong> Google Analytics registrerer det fulde beløb for ordren som returneret. Dette gælder også fragten, som kunden typisk ikke får refunderet.</p>

<h3 id="article-header-id-3">Hvornår registreres returneringer?</h3>

Både ordre og returneringer bliver registreret på det tidspunkt de bliver sendt til Google Analytics. Dvs. hvis man kigger på den dag ordren blev lavet vil man kun se omsætningen.

<figure><a href="{{ '/assets/images/2019/08/transaction-day.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/transaction-day.png' | relative_url }}" alt="Dagen hvor ordren blev lagt." width="1421" height="275" class="size-full wp-image-1876" /></a><figcaption>Dagen hvor ordren blev lagt.</figcaption></figure>

Og hvis man kigger på dagen hvor returneringen blev sendt til Google Analytics, som fx kan være 7 dage senere, så vil man kun se det returnerede beløb.

<figure><a href="{{ '/assets/images/2019/08/refund-day.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/refund-day.png' | relative_url }}" alt="Dagen hvor returneringen blev registreret." width="1419" height="251" class="size-full wp-image-1877" /></a><figcaption>Dagen hvor returneringen blev registreret.</figcaption></figure>

Hvis du istedet vælger hele tidsperioden, hvor både ordren og returneringen blev registreret, vil du se de rigtige tal.

<figure><a href="{{ '/assets/images/2019/07/eec-refund-sales-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/eec-refund-sales-performance.png' | relative_url }}" alt="Tal for hele perioden." width="1473" height="216" class="size-full wp-image-1734" /></a><figcaption>Tal for hele perioden.</figcaption></figure>

Det er især vigtigt når der skal analyseres på perioder med høj omsætning, fx Black Friday og december. Varerne bliver måske først sendt retur i januar, så derfor er det nødvendigt at se på data for både december og januar, for at se det rigtige billede af hvor meget der blev solgt og sendt tilbage.

<h3 id="article-header-id-4">Returnering af dele af ordren</h3>

Enhanced Ecommerce understøtter også at kunden returnerer noget af ordren. Hvis kunden kun sender de købte jeans tilbage (som kostede 700,-) skal man blot sende ordrenummeret som ovenfor, samt produkt ID'et og antal for de varer der er returneret.

<pre><code class="language-javascript">dataLayer.push({
  'event': 'refund',
  'ecommerce': {
    'refund': {
      'actionField': {'id': '12345'},
      'products': [
            {'id': '456', 'quantity': 1}
       ]
     }
  }
});
</code></pre>

Under <code>Sales performance</code> kan man nu se at ordren har haft en omsætning på 1050,- samt returvarer for 700,-.

<figure><a href="{{ '/assets/images/2019/07/eec-partial-refund-sales-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/eec-partial-refund-sales-performance.png' | relative_url }}" alt="Med delvis returnering har ordren en omsætning på 1050,- og returvarer for 700,-." width="1467" height="221" class="size-full wp-image-1745" /></a><figcaption>Med delvis returnering har ordren en omsætning på 1050,- og returvarer for 700,-.</figcaption></figure>

Under <code>Product performance</code> er der købt to produkter, hvor den ene er refunderet.

<figure><a href="{{ '/assets/images/2019/07/eec-partial-refund-product-performance.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/eec-partial-refund-product-performance.png' | relative_url }}" alt="Der er købt to produkter hvoraf det ene er refunderet." width="1276" height="394" class="size-full wp-image-1746" /></a><figcaption>Der er købt to produkter hvoraf det ene er refunderet.</figcaption></figure>

<p class="attention"><strong>Pro tip!</strong> Som vist ovenfor vil en fuld returnering også registrere at fragten er refunderet. Hvis du istedet laver en delvis returnering hvor du registrerer at alle produkterne er sendt retur, men ikke fragten, så vil returneringen passe med det beløb kunden rent faktisk har fået retur.</p>

<h2 id="article-header-id-5">Tracking af returneringen</h2>

Okay, nu ved du hvordan returneringer påvirker dine data i Google Analytics. Lad os se på forskellige måder at sende det til Google.

Til sidst i indlægget viser jeg dig en masse tips og faldgrupper når der skal analyseres på dataene, men mere om det senere.

Der findes flere forskellige måder at sende returneringen til Google Analytics afhængigt af:

<ul>
<li>Hvilket system der skal sende det til Google Analytics</li>
<li>Om det sker når kunden anmoder om at sende pakken retur eller når butikken modtager returpakken</li>
<li>Om det skal gøres automatisk eller manuelt</li>
</ul>

<h3 id="article-header-id-6">Track returneringen med JavaScript</h3>

Negative ordre og Enhanced Ecommerce refunds bruger begge JavaScript til at sende returneringen til Google Analytics.

Det involverer typisk et website.

Dvs. det kræver at returneringen sker på et website. Det kan være at kunderne skal registrere returneringen på websitet og fx få mulighed for at printe en returlabel. I den situation kan du tracke returneringen på det tidspunkt.  Det giver dog risiko for forkerte data, hvis kunderne ombestemmer sig og vælger at beholde varen alligevel.

Det kan også være du sender en returlabel med i pakken og dermed kan kunderne bare sende pakken retur uden videre. I det tilfælde kan du tracke returneringen, når du modtager pakken fra kunden. Hvis det sker på et website, så kan du formentlig bruge den normale JavaScript tracking, som jeg har brugt herover.

<h3 id="article-header-id-7">Send data med Measurement Protocol</h3>

Hvis returneringen bliver registreret i et ERP system eller lignende, er det formentlig ikke muligt at afvikle JavaScript og dermed bruge ovenstående metoder til at sende data til Google Analytics.

Løsningen er derfor at bruge Google Analyics' API - Measurement Protocol - som kan bruges af alle systemer der kan sende et HTTP request, hvilket er stort set alle systemer der har adgang til internettet.

Et HTTP request er praktisk talt bare en URL der skal kaldes. Og URL'en har en masse paramtere, som indeholder alle de data der  sendes til Google Analytics.

Dokumentationen for Google Analytics Measurement Protocol indeholder <a href="https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide#commonhits" rel="noopener noreferrer" target="_blank">en masse gode eksempler</a>, herunder Refunds.

<figure><a href="{{ '/assets/images/2019/07/measurement-protocol-refund-documentation.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/measurement-protocol-refund-documentation.png' | relative_url }}" alt="Measurement Protocol Refund eksempel." width="1116" height="547" class="size-full wp-image-1750" /></a><figcaption>Measurement Protocol Refund eksempel.</figcaption></figure>

Lige under koden er der et link, som tager dig over til <a href="https://ga-dev-tools.appspot.com/hit-builder/?v=1&t=event&tid=UA-12345-1&cid=1843026860.1552990676&ec=Ecommerce&ea=Refund&ni=1&ti=T12345&pa=refund" rel="noopener noreferrer" target="_blank">Hit Builder</a>, hvor du kan bygge videre på eksemplet.

<figure><a href="{{ '/assets/images/2019/07/measurement-protocol-refund-with-cookie-id.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/measurement-protocol-refund-with-cookie-id.png' | relative_url }}" alt="Hit Builder med koden til et Refund." width="683" height="588" class="size-full wp-image-1751" /></a><figcaption>Hit Builder med koden til et Refund.</figcaption></figure>

Bemærk feltet <code>cid</code> hvor du kan angive kundens cookie ID og dermed vil returneringen blive koblet sammen med brugerens øvrig data i Google Analytics, som fx brugerens oprindelige trafikkilde da ordren blev lagt.

Test derefter din request URL:

<figure><a href="{{ '/assets/images/2019/07/measurement-protocol-refund-valid-hit.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/measurement-protocol-refund-valid-hit.png' | relative_url }}" alt="Validér at requestet er korrekt." width="922" height="498" class="size-full wp-image-1753" /></a><figcaption>Validér at requestet er korrekt.</figcaption></figure>

Den endelige URL som skal kaldes fåes ved at sætte <code>https://www.google-analytics.com/collect?</code> foran den URL (Hit Payload) som Hit Builder genererer.

Dermed fås denne URL:
<code>https://www.google-analytics.com/collect?v=1&amp;t=event&amp;tid=UA-12345-1&amp;cid=1843026860.1552990676&amp;ec=Ecommerce&amp;ea=Refund&amp;ni=1&amp;ti=T12345&amp;pa=refund</code>

Denne URL kan du nu få dit "offline" system til at lave en POST request til og derefter bliver det sendt til Google Analytics.

<h3 id="article-header-id-8">Upload returneringer med Data Import</h3>

Hvis du kun har ganske få returneringer, kan det måske ikke betale sig at kode en automatisk løsning til det. I det tilfælde kan du også uploade en CSV fil med de ordre ID'er der er returneret via <code>data import</code> inde i Google Analytics interfacet.

Det er en meget simpel og hurtig løsning, hvis det er tilstrækkeligt at returneringer kun bliver importeret fx en gang ugentligt.

Bare husk på at returneringerne vil optræde den dag de er importeret i Google Analytics, så hvis du kun uploader dem ugentligt eller månedligt, så vil alle returneringerne bliver registreret den ene dag.

Først går du ind under <code>Admin</code> -> <code>Property Settings</code> -> <code>Data import</code>.

<figure><a href="{{ '/assets/images/2019/07/data-import-property-settings.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-property-settings.png' | relative_url }}" alt="Admin &gt; Property Settings &gt; Data import" width="1016" height="380" class="size-full wp-image-1756" /></a><figcaption>Admin > Property Settings > Data import</figcaption></figure>

Klik på den røde knap.

<figure><a href="{{ '/assets/images/2019/07/data-import-create-new.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-create-new.png' | relative_url }}" alt="Opret en ny Data Import." width="1297" height="545" class="size-full wp-image-1759" /></a><figcaption>Opret en ny Data Import.</figcaption></figure>

Vælg "Refund" som type.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-set-type.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-set-type.png' | relative_url }}" alt="Vælg &quot;Refund&quot; som type." width="908" height="634" class="size-full wp-image-1760" /></a><figcaption>Vælg "Refund" som type.</figcaption></figure>

Giv den et godt navn.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-set-details.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-set-details.png' | relative_url }}" alt="Giv den et godt navn." width="393" height="385" class="size-full wp-image-1761" /></a><figcaption>Giv den et godt navn.</figcaption></figure>

Derefter kan du se de felter der skal uploades. Hvis du bare vil returnere hele ordren, så er <code>Transaction ID</code> som set ovenfor det eneste påkrævede felt.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-set-schema.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-set-schema.png' | relative_url }}" alt="Transaction ID er det eneste påkrævede felt." width="1230" height="579" class="size-full wp-image-1762" /></a><figcaption>Transaction ID er det eneste påkrævede felt.</figcaption></figure>

Du kan også lave <code>Partial Refunds</code> med <code>Data import</code> hvor der kan angives nogle flere værdier, fx de produkter der er sendt tilbage.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-set-schema-optional.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-set-schema-optional.png' | relative_url }}" alt="Delvise returneringer har nogle flere mulige felter." width="1236" height="515" class="size-full wp-image-1769" /></a><figcaption>Delvise returneringer har nogle flere mulige felter.</figcaption></figure>

<code>Product SKU</code> og <code>Quantity Refunded</code> er de samme felter som vi har kigget på tidligere. Men med <code>Data Import</code> er der flere muligheder.

Hvis en kunde sender et produkt tilbage som er brugt lidt og han derfor ikke skal have det fulde beløb tilbage, kan du angive det beløb kunden får tilbage i <code>Product Price</code>.

Hvis du ikke vil lave en delvis returnering, dvs. sende specifikke produkt ID'er med, men stadig gerne vil tracke et andet beløb end den oprindelige omsætning på ordren, så kan du bruge <code>Revenue</code>-feltet. Som tidligere nævnt, så vil Google Analytics nemlig selv finde omsætningen, hvis du blot indsender et ordre ID.

<h3>Data Import template</h3>

Derefter klikker du "Get Schema" for at hente templaten.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-get-schema.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-get-schema.png' | relative_url }}" alt="Hent templaten." width="1206" height="466" class="size-full wp-image-1771" /></a><figcaption>Hent templaten.</figcaption></figure>

Det er kun <code>ga:transactionId</code> der er obligatorisk, så de andre felter kan du bare lade være tomme. Hver ordre der skal returneres placeres på sin egen række i filen.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-csv-file.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-csv-file.png' | relative_url }}" alt="CSV fil der skal uploades." width="1193" height="133" class="size-full wp-image-1772" /></a><figcaption>CSV fil der skal uploades.</figcaption></figure>

Det er dog ikke muligt at blande <code>Partial Refunds</code> med komplette <code>Refunds</code> i samme fil, så det skal uploades i hver sin fil.

Jeg plejer derfor at oprette to <code>Data Imports</code> for at holde det helt adskilt.

<figure><a href="{{ '/assets/images/2019/07/data-import-overview.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-overview.png' | relative_url }}" alt="Brug separate Data Imports til delvise og komplette returneringer for at holde det adskilt." width="1299" height="399" class="size-full wp-image-1777" /></a><figcaption>Brug separate Data Imports til delvise og komplette returneringer for at holde det adskilt.</figcaption></figure>

Upload CSV filen.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-upload-csv-file.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-upload-csv-file.png' | relative_url }}" alt="Upload CSV filen." width="755" height="612" class="size-full wp-image-1774" /></a><figcaption>Upload CSV filen.</figcaption></figure>

Hvis filen fejler, kan du klikke på linket og få en forklaring. Typisk skyldes det formattering af CSV filen. Her er det vigtigt at der bruges komma og ikke semikolon som separator. Læs mere om <a href="https://support.google.com/analytics/answer/6014981?hl=en-GB&utm_id=ad" rel="noopener noreferrer" target="_blank">hvordan filen skal formatteres her</a>.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-csv-file-failed.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-csv-file-failed.png' | relative_url }}" alt="CSV fil som ikke validerer." width="1284" height="255" class="size-full wp-image-1775" /></a><figcaption>CSV fil som ikke validerer.</figcaption></figure>

Med fejlen rettet, bliver filen nu godkendt.

<figure><a href="{{ '/assets/images/2019/07/data-import-data-csv-file-completed.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/data-import-data-csv-file-completed.png' | relative_url }}" alt="Godkendt CSV fil." width="1284" height="313" class="size-full wp-image-1776" /></a><figcaption>Godkendt CSV fil.</figcaption></figure>

Derefter er det blot at vente. <code>Data Imports</code> tager typisk noget længere end almindelige data om at blive behandlet og vist i rapporterne, men de plejer at være synlige indenfor 24 timer.

<h2 id="article-header-id-9">Analyse af Refund data</h2>

Okay, nu har vi fået sendt data til Googles servere. Lad os kigge på hvordan vi kan analysere de nye data.

<h3 id="article-header-id-10">Udregn de rigtige tal med Calculated Metrics</h3>

For at få et godt overblik over antal returneringer og den omsætning der er sendt retur, kan man lave en Custom Report.

<figure><a href="{{ '/assets/images/2019/07/custom-report-refunds-overview.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/custom-report-refunds-overview.png' | relative_url }}" alt="Custom Report med overblik over refunds." width="1076" height="143" class="size-full wp-image-1788" /></a><figcaption>Custom Report med overblik over refunds.</figcaption></figure>

Det kunne være fedt hvis Google Analytics automatisk trak returvarer fra omsætningen i Analytics. Men omvendt giver det nogle gode muligheder at have salg og retur særskilt, herunder et godt indblik i hvor meget der bliver sendt retur, fordelt på varer og kategorier. Det ville ikke være muligt hvis Google Analytics blot justerede omsætningen.

Men den rigtige omsætning, er heldigvis nem at udregne.

<code>Calculated Metrics</code> i Google Analytics giver mulighed for at udregne nye metrics på baggrund af andre eksisterende metrics.

Du finder Calculated Metrics under View settings.

<figure><a href="{{ '/assets/images/2019/07/calculated-metrics-view-settings.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/calculated-metrics-view-settings.png' | relative_url }}" alt="Calculated Metrics findes under View settings." width="520" height="682" class="size-full wp-image-1785" /></a><figcaption>Calculated Metrics findes under View settings.</figcaption></figure>

Her kan du indtaste <code>Revenue</code> i feltet og derefter <code>minus</code> og så <code>Refund Amount</code>.

<figure><a href="{{ '/assets/images/2019/07/calculated-metrics-create-new.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/calculated-metrics-create-new.png' | relative_url }}" alt="Justeret omsætning udregnes som omsætning minus retur beløb." width="992" height="625" class="size-full wp-image-1784" /></a><figcaption>Justeret omsætning udregnes som omsætning minus retur beløb.</figcaption></figure>

Jeg udregner også lige antal ordre.

<figure><a href="{{ '/assets/images/2019/07/calculated-metrics-adjusted-transactions-1.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/calculated-metrics-adjusted-transactions-1.png' | relative_url }}" alt="Udregning af det rigtige antal ordre." width="977" height="160" class="size-full wp-image-1791" /></a><figcaption>Udregning af det rigtige antal ordre.</figcaption></figure>

De to nye Calculated Metrics tilføjes til Custom Report'en.

<figure><a href="{{ '/assets/images/2019/07/calculated-metrics-in-custom-report.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/calculated-metrics-in-custom-report.png' | relative_url }}" alt="Calculated Metrics tilføjes til Custom report." width="1158" height="397" class="size-full wp-image-1787" /></a><figcaption>Calculated Metrics tilføjes til Custom report.</figcaption></figure>

Og dermed har jeg en custom report med de endelige ordre og omsætning.

<figure><a href="{{ '/assets/images/2019/07/custom-report-adjusted-overview.png' | relative_url }}"><img src="{{ '/assets/images/2019/07/custom-report-adjusted-overview.png' | relative_url }}" alt="Custom report med justeret ordre og omsætning." width="1077" height="165" class="size-full wp-image-1789" /></a><figcaption>Custom report med justeret ordre og omsætning.</figcaption></figure>

<p class="attention"><strong>Pro tip!</strong> De fleste ændringer på data i Google Analytics virker kun fremadrettet, fx filtre, mål og Content Grouping. Men Calculated Metrics virker også på historiske data.</p>

<h3 id="article-header-id-11">Den korrekte konverteringsrate</h3>

Skal ordre som returneres regnes med i din konverteringsrate? Eller skal den kun indeholde endelige ordre?

På samme måde som med ordre, kan vi lave en Calculcated Metric som udregner konverteringsraten for returneringer. Dvs. hvor stor en andel af dine besøgende der returnerer ordre igen.

Derefter kan du lave endnu en Calculated Metric, hvor du trækker konverteringsraten for returneringer fra den normale konverteringsrate og dermed får du konverteringsraten for de ordre der ikke bliver returneret, dvs. de ordre du faktisk ender med at tjene penge på.

<h3 id="article-header-id-12">Find produkter der ofte bliver sendt retur</h3>

<a href="https://nochmal.dk/podcasts/hm163-5-datadrevne-tips-til-at-stoppe-hullerne-i-din-webshop-hvor-pengene-fosser-ud/" rel="noopener noreferrer" target="_blank">Returvarer kan kvæle en webshop</a>, både fordi det er mistet omsætning, men også fordi det kræver en masse tid at håndtere.

<blockquote><p>Sælger du tøj, kan du fx risikere at få den samme vare retur, fordi størrelsesangivelsen er misvisende. Justerer du teksten på dit site til folks forventninger, nedsætter du mængden af returvarer (og dermed tid og penge) betragteligt.<cite><a href="https://nochmal.dk/podcasts/hm163-5-datadrevne-tips-til-at-stoppe-hullerne-i-din-webshop-hvor-pengene-fosser-ud/" target="_blank" rel="noopener noreferrer">Morten Vadskær i Help Marketing Podcast</a></cite></p></blockquote>

Der er stor værdi i at identificere de produkter som oftest bliver sendt retur, og justere produktbeskrivelsen på websitet.

Du laver en ny Calculated Metric, som viser forholdet mellem solgte og returnerede produkter i procent.

<figure><a href="{{ '/assets/images/2019/08/product-refund-rate-calculated-metric.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/product-refund-rate-calculated-metric.png' | relative_url }}" alt="Calculated Metric: Product Refund Rate" width="498" height="539" class="size-full wp-image-1846" /></a><figcaption>Calculated Metric: Product Refund Rate</figcaption></figure>

Derefter laver du følgende Custom Report.

<figure><a href="{{ '/assets/images/2019/08/product-refund-rate-custom-report-settings.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/product-refund-rate-custom-report-settings.png' | relative_url }}" alt="Custom Report til at finde hyppige returvarer." width="959" height="502" class="size-full wp-image-1850" /></a><figcaption>Custom Report til at finde hyppige returvarer.</figcaption></figure>

Med den kan du både sortere på <code>Product Refunds</code> for at finde de produkter der er returneret mest, samt sortere på <code>Refund Rate</code> for at se hvilke produkter der oftest bliver sendt retur i forhold til hvor tit de bliver købt.

<figure><a href="{{ '/assets/images/2019/08/product-refund-rate-custom-report.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/product-refund-rate-custom-report.png' | relative_url }}" alt="De mest returnerede produkter." width="1434" height="565" class="size-full wp-image-1851" /></a><figcaption>De mest returnerede produkter.</figcaption></figure>

<h3 id="article-header-id-13">Pas på med trafikkilder!</h3>

En anden lidt mærkelig ting med Refunds er at de bliver attribueret til den sidste trafikkilde brugeren har haft - ikke den trafikkilde som brugeren havde da ordren blev lagt.

Se eksemplet herunder hvor brugeren kom fra <code>google / cpc</code> da ordren blev lagt og efterfølgende havde et besøg fra <code>facebook / social</code> inden returneringer blev registreret. Dermed bliver ordren attribueret til <code>google / cpc</code> mens returneringen bliver attribueret til <code>facebook / social</code>.

Man kan derfor ikke konkludere at det er trafik fra facebook der ofte sender produkter retur, selvom det umiddelbart ser sådan ud - man er nødt til at kigge på trafikkilde for den oprindelige ordre. Det er ikke så logisk.

<figure><a href="{{ '/assets/images/2019/08/source-change-on-refund.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/source-change-on-refund.png' | relative_url }}" alt="Pas på når du analyserer på trafikkilder!" width="1364" height="307" class="size-full wp-image-1880" /></a><figcaption>Pas på når du analyserer på trafikkilder!</figcaption></figure>

<h2 id="article-header-id-14">Opsummering</h2>

For at det er muligt at bruge data fra Google Analytics til at styre forretningen præcist er det altafgørende at Google Analytics afspejler virkeligheden. Filtrering af intern trafik og trafik fra udviklingsdomæner, import af cost data fra facebook, konsistent brug af UTM koder og lignende er altsammen med til at sikre at Google Analytics data er så korrekte som muligt. Tracking af returvarer er oplagt at tilføje til den liste for alle webshops og dermed komme tættere på at have sandheden i Google Analytics.

Hvad tænker du? Skal du igang med at tracke returvarer?

Er der noget jeg kunne beskrive bedre?

Skriv en kommentar herunder!