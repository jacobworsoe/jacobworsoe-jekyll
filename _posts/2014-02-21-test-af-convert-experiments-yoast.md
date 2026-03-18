---
layout: post
title: Test af Convert Experiments by Yoast
date: 2014-02-21 08:09:44
slug: test-af-convert-experiments-yoast
wordpress_id: 525
categories:
  - Konverteringsoptimering
---

<a href="http://wordpress.org/plugins/convert-experiments/" target="_blank" rel="noopener">Convert Experiments by Yoast</a> er navnet på et nyt Wordpress plugin af Joost de Valk, som står bag mange fede plugins, hvoraf de fleste nok kender <a href="http://wordpress.org/plugins/google-analytics-for-wordpress/" target="_blank" rel="noopener">Google Analytics for WordPress</a> og <a href="http://wordpress.org/plugins/wordpress-seo/" target="_blank" rel="noopener">WordPress SEO by Yoast</a>. Begge to hamre gode plugins og det nye plugin lyder bestemt også til at være spændende, da det byder på simple A/B splittests på en Wordpress platform, og jeg har kigget lidt nærmere på hvad det kan.

<h2>Hvad er Convert Experiments by Yoast?</h2>

Det er faktisk bare et plugin som indsætter det nødvendige tracking script på dit Wordpress site, så du kan opsætte splittests i et andet værktøj - <a href="http://www.convertexperiments.com" target="_blank" rel="noopener">Convert Experiments</a>. Ikke så meget fancy der. Men så alligevel... For Convert Experiments har en smart feature hvor du kan indsætte nogle custom variabler i scriptet, hvor man kan angive bestemte parametre omkring den enkelte side. Og alt den information sørger dette plugin for at hente fra Wordpress og indsætte i scriptet, uden at du skal røre en finger.

Det giver mulighed for at køre splittests på bestemte dele af sitet, uden at man skal sidde at finde mønstre i URL'erne på de sider testen skal køre på, fx alle produktsider, kategorisider, etc. Mere præcist indsætter den følgende variable i scriptet:

<ul>
    <li>Page type (fx post, page, archieve, etc.)</li>
    <li>Sidens titel</li>
    <li>Kategori ID</li>
    <li>Kategori navn</li>
</ul>

Man kan derved, meget nemt, køre en splittest fx på alle blogindlæg, undtagen gæsteindlæg. Ulempen er bare at, selvom scriptet er gratis og indsætter alle disse informationer, så skal man som minimum have et "Expert" abonnement til $399 om måneden <a href="http://support.convert.com/entries/21795481-Targeting-using-advanced-page-tagging" target="_blank" rel="noopener">for at kunne bruge dem i Convert Experiments</a>. Og det var sgu lidt et antiklimaks, at opdage det.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-23.01.11.png"><img class="size-medium wp-image-527" alt="Priser for Convert Experiments" src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-23.01.11-750x417.png" width="750" height="417" /></a><figcaption>Priser for Convert Experiments</figcaption></figure>

Men der er også fordele. Igennem Yoast får man nemlig en gratis konto til Convert Experiments, hvor man kan teste på 5.000 besøgende om måneden i 12 måneder. Uden Yoast kan man kun få en 15 dages gratis trial.

<h2>Opsætning i Wordpress</h2>

For at afprøve hvordan det virkede, opsatte jeg en helt simpel "rød eller grøn knap"-test på mit linkkatalog, som også er min Wordpress legeplads.

Det eneste man skal gøre, er at koble det nye plugin sammen med den konto man opretter på Convert Experiments via et konto ID og så er man færdig med at rode i Wordpress - resten foregår via webinterfacet i Convert Experiments.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-19.46.27.png"><img class="size-medium wp-image-528" alt="Sammenkobling af Wordpress og Convert Experiments." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-19.46.27-750x308.png" width="750" height="308" /></a><figcaption>Sammenkobling af Wordpress og Convert Experiments.</figcaption></figure>

Derefter hopper man over i et lækkert interface og opretter et eksperiment.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-19.36.52.png"><img class="size-medium wp-image-529" alt="Convert Experiment's webinterface." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-19.36.52-750x371.png" width="750" height="371" /></a><figcaption>Convert Experiment's webinterface.</figcaption></figure>

Man giver testen et navn og vælger hvilken URL man vil bruge til at opsætte testen. Senere kan den udvides til at køre på flere URL'er. I den gratis version kan man lave to typer splittest. A/B experiment, hvor man designer en "virtuel" variant i værktøjet og Split-test experiment, hvor man selv laver en anden version på en anden URL og bare lader værktøjet dele trafikken mellem de to URL'er.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-20.14.34.png"><img class="size-medium wp-image-530" alt="Navngivning og valg af eksperiment type." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-20.14.34-750x525.png" width="750" height="525" /></a><figcaption>Navngivning og valg af eksperiment type.</figcaption></figure>

Man bliver derefter sendt til den visuelle designer, hvor man kan foretage ændringer på den side man gerne vil teste.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.07.05.png"><img class="size-medium wp-image-532" alt="Visuel designer." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.07.05-750x372.png" width="750" height="372" /></a><figcaption>Visuel designer.</figcaption></figure>

