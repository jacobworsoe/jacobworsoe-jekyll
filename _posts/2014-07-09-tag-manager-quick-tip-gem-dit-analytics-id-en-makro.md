---
layout: post
title: "Tag Manager Quick Tip: Gem dit Analytics ID i en makro"
date: 2014-07-09 09:11:02
slug: tag-manager-quick-tip-gem-dit-analytics-id-en-makro
wordpress_id: 603
categories:
  - Analytics
---

Jeg arbejder rigtig meget med Google Tag Manager for tiden og elsker det mere og mere, men en af de ting der kan gøre processen lidt besværlig er at man skal indtaste sit Google Analytics ID (fx UA-11679419-1) på hver enkelt Tag, istedet for at sætte det globalt.

<figure><a href="{{ '/assets/images/google-tag-manager-ua-på-hvert-tag.png' | relative_url }}"><img class="size-full wp-image-604" src="{{ '/assets/images/google-tag-manager-ua-på-hvert-tag.png' | relative_url }}" alt="Analytics ID skal indsættes på hvert enkelt Tag." width="710" height="680" /></a><figcaption>Analytics ID skal indsættes på hvert enkelt Tag.</figcaption></figure>

Det er selvfølgelig smart at man kan skyde Tags afsted til forskellige Google Analytics ejendomme og styre det hele via den samme container. Det kan dog blive en udfordring i forbindelse med test, hvis der er opsat en lang række Tags som sender data til Google Analytics, typisk Event Tracking. Jeg plejer at teste opsætningen på en dedikeret test ejendom i Google Analytics, så der ikke kommer test data ind på den rigtige ejendom. Når testen så er færdig, skal jeg ind på alle Tags og ændre mit Analytics UA, så den sender data til den rigtige ejendom. Det kan godt blive lidt tungt hvis der er rigtig mange Tags.
<h2>Løsningen</h2>
Du kan dog godt sætte dit UA et globalt sted, nemlig som en makro. Makroer bruges normalt til at overføre data fra websitet til Tag Manager. Disse data kan fx være variable i et Data Layer, URL'er eller klasser/ID'er på de elementer på siden der interageres med. Ovre i Tag Manager kan du så overføre disse data til Google Analytics som værdier i Event Tracking eller Custom variabler, eller du kan opsætte regler på baggrund af værdien af de makroer, fx når en bruger lander på en bestemt URL.

Men makroer behøver ikke komme fra websitet - du kan også sætte dine egne værdier, fx dit Analytics ID.

<figure><a href="{{ '/assets/images/google-tag-manager-ua-i-en-makro.png' | relative_url }}"><img class="size-full wp-image-605" src="{{ '/assets/images/google-tag-manager-ua-i-en-makro.png' | relative_url }}" alt="Analytics ID i en makro." width="283" height="329" /></a><figcaption>Analytics ID i en makro.</figcaption></figure>

Når du fremover opretter Tags, indsætter du nu makroen istedet for at skrive dit ID ind og du kan derefter lynhurtigt ændre dit ID ét sted, hvorefter det slår igennem på alle Tags!

<figure><a href="{{ '/assets/images/google-tag-manager-indsæt-makro-i-tag.png' | relative_url }}"><img class="size-full wp-image-606" src="{{ '/assets/images/google-tag-manager-indsæt-makro-i-tag.png' | relative_url }}" alt="Indsæt makroen i dine Tags." width="344" height="591" /></a><figcaption>Vælg makroen fra listen og indsæt i dine Tags.</figcaption></figure>

Tag Manager handler blandt andet om at kunne foretage lynhurtige ændringer i dit tracking setup og med ovenstående trick er det lige blevet en lille smule hurtigere. Især hvis man tracker 30+ Events rundt omkring på sitet, og hvis du læser med her på bloggen, så er der en god chance for at du også indsamler massevis af data fra dit website?