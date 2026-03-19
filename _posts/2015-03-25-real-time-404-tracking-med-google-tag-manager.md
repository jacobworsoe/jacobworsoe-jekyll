---
layout: post
title: Real-time 404 tracking med Google Tag Manager
date: 2015-03-25 14:50:50
slug: real-time-404-tracking-med-google-tag-manager
wordpress_id: 674
categories:
  - Analytics
---

En af de vigtigste opgaver når man lancerer et nyt website er at få opsat redirects fra alle de gamle URL'er. Det har jeg tidligere skrevet om her: <a href="https://www.jacobworsoe.dk/husk-301-nar-du-far-ny-hjemmeside/" title="Husk 301 når du får ny hjemmeside" target="_blank" rel="noopener noreferrer">Husk redirects når du får nyt website</a>.

Men selvom man har været grundig kan der være svipsere, så derfor er det vigtigt at holde øje med trafikken på 404 sider i timerne efter launch. Når vi launcher et nyt website for en kunde eller os selv i IMPACT sidder jeg altid med et champagneglas i hånden og overvåger 404 siderne i Real-time rapporterne i Google Analytics via mit Real-time 404 tracking system.

Jeg bruger Google Tag Manager da det giver mulighed for at opsætte avanceret tracking ud fra nogle smarte regler. Her vil jeg gennemgå hvordan jeg har opsat Google Tag Manager på vores nye website som blev lanceret da vi skiftede navn til IMPACT den 27. februar 2015.

Mit system giver mig følgende oplysninger i samme øjeblik en bruger lander på en 404 side:

<ul>
<li>Den URL som brugeren har forsøgt at tilgå</li>
<li>Hvor brugeren kom fra</li>
</ul>

Jeg bruger Event Tracking for at indsamle alle oplysningerne i hvert sit felt i Google Analytics. Strukturerede data er vejen frem!

<h2>1. Regel / udløser</h2>

Jeg starter med at lave den regel som skal styre hvornår mit Event skal affyres. Typisk har 404 siden altid den samme <code><title></code> så den bruger jeg oftest. Ind og kigge i kildekoden og finde dette stykke kode: <code><title>Siden blev ikke fundet - IMPACT</title></code>. Jeg opsætter en regel i Tag Manager som tjekker titlen på siden:</span>

<figure><a href="{{ '/assets/images/404-tracking-reglen.png' | relative_url }}"><img class="size-full wp-image-676" src="{{ '/assets/images/404-tracking-reglen.png' | relative_url }}" alt="Reglen i Tag Manager." width="515" height="155" /></a><figcaption>Reglen i Tag Manager.</figcaption></figure>

<h2>2. Makroer / variabler</h2>

Derefter skal jeg bruge det data der skal sendes til Google Analytics når en bruger rammer en 404 side. Jeg skal vide hvilken URL brugeren forsøgte at tilgå samt hvor brugeren er kommet fra.

Det sidste er nemt nok, for der har Tag Manager den indbyggede makro <code>&#123;&#123;referrer&#125;&#125;</code> som indeholder den URL brugeren kom fra. Denne information er guld værd, så jeg kan kontakte sider der linker til de gamle URL'er på sitet og bede om at få opdateret linket. Jeg laver selvfølgelig en redirect med det samme, så trafikken fremover ikke går tabt, men det er kun omkring 75% af den oprindelige link juice der bliver ført gennem et redirect, så hvis det er muligt at få andre sites til at linke direkte til den nye URL kan jeg score 25% ekstra link juice.

Den næste kræver lidt arbejde. Jeg skal vide præcis hvilken URL brugeren har forsøgt at tilgå. Uden den information kan jeg ikke opsætte et redirect for siden. Tag Manager har nogle indbyggede makroer som kan fange stykker af URL'er men ingen af dem fanger den komplette URL. En URL som Tag Managers indbyggede makroer ikke kan fange er denne:

<strong>http://www.impact.dk/kontakt?utm_source=google#billeder</strong>

Jeg opretter derfor følgende makro med en lille JavaScript funktion:

<figure><a href="{{ '/assets/images/404-tracking-makro.png' | relative_url }}"><img class="size-full wp-image-677" src="{{ '/assets/images/404-tracking-makro.png' | relative_url }}" alt="Makroen som fanger hele URL'en" width="741" height="536" /></a><figcaption>Makroen som fanger hele URL'en</figcaption></figure>

Det er denne kode jeg skriver ind i feltet (du må godt copy/paste den):

<pre><code class="language-javascript">function() {
var UrlCompletePath = location.pathname + location.search + location.hash;
return UrlCompletePath;
}
</code></pre>

<h2>3. Event tracking Tag</h2>

Så skal informationerne sendes afsted. Det klarer jeg med et Event Tracking tag som sender de to makroer afsted når reglen er opfyldt. Det ser således ud:

<figure><a href="{{ '/assets/images/404-tracking-event-tag.png' | relative_url }}"><img class="size-full wp-image-678" src="{{ '/assets/images/404-tracking-event-tag.png' | relative_url }}" alt="Event Tracking tag som sender dataene til Google Analytics." width="471" height="290" /></a><figcaption>Event Tracking tag som sender dataene til Google Analytics.</figcaption></figure>

<h2>Hvad kan jeg så se i Google Analytics?</h2>

Når websitet går i luften sidder jeg i Real-time rapporten i Google Analytics og holder øje med om der er brugere der lander på 404 siden. Hvis de gør det kan jeg øjeblikkeligt se præcis hvilken side de ramte, så jeg kan opsætte en redirect og jeg kan se hvor brugeren kom fra, så jeg kan få rettet linket.

<figure><a href="{{ '/assets/images/404-tracking-google-analytics.png' | relative_url }}"><img src="{{ '/assets/images/404-tracking-google-analytics-750x491.png' | relative_url }}" alt="Real-time Google Analytics rapporten viser mig 404 sider når de rammes." width="750" height="491" class="size-medium wp-image-691" /></a><figcaption>Real-time Google Analytics rapporten viser mig 404 sider når de rammes.</figcaption></figure>

Nemt og mega værdifuldt!

Det kan godt lade sig gøre at lave samme trick uden Tag Manager ved at indsætte Event tracking koden på 404 siden, men det er kun med Tag Manager at man kan gøre det uden at forstyrre sin programmør.