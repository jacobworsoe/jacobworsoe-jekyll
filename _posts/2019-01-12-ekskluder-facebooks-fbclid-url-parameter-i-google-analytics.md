---
layout: post
title: Ekskluder facebooks fbclid URL parameter i Google Analytics
date: 2019-01-12 00:13:39
slug: ekskluder-facebooks-fbclid-url-parameter-i-google-analytics
categories:
  - Analytics
---

Her er et hurtig tip til at undgå at facebooks fbclid URL parameter ødelægger dine GA data.

[caption id="attachment_1477" align="alignnone" width="1552"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/fbclid-url-parameter-eksempel.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/fbclid-url-parameter-eksempel.png" alt="facebooks fbclid URL parameter." width="1552" height="215" class="size-full wp-image-1477" /></a> facebooks fbclid URL parameter.[/caption]

<h2>Indhold</h2>

<ul>
<li><a href="#article-header-id-0">Hvad er fbclid?</a></li>
<li><a href="#article-header-id-1">Samme teknik som cross-domain tracking i Google Analytics</a></li>
<li><a href="#article-header-id-2">Hvorfor er det et problem i Google Analytics?</a></li>
<li><a href="#article-header-id-3">Ekskluder fbclid som URL parameter</a></li>
</ul>

<h2 id="article-header-id-0">Hvad er fbclid?</h2>

fbclid er en URL parameter som facebook er begyndt at sætte på alle udgående links fra facebook - også almindelige organiske opslag. Grunden til at facebook er begyndt at sætte den URL parameter på deres udgående links er Apples <a href="https://webkit.org/blog/7675/intelligent-tracking-prevention/" rel="noopener noreferrer" target="_blank">Intelligent Tracking Prevention</a>. Da <a href="https://webkit.org/blog/8311/intelligent-tracking-prevention-2-0/" rel="noopener noreferrer" target="_blank">ITP 2.0 udkom</a> sammen med Safari 12, som kom sammen med iOS 12, begyndte Safari at blokere adgangen til 3. parts cookies, så de ikke kunne bruges til tracking.

Den 24. oktober 2018 gjorde facebook det derfor muligt at skifte til en 1. parts cookie, dvs. en cookie som er sat på websitets domæne (fx jacobworsoe.dk) og ikke fx facebook.com.

[caption id="attachment_1486" align="alignnone" width="692"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/facebook-first-party-cookie-announcement.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/facebook-first-party-cookie-announcement.png" alt="facebook gør det muligt at facebook pixel bruger en 1. parts cookie." width="692" height="505" class="size-full wp-image-1486" /></a> facebook gør det muligt at facebook pixel bruger en 1. parts cookie.[/caption]

Facebook sender derfor et unik ID med i alle udgående links og når brugeren lander på din side, bruger din facebook pixel dette ID til at sætte en 1. parts cookie i brugerens browser, for at tracke ham i eftefølgende besøg og attributere værdi tilbage til facebook som trafikkilde. Herunder kan du se hvordan ID'et fra URL'en er det samme som bliver gemt i cookien og at cookie domænet er .jacobworsoe.dk. Dermed vil Safari ikke blokere adgangen til den cookie.

[caption id="attachment_1476" align="alignnone" width="1821"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/fbclid-gemt-i-first-party-cookie.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/fbclid-gemt-i-first-party-cookie.png" alt="fbclid gemt i 1. parts cookie." width="1821" height="846" class="size-full wp-image-1476" /></a> fbclid gemt i 1. parts cookie.[/caption]

Du kan prøve at klikke på linket i <a href="https://www.facebook.com/Bridenista/posts/1568623119846968" rel="noopener noreferrer" target="_blank">dette facebook opslag</a>, og se at der kommer et fbclid på URL'en.

<h2 id="article-header-id-1">Samme teknik som cross-domain tracking i Google Analytics</h2>

Det er i øvrigt samme teknik som Google Analytics bruger til at tracke den samme bruger over flere forskellige domæner. Her har de forskellige domæner ikke adgang til hinandens cookies, så derfor bliver der sat en parameter på alle links mellem domænerne som indeholder brugerens Google Analytics client ID, fx sådan her:
<code>?_ga=1.438974397439.32979498743.4376748368473</code>.

Når man lander på det andet domæne, vil Google Analytics bruge dette client ID og dermed fortsætte brugerens session, fremfor at skabe et nyt client ID og en ny session.

<h2 id="article-header-id-2">Hvorfor er det et problem i Google Analytics?</h2>

Set ud fra et tracking synspunkt er det super fedt at facebook har lavet en løsning til ITP 2.0, men det skaber noget støj i dine Google Analytics data. Udfordringen er at alle personer får et unikt fbclid og dermed vil alt din trafik fra facebook bliver opdelt på forskellige sider i Google Analytics, som det ses herunder.

[caption id="attachment_1479" align="alignnone" width="1436"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/sider-med-fbclid-url-parameter.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/sider-med-fbclid-url-parameter.png" alt="fbclid skaber en masse unikke sider i Google Analytics." width="1436" height="699" class="size-full wp-image-1479" /></a> fbclid skaber en masse unikke sider i Google Analytics.[/caption]

Og det kan være et kæmpe problem, hvis du får meget trafik fra facebook, da det bliver svært at se hvor meget trafik en bestemt side har fået. Min blog har pt. 54 unikke fbclid ID'er i Google Analytics.

[caption id="attachment_1475" align="alignnone" width="803"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/54-unikke-fbclid-værdier.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/54-unikke-fbclid-værdier.png" alt="54 unikke fbclid ID&#039;er." width="803" height="128" class="size-full wp-image-1475" /></a> 54 unikke fbclid ID'er.[/caption]

<h2 id="article-header-id-3">Ekskluder fbclid som URL parameter</h2>

Umiddelbart har du ikke noget gavn af at kunne se fbclid ID'erne i Google Analytics, så løsningen er at ekskludere fbclid som URL parameter i indstillingerne for dine Views i Google Analytics.

[caption id="attachment_1480" align="alignnone" width="512"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/ga-view-settings-exclude-url-query-parameters.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/ga-view-settings-exclude-url-query-parameters.png" alt="Ekskluder fbclid som URL parameter i Google Analytics." width="512" height="510" class="size-full wp-image-1480" /></a> Ekskluder fbclid som URL parameter i Google Analytics.[/caption]

Derefter vil Google Analytics fjerne fbclid parameteren fra URL'en i rapporterne i Google Analytics og det bliver meget nemmere at analysere dine data.

Er der andre parametre du altid ekskluderer? Kan du se en grund til at beholde fbclid i Google Analytics? Smid en kommentar herunder!