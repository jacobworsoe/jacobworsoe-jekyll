---
layout: post
title: Tracking af retina skærme med Google Tag Manager
date: 2017-05-14 10:35:46
slug: tracking-retina-skaerme-google-tag-manager
categories:
  - Analytics
---

<p>Nå, men hvor mange brugere sidder egentlig på retina skærme? Vi ved at nye smartphones og tables har retina skærme som er super fede at læse på, men desværre får grafikker til at se forfærdelige ud, medmindre de er optimeret til skærme med 2x opløsning. Men hvad med desktop? Hvor udbredt er det, udover de nyeste Macbook Pro? Lad os finde ud af det med Google Tag Manager.</p>
<h2>Hent værdien af devicePixelRatio som variabel</h2>
<p>Alle nyere browser har en global property på window objektet, som vi nemt kan snuppe med JavaScript i Tag Manager.</p>
<p><a href="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-browser-support.png"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-1124" src="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-browser-support.png" alt="devicePixelRatio-browser-support" width="1264" height="482" srcset="https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-browser-support.png 1264w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-browser-support-690x263.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-browser-support-768x293.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-browser-support-725x276.png 725w" sizes="auto, (max-width: 1264px) 100vw, 1264px" /></a></p>
<p>Værdien af devicePixelRatio angiver forholdet mellem fysiske pixels og CSS pixels som normalt er 1 for desktop skærme og ældre smartphones og 2 for nyere retina skærme som er dobbelt så mange CSS pixels på den samme fysiske plads. Du vil få det samme resultat hvis du zoomer 200% i din browser.</p>
<p>Værdien hentes ved at lave en JavaScript variabel som henter værdien af devicePixelRatio.</p>
<p><a href="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-javascript-variable.png"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-1128" src="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-javascript-variable.png" alt="devicePixelRatio-javascript-variable" width="1177" height="312" srcset="https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-javascript-variable.png 1177w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-javascript-variable-690x183.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-javascript-variable-768x204.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-javascript-variable-725x192.png 725w" sizes="auto, (max-width: 1177px) 100vw, 1177px" /></a></p>
<p>Derefter laves en custom dimension, som sættes til user scope, da værdien typisk ikke ændrer sig for den samme browser cookie.</p>
<p><a href="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-dimension.png"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-1125" src="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-dimension.png" alt="devicePixelRatio-custom-dimension" width="791" height="379" srcset="https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-dimension.png 791w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-dimension-690x331.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-dimension-768x368.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-dimension-725x347.png 725w" sizes="auto, (max-width: 791px) 100vw, 791px" /></a></p>
<p>Det normale Pageview Tag udvides så den sender værdien af devicePixelRatio til GA på alle pageviews.</p>
<p><a href="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag.png"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-1127" src="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag.png" alt="devicePixelRatio-edit-pageview-tag" width="947" height="128" srcset="https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag.png 947w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag-690x93.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag-768x104.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag-725x98.png 725w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-edit-pageview-tag-940x128.png 940w" sizes="auto, (max-width: 947px) 100vw, 947px" /></a></p>
<p>Med de nye data kan vi bygge en Custom Report, som viser fordelingen og dermed kan vi analysere om desktop sitet også bør optimeres til retina skærme (det skal det nok).</p>
<p><a href="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-report.png"><img loading="lazy" decoding="async" class="alignnone size-full wp-image-1126" src="http://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-report.png" alt="devicePixelRatio-custom-report" width="1171" height="522" srcset="https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-report.png 1171w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-report-690x308.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-report-768x342.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/devicePixelRatio-custom-report-725x323.png 725w" sizes="auto, (max-width: 1171px) 100vw, 1171px" /></a></p>
<h2>Den bedste måde at optimere til retina på</h2>
<p>Det er at bruge srcset til at angive de forskellige størrelser af billedet. Sådan her:</p>
<pre><code class="" data-line="">&lt;img src=&quot;picture-1x.jpg&quot;
     srcset=&quot;picture-2x.jpg 2x,
             picture-1x.jpg 1x&quot;
     sizes=&quot;100%&quot;
     alt=&quot;&quot;&gt;
</code></pre>
<p>På den måde kan browsere selv vælge at hente det store retina optimerede billede, hvis skærmen er 2x men den kan også vælge at hente det almindelige billede, hvis den er på en langsom 3G forbindelse. Skide smart!</p>

