---
layout: post
title: 11 fordele ved et statisk website (udover at det loader på 0,2 sek!)
date: 2016-09-21 22:15:08
slug: fordele-ved-et-statisk-website
wordpress_id: 933
categories:
  - Webdesign
---

Vi kan lige så godt tage den største fordel først. Statiske websites er lynende hurtige!

<a href="https://tools.pingdom.com/#!/eJQ7vr/http://jacobworsoe.github.io/exchangemycoins-jekyll-blog/"><figure><img src="https://www.jacobworsoe.dk/wp-content/uploads/Jekyll-Pingdom-tools-Github-pages-1.png" alt="Statiske websites er hurtige... meget hurtige!" width="750" height="209" class="size-medium wp-image-991" /><figcaption>Statiske websites er hurtige... meget hurtige!</figcaption></figure></a>

<strong>178 ms!</strong>

Det er hurtigt.

Men hvad er et statisk website? Og hvorfor er det så hurtigt?

Et <strong>statisk website</strong> består kun at statiske HTML filer. Ingen server-side filer med PHP eller ASP kode.

Og nu tænker du sikkert: "Jamen, er det ikke håbløst gammeldags?!"

Nej, ikke længere. Med en statisk website generator som <a href="https://jekyllrb.com/">Jekyll</a>, er statiske websites blevet smarte igen.

<a href="https://jekyllrb.com/"><img src="https://www.jacobworsoe.dk/wp-content/uploads/jekyll-logo-light-solid.png" alt="jekyll-logo-light-solid" width="960" height="489" class="alignnone size-full wp-image-1005" /></a>

Vores blog på <a href="https://www.exchangemycoins.com/blog">ExchangeMyCoins.com</a> er drevet af Jekyll og består kun af statiske HTML filer og serveren skal derfor ikke først lave en masse arbejde, før websiden kan sendes til brugeren. Og det gør sitet lynende hurtigt!

<h2>Statiske vs. dynamiske websites</h2>

Da internettet startede, var alle websites bygget af statiske HTML sider. Senere hen kom ASP og PHP til, som gjorde det muligt at lave dynamiske websites med kontaktformularer, kommentarfelter og fora, for slet ikke at nævne webshops og sociale medier. Dynamiske websites banede også vejen for web 2.0 med brugerdrevet indhold i massevis. Alt sammen drevet af en database som brugerne kunne putte indhold ned i og dermed selv bidrage med indhold til websitet. Det gav også mulighed for CMS’er som Wordpress, hvor en bruger kunne skabe websites i et lækkert interface uden at skulle rode med HTML filer.

Dynamiske websites har også mulighed for at genbruge indhold på tværs af sider, fx en menu eller en footer, ved at lægge indholdet ud i en separat fil, som så inkluderes på alle sider. Dermed skal man kun rette i én fil, hvis man fx skal tilføje et menupunkt til menuen og så vil det automatisk blive inkluderet på alle siderne.

I Wordpress og andre CMS’er er alt drevet af templates som dynamisk udfyldes med indhold fra databasen, fx på en blog hvor der er én template til alle blogindlæg. Templaten styrer det overordnede design for siden, mens indholdet hentes dynamisk op fra databasen, afhængig af den URL brugeren besøger. Dette har igen den fordel at man kan rette designet for alle ens blogindlæg, eller produkter i en webshop, ved kun at rette i én template.

<h2>Ulempen er performance</h2>

Dynamiske websites har altså en masse fordele men det har også en stor ulempe – performance! Fordi alting er dynamisk skal hver side genereres hver gang en bruger vil se en side. På et typisk blogindlæg skal webserveren sammensætte siden med logo, menu, søgefunktion, selve blogindlægget, kommentarer, sidebar, seneste kommentarer, mest populære indlæg, etc. Og alle de informationer skal hentes forskellige steder i databasen. Dette indlæg henter fx data 39 forskellige steder(!) i databasen før siden kan bygges og sendes til browseren:

<figure><img src="https://www.jacobworsoe.dk/wp-content/uploads/Wordpress-39-database-queries.png" alt="Wordpress henter indhold 39 steder i databasen, for at kunne vise dette indlæg." width="706" height="347" class="size-full wp-image-981" /><figcaption>Wordpress henter indhold 39 steder i databasen, for at kunne vise dette indlæg.</figcaption></figure>

