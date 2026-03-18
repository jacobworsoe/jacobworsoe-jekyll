---
layout: post
title: Visualisering af Google Analytics data med Excel heatmaps
date: 2019-06-16 11:20:41
slug: visualisering-af-google-analytics-data-med-excel-heatmaps
wordpress_id: 1444
categories:
  - Analytics
---

Lige siden Google Analytics app'en udkom, har den haft en fed måde at visualisere sessioner fordelt på dage og timer.

<figure><a href="{{ '/assets/images/2019/06/GA-mobile-app-sessioner-fordelt-på-dage-timer-v2.png' | relative_url }}"><img src="{{ '/assets/images/2019/06/GA-mobile-app-sessioner-fordelt-på-dage-timer-v2-690x1057.png' | relative_url }}" alt="Google Analytics app&#039;en har altid haft en fed oversigt over timer og dage." width="690" height="1057" class="size-medium wp-image-2018" /></a><figcaption>Google Analytics app'en har altid haft en fed oversigt over timer og dage.</figcaption></figure>

Den har jeg længe savnet i det normale Google Analytics interface og først for nyligt er der kommet mulighed for at se besøgende fordelt på ugen med den nye startside i Google Analytics.

<figure><a href="{{ '/assets/images/GA-web-view-sessioner-fordelt-på-dage-timer.png' | relative_url }}"><img src="{{ '/assets/images/GA-web-view-sessioner-fordelt-på-dage-timer.png' | relative_url }}" alt="Besøgende fordelt på ugen i det normale Google Analytics web interface." width="429" height="704" class="size-full wp-image-1490" /></a><figcaption>Besøgende fordelt på ugen i det normale Google Analytics web interface.</figcaption></figure>

Men besøg er kun én af de vigtige metrics på et website. Der findes mange andre, fx konverteringsrate og basket size, som også er værdifulde at analysere på samme måde. Derfor har jeg lavet en template i Excel som kan vise præcis de tal jeg ønsker - og til sidst i indlægget får du mit Excel ark, så du selv kan få det unikke overblik.

<h2>Indhold</h2>

<ul>
<li><a href="#article-header-id-0"> Konvertering</a></li>
<li><a href="#article-header-id-1"> Basket size</a></li>
<li><a href="#article-header-id-2"> Omsætning</a></li>
<li><a href="#article-header-id-3"> Ordre</a></li>
<li><a href="#article-header-id-4"> Forstå adfærden omkring Black Friday</a></li>
<li><a href="#article-header-id-5"> Få overblikket over dine egne data</a>

<ul>
<li><a href="#article-header-id-6"> 1. Custom Report med de 5 metrics fordelt på dage og timer</a></li>
<li><a href="#article-header-id-7"> 2. Eksportér data</a></li>
<li><a href="#article-header-id-8"> 3. Hent min Excel template</a></li>
<li><a href="#article-header-id-9"> 4. Indsæt dine Google Analytics data i min template</a></li>
</ul></li>
<li><a href="#article-header-id-10"> Tak til Bjarke Bekhøj</a></li>
</ul>

<figure><a href="{{ '/assets/images/one-year-sessions-2.png' | relative_url }}"><img src="{{ '/assets/images/one-year-sessions-2.png' | relative_url }}" alt="Mit eget Excel ark, som viser besøgende (og meget mere) fordelt på ugen." width="846" height="685" class="size-full wp-image-1491" /></a><figcaption>Mit eget Excel ark, som viser besøgende (og meget mere) fordelt på ugen.</figcaption></figure>

Excel arket giver dig mulighed for at se 5 vigtige metrics fordelt på dage og timer:

<ul>
<li>Sessioner</li>
<li>Konvertering</li>
<li>Basket size</li>
<li>Omsætning</li>
<li>Ordre</li>
</ul>

Det hele er opstillet og farvekodet, så du meget nemt kan spotte udsving i dine vigtigste metrics. Ofte er der nemlig nogle helt faste mønstre i hvornår på dagen og ugen kunderne er mest tilbøjelige til at besøge sitet eller udfører bestemte handlinger, fx køb. Jeg har lavet to tabeller med forskellige farvekodning. Den første viser hvor tallene er størst og mindst baseret på hele ugen. Den anden kigger kun på de enkelte dage.