Jeg skal bare lave et helt simpelt eksperiment, så jeg scroller ned til knappen, klikker på den og vælger "Change Background Color" i menuen der kommer frem. Som det ses herunder kan man også lave en masse avancerede ting, ligesom i de andre splittest værktøjer der findes på markedet.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-20.15.20.png"><img class="size-full wp-image-533" alt="Ændring af knappens farve." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-20.15.20.png" width="417" height="433" /></a><figcaption>Ændring af knappens farve.</figcaption></figure>

Efter knappen er blevet grøn, vælger jeg målet for testen. I dette tilfælde vil jeg måle på hvor mange der klikker på knappen.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.11.33.png"><img class="size-full wp-image-534" alt="Valg af mål." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.11.33.png" width="515" height="419" /></a><figcaption>Valg af mål.</figcaption></figure>

Og så er testen faktisk klar til at blive sat igang. Lige inden du sætter den igang giver værktøjet en fin opsummering af indstillingerne, sat op på en lidt utraditionel måde.

Bemærk at de har valgt et lidt utraditionelt signifikansniveau for deres tests som standard på 97%, som alt andet lige kræver mere data/tid, for at kunne træffe konklusioner. Jeg vil dog anbefale at skrue det ned til 95% signifikans, som giver et bedre mix mellem den tid det tager at køre testen og den sikkerhed du har for at træffe korrekte beslutninger. Hvis alt dette er sort snak, så vil jeg anbefale dig denne artikler, hvor jeg gennemgår alle disse begreber: <a href="//www.jacobworsoe.dk/statistikken-bag-google-website-optimizer/" target="_blank" rel="noopener">Statistikken bag en splittest</a>.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.21.58.png"><img class="size-medium wp-image-535" alt="Smart opsummering af indstillingerne for testen." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.21.58-750x319.png" width="750" height="319" /></a><figcaption>Smart opsummering af indstillingerne for testen.</figcaption></figure>

Det er i øvrigt samme opstilling som <a href="https://www.v4d5.net/" target="_blank" rel="noopener">Morten Vadskær</a> <a href="http://www.v4d5.net/blog/tag-dine-formularer-alvorligt" target="_blank" rel="noopener">implementerede på faktorfobi for snart 2 år siden</a>, og den er der endnu, så mon ikke det er en meget god måde at præsentere information på? :)

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/faktorfobi-checkout.png"><img class="size-medium wp-image-550" alt="Betalingsflowet på faktorfobi." src="//www.jacobworsoe.dk/wp-content/uploads/faktorfobi-checkout-750x449.png" width="750" height="449" /></a><figcaption>Betalingsflowet på faktorfobi.</figcaption></figure>

Næste trin er en fin rapport over testens udvikling, som man kender det fra andre splittest værktøjer - ikke så meget innovation her.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.23.49.png"><img class="size-medium wp-image-536" alt="Statusrapport for testen." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-21-00.23.49-750x328.png" width="750" height="328" /></a><figcaption>Statusrapport for testen.</figcaption></figure>

<h2>Et lille es i ærmet</h2>

Som en smart lille ting kan værktøjet hente omsætningen fra dit Google Analytics E-commerce script, som du selvfølgelig allerede har på siden. Det kan Visual Website Optimizer fx ikke, og kræver at man indsætter deres eget script på sin kvitteringsside, hvis man vil have omsætningen med som mål for testen. I kombination med dette nye plugin, er det en smart lille detajle, som gør det så meget nemmere og hurtigere at komme igang med, for dem som ikke selv vil rode med scripts.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-20.54.16.png"><img class="size-full wp-image-537" alt="Convert Experiments snupper omsætningen fra dit Google Analytics script - smart." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-20.54.16.png" width="679" height="109" /></a><figcaption>Convert Experiments snupper omsætningen fra dit Google Analytics script - smart.</figcaption></figure>

<h2>Konklusion</h2>

Med dette plugin er det blevet utrolig nemt at opsætte splittests på et Wordpress site, hvor man tilmeld kan afprøve det i et helt år. Det virker dog til at Convert Experiments først bliver rigtig sjovt, når man begynder at betale for det og får adgang til alle features. Og her er det cirka det samme som konkurrenterne.

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-23.03.19.png"><img class="size-medium wp-image-538" alt="Priserne hos Optimizely." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-23.03.19-750x275.png" width="750" height="275" /></a><figcaption>Priserne hos Optimizely.</figcaption></figure>

<figure><a href="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-23.03.36.png"><img class="size-full wp-image-539" alt="Priserne hos Visual Website Optimizer." src="//www.jacobworsoe.dk/wp-content/uploads/Screenshot-2014-02-20-23.03.36.png" width="724" height="256" /></a><figcaption>Priserne hos Visual Website Optimizer.</figcaption></figure>

Herover ses priserne på Visual Website Optimizer og Optimizely. Sammenligner man prisen for 200.000 besøgende (der hvor Convert Experiments giver adgang til de smarte filtre og segmenteringer) så er det samme pris som Optimizely nemlig $399 om måneden, mens VWO koster $500 om måneden.

Jeg synes derfor at den konkurrencedygtige pris, kombineret med den nemme opsætning, gør det til en rigtig spændende kombination, for både store og små Wordpress sites.