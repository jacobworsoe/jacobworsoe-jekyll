---
layout: post
title: Kør en test på tværs af dit website
date: 2009-12-06 01:03:58
slug: kor-en-test-pa-tvaers-af-dit-website
wordpress_id: 4
categories:
  - Konverteringsoptimering
---

Normalt når man bruger Google Website Optimizer (GWO) til at teste et website, så tester man en enkelt side af gangen, f.eks. en specifik landingpage med en meget høj bouncerate. Men nogle gange vil man gerne teste elementer på tværs af hele sitet. Det kan f.eks. være "Køb"-knappen, linket til kontaktformularen eller måske hele navigationen. I de tilfælde kan det være smart at køre testen på tværs af hele sitet. Det er der primært to grunde til:

<ul>
<li>Du får mere trafik at basere din test på ved at køre den på samtlige sider.</li>
<li>Din test bliver meget mere konsistent, så en bruger får samme menu/knap/link at se på alle de sider han besøger.
</ul>
Umiddelbart er det dog ikke muligt at lave det med Google Website Optimizer, da man kun kan indtaste en test URL når man opsætter sin test. Det kan dog lave sig gøre med et lille "hack".</li>
</ul>

<h2>Løsningen</h2>

Hele finten i dette trick går ud på at GWO faktisk slet ikke bruger din test URL til noget som helst når først testen kører. Det eneste formål den har er at Google bruger den til at validere at <em>Control Scriptet</em> og <em>Tracking Scriptet</em> kan findes på siden. Efter Google har sikret sig at scriptet er på plads, så bliver den URL faktisk ikke brugt mere. Det vil altså sige at testen ikke kun bliver kørt på den ene side, men faktisk på alle de sider hvor scriptet er placeret. Hvis man f.eks. indtaster index.html som Test Page under opsætningen men indsætter scriptet på både index.html og kontakt.html, så er det altså ligemeget om brugeren besøger index.html eller kontakt.html - testen bliver kørt på begge sider. Det kan godt virke lidt kringlet, så vi tager lige et praktisk eksempel:

<h2>Et praktisk eksempel</h2>

Jeg driver til dagligt et linkkatalog hvor brugere kan tilmelde et link og få noget linkjuice tilbage. Derfor er det selvfølgelig vigtigt at det er nemt for brugeren at finde formularen hvor man kan tilmelde sit link. Min menu ser som udgangpunkt således ud:

<a href="http://www.jacobworsoe.dk/wp-content/uploads/original.jpg"><img class="alignnone size-full wp-image-5 no-border" title="original" alt="" src="http://www.jacobworsoe.dk/wp-content/uploads/original.jpg" width="387" height="65" /></a>

Den menu fungerer jo meget godt, men set i det lys at "Tilmeld link" er mit <em>Most Wanted Response</em>, så bør den være meget mere fremtrædende i forhold til de andre punkter i menuen. Derfor besluttede jeg at give det link en henholdsvis grøn og rød farve og teste det op mod originalen:

<a href="http://www.jacobworsoe.dk/wp-content/uploads/green.jpg"><img class="alignnone size-full wp-image-6 no-border" title="green" alt="" src="http://www.jacobworsoe.dk/wp-content/uploads/green.jpg" width="387" height="65" /></a>

<a href="http://www.jacobworsoe.dk/wp-content/uploads/red.jpg"><img class="alignnone size-full wp-image-7 no-border" title="red" alt="" src="http://www.jacobworsoe.dk/wp-content/uploads/red.jpg" width="386" height="65" /></a>
Det er jo et noget stærkere Call-To-Action og samtidig kan vi også lige få testet hvor meget det betyder om knappen er rød eller grøn, og det skader jo aldrig :)

<h2>Opsætning af testen</h2>

Jeg hoppede ind i Google Website Optimizer og opsatte en test. Hvis du ikke er helt sikker på hvordan det foregår, så kan jeg anbefale <a href="http://www.v4d5.net/">denne video.</a> Den eneste forskel i forhold til videoen, er bare at denne test skal køres som en <em>Multivariate Test</em>, men mere om det senere.

<h3>Control og Tracking script</h3>

Da testen skal køres på tværs af hele sitet kan du faktisk bare indtaste en tilfældig side som Test Page, jeg indtastede bare forsiden. Google Website Optimizer tester derefter om siden kan findes. Derefter skal der indsættes noget kode, og nu skal der laves lidt tricks.

GWO kører testen på alle sider hvor <em>Control Scriptet</em> er placeret, og derfor gælder det om at få det placeret på ALLE sider på sitet. Mange standard systemer har en footer, som bliver inkluderet på alle sider, hvor du f.eks. kan placere din tracking kode til Google Analytics. På samme måde findes der ofte en header-sektion der f.eks. indeholder noget banner-grafik og menuen. Denne bliver ligeledes inkluderet på alle sider, så derfor indsætter du dit <em>Control Script</em> fra GWO i header-sektionen og dit<em>Tracking Script</em> i footer-sektionen.

På mit linkkatalog har jeg lagt min menu i en seperat fil som jeg så inkluderer på alle sider. Jeg indsatte derfor <em>Control Scriptet</em> øverst i den fil og på den måde var jeg sikker på at scriptet blev kørt hver gang menuen blev vist.

<h3>utmx_section</h3>

Da dette køres som en multivariate test, skal man også markere de sektioner man gerne vil teste. Jeg har gjort det ved at GWO udskifter knappen's CSS class. Derfor indsætter jeg <code><script>utmx_section("menu-button")</script></code> og <code></noscript></code> rundt om linket i menuen. Den kode som jeg inkluderer på samtlige sider ser derved således ud:

<pre><code class="language-html"><script>utmx_section("menu-button")</script>
<a href="http://www.justlaunched.dk/tilmeld-link">
</code></pre>

Inde i GWO har jeg så sat to varianter op:

<pre><code class="language-html"><a href="http://www.justlaunched.dk/tilmeld-link">
<a href="http://www.justlaunched.dk/tilmeld-link">
</code></pre>

Det vil altså sige at hver gang Control Scriptet bliver kaldt, så udskifter GWO den originale linje med en af de to ovenstående linjer hvis der skal vises en variant, ellers viser den originale. Hvis GWO viser den linje der indeholder <code>class="submit-red"</code>, bliver knappen rød og ligeledes med den grønne - og det gælder altså uanset hvilken side <em>Control Scriptet</em> bliver kaldt fra - nu har du vist forstået det :)

<h3>Målside</h3>

Min målside i testen er den side som indeholder formularen hvor man kan tilmelde sit link. På den side indsætter jeg derfor<em>Conversion Scriptet</em> i bunden af koden.

På den måde kan du få kørt en test på tværs af hele dit website. Jeg håber det er lykkedes at forklare det, så det er til at forstå. Skriv gerne en kommentar herunder og lad mig høre om du kunne bruge det til noget.