<figure><a href="{{ '/assets/images/one-year-sessions-begge-tabeller-1.png' | relative_url }}"><img src="{{ '/assets/images/one-year-sessions-begge-tabeller-1.png' | relative_url }}" alt="De to tabeller, som viser højeste tal på hele ugen og de enkelte dage." width="1097" height="555" class="size-full wp-image-1495" /></a><figcaption>De to tabeller, som viser højeste tal på hele ugen og de enkelte dage.</figcaption></figure>

Det er rigtig smart hvis du fx har et B2B website, hvor trafikken er meget lavere i weekenden, men du stadig gerne vil kunne se hvornår i weekenden der er flest på websitet. I eksemplet herover er det nemt at se at din kundeservice skal være åben mandag-fredag kl. 7-16, men på fredage kan nogle af dem i kundeservice godt få fri kl. 15. Derudover kan du se at det vil være en god idé at holde øje med mailen lørdag kl. 7-11, samt søndag kl. 9-15. Derefter kan du godt holde weekend :)

Her er et andet eksempel fra en B2C webshop, hvor trafikken tydeligt ligger senere på dagen og om aftenen, dog ikke fredag og lørdag aften, som giver meget god mening. Men også rigtig meget trafik søndag eftermiddag og aften.

<figure><a href="{{ '/assets/images/one-year-sessions-5.png' | relative_url }}"><img src="{{ '/assets/images/one-year-sessions-5.png' | relative_url }}" alt="Besøg på en B2C webshop." width="832" height="633" class="size-full wp-image-1586" /></a><figcaption>Besøg på en B2C webshop.</figcaption></figure>

Et andet eksempel er dette website som oftest bruges tidligt om morgenen og igen om eftermiddagen.

<figure><a href="{{ '/assets/images/one-year-sessions-4.png' | relative_url }}"><img src="{{ '/assets/images/one-year-sessions-4.png' | relative_url }}" alt="Mest trafik tidlig morgen og eftermiddag." width="844" height="634" class="size-full wp-image-1584" /></a><figcaption>Mest trafik tidlig morgen og eftermiddag.</figcaption></figure>

Ved at summere antal sessions på hhv. ugedage og timer kan jeg se de dage og tidspunkter hvor der er flest besøg på min blog. Det kan jeg bruge til at udgive nyt indhold på de dage hvor mine læsere typisk besøger sitet alligevel. Bliver mit indhold om Google Analytics typisk læst i ugedagene eller i weekenden? Det kan jeg bruge til at poste mine nye indlæg på de sociale medier på de bedste dage.

<figure><a href="{{ '/assets/images/2019/06/Mest-besøgte-dage-og-timer-på-jacobworsoe.dk_.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/06/Mest-besøgte-dage-og-timer-på-jacobworsoe.dk_.jpg' | relative_url }}" alt="Der er flest besøgende på min blog mandag og tirsdag." width="833" height="578" class="size-full wp-image-1989" /></a><figcaption>Der er flest besøgende på min blog mandag og tirsdag.</figcaption></figure>

Den nederste række på dette heatmap viser at der er færrest besøgende på min blog i weekenden. Det er bedst at poste nye blogindlæg mandag eller tirsdag.

Den sidste kolonne viser at der er flest besøg i arbejdstiden og ikke om aftenen. Det skal også tænkes ind i SoMe strategien :)

<h2 id="article-header-id-0">Konvertering</h2>

Din konverteringsrate er heller ikke den samme hele ugen. Måske researcher kunderne mest om morgenen og køber om aftenen. Eller også køber de kun i weekenden?

En forståelse for hvornår konverteringen er højst og lavest vil give en bedre forståelse for kunderejsen og købsadfærden for dine kunder.

Hvis den højeste konvertering ligger om aftenen og i weekenden, kan det være et udtryk for at det er et overvejelseskøb, hvor kunderne researcher i løbet af ugen, men købet sker først om aftenen eller i weekenden. Omvendt kan nemme rutinekøb nemt ordnes i løbet af dagen.

Det kan også bruges til at planlægge det bedste tidspunkt at sende nyhedsbreve og måske skal du overveje at byde højere på Adwords på de dage hvor konverteringen er højst, for at være sikker på at få kunderne ind i din shop på de dage hvor de er mest købeklare.

Du kan bruge dette til at se hvornår du SKAL være synlig for kunderne.

<a href="{{ '/assets/images/2019/06/one-year-conversion-2.png' | relative_url }}"><img src="{{ '/assets/images/2019/06/one-year-conversion-2.png' | relative_url }}" alt="" width="898" height="687" class="alignnone size-full wp-image-1896" /></a>

