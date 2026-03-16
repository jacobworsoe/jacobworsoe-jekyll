---
layout: post
title: Hvilken side ser brugerne efter forsiden?
date: 2021-04-03 20:41:20
slug: hvilken-side-ser-brugerne-efter-forsiden
categories:
  - Analytics
---

Et af de spørgsmål som mange stiller er:

<blockquote>Kan vi se hvad brugerne gør efter de ser forsiden?</p></blockquote>

<p>Det er et godt spørgsmål!

Men umiddelbart ikke så nemt at svare på...

<h2>Problemet med Next Page Path</h2>

Problemet er at der findes ikke en next path dimension.

Eller joh, det gør der. Den hedder Next Page Path. Men du får ikke det der står udenpå æsken.

Den giver bare det samme som Page dimensionen.

Det skyldes at et givent hit eller pageview i Google Analytics, isoleret set, ikke har informationer om hvad der sker efterfølgende. Man kan derfor ikke vælge forsiden i "All pages"-rapporten og derefter se hvad brugerne gør derefter med <code>Next Page Path</code> dimensionen. Den indeholder nemlig præcis det samme som <code>Page</code> dimensionen.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path.jpg" alt="" width="812" height="390" class="alignnone size-full wp-image-2132" /></a>

Next Page Path er misvisende, hvilket også er grunden til at Google Analytics har gjort den deprecated og fjerner den på et tidspunkt.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated.jpg" alt="" width="826" height="99" class="alignnone size-full wp-image-2133" /></a>

Du får også en advarsel hvis du bruger den i en custom report.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning-860x311.jpg" alt="" width="860" height="311" class="alignnone size-large wp-image-2134" /></a>

<h2>Previous Page er løsningen</h2>

Til gengæld kan man altid se den forrige side, via <code>document.referrer</code> som bliver tracket i dimensionen Previous Page Path.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/document.referrer.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/document.referrer.jpg" alt="" width="567" height="151" class="alignnone size-full wp-image-2135" /></a>

Tricket til at se den næste side efter forsiden er derfor at lave en rapport som kigger på alle sider og filtrere så du kun ser de sider hvor den <em>forrige</em> side er forsiden. Det kan nemt laves i en custom report sådan her:

[caption id="attachment_2138" align="alignnone" width="860"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings-860x285.jpg" alt="Custom Report filtreret så Previous Page er forsiden." width="860" height="285" class="size-large wp-image-2138" /></a> Custom Report filtreret så Previous Page er forsiden.[/caption]

Og dermed får du den ønskede oversigt:

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view-860x356.jpg" alt="" width="860" height="356" class="alignnone size-large wp-image-2137" /></a>