Når alle data er hentet, skal det hele indsættes i templaten og derefter sendes til brugeren som en HTML fil - alt imens brugeren bare sidder og venter – og det kan sagtens tage mere end 5 sekunder at generere en side!

Især hvis der også bruges en lang række plugins, som hver især tilføjer noget funktionalitet til siden, som skal genereres på hver sidevisning. Det kan fx være relaterede indlæg, som er en rigtig tung operation fordi det aktuelle indlæg skal sammenlignes med <u>alle</u> de andre indlæg i databasen og finde dem som matcher bedst, hvilket også har gjort at webhoteller som <a href="https://wpengine.com/support/disallowed-plugins/">wpengine.com</a> og <a href="https://mediatemple.net/community/products/wordpress/204405734/which-plugins-and-activities-are-not-allowed-with-my-wordpress-hosting-service">mediatemple.net</a> har forbudt den slags plugins.

<h2>5 sekunder for Time-to-first-byte?</h2>

Ja, det kan sagtens tage 5 sekunder for tunge dynamiske websites at bygge siden inden den er klar til at blive sendt til brugeren. Se fx disse forskelle i time-to-first-byte for forsiden af nogle forskellige sider:

<strong>Statisk site bygget med Jekyll: 43 ms</strong>
<figure><img src="https://www.jacobworsoe.dk/wp-content/uploads/TTFB-Jekyll.png" alt="Statisk site bygget med Jekyll" width="750" height="210" class="size-medium wp-image-983" /><figcaption>Statisk site bygget med Jekyll</figcaption></figure>

<strong>jacobworsoe.dk (med caching): 46 ms</strong>
<figure><img src="https://www.jacobworsoe.dk/wp-content/uploads/TTFB-Wordpress-med-caching.png" alt="jacobworsoe.dk (med caching)" width="750" height="197" class="size-medium wp-image-986" /><figcaption>jacobworsoe.dk (med caching)</figcaption></figure>

<strong>jacobworsoe.dk (uden caching): 763 ms</strong>
<figure><img src="https://www.jacobworsoe.dk/wp-content/uploads/TTFB-Wordpress-uden-caching.png" alt="jacobworsoe.dk (uden caching)" width="750" height="205" class="size-medium wp-image-984" /><figcaption>jacobworsoe.dk (uden caching)</figcaption></figure>

<strong>Wordpress Woocommerce webshop (uden caching): 6,53 sekunder!</strong>
<figure><img src="https://www.jacobworsoe.dk/wp-content/uploads/TTFB-Wordpress-Woocommerce.png" alt="Wordpress Woocommerce webshop (uden caching)" width="750" height="250" class="size-medium wp-image-985" /><figcaption>Wordpress Woocommerce webshop (uden caching)</figcaption></figure>

<strong>0,043 sekunder vs. 6,53 sekunder!</strong>

Dette er en af de helt store årsager til at mange websites er så langesomme.

Og det værste er at alt dette arbejde laves hver gang den samme side besøges, uanset om indholdet har ændret sig eller ej - medmindre siden caches, men det kommer vi tilbage til.

<h2>Fordelen ved statiske websites</h2>

På et statisk website bygges alle sider på forhånd og ikke først når brugeren besøger siden. Alt det hårde arbejde er dermed lavet og siderne ligger klar på webserveren til at blive sendt til brugeren, med det samme, når de besøger siden. Dermed kan loadtiden skæres ned fra 5+ sekunder til under 0,2 sekund!

Med en statisk website generator som Jekyll, genereres HTML filerne, når jeg ændrer noget på sitet, fx tilføjer et blogindlæg.

Selve blogindlægget bliver lavet, ved at Jekyll indsætter indholdet i en vores template sammen med header og footer og samler det til én HTML fil. Forsiden ændres, så det nye indlæg bliver vist på forsiden sammen med et link til indlægget. RSS feeds og XML sitemaps opdateres. Vi har også paginering på bloggen, så side 2 og side 3 af forsiden, bliver også genereret på ny, da det nye bogindlæg jo har skubbet alle andre blogindlæg ét hak ned og dermed ændrer alle sider sig. Jekyll laver alt dette på for os og det skal kun gøres når der er lavet ændringer på sitet. Dette giver en masse fordele.