Her er et andet eksempel for en B2B webshop, hvor konverteringen er højest kl. 9-16 i hverdagene, men det er også interessant at søndag aften er bedre end lørdag aften.

<a href="{{ '/assets/images/one-year-conversion.png' | relative_url }}"><img src="{{ '/assets/images/one-year-conversion.png' | relative_url }}" alt="" width="848" height="685" class="alignnone size-full wp-image-1571" /></a>

<h2 id="article-header-id-1">Basket size</h2>

En anden vigtig KPI er basket size, som også kan variere i løbet af ugen. I eksemplet herunder er basket size markant højere onsdag aften, så her kan man også køre med en lidt højere klikpris end normalt og stadig holde en god ROAS. Det er også interessant at se at selvom der typisk ikke bliver købt så meget om natten, så er det faktisk nogle store ordre der bliver lagt om natten.

<figure><a href="{{ '/assets/images/one-year-basket-size.png' | relative_url }}"><img src="{{ '/assets/images/one-year-basket-size.png' | relative_url }}" alt="Basket size er størst onsdag aften." width="850" height="687" class="size-full wp-image-1573" /></a><figcaption>Basket size er størst onsdag aften.</figcaption></figure>

<h2 id="article-header-id-2">Omsætning</h2>

Sessioner, konvertering og basket size er altid kritiske KPI'er at have styr på, fordi de tilsammen giver omsætningen.

<code>Sessioner x konverteringsrate x basket size = omsætning</code>

Det er også vigtigt at vide hvordan omsætningen fordeler sig over ugen. Det kan fx være nyttigt hvis du skal får brug for at lave en planlagt opdatering hvor sitet vil være nede i en periode. Hvis du ikke kan gøre det om natten, så er det vigtigt at vide hvornår der typisk er lavest omsætning.

<h2 id="article-header-id-3">Ordre</h2>

Afhængigt af ordrestørrelsen er det ikke nødvendigvis samme time hvor der er højst omsætning og flest ordre. Hvis du har et team der pakker ordre, så kan du bruge ordreoversigten til at se hvornår der typisk skal pakkes flest ordre.

<h2 id="article-header-id-4">Forstå adfærden omkring Black Friday</h2>

Indtil nu har jeg kigget på data for et helt år for at se på de store tendenser, renset for sæsonudsving. Men det kan også være interessant at zoome ind på fx perioden omkring Black Friday. Herunder ses et typisk eksempel jeg har set på mange shops hvor konverteringen er helt i bund i ugen op til Black Friday men tårnhøj hele fredagen og især i de sidste timer, hvor det er ved at være sidste chance for at få et godt tilbud.

<figure><a href="{{ '/assets/images/black-friday-week-conversion-2.png' | relative_url }}"><img src="{{ '/assets/images/black-friday-week-conversion-2.png' | relative_url }}" alt="Konvertering i Black Friday ugen." width="855" height="688" class="size-full wp-image-1590" /></a><figcaption>Konvertering i Black Friday ugen.</figcaption></figure>

I forhold til at få serverne til at holde til presset fra de mange besøgende, så er det interessant at den time med flest besøg faktisk er torsdag aften, hvor kunderne ser om tilbudene er offentliggjort. Det er vildt at se at trafikken på en enkelt time er mere end 5 gange højere end de andre "normale" aftener på ugen! Så der er pres på serverne allerede om torsdagen.

<figure><a href="{{ '/assets/images/black-friday-week-sessions.png' | relative_url }}"><img src="{{ '/assets/images/black-friday-week-sessions.png' | relative_url }}" alt="Der er mange besøg på sitet torsdag før Black Friday." width="852" height="689" class="size-full wp-image-1591" /></a><figcaption>Der er mange besøg på sitet torsdag før Black Friday.</figcaption></figure>

<h2 id="article-header-id-5">Få overblikket over dine egne data</h2>

For at få overblikket over dine egne data, skal der gøres følgende:

<ol>
<li>Lav en Custom Report i Google Analytics</li>
<li>Eksportér data til Excel</li>
<li>Hent min Excel template</li>
<li>Indsæt dine Google Analytics data i min template</li>
<li>Se de tre faner som viser de tre KPI'er</li>
</ol>

<h3 id="article-header-id-6">1. Custom Report med de 5 metrics fordelt på dage og timer</h3>

