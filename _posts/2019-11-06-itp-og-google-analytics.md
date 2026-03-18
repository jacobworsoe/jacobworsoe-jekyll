---
layout: post
title: ITP og Google Analytics
date: 2019-11-06 21:56:19
slug: itp-og-google-analytics
wordpress_id: 2001
categories:
  - Analytics
---

Dette indlæg er for dig der har Google Analytics og gerne vil vide hvordan det påvirker dine Google Analytics data.

Der er skrevet meget om ITP, men lad mig lige starte med at opridse de store milepæle i ITP:

<ul>
<li><strong><a href="https://webkit.org/blog/7675/intelligent-tracking-prevention/">ITP 1:</a></strong> Begrænser levetiden af 3. parts cookies</li>
<li><strong><a href="https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/">ITP 2.1:</a></strong> Begrænser levetiden af  1. parts cookies (dvs. også Google Analytics)</li>
<li><strong><a href="https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/">ITP 2.3:</a></strong> Begrænser levetiden af localStorage</li>
</ul>

Sådan ser udrulningen af de forskellige ITP-versioner ud på <a href="https://www.googlemerchandisestore.com/" rel="noopener noreferrer">Google Merchandise Store</a>. Det er interessant at ITP 1.1 kun blev rullet ud til desktop brugere, mens mobile fortsatte på ITP 1.0.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout-860x456.jpg" alt="ITP roll-out: Ugentlige besøg pr. ITP version" width="860" height="456" class="size-large wp-image-2446" /></a><figcaption>ITP roll-out: Ugentlige besøg pr. ITP version</figcaption></figure>

<ol>
<li>parts cookies har med ITP 2.1 en levetid på 7 dage - men kun hvis de sættes client-side med JavaScript via <code>document.cookie</code>.</li>
</ol>

Google Analytics bruger (og har altid brugt) en 1. parts cookie sat med JavaScript. Fra og med ITP 2.1 har din Google Analytics cookie en levetid på 7 dage.

<h2>Hvor meget bliver dine Google Analytics data ødelagt af ITP?</h2>

Der er primært fire måder ITP kan ødelægge dine data:

<ol>
<li>Nye vs. tilbagevendende besøg</li>
<li>Sessioner pr. bruger</li>
<li>Attribuering over tid</li>
<li>Målgrupper til annoncering</li>
</ol>

<h3>1. Nye vs. tilbagevendende besøg</h3>

Fordi <code>_ga</code> cookien slettes efter 7 dage istedet for 2 år, kan andelen af nye besøgende i Google Analytics stige.

Jeg har kigget på hvordan det ser ud i praksis, for de forskellige ITP-versioner.

Som det kan ses herover er der stor forskel på hvor længe ITP-versionerne har eksisteret. Jeg har derfor udregnet andelen af nye besøg pr. uge og fjernet alle de uger hvor der var mindre en 50 besøg fra hver enkelt ITP-version.

Jeg har derefter taget gennemsnittet af alle ugerne. Bemærk at <a href="https://www.youtube.com/watch?v=14VYnFhBKcY">Y-aksen ikke starter ved 0</a>.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version.jpg" alt="Andel nye besgøende pr. ITP-version" width="1170" height="652" class="size-full wp-image-1965" /></a><figcaption>Andel nye besgøende pr. ITP-version</figcaption></figure>

Forventningen er at der sker en markant stigning ved ITP 2.1, men som det ses herover er det ikke tilfældet.

Underligt nok er andelen højest ved ITP 1.0.

Fra ITP 1.1 og frem stiger andelen af nye besøg ved hver ny ITP version, men altså ikke nogen markant stigning ved ITP 2.1.

Det ændrer sig dog markant, når jeg bryder det ned på device.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device.jpg" alt="Andel nye besgøende pr. ITP-version og device" width="1106" height="568" class="size-full wp-image-1966" /></a><figcaption>Andel nye besgøende pr. ITP-version og device</figcaption></figure>

Her stiger andelen af nye besøgende meget mere i de nyeste ITP-versioner. Men kun på desktop!

Tværtimod falder andelen af nye besøg på mobile. Meget overraskende. Det hænger slet ikke sammen med forventningen. Virker ITP anderledes på mobile og desktop?

Mere om det senere!

<h3>2. Sessioner pr. bruger</h3>

Når cookies slettes efter 7 dage, vil antallet af unikke brugere på dit website stige og blive kunstigt højt.

Samtidig betyder det at antallet af sessioner pr. bruger blive lavere end det i virkeligheden her.

Det ser sådan her ud pr. ITP-version og device.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device.jpg" alt="Sessioner pr. bruger fordelt på ITP-version og device" width="909" height="462" class="size-full wp-image-1970" /></a><figcaption>Sessioner pr. bruger fordelt på ITP-version og device</figcaption></figure>

Bemærk igen hvordan mobile og desktop påvirkes forskellige i de nyeste ITP-versioner.

Det skal vi have kigget på og jeg skal nok komme tilbage til det. Det lover jeg!

Men vi skal lige se på de sidste to måder ITP påvirker dine GA data.

<h3>3. Attribuering</h3>

Når cookies slettes efter 7 dage, kan du ikke lave korrekte analyser af kunderejser, hvor der er længere end 7 dage mellem de enkelte besøg. Særligt er der risiko for at du ikke attribuere salg og omsætning til de kanaler der ligger tidligt i kunderejsen. Men det påvirker ikke din last-click attribuering.

<h3>Last click påvirkes ikke af ITP</h3>

Dette er en vigtig pointe. De senere år er der kommet stor fokus på forskellige attributionsmodeller og det faktum at last click attribuering ikke tilskriver den korrekte værdi til de kanaler og marketing kanaler der typisk ligger tidligt i købsrejsen.