<h2>Fordel #1: Man arbejder stadig i templates</h2>

Det rigtig smarte ved værktøjer som Jekyll, er at man stadig kan arbejde med templates, dvs. hvis man vil indsætte et nyt logo i headeren, så skal det kun rettes ét sted, nemlig i header templaten, som bliver indsat på alle sider, når Jekyll bygger websitet. Fuldstændigt som du kender det, hvis du har bygget templates til Wordpress eller blot har brugt include i PHP.

Templates i Jekyll er drevet af Liquid som er et template-sprog udviklet af Shopify og gør det mega nemt at opsætte templates. Herunder ses et eksempel på den template som bruges til at vise blogindlæg.

<pre><code class="language-html">&#123;% include header.html %&#125;
<article id="&#123;&#123; page.id &#125;&#125;" class="&#123;&#123; page.id &#125;&#125;">
       <h1>&#123;&#123; page.title &#125;&#125;</h1>
       <p class="post-date">&#123;&#123; page.date | date: '%B %d, %Y' &#125;&#125;</p>
       &#123;&#123; content &#125;&#125;
</article>
&#123;% include footer.html %&#125;
</code></pre>

<h2>Fordel #2: Det tunge arbejde laves ved ændringer – ikke læsninger</h2>

Det helt geniale – ud fra et performancesynspunkt – ved Jekyll er, at det tunge arbejde med at bygge websitet ved at hente indhold og samle det med templates til færdige HTML sider, bliver lavet når jeg ændrer noget på websitet og ikke hver gang en side bliver vist. Og det er jo den helt rigtige tilgang. Så længe der ikke er ændret noget på websitet er der ingen grund til at de færdige HTML sider skal bygges fra bunden igen.

<h2>Fordel #3: HTML filer kan ikke hackes</h2>

Når Jekyll har bygget websitet, er det eneste jeg uploader til webserveren de færdige HTML, CSS og JavaScript filer, samt billeder. Det er det! Der er altså ingen database der kan hackes eller skal opdateres. Der er ikke en backend som brugere kan hacke sig ind i og begynde at slette indhold og andre skadelige ting.

<h2>Fordel #4: Ikke flere sikkerhedsopdateringer</h2>

Hvis du har et Wordpress website, så ved du hvor tit der findes nye sikkerhedshuller som skal lukkes med en opdatering. Selvom Wordpress teamet er hurtige, så går der stadig noget tid fra hullet opdages til de har lukket det med en opdatering. Alt den tid vil websitet være sårbart. Med Jekyll er dette problem elimineret og du slipper for at bekymre dig om sikkerhedsopdateringer. Det er rart hvis du har mange sites!

<h2>Fordel #5: Skalering</h2>

Når serveren har de færdige HTML filer liggende klar på serveren, betyder det ikke kun at siderne kan sendes til brugeren med det samme og dermed sænker loadtiden til et minimum. Det betyder også at serveren har meget mindre at lave. Faktisk næsten ingenting. Den skal bare sende HTML sider og billeder til brugerne. Og dét er webservere rigtig gode og hurtige til! Det betyder dermed at serveren kan håndtere mange flere brugere inden den går ned – hvilket er en kæmpe fordel, hvis du bliver nævnt på forsiden af EB.dk eller lignende.

Under Obamas valgkamp i 2012 skulle hans webteam bruge et website der kunne klare meget trafik – rigtig meget trafik! I USA er valgkampagnerne meget afhængige af donationer og Obamas webteam med Kyle Rush – der i dag er Head of Optimization hos Optimizely – i spidsen, var klar over at online var et vigtigt element i at nå donationsmålet på $1.000.000.000 (ja, 9 nuller!).

De havde derfor brug for et website der kunne klare ekstremt meget trafik og mange transaktioner.

<blockquote>Our highest surge was $3 million an hour so any down time would have been very costly.<cite>Kyle Rush</cite></blockquote>

