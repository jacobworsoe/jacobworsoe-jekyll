---
layout: post
title: Den komplette guide til Google Tag Manager
date: 2014-03-31 20:09:59
slug: den-komplette-guide-til-google-tag-manager
wordpress_id: 2665
categories:
  - Analytics
---

Med Google Tag Manager har du mulighed for at opsætte og tilpasse tracking på dit website, uden hjælp fra en programmør. Det er dermed et redskab, som kan give dig øget fleksibilitet i dit arbejde med at indsamle værdifuldt data om brugeradfærd, og i øvrigt spare dig tid og ressourcer. Vi har skrevet en udførlig guide til, hvordan du kommer i gang med at høste fordelene af et værktøj, som vi forventer os rigtig meget af i fremtiden.

Udvikling af e-commerce platforme sker ofte i faser, hvor ny funktionalitet løbende tilføjes og i nogle tilfælde kræver det tilføjelser til det oprindelige tracking setup på sitet. Et godt eksempel er tilføjelse af klub funktionalitet, hvor man, for at kunne spore tilmeldinger og brug af klubben, er nødt til at udbygge det oprindelige tracking setup.

Derudover kan der opstå behov for at måle på, hvor mange brugere, der klikker på et bestemt element eller link på sitet, fx for at se, om det er overflødigt og kan fjernes. Selv mindre tracking udvidelser som denne vil kræve, at en programmør indsætter noget ekstra kode på sitet, og derfor skal webmasteren vente på, at programmøren har tid. Det betyder tab af værdifulde data, og i værste fald bliver det slet ikke gjort.

<h2>Løsningen er Google Tag Manager</h2>

Google Tag Manager (GTM) er Googles løsning på webmasterens behov for at kunne opsætte tracking uden at skulle involvere en programmør. Både i det tilfælde, hvor der skal tilføjes noget til den eksisterende Google Analytics tracking, men også hvis der skal indsættes nye tracking scripts. Det kan fx være tracking af affiliate kampagner eller remarketing scripts. Det kan både være scripts, som skal indsættes på alle sider på websitet eller kun på udvalgte sider.

Med GTM skal du kun have din programmør til at indsætte ét script på sitet, og derefter kan du selv loade andre scripts via et smart webinterface uden at være afhængig af din programmør. GTM er baseret på fleksible regler, hvilket gør, at du meget præcist kan styre hvilke scripts, der bliver indlæst på hvilke sider.

Udover øget fleksibilitet kan du med GTM også gøre dit website hurtigere. En af Googles missioner er at gøre internettet hurtigere, og en af de ting, der gør et website hurtigt er, at scripts bliver indlæst asynkront, hvilket betyder, at de bliver hentet i baggrunden, uden at forsinke indlæsningen af selve siden. GTM sørger derfor for, at alle scripts, som bliver indlæst igennem GTM, bliver indlæst asynkront, hvilket gør dit website hurtigere.

<h2>Opbygningen af Google Tag Manager</h2>

Google Tag Manager er som sagt et regelbaseret system til at styre den tracking, der kører på websitet, og GTM er overordnet opbygget af fem elementer, som jeg lynhurtigt vil introducere dig for.

<h3>1. Container</h3>

Det første du skal gøre, efter at have oprettet dit website i GTM, er at indsætte container scriptet på websitet. Dette script afløser alle andre tracking scripts på sitet, da scriptet sørger for at indlæse alle andre scripts via de regler, du senere opsætter i GTM.

<h3>2. Regler</h3>

Reglerne i GTM styrer hvornår container scriptet skal indlæse bestemte tracking scripts, eller hvornår en bestemt hændelse (event) er udført og skal registreres i Google Analytics.
En regel kan fx være opfyldt, når brugeren lander på kvitteringssiden, efter de har lagt en ordre. Denne regel bliver fx brugt til at indlæse e-commerce tracking scriptet, som normalt kodes ind på kvitteringssiden.

<h3>3. Tags</h3>

Tags er basalt set alt det, du ellers ville få din programmør til at kode ind på dit site. Det kan fx være det normale Google Analytics script eller Event Tracking på din købeknap. Alt dette kan nu opsættes herfra og udføres på baggrund af de ovenstående regler.

