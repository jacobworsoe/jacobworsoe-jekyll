---
layout: post
title: Husk 301 når du får ny hjemmeside
date: 2013-09-03 07:12:21
slug: husk-301-nar-du-far-ny-hjemmeside
wordpress_id: 226
categories:
  - SEO
---

<a href="http://www.hifiklubben.dk/" target="_blank">Hi-Fi klubben</a> har fået nyt website og det er et virkelig fedt website! Måden jeg opdagede det på var dog mindre fed...

Da jeg opsatte denne blog, lyttede jeg til et <a href="http://www.antphilosophy.com/category/podcasts/" target="_blank">The Industrious Geeks</a> podcast, hvor de giver masser af gode <a href="http://www.antphilosophy.com/opsaetning-af-wordpress/" target="_blank">tips og tricks til opsætning af Wordpress</a>. De nævnte blandt andet <a href="http://wordpress.org/plugins/broken-link-checker/" target="_blank">Broken Link Checker</a> som løbende holder øje med alle interne og eksterne links på din blog og giver dig besked hvis de er døde. I går sendte min blog mig så denne mail:

<figure><img class="size-full wp-image-227" alt="Mit link til Hi-Fi klubben var dødt." src="{{ '/assets/images/hifi-klubben-broken-link-checker.png' | relative_url }}" width="508" height="170" /><figcaption>Mit link til Hi-Fi klubben var dødt.</figcaption></figure>

Linket findes i et gammelt blogindlæg om at <a title="HDMI kabel – Skal det virkelig koste 249 kroner?" href="{{ '/skal-et-hdmi-kabel-koste-249/' | relative_url }}" target="_blank">købe billige HDMI kabler i Østen</a>. Grunden til at linket nu er dødt er fordi Hi-Fi klubbens nye website har en anden URL struktur end det gamle site og produkterne har dermed ikke samme URL som tidligere. Det produkt jeg linkede til, lå tidligere på:

<code>http://www.hifiklubben.dk/produkter/tilbehor/kabel/hdmi-kabel/qed_reference_hdmi-kabel_5-meter.htm</code>

men ligger nu på:

<code>http://www.hifiklubben.dk/Products/qed-reference-hdmi-kabel-28642/</code>

Det betyder at man nu lander på en fejlside på den gamle URL.

<figure><a href="{{ '/assets/images/hifiklubben-404.png' | relative_url }}"><img class="size-medium wp-image-229" alt="Den gamle URL giver nu bare en fejlside." src="{{ '/assets/images/hifiklubben-404-640x619.png' | relative_url }}" width="640" height="619" /></a><figcaption>Den gamle URL giver nu bare en fejlside.</figcaption></figure>

<h2>301 redirect er løsningen</h2>

For at undgå fejlsider når man skifter URL struktur skal der opsættes 301 redirects fra alle de gamle URL'er til deres nye URL. Hvis den gamle URL er udgået bør der istedet peges på en overordnet side, fx en kategoriside med lignende produkter.

Hi-Fi klubbens website indeholder ifølge Googles indeks 7.170 sider, så det vil være ret tidskrævende at gå igennem alle siderne og opsætte redirects. En hurtigere løsning vil være at hoppe ind i Google Analytics og trække fx top 500 landingssider ud og hive dem ind i Excel. Derved har du en prioriteret liste over de vigtigste sider som skal redirectes.

Derefter ville jeg redirecte resten til relevante kategorisider. I dette tilfælde indeholder den gamle URL faktisk hele kategoristrukturen, så man kunne nemt lave et filter i Excel på <em>/tilbehor/kabel/hdmi-kabel/<strong> </strong></em>og redirecte alle resterende sider der indeholder dette til <a href="http://www.hifiklubben.dk/Kabler/HDMI-kabel/">http://www.hifiklubben.dk/Kabler/HDMI-kabel/</a>.

Til sidst ville jeg tage alle de resterende sider og redirecte til forsiden, så man i det mindste ikke får en fejlside.