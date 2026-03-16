---
layout: post
title: ITP og Google Analytics
date: 2019-11-06 21:56:19
slug: itp-og-google-analytics
categories:
  - Analytics
---

<p>Dette indlæg er for dig der har Google Analytics og gerne vil vide hvordan det påvirker dine Google Analytics data.</p>
<p>Der er skrevet meget om ITP, men lad mig lige starte med at opridse de store milepæle i ITP:</p>
<ul>
<li><strong><a href="https://webkit.org/blog/7675/intelligent-tracking-prevention/">ITP 1:</a></strong> Begrænser levetiden af 3. parts cookies</li>
<li><strong><a href="https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/">ITP 2.1:</a></strong> Begrænser levetiden af  1. parts cookies (dvs. også Google Analytics)</li>
<li><strong><a href="https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/">ITP 2.3:</a></strong> Begrænser levetiden af localStorage</li>
</ul>
<p>Sådan ser udrulningen af de forskellige ITP-versioner ud på <a href="https://www.googlemerchandisestore.com/" rel="noopener noreferrer">Google Merchandise Store</a>. Det er interessant at ITP 1.1 kun blev rullet ud til desktop brugere, mens mobile fortsatte på ITP 1.0.</p>
<div id="attachment_2446" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2446" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout-860x456.jpg" alt="ITP roll-out: Ugentlige besøg pr. ITP version" width="860" height="456" class="size-large wp-image-2446" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout-860x456.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout-690x366.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout-768x407.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/itp-rollout.jpg 1398w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2446" class="wp-caption-text">ITP roll-out: Ugentlige besøg pr. ITP version</p></div>
<ol>
<li>parts cookies har med ITP 2.1 en levetid på 7 dage &#8211; men kun hvis de sættes client-side med JavaScript via <code class="" data-line="">document.cookie</code>.</li>
</ol>
<p>Google Analytics bruger (og har altid brugt) en 1. parts cookie sat med JavaScript. Fra og med ITP 2.1 har din Google Analytics cookie en levetid på 7 dage.</p>
<h2>Hvor meget bliver dine Google Analytics data ødelagt af ITP?</h2>
<p>Der er primært fire måder ITP kan ødelægge dine data:</p>
<ol>
<li>Nye vs. tilbagevendende besøg</li>
<li>Sessioner pr. bruger</li>
<li>Attribuering over tid</li>
<li>Målgrupper til annoncering</li>
</ol>
<h3>1. Nye vs. tilbagevendende besøg</h3>
<p>Fordi <code class="" data-line="">_ga</code> cookien slettes efter 7 dage istedet for 2 år, kan andelen af nye besøgende i Google Analytics stige.</p>
<p>Jeg har kigget på hvordan det ser ud i praksis, for de forskellige ITP-versioner.</p>
<p>Som det kan ses herover er der stor forskel på hvor længe ITP-versionerne har eksisteret. Jeg har derfor udregnet andelen af nye besøg pr. uge og fjernet alle de uger hvor der var mindre en 50 besøg fra hver enkelt ITP-version.</p>
<p>Jeg har derefter taget gennemsnittet af alle ugerne. Bemærk at <a href="https://www.youtube.com/watch?v=14VYnFhBKcY">Y-aksen ikke starter ved 0</a>.</p>
<div id="attachment_1965" style="width: 1180px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1965" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version.jpg" alt="Andel nye besgøende pr. ITP-version" width="1170" height="652" class="size-full wp-image-1965" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version.jpg 1170w, https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version-690x385.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version-768x428.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/09/Andel-nye-besgøende-pr.-ITP-version-725x404.jpg 725w" sizes="auto, (max-width: 1170px) 100vw, 1170px" /></a><p id="caption-attachment-1965" class="wp-caption-text">Andel nye besgøende pr. ITP-version</p></div>
<p>Forventningen er at der sker en markant stigning ved ITP 2.1, men som det ses herover er det ikke tilfældet.</p>
<p>Underligt nok er andelen højest ved ITP 1.0.</p>
<p>Fra ITP 1.1 og frem stiger andelen af nye besøg ved hver ny ITP version, men altså ikke nogen markant stigning ved ITP 2.1.</p>
<p>Det ændrer sig dog markant, når jeg bryder det ned på device.</p>
<div id="attachment_1966" style="width: 1116px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1966" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device.jpg" alt="Andel nye besgøende pr. ITP-version og device" width="1106" height="568" class="size-full wp-image-1966" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device.jpg 1106w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device-690x354.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device-768x394.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Andel-nye-besgøende-pr.-ITP-version-og-device-725x372.jpg 725w" sizes="auto, (max-width: 1106px) 100vw, 1106px" /></a><p id="caption-attachment-1966" class="wp-caption-text">Andel nye besgøende pr. ITP-version og device</p></div>
<p>Her stiger andelen af nye besøgende meget mere i de nyeste ITP-versioner. Men kun på desktop!</p>
<p>Tværtimod falder andelen af nye besøg på mobile. Meget overraskende. Det hænger slet ikke sammen med forventningen. Virker ITP anderledes på mobile og desktop?</p>
<p>Mere om det senere!</p>
<h3>2. Sessioner pr. bruger</h3>
<p>Når cookies slettes efter 7 dage, vil antallet af unikke brugere på dit website stige og blive kunstigt højt.</p>
<p>Samtidig betyder det at antallet af sessioner pr. bruger blive lavere end det i virkeligheden her.</p>
<p>Det ser sådan her ud pr. ITP-version og device.</p>
<div id="attachment_1970" style="width: 919px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1970" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device.jpg" alt="Sessioner pr. bruger fordelt på ITP-version og device" width="909" height="462" class="size-full wp-image-1970" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device.jpg 909w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device-690x351.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device-768x390.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Sessioner-pr.-bruger-fordelt-på-ITP-version-og-device-725x368.jpg 725w" sizes="auto, (max-width: 909px) 100vw, 909px" /></a><p id="caption-attachment-1970" class="wp-caption-text">Sessioner pr. bruger fordelt på ITP-version og device</p></div>
<p>Bemærk igen hvordan mobile og desktop påvirkes forskellige i de nyeste ITP-versioner.</p>
<p>Det skal vi have kigget på og jeg skal nok komme tilbage til det. Det lover jeg!</p>
<p>Men vi skal lige se på de sidste to måder ITP påvirker dine GA data.</p>
<h3>3. Attribuering</h3>
<p>Når cookies slettes efter 7 dage, kan du ikke lave korrekte analyser af kunderejser, hvor der er længere end 7 dage mellem de enkelte besøg. Særligt er der risiko for at du ikke attribuere salg og omsætning til de kanaler der ligger tidligt i kunderejsen. Men det påvirker ikke din last-click attribuering.</p>
<h3>Last click påvirkes ikke af ITP</h3>
<p>Dette er en vigtig pointe. De senere år er der kommet stor fokus på forskellige attributionsmodeller og det faktum at last click attribuering ikke tilskriver den korrekte værdi til de kanaler og marketing kanaler der typisk ligger tidligt i købsrejsen.</p>
<p>Det er rigtig godt, men det er også besværligt. Og derfor bliver der stadig ofte brugt last click attribuering i mange analyser. Og disse analyser vil ikke blive påvirket af ITP.</p>
<p>I hvert fald kun meget lidt. For der er jo lige den finte at Google Analytics ikke bruger last click som standard. Den bruger last non-direct click.</p>
<h3>Udelad Safari?</h3>
<p>Men måske kan du bare udelade Safari fra disse analyser?</p>
<p>Det kan du formentlig godt på desktop trafik, hvor Safari udgør en rimelig lille andel.</p>
<p>Lad os lige trække nogle friske tal på browsernes markedsandele på desktop og mobile for september 2019.</p>
<div id="attachment_1971" style="width: 911px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1971" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device.jpg" alt="Browser markedsandele pr. device" width="901" height="425" class="size-full wp-image-1971" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device.jpg 901w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device-690x325.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device-768x362.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Browser-markedsandele-pr.-device-725x342.jpg 725w" sizes="auto, (max-width: 901px) 100vw, 901px" /></a><p id="caption-attachment-1971" class="wp-caption-text">Browser markedsandele pr. device</p></div>
<p>Safari har kun 5% markedsandel på desktop, så der kan du nok godt klare dig, ved at lave analysen på de resterende 95%.</p>
<p>Men hvad med mobil trafik? Her er Safari 36% af trafikken.</p>
<p>Og desktop og mobil bør analyseres særskilt, da kunderejsen kan være meget forskellig.</p>
<p>De ovenstående tal er som nævnt fra <a href="https://www.googlemerchandisestore.com/" rel="noopener noreferrer">Google Merchandise Store</a>. Det er anderledes i Danmark. Sådan her ser fordelingen ud for <a href="https://www.jacobworsoe.dk/">jacobworsoe.dk</a> hvor desktop er næsten identisk med en meget stor markedsandel til Chrome, men der er langt flere iPhones i Danmark og dermed udgør Safari på mobile 62% af trafikken.</p>
<p>Det er altså en stor del af trafikken, hvor data nu er forkerte!</p>
<div id="attachment_2620" style="width: 870px" class="wp-caption aligncenter"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2620" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_-860x441.jpg" alt="Browser markedsandele pr. device (jacobworsoe.dk)" width="860" height="441" class="size-large wp-image-2620" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_-860x441.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_-690x354.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_-768x394.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Browser-markedsandele-pr.-device-jacobworsoe.dk_.jpg 1522w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2620" class="wp-caption-text">Browser markedsandele pr. device (jacobworsoe.dk)</p></div>
<h3>4. Målgrupper til annoncering</h3>
<p>Du kan godt løse ITP for dit eget site. Men andre sites er stadig berørt. Det betyder fx at Google Ads Custom Intent kampagner og lignende, hvor du rammer brugere baseret på hvilke andre websites de har besøgt, ikke virker nær så godt længere, fordi cookies bliver slettet efter 7 dage. Det samme gælder målgrupper baseret på de <a href="https://support.google.com/analytics/answer/2799357?hl=en">demografiske data</a>, såsom alder, køn og interesser, som er tilgængelige i Google Analytics.</p>
<h2>Er ITP udrullet på mobile enheder?</h2>
<p>Okay, nu skal vi lige have kigget hvad der sker med de der mobile enheder.</p>
<p>Jeg har crunchet rigtig meget ITP-data de siden <a href="https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/" rel="noopener noreferrer">ITP 2.1 ramte i februar 2019</a> og jeg oplevede flere gange at det var svært at se den forventede effekt af ITP på mobile enheder.</p>
<p>Jeg opsatte derfor en test, hvor jeg besøgte et site fra min iPhone. Jeg lavede en række besøg med mere end 7 dage mellem hvert besøg.</p>
<p>På sitet fanger jeg brugerens Client ID (Cookie ID) og gemmer det i en custom dimension. Dermed kan jeg se om Client ID forbliver det samme i alle besøgene og dermed om cookien slettes.</p>
<p>Resultatet ser således ud. Jeg har lavet 7 besøg fra 10. juli til 2. oktober og der er mindst 7 dage mellem alle besøgene. Client ID forbliver det samme, så cookien slettes ikke.</p>
<div id="attachment_1973" style="width: 1407px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1973" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg.jpg" alt="GA cookie bevares mellem besøg." width="1397" height="401" class="size-full wp-image-1973" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg.jpg 1397w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg-690x198.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg-768x220.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-cookie-bevares-mellem-7-dage-besøg-725x208.jpg 725w" sizes="auto, (max-width: 1397px) 100vw, 1397px" /></a><p id="caption-attachment-1973" class="wp-caption-text">GA cookie bevares mellem besøg.</p></div>
<p>Lad os tjekke hvad cookiens levetid bliver sat til.</p>
<p>Ved at koble din iPhone sammen med din Mac med et kabel, kan du bruge Developer Tools i Safari på Mac&#8217;en til at debugge det der sker på telefonen. Dermed kan du fx se de cookies der bliver sat på din telefon.</p>
<p>Herunder ses et flot stykke grafisk arbejde, som viser levetiden på _ga cookien på hhv. Mac (2 år) og iPhone (7 dage). Bemærk at &#8220;Prevent Cross-Site Tracking&#8221; er aktiveret på iPhonen, som er det der aktiverer ITP.</p>
<div id="attachment_1974" style="width: 1154px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1974" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry.png" alt="_ga cookien levetid på hhv. Mac og iPhone." width="1144" height="747" class="size-full wp-image-1974" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry.png 1144w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry-690x451.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry-768x501.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/ITP-iOS-safari-2-years-cookie-expiry-725x473.png 725w" sizes="auto, (max-width: 1144px) 100vw, 1144px" /></a><p id="caption-attachment-1974" class="wp-caption-text">_ga cookien levetid på hhv. Mac og iPhone.</p></div>
<p>Lad os lige opsummere.</p>
<ol>
<li>Andelen af nye besøg og besøg pr. bruger har ikke ændret sig som forventet på mobile i de seneste ITP-versioner.</li>
<li>Client ID er det samme, selvom der går mere end 7 dage mellem besøgene på iPhone.</li>
<li>_ga cookien bliver begrænset til 7 dage på Mac, men på iPhone er den stadig 2 år.</li>
</ol>
<p>3 ting der peger i retning af at ITP endnu ikke er aktiveret på mobile enheder.</p>
<p>De to sidste af disse observationer er dog kun lavet på min telefon. Måske er min telefon bare en del af en kontrolgruppe, hvor ITP ikke er aktiveret endnu? Det er ikke utænkeligt. Hvis jeg var Apple, så ville jeg heller ikke rulle ITP ud til 100% af brugerne.</p>
<p>Istedet ville det være naturligt at beholde fx 10% af brugerne i en kontrolgruppe, til at måle hvordan ITP påvirker adfærden i Safari, hvor brugeroplevelsen på nettet generelt vil være langt mindre personaliseret og relevant.</p>
<p>Måske er det bare det der sker?</p>

