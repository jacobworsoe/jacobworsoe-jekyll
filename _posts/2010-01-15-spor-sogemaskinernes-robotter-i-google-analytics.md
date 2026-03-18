---
layout: post
title: Spor søgemaskinernes robotter i Google Analytics
date: 2010-01-15 01:53:51
slug: spor-sogemaskinernes-robotter-i-google-analytics
wordpress_id: 25
categories:
  - Analytics
---

For små to måneder siden begyndte jeg at kigge mig om efter en metode til at spore søgemaskinernes robotter i Google Analytics. Det kan for det første være meget sjovt at se hvornår de kommer forbi første gang efter en ny side er lanceret, men også efterfølgende at følge lidt med i hvor tit de kigger forbi og leder efter nyt indhold. Jeg fandt frem til en engelsk artikel, som er en oversættelse af en fransk artikel (ikke er tilgængelig mere), hvor de fortalte om et lille PHP script de havde lavet så det var muligt at spore søgerobotterne i Google Analytics.

Nåh, men jeg fandt altså frem til dette script som franskmændene havde lavet og fik det implementeret, og det fungerer faktisk rigtig godt, så derfor vil jeg lige dele det med jer her, samt lidt erfaringer med det. Da den oprindelige franske artikel ikke findes mere er der også begyndt at mangle nogle screenshots ovre i den engelsk artikel, så derfor har jeg lavet nogle nye som jeg vil forklare ud fra.
<h2>Opsætning i Google Analytics</h2>
Først starter du med at oprette en ny profil til dit websted:

<a href="{{ '/assets/images/spor-bots-ga-1.jpg' | relative_url }}"><img class="alignnone  wp-image-26 no-border" title="spor-bots-ga-1" alt="" src="{{ '/assets/images/spor-bots-ga-1.jpg' | relative_url }}" /></a>

Sæt den øverste indstilling til "Add a profile for a new domain" og giv profilen et passende navn f.eks. "robots.jacobworsoe.dk", sæt tidszonen korrekt og tryk på "finish":

<a href="{{ '/assets/images/spor-bots-ga-2.jpg' | relative_url }}"><img class="alignnone  wp-image-27 no-border" title="spor-bots-ga-2" alt="" src="{{ '/assets/images/spor-bots-ga-2.jpg' | relative_url }}" /></a>

Derefter skal du downloade denne pakke med 3 php-filer og pak dem ud i din web-mappe. I den fil som hedder config.php skal der ændres 3 ting. Den første linje som hedder "$var_utmhn" skal indeholde navnet på dit domæne, i dette tilfælde "jacobworsoe.dk". Den næste linje skal indeholde ID'et for den profil du lige har lavet. Den finder du ved at gå tilbage til oversigten i GA:

<a href="{{ '/assets/images/spor-bots-ga-3.jpg' | relative_url }}"><img class="alignnone size-full wp-image-28 no-border" title="spor-bots-ga-3" alt="" src="{{ '/assets/images/spor-bots-ga-3.jpg' | relative_url }}" width="747" height="321" /></a>

I den sidste linje skal du indsætte en værdi som du finder i den cookie som GA laver i din browser når du besøger din egen side. Bemærk er det kun er de tal der er markeret på billedet der skal med, altså kun dem før det første punktum:

<a href="{{ '/assets/images/spor-bots-ga-4.jpg' | relative_url }}"><img class="alignnone size-full wp-image-29 no-border" title="spor-bots-ga-4" alt="" src="{{ '/assets/images/spor-bots-ga-4.jpg' | relative_url }}" width="435" height="472" /></a>

Config.php kommer derved til at se således ud:
<div> <a href="{{ '/assets/images/spor-bots-ga-5.jpg' | relative_url }}"><img class="alignnone size-full wp-image-30 no-border" title="spor-bots-ga-5" alt="" src="{{ '/assets/images/spor-bots-ga-5.jpg' | relative_url }}" width="578" height="164" /></a></div>
<div>

