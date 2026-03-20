---
layout: post
title: Kan browser fingerprinting erstatte cookies?
date: 2022-01-11 22:01:18
slug: browser-fingerprinting-erstatte-cookies
wordpress_id: 2166
categories:
  - Analytics
---

Tilbage i 2019 satte jeg mig for at undersøge om browser fingerprinting kunne være en erstatning for cookies til web analytics. Jeg indsamlede en masse data og <a href="https://www.linkedin.com/posts/laust-kehlet-741158a_5-danske-5-internationale-digitale-marketingblogs-activity-6885129039544160256-XCXn/">for nyligt blev jeg motiveret</a> til at få det analyseret og udgive et nyt blogindlæg.

<figure><a href="{{ '/assets/images/2022/01/Fingerprint-vs-sessions.jpg' | relative_url }}"><img src="{{ '/assets/images/2022/01/Fingerprint-vs-sessions-860x213.jpg' | relative_url }}" alt="Fingerprint data blev indsamlet tilbage i 2019-2020." width="860" height="213" class="size-large wp-image-2746" /></a><figcaption>Fingerprint data blev indsamlet tilbage i 2019-2020.</figcaption></figure>

<h2>Cookies er geniale men begrænsede</h2>

De seneste år er cookies blevet stærkt begrænset som redskab til at tracke brugere. Både fordi 3. part cookies er blevet begrænset med fx <a href="{{ '/itp-og-google-analytics/' | relative_url }}">ITP</a> men også fordi brugere nu skal give consent til cookies og dermed tracking.

Cookies er geniale til at genkende en bestemt browser på tværs af sidevisninger og sessioner. Det er helt anonymt og brugeren har fuld kontrol og kan slette cookies efter behov.

<h2>Browser fingerprinting</h2>

Et alternativ til at sætte en cookie med et anonymt ID kan være at forsøge at genkende og adskille browsere fra hinanden, baseret på alle de indstillinger og informationer man kan se om en given bruger med JavaScript. Dette kaldes <a href="https://en.wikipedia.org/wiki/Device_fingerprint">browser fingerprinting</a>.

Browser fingerprinting er stærkt kritiseret, fordi det sker uden at brugeren er klar over det og <a href="https://blog.mozilla.org/security/2020/01/07/firefox-72-fingerprinting/">browsere forsøger derfor at blokere for det</a>.

På <a href="https://amiunique.org/">amiunique.org</a> kan du se om der kan laves et unikt fingerprint af din browsere og se hvilke datapunkter der indgår i et fingerprint.

<h2>Hvad indgår i et fingerprint?</h2>

Her er en ikke-udtømmende liste over hvad der kan indgå i et fingerprint.

<ul>
<li>User Agent</li>
<li>Sprog</li>
<li>Operativ system</li>
<li>Tidszone</li>
<li>Hvilke fonts der er installeret</li>
<li>Om der bruges Adblocker</li>
<li>Browser</li>
<li>Browser version</li>
<li>Om Java er aktiveret</li>
<li>Hvilke plugins der er installeret</li>
<li>Skærm opløsning</li>
<li>Om browseren må bruge kamera og mikrofon</li>
<li>Og mange flere...</li>
</ul>

Men også ting som batteri status og om ens statuslinje er vist eller skjult.

<a href="{{ '/assets/images/2021/08/Fingerprint-data-points.jpg' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-data-points-860x452.jpg' | relative_url }}" alt="" width="860" height="452" class="aligncenter size-large wp-image-2709" /></a>

Se hele listen på <a href="https://amiunique.org/">amiunique.org</a>.

Men spørgsmålet er om det ovenhovedet gør browseren unik?

<h2>Kan fingerprinting erstatte cookies?</h2>

Fra et teknisk synspunkt er det interessant at teste om fingerprinting overhovedet kan være en erstatning for cookies i forhold til at identificere brugere i Google Analytics. Jeg lavede en test hvor jeg brugte <a href="https://github.com/fingerprintjs/fingerprintjs">fingerprintjs</a> til at generere et fingerprint og gemme det com custom dimension i Google Analytics. Selvfølgelig <a href="http://joshwayman.com/how-to-implement-fingerprint-js-with-gtm/">opsat i GTM</a>.

<a href="https://github.com/fingerprintjs/fingerprintjs">Fingerprintjs</a> laver et Array med alle datapunkterne som derefter hashes så man får en værdi som fx <code>69a45868bbc98e83a463e2e0730be988</code>.

<figure><a href="{{ '/assets/images/2021/08/Fingerprint-components-console.png' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-components-console-860x495.png' | relative_url }}" alt="Datapunkter der indgår i et fingerprintjs fingerprint som derefter hashes." width="860" height="495" class="size-large wp-image-2718" /></a><figcaption>Datapunkter som <a href="https://github.com/fingerprintjs/fingerprintjs">fingerprintjs</a> bruger til at lave et fingerprint som derefter hashes.</figcaption></figure>

Herunder ses nogle eksempler på fingerprints, device, browser samt hvor mange GA users der har præcis denne kombination. Hvis et fingerprint skal være unikt, skal det kun matche én bestemt User. Ellers er der dermed flere browsere som har det samme fingerprint og så kan det ikke bruges til at genkende én browser mellem sidevisninger og besøg, som en cookie kan.

<a href="{{ '/assets/images/2021/08/Fingerprint-10-random-fingerprints.jpg' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-10-random-fingerprints-860x352.jpg' | relative_url }}" alt="" width="860" height="352" class="aligncenter size-large wp-image-2712" /></a>