3 millioner dollars i timen! Som du nok har gættet, valgte de et statisk website, bygget med Jekyll, for at kunne klare presset. Og presset var faktisk så stort at det svageste led i kæden var deres betalingsgateway. De var derfor nødt til at lave et redundant setup med to betalingsgateways, og et system som fordelte trafikken mellem de to gateways. Et ret avanceret setup, men med et meget simpelt website.

Og de nåede målet. Der blev indsamlet $1,1 milliard hvoraf $690 millioner blev hentet online!

Det nye site var 60 % hurtigere end det gamle, målt på time-to-paint, altså hvornår brugeren ser websitet på skærmen. De A/B testede det op mod det gamle website med en identisk side, og konverterede 14 % bedre eller hvad der svarer til $32 millioner dollars mere i donationer.

<h2>Fordel #6: Billig hosting</h2>

Når websitet ikke kræver hverken database eller noget backend kode som PHP eller ASP, så skal hosting heller ikke være så avanceret og dermed billigere. Og det kan faktisk blive gratis.

Githubs webhosting service, Github Pages, er gratis for alle brugere og er drevet af Jekyll. Du kan dermed få gratis hosting på Githubs meget stabile servere og nyde godt af deres CDN med servere fordelt over hele verdenen, så du får endnu hurtigere loadtid, uanset hvor dine brugere befinder sig.

Du uploader simpelthen bare dine ændringer til Github, ligesom man normalt gør med kode og når Github opdager at du har lavet en ændring til dit Jekyll website, bygger de et nyt website for dig og websitet kommer til at ligge på Github.io.

Og hvis du roder lidt med <a href="https://help.github.com/articles/using-a-custom-domain-with-github-pages/">CNAME</a> kan du også få dit eget domæne på websitet.

Her er desuden en rigtig fed analyse af loadtiden på 6 forskellige hosts: <a href="https://www.savjee.be/2017/10/Static-website-hosting-who-is-fastest/">Static website hosting: who's fastest? AWS, Google, Firebase, Netlify or GitHub?</a>

<h2>Fordel #7: Backup og historik</h2>

Da Tom Preston-Warner skabte Jekyll, var en af grundene at han var træt af at miste sit indhold. Han havde lavet flere websites, som var gået tabt og indholdet var for evigt borte. En vigtig feature for Jekyll var dermed nem og sikker backup. Med Jekyll er backup nemt.

Ved at bruge Github til at hoste dit website, har de også automatisk backup af dit site, fordi koden til sitet og alt indholdet altid ligger på deres servere. Github er bygget til udviklere, som skal holde styr på deres kode, når de samarbejder med andre eller bare er dem selv. Derfor har Github et lækkert system til versionering og historik, og du har dermed også uendelig historik. Ikke kun på koden, men også af indholdet på dit site. Det er fedt!

Ligesom med kode, har man også en lokal kopi af det hele på ens computer, så jeg har også en komplet backup og historik på alle mine computere. Og derudover har mine kollegaer i ExchangeMyCoins også en kopi på deres computer. Så der skal gå meget galt, hvis vi skal miste det hele.

<h2>Fordel #8: Markdown</h2>

Indhold kan både skrives i HTML format og Markdown. Jeg mener at alle der arbejder med web bør lære sig selv det mest basale HTML, så man har styr på formatering af tekst og kan skrive fed og kursiv, samt opstille lister, lave overskrifter og links. Det er nemt at lære og kan gøre livet som webredaktør meget nemmere, når man selv kan det mest basale. Men selv hvis man ikke kan det, så kan man stadig bruge Jekyll, da indhold også kan skrives i Markdown format. Derudover har Markdown <a href="http://mediatemple.net/blog/tips/you-should-probably-blog-in-markdown/">mange fordele fremfor at skrive indholdet i HTML</a>.

<h2>Fordel #9: Do-follow link fra Github.com – et DA 95 website</h2>