Nu skal du så bare sørge for at inkludere den fil der hedder "analytics.php" på alle dine sider og scriptet vil derefter sørge for at spore ikke mindre end 841 forskellige bots og så kan du holde øje med dem via den nye profil du har oprettet. De bliver altså ikke blandet sammen med dine "rigtige" besøgende som du tracker på almindelig vis. Jeg har lagt alle 3 php-filer i en mappe for sig som jeg kalder "analytics" og jeg inkluderer derfor filen med <em>include("analytics/analytics.php");</em>. I kommentarerne på den engelsk blog bliver der spurgt om man også skal indsætte GA tracking scriptet fra den nye profil, men det skal man ikke - det hele foregår via PHP scriptet, så det er ikke nødvendigt.
<h2>Hvad kan jeg så se?</h2>
Nu har du adgang til en masse informationer om de bots der besøger din side. Jeg implementerede det på mit linkkatalog den 23. november og der er nu ved at være samlet lidt data vi kan kigge på. I Google Analytics går du ind under "Traffic sources - search engines" og får en liste over alle de forskellige bots der har crawlet din side:

</div>
<div><a href="{{ '/assets/images/spor-bots-ga-6.jpg' | relative_url }}"><img class="alignnone size-full wp-image-31 no-border" title="spor-bots-ga-6" alt="" src="{{ '/assets/images/spor-bots-ga-6.jpg' | relative_url }}" width="777" height="426" /></a></div>
Hvis man klikker på de enkelte bots kan man se at der faktisk er meget forskel på hvordan de crawler en side. Yahoo kommer f.eks. næsten hver dag og crawler et lille udsnit af sitet hver gang:
<div><a href="{{ '/assets/images/spor-bots-ga-7.jpg' | relative_url }}"><img class="alignnone size-full wp-image-32 no-border" title="spor-bots-ga-7" alt="" src="{{ '/assets/images/spor-bots-ga-7.jpg' | relative_url }}" width="779" height="247" /></a></div>
Google kommer derimod kun sjældent, men crawler så til gengæld 811 sider og holder sig så væk. Botten kommer dog forbi engang imellem når der kommer nyt indhold på sitet og crawler de nye sider, men alle de "gamle" sider bliver kun crawlet sjældent. I hvert fald på mit linkkatalog, men det afhænger selvfølgelig meget af sitet:
<div><a href="{{ '/assets/images/spor-bots-ga-8.jpg' | relative_url }}"><img class="alignnone size-full wp-image-33 no-border" title="spor-bots-ga-8" alt="" src="{{ '/assets/images/spor-bots-ga-8.jpg' | relative_url }}" width="784" height="248" /></a></div>
<div>

Man kan derudover også se hvilke sider der er besøgt og her er robots.txt en klar topscorer, men også de vigtigste undersider bliver crawlet ofte:
<div> <a href="{{ '/assets/images/spor-bots-ga-9.jpg' | relative_url }}"><img class="alignnone size-full wp-image-34 no-border" title="spor-bots-ga-9" alt="" src="{{ '/assets/images/spor-bots-ga-9.jpg' | relative_url }}" width="773" height="341" /></a></div>
Til sidst et eksempel fra denne blog, hvor man kan se at Google har en bestemt bot som kun crawler rss-feeds. Det var ny viden for mig :)
<div><a href="{{ '/assets/images/spor-bots-ga-10.jpg' | relative_url }}"><img class="alignnone size-full wp-image-35 no-border" title="spor-bots-ga-10" alt="" src="{{ '/assets/images/spor-bots-ga-10.jpg' | relative_url }}" width="777" height="126" /></a></div>
Alt i alt et ganske smart lille trick som kan give lidt ny viden hvis man interesserer sig lidt for hvordan de forskellige bots egentlig opfører sig i praksis. Jeg glæder mig til at høre om det er noget I andre også finder sjovt?
<div></div>
</div>
<div></div>
<div></div>