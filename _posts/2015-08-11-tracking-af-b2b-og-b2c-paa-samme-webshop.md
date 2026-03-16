---
layout: post
title: Tracking af B2B og B2C på samme webshop
date: 2015-08-11 23:46:45
slug: tracking-af-b2b-og-b2c-paa-samme-webshop
categories:
  - Analytics
---

Nogle webshops handler både med B2B og B2C segmentet. Nogle webshops har tilmed begge dele på samme webshop, hvilket kan give nogle udfordringer i forhold til analytics. Lad os kigge på de mulige løsninger i prioriteret rækkefølge.

<h2>Problemet med B2B/B2C</h2>

Købsadfærden for B2B og B2C kan være vidt forskellig. Ofte er B2B i langt højere grad genkøb, hvilket giver højere konverteringsrater. B2B har typisk også langt større ordrestørrelser. Dette kan fx være på en webshop, hvor private kan købe, men hvor forhandlere kan logge ind og få nogle andre priser, fordi de køber større ind og har en aftale om en bedre pris. Dette kan gøre det svært at analysere på data efterfølgende, hvis det hele er mudret sammen, og man derfor kun kan se gennemsnittet, hvilket ikke giver mening at kigge på, hvis der er store forskelle.

<h2>Hvorfor blande det sammen?</h2>

Fordelene ved at køre det hele på samme webshop er mange. De største er mindre udviklingsomkostninger, man skal ikke skrive unikke produktbeskrivelser til de to shops for at undgå duplicate content og man har ikke to webshops der skal markedsføres og laves SEO på. Men det er vigtigt at data bliver opdelt, så man kan analysere særskilt på B2C og B2B.

<h2>Opdeling af data på ejendomme</h2>

Den første mulighed er at have to Google Analytics ejendomme og registrere på ejendom 1 som standard og når brugeren er logget ind ved vi at det er en B2B kunde og derefter registrere på ejendom 2.
<strong>Fordele:</strong>

<ul>
<li>Alle B2B ordre bliver lagt på sin egen GA ejendom og ecommerce data er dermed helt adskilte.</li>
</ul>

<strong>Ulemper:</strong>

<ul>
<li>Du mister trafikkilden på ejendom 2. Besøget registreres som et nyt besøg på ejendom 2 og den sidst sete side og dermed trafikkilden er sitet selv, så trafikkilden bliver Direct / none.</li>
<li>Trafikken bliver kun til dels opdelt, da vi først kan begynde at registrere på ejendom 2 når kunden er logget ind, og B2B kunder som besøger sitet uden at være logget ind vil derfor blive registreret på ejendom 1.</li>
</ul>

En optimering af denne løsning kan være at gemme en cookie på brugerens computer når de logger ind som B2B kunde. Derved kan vi genkende dem på næste besøg med det samme og trafikkilden bevares dermed. På denne måde kan vi også fange dem som er B2B kunder men ikke logger ind hver gang de besøger sitet. Der vil dog stadig være mange som ikke bliver tracket korrekt, fx når de bruger deres mobiltelefon hvor vi ikke har en cookie gemt. Der vil derved stadig være B2B kunder som bliver tracket på B2C ejendommen.

<h2>Opdeling via affiliation</h2>

Når der sendes Ecommerce data til Google Analytics på kvitteringssiden kan affiliation feltet bruges til at angive om ordre er B2B eller B2C.
<strong>Fordele:</strong>

<ul>
<li>Alt trafik samles nu på samme ejendom trafikkilder bliver derfor ikke ødelagt.</li>
<li>Det hele er samlet på én ejendom og det er derfor nemt at få et overblik over det samlede antal besøg og udviklingen i trafik til sitet.</li>
<li>Via en tilpasset rapport eller segmenter kan Ecommerce data opdeles i B2B/B2C.</li>
</ul>

<strong>Ulemper:</strong>

<ul>
<li>Opdelingen sker først når ordren afgives.</li>
<li>Alt trafik er samlet på én ejendom og kan ikke segmenteres. Kun Ecommerce data kan segmenteres.</li>
</ul>

<h2>Opdeling via tilpasset dimension (custom dimension)</h2>

Alt trackes på samme ejendom. Der sættes som standard en sessionbaseret tilpasset dimension på alle besøg med værdien B2C. Når en B2B kunde har en cookie, logger ind eller afgiver en ordre ændres den tilpassede dimension til B2B. Det smarte ved sessionbaserede dimensioner er at de først bliver registreret i Google Analytics når sessionen (brugerens besøg) afsluttes, hvilket sker når brugeren har være inaktiv i 30 minutter. Dimensionen sættes til den sidste værdi den har haft, dvs. selvom dimensionen starter som B2C og senere ændres til B2B, vil hele besøget registreres som B2B.
<strong>Fordele:</strong>

<ul>
<li>Alt data er samlet på en ejendom og giver nemt overblik.</li>
<li>Trafikkilde bevares.</li>
<li>B2B kunder registreres så snart det er muligt og hele deres besøg (incl evt. Ecommerce data) registreres som et B2B besøg.</li>
<li>Tilpassede dimensioner kan bruges både i segmenter og tilpassede rapporter.</li>
<li>Mulighed for at segmentere både trafik, adfærd på sitet og Ecommerce data på B2C/B2B.</li>
</ul>

<strong>Ulemper:</strong>

<ul>
<li>Brugeren skal først genkendes som B2B før han registreres korrekt. Den eneste måde at komme udenom det er ved at lave en seperat B2B webshop på sit eget domæne med sin egen Google Analytics ejendom.</li>
</ul>

<h2>Konklusion</h2>

Fordelene ved at have B2C og B2B er som beskrevet i starten mange. Men det gør tracking besværlig. Data kan nemt ødelægges og gøres ubruglige, især trafikkilden. Udfordringen er at man oftest ikke ved om brugerne er B2C eller B2B før de logger ind eller afgiver en ordre. Hvis B2B brugerne har deres egne priser vil de dog typisk logge ind med det samme. De ovenstående løsninger er prioriteret efter hvad der oftest vil være den bedste løsning, med den bedste til sidst (opdeling via tilpasset dimension) men i nogle tilfælde kan en af de andre være at foretrække.

Hvilken løsning har I valgt? En af de tre jeg beskriver her eller en helt fjerde løsning? Lad os tage en snak om det i kommentarerne!