Og her kan man allerede se problemet, hvor flere Users har det samme fingerprint.

Hvis vi kigger på hele datasættet opdelt i desktop og mobile er der dog en stor andel af fingerprint værdierne der kun har én GA user, så de er unikke.

<a href="{{ '/assets/images/2021/08/Fingerprint-Record-count.jpg' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-Record-count-860x430.jpg' | relative_url }}" alt="" width="860" height="430" class="aligncenter size-large wp-image-2713" /></a>

Langt størstedelen af desktop har kun én User, men der er stadig 26 fingerprints som er fælles for mere end 5 GA Users. På mobile ser det dog anderledes ud, hvor der stadig er flest som matcher én User, men der er mange som matcher mere end én.

Dette skyldes at fingerprint afhænger af hvor meget man har ændret indstillingerne på sin computer og browser, samt installeret fonts og lignende. Og det gør man bare ikke i nær så høj grad på mobile.

Derudover er der også mange flere forskellige computere, med forskellige skærmopløsninger, osv. 
På mobile i Danmark er der rigtig mange brugere fordelt på de nyeste modeller af iPhone.

Men det bliver værre endnu.

For som det ses herover er der 200 fingerprints som matcher mere end 5 users og der er faktisk ét fingerprint som er ens for 128 forskellige browsere. Der er altså 128 iPhones som er 100% identiske i forhold til alle de datapunkter som fingerprintet bruger.

<a href="{{ '/assets/images/2021/08/Fingerprint-Top-10-fingerprints.jpg' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-Top-10-fingerprints-860x283.jpg' | relative_url }}" alt="" width="860" height="283" class="aligncenter size-large wp-image-2711" /></a>

Herunder ses antal users i datasættet fordelt på Device Category og Operating System. Der er 6304 users på iPhone og iPad, så når der er 128 brugere med samme fingerprint, så er det 2% af alle iPhones/iPads der har identisk fingerprint. Ikke særlig unikt, må man sige.

<a href="{{ '/assets/images/2022/01/Users-by-device-and-os.jpg' | relative_url }}"><img src="{{ '/assets/images/2022/01/Users-by-device-and-os-860x326.jpg' | relative_url }}" alt="" width="860" height="326" class="aligncenter size-large wp-image-2742" /></a>

For at se den totale udfordring med at bruge fingerprint til at gøre browsere unikke, har jeg vist summen af GA Users i de enkelte buckets herunder.

<a href="{{ '/assets/images/2021/08/Fingerprint-User-count-buckets.jpg' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-User-count-buckets-860x431.jpg' | relative_url }}" alt="" width="860" height="431" class="aligncenter size-large wp-image-2714" /></a>

Her ses det at der fx for mobile er 3655 users som har et unikt fingerprint. Men der findes samtidig 3923 users som har et fingerprint som deles af mere end 5 brugere.

Hvis vi opdeler dem i to grupper: Unikke fingerprints (som kun matcher én GA user) og ikke unikke fingerprints, så ser fordelingen således ud.

<a href="{{ '/assets/images/2021/08/Fingerprint-Unikt-vs-ikke-unikt-vs-device.jpg' | relative_url }}"><img src="{{ '/assets/images/2021/08/Fingerprint-Unikt-vs-ikke-unikt-vs-device-860x428.jpg' | relative_url }}" alt="" width="860" height="428" class="aligncenter size-large wp-image-2733" /></a>

På mobile er det altså kun 37% af brugere der har et unikt fingerprint, mens det på desktop er 89%. Totalt set har 58% af brugerne et unikt fingerprint og når andelen af trafik fra mobile tilmed er stigende er det derfor totalt umuligt at bruge fingerprint til at identificere og genkende brugere og dermed være en erstatning for cookies.

<h2>Andre alternativer til cookies</h2>

<a href="https://plausible.io/">Plausible Analytics</a> er en ny analytics platform, som kan lave (simpel) analytics uden brug af cookies.

<a href="{{ '/assets/images/2022/01/plausible-analytics-jacobworsoe-dk.jpg' | relative_url }}"><img src="{{ '/assets/images/2022/01/plausible-analytics-jacobworsoe-dk-860x777.jpg' | relative_url }}" alt="" width="860" height="777" class="aligncenter size-large wp-image-2737" /></a>

I stedet for cookies bruger laver de et hash af IP adresse og User Agent samt et daily salt. Derved kan de genkende den samme bruger på den samme dag, men næste dag vil der være et nyt salt og så vil brugere være en ny unik bruger. Teoretisk vil der sagtens kunne være flere forskellige brugere fra den samme IP som har samme User Agent, men i praksis vil det være marginalt, så det er et OK kompromis. Meget bedre end fingerprinting, som faktisk ikke bruger IP adressen.

Under afsnittet <a href="https://plausible.io/data-policy">How we count unique users without cookies</a> kan du læse mere om hvordan Plausible Analytics tæller unikke brugere uden cookies. Eller du kan læse det her:

<a href="{{ '/assets/images/2022/01/Plausible-analytics-unique-visitors-without-cookies.jpg' | relative_url }}"><img src="{{ '/assets/images/2022/01/Plausible-analytics-unique-visitors-without-cookies.jpg' | relative_url }}" alt="" width="693" height="1232" class="aligncenter size-full wp-image-2738" /></a>