Det er rigtig godt, men det er også besværligt. Og derfor bliver der stadig ofte brugt last click attribuering i mange analyser. Og disse analyser vil ikke blive påvirket af ITP.

I hvert fald kun meget lidt. For der er jo lige den finte at Google Analytics ikke bruger last click som standard. Den bruger last non-direct click.

<h3>Udelad Safari?</h3>

Men måske kan du bare udelade Safari fra disse analyser?

Det kan du formentlig godt på desktop trafik, hvor Safari udgør en rimelig lille andel.

Lad os lige trække nogle friske tal på browsernes markedsandele på desktop og mobile for september 2019.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device.jpg" alt="Browser markedsandele pr. device" width="901" height="425" class="size-full wp-image-1971" /></a><figcaption>Browser markedsandele pr. device</figcaption></figure>

Safari har kun 5% markedsandel på desktop, så der kan du nok godt klare dig, ved at lave analysen på de resterende 95%.

Men hvad med mobil trafik? Her er Safari 36% af trafikken.

Og desktop og mobil bør analyseres særskilt, da kunderejsen kan være meget forskellig.

De ovenstående tal er som nævnt fra <a href="https://www.googlemerchandisestore.com/" rel="noopener noreferrer">Google Merchandise Store</a>. Det er anderledes i Danmark. Sådan her ser fordelingen ud for <a href="https://www.jacobworsoe.dk/">jacobworsoe.dk</a> hvor desktop er næsten identisk med en meget stor markedsandel til Chrome, men der er langt flere iPhones i Danmark og dermed udgør Safari på mobile 62% af trafikken.

Det er altså en stor del af trafikken, hvor data nu er forkerte!

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_-860x441.jpg" alt="Browser markedsandele pr. device (jacobworsoe.dk)" width="860" height="441" class="size-large wp-image-2620" /></a><figcaption>Browser markedsandele pr. device (jacobworsoe.dk)</figcaption></figure>

<h3>4. Målgrupper til annoncering</h3>

Du kan godt løse ITP for dit eget site. Men andre sites er stadig berørt. Det betyder fx at Google Ads Custom Intent kampagner og lignende, hvor du rammer brugere baseret på hvilke andre websites de har besøgt, ikke virker nær så godt længere, fordi cookies bliver slettet efter 7 dage. Det samme gælder målgrupper baseret på de <a href="https://support.google.com/analytics/answer/2799357?hl=en">demografiske data</a>, såsom alder, køn og interesser, som er tilgængelige i Google Analytics.

<h2>Er ITP udrullet på mobile enheder?</h2>

Okay, nu skal vi lige have kigget hvad der sker med de der mobile enheder.

Jeg har crunchet rigtig meget ITP-data de siden <a href="https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/" rel="noopener noreferrer">ITP 2.1 ramte i februar 2019</a> og jeg oplevede flere gange at det var svært at se den forventede effekt af ITP på mobile enheder.

Jeg opsatte derfor en test, hvor jeg besøgte et site fra min iPhone. Jeg lavede en række besøg med mere end 7 dage mellem hvert besøg.

På sitet fanger jeg brugerens Client ID (Cookie ID) og gemmer det i en custom dimension. Dermed kan jeg se om Client ID forbliver det samme i alle besøgene og dermed om cookien slettes.

Resultatet ser således ud. Jeg har lavet 7 besøg fra 10. juli til 2. oktober og der er mindst 7 dage mellem alle besøgene. Client ID forbliver det samme, så cookien slettes ikke.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg.jpg" alt="GA cookie bevares mellem besøg." width="1397" height="401" class="size-full wp-image-1973" /></a><figcaption>GA cookie bevares mellem besøg.</figcaption></figure>

Lad os tjekke hvad cookiens levetid bliver sat til.

Ved at koble din iPhone sammen med din Mac med et kabel, kan du bruge Developer Tools i Safari på Mac'en til at debugge det der sker på telefonen. Dermed kan du fx se de cookies der bliver sat på din telefon.

Herunder ses et flot stykke grafisk arbejde, som viser levetiden på _ga cookien på hhv. Mac (2 år) og iPhone (7 dage). Bemærk at "Prevent Cross-Site Tracking" er aktiveret på iPhonen, som er det der aktiverer ITP.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry.png" alt="_ga cookien levetid på hhv. Mac og iPhone." width="1144" height="747" class="size-full wp-image-1974" /></a><figcaption>_ga cookien levetid på hhv. Mac og iPhone.</figcaption></figure>

Lad os lige opsummere.

<ol>
<li>Andelen af nye besøg og besøg pr. bruger har ikke ændret sig som forventet på mobile i de seneste ITP-versioner.</li>
<li>Client ID er det samme, selvom der går mere end 7 dage mellem besøgene på iPhone.</li>
<li>_ga cookien bliver begrænset til 7 dage på Mac, men på iPhone er den stadig 2 år.</li>
</ol>

3 ting der peger i retning af at ITP endnu ikke er aktiveret på mobile enheder.

De to sidste af disse observationer er dog kun lavet på min telefon. Måske er min telefon bare en del af en kontrolgruppe, hvor ITP ikke er aktiveret endnu? Det er ikke utænkeligt. Hvis jeg var Apple, så ville jeg heller ikke rulle ITP ud til 100% af brugerne.

Istedet ville det være naturligt at beholde fx 10% af brugerne i en kontrolgruppe, til at måle hvordan ITP påvirker adfærden i Safari, hvor brugeroplevelsen på nettet generelt vil være langt mindre personaliseret og relevant.

Måske er det bare det der sker?