Der er et tæt samarbejde mellem Github og Jekyll, primært fordi de begge er startet af <a href="https://en.wikipedia.org/wiki/Tom_Preston-Werner">Tom Preston-Werner</a>. Derfor giver Github gratis hosting til Jekyll websites og Gtihub hjælper også med at udbrede kendskabet til Jekyll og hjælpe nye brugere i gang. Github har derfor lavet en <a href="https://github.com/jekyll/jekyll/wiki/Sites">oversigt over websites lavet med Jekyll</a> med link til websitet samt kildekoden, så nye brugere kan se hvad der kan laves med Jekyll og hvordan det er lavet. Dermed får du et lækkert dofollow link fra Github.com – et website med indgående links fra 8049 domæner og en Domain Authority på 95. Det er da også værd at tage med.

<h2>Fordel #10: Slut med at have bloggen på et subdomæne</h2>

En af grundene til at jeg valgte at bruge Jekyll til vores blog var at mit foretrukne værktøj til blogging er Wordpress. Vores website er dog bygget i ASP, så derfor var jeg nødt til at smide bloggen på blog.exchangemycoins.com så linkjuice ville blive spredt over to domæner. Jekylls statiske HTML filer kan køre på alle webservere, så uanset om man bruger PHP, ASP, Ruby, etc. vil man altid kunne uploade filerne til en mappe der hedder ”blog” og få samlet det hele på ét domæne. Dette vil alene være argument nok for mange af de virksomheder som blogger på et subdomæne uden optimalt SEO værdi.

<h2>Fordel #11: Et hav af smarte funktioner</h2>

Og der er masser af <a href="https://jekyllrb.com/docs/templates/">smarte funktioner</a>, fx til at generere meta descriptions. Hvis der er skrevet en excerpt til siden, så bliver den brugt. Ellers tager den de første 155 tegn fra selve indholdet, fjernet for html koder og linjeskift.

<pre><code class="language-html"><meta name="description" content="
&#123;% if page.excerpt %&#125;
&#123;&#123; page.excerpt &#125;&#125;
&#123;% else %&#125;
&#123;&#123; page.content | strip_html | strip_newlines | truncate: 155 &#125;&#125;
&#123;% endif %&#125;
">
</code></pre>

Så bare fordi sitet er statisk, kan det stadig lave alt det hårde arbejde for dig.

<h2>Jekyll er for nørder</h2>

Jeg vil ikke lyve. Jekyll kræver lidt teknisk snilde for at man kan bruge det. De fleste kan lære at bruge Wordpress og skrive og udgive nye indlæg. Jekyll kræver lidt mere og er dermed ikke for ikke-tekniske personer. Det kræver at man ikke bliver forskrækket af en kommandoprompt. Der er ikke noget grafisk interface til Jekyll. Når sitet skal bygges, skal der åbnes en prompt og køres en kommando og derefter uploade det færdige website til din webserver. Og det vil være en deal-breaker for nogen. Så hvis du sælger websites til tandlæger og den lokale tennisklub, så skal du ikke bygge sitet på Jekyll. Så skal du holde dig til Wordpress.

Der er dog lavet værktøjer som gør det væsentligt nemmere at være redaktør på et Jekyll website. <a href="http://prose.io/">Prose.io</a> giver redaktører et lækkert interface at skrive indhold i, som man kender det fra fx Wordpress og fungerer ved at man kan rette i filerne på Github gennem deres API.

<a href="http://cloudcannon.com/">Cloudcannon</a> har lavet et helt CMS interface til at styre flere Jekyll websites igennem.

<h2>Ikke optimalt til kommentarer og brugergenereret indhold</h2>

En af de store ulemper ved statiske websites er at brugere ikke kan tilføje indhold til sitet, fx kommentarer til et blogindlæg. Det er dog muligt at få kommentarer, igennem et værktøj som <a href="https://developers.facebook.com/docs/plugins/comments">facebook comments</a> eller <a href="https://disqus.com/">Disqus</a> som jeg bruger på bloggen. Man ejer ikke data selv, men de bliver fint indekseret af Google, så man får stadig SEO værdien af det brugerskabte indhold.