<h3>4.Makroer</h3>

Makroer indeholder informationer fra websitet, som du kan bruge som kriterier i regler eller som data, der kan sendes afsted via Tags til fx Google Analytics. Der findes en række indbyggede makroer i GTM og derudover kan du definere dine egne. En indbygget makro kan være makroen ’URL’, som indeholder URL’en på den aktuelle side, brugeren er på. En makro, som du selv definerer, kan være prisen på en vare eller antal produkter på en vareliste.

<h3>5. Data Layer</h3>

Som beskrevet ovenfor, så er det muligt at trække informationer fra websitet over i GTM via makroer, men det stiller store krav til konsistensen i koden over tid. Hvis din kode ændrer sig, fx i forbindelse med et redesign af siden, vil informationer måske ikke længere være placeret de samme steder i koden, som tidligere, og så vil trackingen muligvis fejle.

Det er super smart, at du kan trække informationer ud af websitet uden at involvere din programmør, men det kræver, at din programmør ved hvilke ting, du tracker på, så han ikke ændrer på dem uden at snakke med dig først. Endvidere er det besværligt at definere komplekse dataudtræk som fx e-handelsdata og ordrelinjer alene ud fra deres placering i kildekoden.

For at løse dette har Google introduceret Data Layer, som er en struktureret og mere robust måde at sende informationer til GTM. Det nye Data Layer er et simpelt JavaScript array og fungerer ved, at man angiver de informationer, man gerne vil udtrække som variabler i sit Data Layer. Ved at trække informationerne ud i et Data Layer adskilles det fra sidens øvrige kode, som dermed kan ændres frit fx i forbindelse med et redesign.

En anden fordel ved det nye Data Layer er, at andre tracking værktøjer kan trække information derfra. Det kan fx være splittest værktøjer, affiliate scripts og lignende, der skal bruge informationer om omsætning. Alt dette vil være tilgængeligt i GTM, hvis det opsættes i et Data Layer, og du kan derfor opsætte et nyt affiliate script inkl. omsætningsdata uden at involvere din programmør.

For mere information om Data Layer vil jeg anbefale denne video:

<div class="videoWrapper">
<iframe loading="lazy" width="560" height="315" src="//www.youtube.com/embed/EIph_lai3xc?enablejsapi=1" frameborder="0" allowfullscreen></iframe>
</div>

<h2>Opsætning i Tag Manager</h2>

Nu hvor vi har de grundlæggende elementer i Google Tag Manager på plads, vil jeg gennemgå et par eksempler på, hvordan tracking opsættes i GTM.

<h3>1. Container scriptet</h3>

Det første, der skal opsættes, er container scriptet, som din programmør skal indsætte på alle sider på sitet. Scriptet ser således ud:

<pre><code class="language-html"><!-- Google Tag Manager -->
<noscript>
<iframe src="//www.googletagmanager.com/ns.html?id=GTM-XXXXXX" height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>
<script>
(function(w,d,s,l,i){
w[l]=w[l]||[];
w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});
var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),
dl=l!='dataLayer'?'&amp;l='+l:'';
j.async=true;
j.src= '//www.googletagmanager.com/gtm.js?id='+i+dl;
f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');
</script>
<!-- End Google Tag Manager -->
</code></pre>

Derefter kan vi begynde at opsætte Tags og regler i Tag Managers webinterface.

<h3>2. Google Analytics</h3>

Det første Tag, som opsættes, er Google Analytics. Det skal køre på alle sider, så vi skal bruge en regel til det. Denne regel ser således ud:

<a href="{{ '/assets/images/2021/06/GMT2.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GMT2.png' | relative_url }}" alt="" width="512" height="156" class="aligncenter size-full wp-image-2667" /></a>

Derefter kan vi oprette et Tag med det normale Google Analytics script. Dette script er indbygget i Tag Manager, så der skal du blot vælge Klassisk Google Analytics og indsætte dit konto ID. Den normale Google Analytics tracking er baseret på tracking af sidevisninger, så derfor vælges ”sidevisninger” som sporingstype. Som udløsningsregel vælger du den ”Alle sider”-regel som vi lige har opsat og dermed vil dette Tag blive indlæst på alle sider på sitet. Det ser dermed således ud:

<a href="{{ '/assets/images/2021/06/GTM3.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GTM3-860x380.png' | relative_url }}" alt="" width="860" height="380" class="aligncenter size-large wp-image-2668" /></a>

<h3>3. Google Analytics E-commerce</h3>

Nu bliver det lidt mere spændende, for nu skal vi til at hente informationer fra sitet omkring ordrer og hvilke varer, der er købt og sende dette til Google Analytics. Vi opsætter derfor et Data Layer på kvitteringssiden, som indeholder disse informationer.

Det er vigtigt, at variablerne hedder præcis det samme, som står herunder, da Tag Manager vil bruge <a href="https://support.google.com/tagmanager/answer/3002596" target="_blank" rel="noopener">disse variabelnavne</a>. Dette Data Layer minder meget om den normale e-commerce tracking i Google Analytics og ser således ud.

<pre><code class="language-javascript">dataLayer = [{
    transactionId: "1234",
    transactionAffiliation: "Acme Clothing",
    transactionTotal: "11.99",
    transactionTax: "1.29",
    transactionShipping: "5",
    transactionProducts: [
      {
        sku: "DD44",
        name: "T-Shirt",
        category: "Apparel",
        price: "11.99",
        quantity: "1",
      },
      {
        sku: "AA1243544",
        name: "Socks",
        category: "Apparel",
        price: "9.99",
        quantity: "2",
      }
    ]
  }];
</code></pre>

Når det er sat op, har vi adgang til alle disse informationer i GTM og kan bruge dem til vores e-commerce tracking. Men da vi nu har informationerne i nogle fast definerede variabler, kan vi også bruge dem til andre tracking formål. Det er smart!

Det næste, der skal implementeres, er reglen. Denne regel skal kun være opfyldt, når brugeren lander på kvitteringssiden. Vi bruger derfor den indbyggede makro &#123;&#123;url path&#125;&#125;. Denne regel ser således ud:

<a href="{{ '/assets/images/2021/06/GMT4.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GMT4.png' | relative_url }}" alt="" width="509" height="149" class="aligncenter size-full wp-image-2669" /></a>

Så mangler vi kun det Tag, som skal sende informationerne til Google Analytics. Vi opretter derfor et Tag næsten ligesom det almindelige Google Analytics Tag, men hvor du blot vælger ’Transaktion’, som sporingstype. Når brugeren lander på kvitteringssiden, vil reglen sørge for, at Tagget blive udløst, henter informationer fra det opsatte Data Layer og sender det til Google Analytics som en transaktion:

<a href="{{ '/assets/images/2021/06/GMT5.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GMT5-860x436.png' | relative_url }}" alt="" width="860" height="436" class="aligncenter size-large wp-image-2670" /></a>

<h3>4. AdWords conversion tracking</h3>

Nu bliver det rigtig smart! Nu skal vi have opsat AdWords conversion tracking, som sørger for at sende antal transaktioner og omsætning tilbage til AdWords systemet, så du kan se, hvilke kampagner, der giver dig mest omsætning. Før GTM ville det kræve, at du fik din programmør til at indsætte endnu et script på kvitteringssiden, og omsætningen skulle angives som variabel i scriptet. Men fordi vi har opsat et Data Layer, har vi allerede adgang til denne information i GTM. Vi skal blot lige fange dem via en makro.

Vi går derfor ind og opretter en ny makro og definerer, at den skal hente information fra websitet via et Data Layer og angiver navnet på den variabel i dit Data Layer, den skal hente information fra. I dette tilfælde skal den hente information fra den variabel, som hedder ’transactionTotal’ og indeholder omsætningen:

<a href="{{ '/assets/images/2021/06/GMT6.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GMT6.png' | relative_url }}" alt="" width="618" height="478" class="aligncenter size-full wp-image-2671" /></a>

Den nye makro indeholder nu omsætningen for ordren.

Vi opretter nu et nyt Tag og vælger AdWords Konverteringssporing som Tagtype. Derefter indtaster du dit konverterings ID og konverteringsetiket, som du finder inde i AdWords. Som konverteringsværdi vælges den makro, vi lige har sat op, og som udløsningsregel vælges ’Kvitteringsside’, som vi også brugte til at udløse E-commerce tagget:

