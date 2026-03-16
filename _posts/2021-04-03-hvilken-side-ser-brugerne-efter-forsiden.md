---
layout: post
title: Hvilken side ser brugerne efter forsiden?
date: 2021-04-03 20:41:20
slug: hvilken-side-ser-brugerne-efter-forsiden
categories:
  - Analytics
---

<p>Et af de spørgsmål som mange stiller er:</p>
<blockquote><p>Kan vi se hvad brugerne gør efter de ser forsiden?</p>
</blockquote>
<p>Det er et godt spørgsmål!</p>
<p>Men umiddelbart ikke så nemt at svare på&#8230;</p>
<h2>Problemet med Next Page Path</h2>
<p>Problemet er at der findes ikke en next path dimension.</p>
<p>Eller joh, det gør der. Den hedder Next Page Path. Men du får ikke det der står udenpå æsken.</p>
<p>Den giver bare det samme som Page dimensionen.</p>
<p>Det skyldes at et givent hit eller pageview i Google Analytics, isoleret set, ikke har informationer om hvad der sker efterfølgende. Man kan derfor ikke vælge forsiden i &#8220;All pages&#8221;-rapporten og derefter se hvad brugerne gør derefter med <code class="" data-line="">Next Page Path</code> dimensionen. Den indeholder nemlig præcis det samme som <code class="" data-line="">Page</code> dimensionen.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path.jpg" alt="" width="812" height="390" class="alignnone size-full wp-image-2132" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path.jpg 812w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path-690x331.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Page-og-Next-Page-Path-768x369.jpg 768w" sizes="auto, (max-width: 812px) 100vw, 812px" /></a></p>
<p>Next Page Path er misvisende, hvilket også er grunden til at Google Analytics har gjort den deprecated og fjerner den på et tidspunkt.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated.jpg" alt="" width="826" height="99" class="alignnone size-full wp-image-2133" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated.jpg 826w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-690x83.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-768x92.jpg 768w" sizes="auto, (max-width: 826px) 100vw, 826px" /></a></p>
<p>Du får også en advarsel hvis du bruger den i en custom report.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning-860x311.jpg" alt="" width="860" height="311" class="alignnone size-large wp-image-2134" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning-860x311.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning-690x250.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning-768x278.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Next-page-deprecated-warning.jpg 915w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<h2>Previous Page er løsningen</h2>
<p>Til gengæld kan man altid se den forrige side, via <code class="" data-line="">document.referrer</code> som bliver tracket i dimensionen Previous Page Path.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/document.referrer.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/document.referrer.jpg" alt="" width="567" height="151" class="alignnone size-full wp-image-2135" /></a></p>
<p>Tricket til at se den næste side efter forsiden er derfor at lave en rapport som kigger på alle sider og filtrere så du kun ser de sider hvor den <em>forrige</em> side er forsiden. Det kan nemt laves i en custom report sådan her:</p>
<div id="attachment_2138" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2138" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings-860x285.jpg" alt="Custom Report filtreret så Previous Page er forsiden." width="860" height="285" class="size-large wp-image-2138" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings-860x285.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings-690x229.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings-768x255.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-settings.jpg 1459w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2138" class="wp-caption-text">Custom Report filtreret så Previous Page er forsiden.</p></div>
<p>Og dermed får du den ønskede oversigt:</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view-860x356.jpg" alt="" width="860" height="356" class="alignnone size-large wp-image-2137" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view-860x356.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view-690x286.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view-768x318.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/custom-report-previous-page-og-page-view.jpg 1414w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>