I den danske blogverden har antallet af kommentarer været kraftigt faldende de par seneste år, hvilket jeg har <a href="https://plus.google.com/u/0/+jacobworsoe/posts/YsCqBLCn1oi">analyseret her</a> og Anders Saugstrup <a href="http://marketers.dk/blog/den-sidste-kommentator/">skrev også om det her</a>. Debatten er flyttet over på de sociale medier. Så måske er der ikke så meget at miste. Måske er det ligefrem en fordel af bruge facebook comments?

Men du kan sagtens eje data selv. Bare fordi sitet ikke selv bruger server-side kode, kan man stadig sagtens hente og sende data til en database med lidt AJAX. Det er der flere der har gjort, for at få et kommentarsystem, hvor man selv ejer data. Det kan fx bygges med <a href="https://css-tricks.com/building-a-jekyll-site-part-3-of-3/">Firebase</a> eller <a href="http://savaslabs.com/2016/04/20/squabble-comments.html">Lumen</a>. Men det er ikke noget der er indbygget i Jekyll, så du skal kode alt selv.

<blockquote>The major downside of building your own comment hosting application is that you have to … build your own comment hosting application. In other words, nothing comes for free — you have to build every feature yourself.<cite><a href="http://savaslabs.com/2016/04/20/squabble-comments.html" target="_blank" rel="noopener noreferrer">Kosta Harlan</a></cite></blockquote>

<h2>Kan det ikke bare løses med et caching plugin?</h2>

Det her med at gemme websitet som statiske HTML filer er faktisk lige præcis det et caching plugin som <a href="https://wordpress.org/plugins/w3-total-cache/">W3C Total Cache</a> gør. Og på den måde får du faktisk det bedste af to verdener – et dynamisk website med brugerskabt indhold og statiske HTML filer der loader lynhurtigt. Udfordringen er bare at caching er skide svært at kode optimalt.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.</p>&mdash; Jeff Atwood (@codinghorror) <a href="https://twitter.com/codinghorror/status/506010907021828096">August 31, 2014</a></blockquote>

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Du skal sørge for at cachen bliver clearet på de rigtige tidspunkter og samtidig sørge for at cachen ikke bliver clearet unødigt ofte, så websitet skal genskabe cachen hele tiden, fx lige præcis i det øjeblik hvor Googlebot kommer forbi og Googlebot derfor oplever at du har et langsomt website. Og se bare på alle de indstillinger der er i de populære caching plugins til fx Wordpress. Caching er ikke man bare lige sætter op – det skal gøres rigtigt, hvis det ikke skal backfire. Men til gengæld får du alle fordelene ved at dynamisk website.

Der er ikke noget der er rigtigt og forkert - det afhænger af projektet. Men caching løser ikke alle de problemer, som Jekyll løser. Der er stadig udfordringerne med skalering, hosting, hacking, sikkerhedsopdateringer, backup, osv.

Men det rigtige værktøj til opgaven. Hvis jeg skal bygge et site som skal kunne noget dynamisk, så vil jeg stadig bygge det på Wordpress med caching.

<h2>Har du brug for et dynamisk website?</h2>

Jekyll er lavet til nørder. Det er ikke et godt system til ikke-tekniske brugere. Der vil Wordpress være bedre.

Jekyll er lavet til statiske websites. Hvis dit website skal kunne noget dynamisk, fx at brugere skal kunne logge ind eller skrive kommentarer, så er Jekyll ikke optimalt.

Men der findes rigtig mange Wordpress sites derude, som ikke behøver være dynamiske fordi de opdateres meget sjældent. Fx visitkort websitet hos din tandlæge eller din lokale idrætsklub som bliver opdateret to gange om året med nye åbningstider eller næste sæsons træningstider, og som måske udelukkende vedligeholdes af et webbureau. De websites har ikke brug for at være dynamiske og kunne derfor få en masse fordele ved at blive lavet som et statisk website.

Så hvis du har et website, som kun vedligeholdes af dig selv og som ikke kræver noget dynamisk indhold, så overvej at bygge det med Jekyll og få en masse fordele og et lynhurtigt website!

<strong>Opdatering:</strong> Denne artikel skabte også en spændende debat om statiske websites i <a href="https://www.facebook.com/groups/158668454225674/permalink/1145680752191101/">Frontenders.dk gruppen på facebook</a>.