<a href="{{ '/assets/images/2021/06/GMT7.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GMT7-860x319.png' | relative_url }}" alt="" width="860" height="319" class="aligncenter size-large wp-image-2672" /></a>

Og så er der AdWords conversion tracking på sitet. Så hurtige er der ingen udviklere der er!

<h3>5. Remarketing scripts</h3>

Når der arbejdes med remarketing scripts, er det smart at segmentere brugerne, så man kan differentiere budskaberne, når man markedsfører sig overfor dem senere hen. En måde at gøre det på er at lave to remarketing segmenter med hvert sit script.

Det ene indsættes på alle sider undtagen kvitteringssiden, og disse brugere vil blive efterfulgt af markedsføring, som skal få dem tilbage på siden og færdiggøre købet. Det andet script indsættes kun på kvitteringssiden og sørger for, at brugerne ikke bliver præsenteret for budskaber, produkter eller ydelser, de lige har købt, men i stedet komplimentære produkter eller ydelser.

I GTM kan regler både bruges som udløsningsregler og blokeringsregler. I det første tilfælde skal ’Alle sider’ dermed bruges som udløsningsregel og ’Kvitteringsside’ bruges som blokeringsregel. Dermed vil scriptet blive indlæst på alle sider undtagen kvitteringssiden. Det andet script, som kun skal køres på kvitteringssiden, behøver ingen blokeringssregel, kun ’kvitteringsside’, som udløsningsregel.

Hvis du bruger et 3. parts værktøj til remarketing, skal du tage det script, du ellers ville få din programmør til at indsætte på siden og i stedet indsætte det i GTM, hvorefter GTM vil indlæse det på siden asynkront, når reglerne er opfyldt. Og det smarte er, at du også kan bruge dine makroer her. Hvis dit remarketing script understøtter, at du sender omsætningen med, så du senere hen kan segmentere på, hvor mange penge dine kunder har købt for, kan du indsætte makroen &#123;&#123;transactionTotal&#125;&#125; nede i scriptet og dermed få omsætningen registreret i dit remarketing værktøj.

<a href="{{ '/assets/images/2021/06/GTM8.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GTM8-860x421.png' | relative_url }}" alt="" width="860" height="421" class="aligncenter size-large wp-image-2673" /></a>

<h3>6. Hændelser / events</h3>

På de fleste websites er der også en række knapper og links, som skal trackes, når brugere klikker på dem. Et eksempel er ’læg i kurv’-knappen, som ofte både findes på varelister og produktsider.

For at kunne tracke, når nogen klikker på knapper, skal vi have flere ting i spil. Det første vi skal bruge, er en funktion, som holder øje med, hvornår brugeren klikker på noget på websitet. Vi opsætter derfor et Tag og kalder det ’Click Listener’ og vælger ’Klikfunktion’, som Tag type.

Dette Tag skal køre på alle sider, dvs. ’Alle sider’ skal være valgt som udløsningsregel. Når en bruger klikker på noget på websitet vil dette Tag sende et event tilbage til GTM, som vi kan ”lytte” på og dermed gøre noget, når brugeren klikker. Det skal vi bruge, når vi skal holde øje med, hvor mange der klikker på ’læg i kurv’-knapperne.

<a href="{{ '/assets/images/2021/06/GMT9.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GMT9.png' | relative_url }}" alt="" width="292" height="405" class="aligncenter size-full wp-image-2674" /></a>

Derefter skal vi kunne identificere knappen, så vi ved, at brugeren har klikket på lige præcis den knap. Knappen kan fx identificeres ved, at den har en bestemt class eller ID, som bruges til styling af knappen. Det kan fx være, at knappen har en class, der hedder ’addToCart’. Vi kan dermed bruge denne class til at holde øje med, om der klikkes på knappen.

