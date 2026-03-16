---
layout: post
title: Workarounds på ITP
date: 2019-11-08 21:56:20
slug: workarounds-paa-itp
wordpress_id: 2614
categories:
  - Analytics
---

Der er mange mulige workarounds på ITP. Simo Ahava har <a href="https://www.simoahava.com/analytics/itp-2-1-and-web-analytics/" rel="noopener noreferrer">samlet en god oversigt her</a>.

Overordnet set kan workarounds deles op i to metoder:

<ol>
   <li>Der gemmes et ID i localStorage (lukket af ITP 2.3)</li>
   <li>Der gemmes et ID i en server-side cookie</li>
</ol>

Cookies der er sat server-side med <code>Set-Cookie</code> er pt. ikke berørt af ITP.

<h2>Server-side cookies (HTTP cookies)</h2>

Lad os lige se på forskellen mellem client-side og server-side cookies.

<ul>
    <li>Client-side cookies sættes med JavaScript</li>
    <li>Server-side cookies kommer direkte fra serveren og bliver sat med Set-Cookie i HTTP headeren i det HTTP response der kommer retur fra serveren</li>
</ul>

Her er hvad der sker når du skriver <a href="https://www.jacobworsoe.dk">jacobworsoe.dk</a> i din browser.

<ol>
<li>Browseren sender et HTTP request på en URL til serveren, fx. <a href="https://www.jacobworsoe.dk">jacobworsoe.dk</a></li>
<li>Web serveren sender et HTTP response tilbage med HTML koden for dén URL. Et HTTP response indeholder nogle Headers som fx status koden (200, 301, 404, etc.), om siden skal caches i browseren og hvor længe, osv. Headeren kan også indeholde en Set-Cookie kommando som sætter en cookie i browseren.</li>
</ol>

<h2>Accutics Cookie Saver</h2>

Måske har du hørt om <a href="https://cookiesaver.io/" rel="noopener noreferrer">Cookie Saver</a> fra danske Accutics. De kan sætte server-side cookies for dig.

Du opretter en CNAME record i din DNS hvor man peger et subdomæne på dit website på Cookie Saver's server. I praksis fungerer det som en redirect.

Derefter indsætter du et stykke JavaScript i din Tag Manager, som sørger for at lave et request til det CNAME med en liste af de cookies du gerne vil have sat server-side. Cookie Saver sørger så for sætte sende et HTTP Response tilbage med de ønskede server-side cookies.

Det har nogle store fordele.

<ol>
<li>Adblockere har ikke så nemt ved at blokere dette request, fordi subdomænet er unikt og kan hedde hvad som helst. Det er derimod meget nemt at blokere Google Analytics, fordi den altid sender til <code>collect.google-analytics.com</code>.</p></li>
<li><p>Når man laver et request til ens eget subdomæne for at sende data, er der mulighed for at serveren sætter en cookie via Set-Cookie som en del af det HTTP response der kommer retur fra serveren. Fordi requestet er lavet til ens eget domæne, kan serveren sætte en første parts server-side cookie, hvilket pt. ikke bliver blokeret af ITP.</p></li>
</ol>

<h2>Google kommer ikke med en "nem" løsning</h2>

<p>I hvert fald ikke hvis løsningen er server-side cookies. Det er simpelthen ikke teknisk muligt for Google at lave en simpel løsning på dette. For at sætte en server-side cookie kræver det at der laves et subdomæne på det website. Det kan Google ikke bare gøre for dig. Det skal du aktivt selv oprette.

Det betyder at du ikke skal sidde og vente på at Google løser det for dig. Det kan de ikke. Rent teknisk kan det ikke lade sig gøre.

Men samtidig betyder det også at Safari måske ikke begynder at blokere server-side cookies i de næste ITP versioner. Netop fordi det kræver en bevidst handling af dig.

En del af problemet som ITP prøver at løse er nemlig at der ofte bliver lavet en masse cross-site tracking af dine brugere - på det eget website - uden at du er klar over det. Bare fordi du har indsat en harmløst script på dit website.

Men med server-side cookies, sker der ikke noget uden du er klar over det, så det er ikke noget en 3. part bare kan gøre, hvilket formentlig er grunden til at ITP ikke blokerer det.

<h2>Er workarounds spild af penge?</h2>

Måske. Facebook <a href="https://www.jacobworsoe.dk/ekskluder-facebooks-fbclid-url-parameter-i-google-analytics/" rel="noopener noreferrer">forsøgte med et workaround</a> og det blev stoppet af ITP 2.1.

Det kan derfor sagtens være at det er spild af penge at implementere workarounds til ITP, som måske bliver blokeret i næste ITP version.

Du er nødt til at overveje hvor meget det koster dig at ITP ødelægger dine data.

Men som beskrevet ovenfor, så kommer Google ikke og løser det hele for dig, så det er værd at have med i overvejelserne i forhold til om det kan betale sig at lave en workaround.