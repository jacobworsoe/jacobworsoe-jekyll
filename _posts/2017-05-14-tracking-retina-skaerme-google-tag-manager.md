---
layout: post
title: Tracking af retina skærme med Google Tag Manager
date: 2017-05-14 10:35:46
slug: tracking-retina-skaerme-google-tag-manager
wordpress_id: 1123
categories:
  - Analytics
---

Nå, men hvor mange brugere sidder egentlig på retina skærme? Vi ved at nye smartphones og tables har retina skærme som er super fede at læse på, men desværre får grafikker til at se forfærdelige ud, medmindre de er optimeret til skærme med 2x opløsning. Men hvad med desktop? Hvor udbredt er det, udover de nyeste Macbook Pro? Lad os finde ud af det med Google Tag Manager.

<h2>Hent værdien af devicePixelRatio som variabel</h2>

Alle nyere browser har en global property på window objektet, som vi nemt kan snuppe med JavaScript i Tag Manager.

<a href="{{ '/assets/images/devicePixelRatio-browser-support.png' | relative_url }}"><img class="alignnone size-full wp-image-1124" src="{{ '/assets/images/devicePixelRatio-browser-support.png' | relative_url }}" alt="devicePixelRatio-browser-support" width="1264" height="482" /></a>

Værdien af devicePixelRatio angiver forholdet mellem fysiske pixels og CSS pixels som normalt er 1 for desktop skærme og ældre smartphones og 2 for nyere retina skærme som er dobbelt så mange CSS pixels på den samme fysiske plads. Du vil få det samme resultat hvis du zoomer 200% i din browser.

Værdien hentes ved at lave en JavaScript variabel som henter værdien af devicePixelRatio.

<a href="{{ '/assets/images/devicePixelRatio-javascript-variable.png' | relative_url }}"><img class="alignnone size-full wp-image-1128" src="{{ '/assets/images/devicePixelRatio-javascript-variable.png' | relative_url }}" alt="devicePixelRatio-javascript-variable" width="1177" height="312" /></a>

Derefter laves en custom dimension, som sættes til user scope, da værdien typisk ikke ændrer sig for den samme browser cookie.

<a href="{{ '/assets/images/devicePixelRatio-custom-dimension.png' | relative_url }}"><img class="alignnone size-full wp-image-1125" src="{{ '/assets/images/devicePixelRatio-custom-dimension.png' | relative_url }}" alt="devicePixelRatio-custom-dimension" width="791" height="379" /></a>

Det normale Pageview Tag udvides så den sender værdien af devicePixelRatio til GA på alle pageviews.

<a href="{{ '/assets/images/devicePixelRatio-edit-pageview-tag.png' | relative_url }}"><img class="alignnone size-full wp-image-1127" src="{{ '/assets/images/devicePixelRatio-edit-pageview-tag.png' | relative_url }}" alt="devicePixelRatio-edit-pageview-tag" width="947" height="128" /></a>

Med de nye data kan vi bygge en Custom Report, som viser fordelingen og dermed kan vi analysere om desktop sitet også bør optimeres til retina skærme (det skal det nok).

<a href="{{ '/assets/images/devicePixelRatio-custom-report.png' | relative_url }}"><img class="alignnone size-full wp-image-1126" src="{{ '/assets/images/devicePixelRatio-custom-report.png' | relative_url }}" alt="devicePixelRatio-custom-report" width="1171" height="522" /></a>

<h2>Den bedste måde at optimere til retina på</h2>

Det er at bruge srcset til at angive de forskellige størrelser af billedet. Sådan her:

<pre><code class="language-html"><img src="picture-1x.jpg"
     srcset="picture-2x.jpg 2x,
             picture-1x.jpg 1x"
     sizes="100%"
     alt="">
</code></pre>

På den måde kan browsere selv vælge at hente det store retina optimerede billede, hvis skærmen er 2x men den kan også vælge at hente det almindelige billede, hvis den er på en langsom 3G forbindelse. Skide smart!