Her er den custom report der skal laves for at kunne eksportere de data der skal bruges. Det er vigtigt at metrics står i samme rækkefølge som herunder, for at Excel skabelonen virker.

<figure><a href="{{ '/assets/images/Custom-report-settings-1.png' | relative_url }}"><img src="{{ '/assets/images/Custom-report-settings-1.png' | relative_url }}" alt="Custom Report med de data der skal bruges." width="1184" height="536" class="size-full wp-image-1634" /></a><figcaption>Custom Report med de data der skal bruges.</figcaption></figure>

På dansk hedder felterne det her (Tak til RNA for at forslå dette i kommentarerne):

<figure><a href="{{ '/assets/images/2019/06/Custom-report-settings-da.png' | relative_url }}"><img src="{{ '/assets/images/2019/06/Custom-report-settings-da.png' | relative_url }}" alt="Felternes danske navne i Custom Reports." width="1020" height="466" class="size-full wp-image-1661" /></a><figcaption>Felternes danske navne i Custom Reports.</figcaption></figure>

I rapporten vælger du "Hour" eller "Time" på dansk som Secondary Dimension. Derefter skulle der gerne komme 168 rækker (7 dage x 24 timer). Derfor skal du vælge at vise 250 rækker i bunden, for at alle rækkerne kommer med når du eksporterer til Excel.

<figure><a href="{{ '/assets/images/custom-report-secondary-dimension-rows.png' | relative_url }}"><img src="{{ '/assets/images/custom-report-secondary-dimension-rows.png' | relative_url }}" alt="Vælg 250 rows i bunden, for at se alle 168 rækker med data for alle timer på alle dage." width="1533" height="757" class="size-full wp-image-1502" /></a><figcaption>Vælg 250 rows i bunden, for at se alle 168 rækker med data for alle timer på alle dage.</figcaption></figure>

Som udgangspunkt kan du vælge data for et helt år, for at undgå sæsonudsving. Det vigtige er at du vælger en periode på et helt antal uger, så der er lige mange mandage, tirsdage, etc. i datasættet.

<h3 id="article-header-id-7">2. Eksportér data</h3>

Oppe i højre hjørne eksporterer du data til Excel.

<a href="{{ '/assets/images/Custom-report-export-1.png' | relative_url }}"><img src="{{ '/assets/images/Custom-report-export-1.png' | relative_url }}" alt="" width="1077" height="602" class="alignnone size-full wp-image-1639" /></a>

<h3 id="article-header-id-8">3. Hent min Excel template</h3>

<a href="{{ '/assets/images/Google-Analytics-heatmap-template.xlsx' | relative_url }}">Google Analytics heatmap template</a>

<h3 id="article-header-id-9">4. Indsæt dine Google Analytics data i min template</h3>

Åbn den Excel fil du eksporterede med dine egne data og vælg den 2. fane i bunden. Markér alle data med Ctrl + A (eller CMD + A på Mac) og kopiér dataene.

Download og åbn min Excel template og vælg fanen <em>Google Analytics export</em>. Vælg den første celle (A1) og indsæt alle dine data, så alle de eksisterende data overskrives.

Derefter kan du se de forskellige KPI'er i de efterfølgende faner og forhåbentlig lære noget nyt om adfærden på dit website.

<h2 id="article-header-id-10">Tak til Bjarke Bekhøj</h2>

Inspirationen til denne Excel template kommer fra min gode ven og tidligere kollega <a href="https://www.linkedin.com/in/bjarkebekhoj/" rel="noopener noreferrer" target="_blank">Bjarke Bekhøj</a>. På <a href="http://dmkonf.dk/" rel="noopener noreferrer" target="_blank">Digital Markedsføring 2014 i Holstebro</a> lavede han et super fedt indlæg med "37 konkrete tips til webshoppen" og tip nummer 3 så således ud:

<figure><a href="{{ '/assets/images/bjarke-bekhøj-tip-3.png' | relative_url }}"><img src="{{ '/assets/images/bjarke-bekhøj-tip-3.png' | relative_url }}" alt="Bjarke Bekhøjs tip nummer 3 som inspirerede dette indlæg." width="959" height="686" class="size-full wp-image-1503" /></a><figcaption>Bjarke Bekhøjs tip nummer 3 som inspirerede dette indlæg.</figcaption></figure>

Super god idé fra den altid kreative Bjarke. Her har jeg taget den idé og udvidet med nogle flere metrics, samt gjort det utrolig nemt for dig at få det samme overblik.