Udfordringen er ofte, at knappen på varelisten og produktsiden har samme class. Så vi kan ikke bruge class’en til at differentiere mellem de to knapper. Vi er derfor nødt til at kigge på andre ting samtidig for at være sikre på, hvilken knap de klikker på. Det kan fx være URL’en, hvor et eksempel kan være, at alle produktsider indeholder en parameter med navnet ID, som bruges til at styre hvilket produkt, der vises på siden. Hvis URL’en på varelisten ikke indeholder denne parameter, så kan vi bruge det til at differentiere knapperne, så vi ved, om de klikker på en ’læg i kurv’-knap på en vareliste eller en produktside.

Den regel, vi skal lave for varelister, skal derfor være følgende: Brugeren skal klikke på noget på websitet. Det, brugeren klikker på, skal have en class, der er lig ’addToCart’ og den URL, som brugeren står på, skal ikke indeholde id=. Hvis de tre ting er opfyldt, så kan vi være sikre på, at brugeren har klikket på ’læg i kurv’-knappen på varelisten. Denne regel opsættes således i GTM:

<a href="{{ '/assets/images/2021/06/GTM10.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GTM10.png' | relative_url }}" alt="" width="515" height="233" class="aligncenter size-full wp-image-2675" /></a>

Den første linje er den event, der bliver sendt til GTM, når brugeren klikker på noget. Den sender altså en event tilbage til GTM med værdien ’gtm.click’, hver gang brugeren klikker. Den anden linje er en indbygget makro, som indeholder class’en på det element, der er klikket på, og den skal altså være ’addToCart’ i dette tilfælde. Den sidste linje sikrer, at URL’en ikke indeholder id=, og vi kan dermed være sikre på, at brugeren er på en vareliste.

Reglen for produktsiden ser således ud, hvor den eneste ændring er den sidste linje:

<a href="{{ '/assets/images/2021/06/GTM11.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GTM11.png' | relative_url }}" alt="" width="511" height="233" class="aligncenter size-full wp-image-2676" /></a>

Med de to regler på plads kan vi lave det Tag, som skal registrere klikket som en event/hændelse i Google Analytics. Der oprettes derfor et Tag, hvor ’Klassisk Google Analytics’ vælges som Tagtype og ’Hændelse’ som sporingstype. Derefter kan kategori, handling og etiket udfyldes, ligesom hvis man koder event tracking direkte ind på sitet. Her kan vi så bruge makroer til at indsætte dynamiske værdier, fx den URL, brugeren står på, når han klikker.

Derved kan vi se, hvilke produkter, der oftest bliver lagt i kurven, samt på hvilke varelister brugeren lægger i kurven direkte fra varelisten, og hvilke varelister hvor de ikke gør, fordi de skal ind på produktsiden og læse mere information, før de er klar til at købe.

Det endelige Tag for varelisten ser dermed således ud og den ovenstående regel vælges som udløsningsregel:

<a href="{{ '/assets/images/2021/06/GTM12.png' | relative_url }}"><img src="{{ '/assets/images/2021/06/GTM12.png' | relative_url }}" alt="" width="459" height="692" class="aligncenter size-full wp-image-2677" /></a>

Dermed trackes der et event i Google Analytics, hver gang brugeren klikker på ’læg i kurv’-knappen på en vareliste.

<h2>Opsummering</h2>

Indrømmet, den sidste her er lidt langhåret, men den viser meget godt, hvor fleksibelt Google Tag Manager systemet er, og hvordan det giver mulighed for meget præcis styring af tracking på sitet, så man faktisk kan lave meget avancerede opsætninger.

Dertil kommer alle fordelene med at genbruge informationer, som er tilgængelige via Data Layer på tværs af Google Analytics og 3. parts scripts, samt hastighedsforbedringerne fordi alting indlæses asynkront. Google har dermed lavet endnu et fedt værktøj til webmastere, især for dem, som døjer med besværlige og langsommelige processer, når noget skal ændres på sitet.

For webmastere giver Tag Manager dermed hurtigere reaktionstider, når der fx skal implementeres et nyt remarketing script på sitet, uanset hvor på sitet, det skal implementeres, og de kan på få minutter opsætte tracking af bestemte brugerhandlinger på sitet, når der opstår behov for lidt ekstra data til en beslutning.

Alt sammen noget, der sikrer at webmastere har korrekte data i rigelige mængder til at træffe datadrevne beslutninger i dagligdagen.