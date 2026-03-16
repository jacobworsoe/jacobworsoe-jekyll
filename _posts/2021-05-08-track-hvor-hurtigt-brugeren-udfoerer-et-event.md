---
layout: post
title: Track hvor hurtigt brugeren udfører et event
date: 2021-05-08 16:21:41
slug: track-hvor-hurtigt-brugeren-udfoerer-et-event
wordpress_id: 1935
categories:
  - Analytics
---

En af de ting jeg næsten altid tracker sammen med Event Tracking er time to event.

Dermed kan jeg se hvor lang tid der går fra brugeren lander på siden til et Event udføres.

Det tilføjer også en spændende dimension til dine data, som ikke er tilgængelig i en standard Google Analytics opsætning, nemlig tid mellem forskellige events indenfor en session.

Google Analytics er god til at vise hvor mange sessioner, transaktioner, etc. du har haft på en given dag eller time, samt den gennemsnitlige varighed for de sessioner. Men der er ikke noget data på rækkefølgen af events eller tiden mellem de enkelte events. Det tilføjer vi noget af i dag.

Her viser jeg hvordan du sætter det op og eksempler på hvordan det kan forbedre dine analyser.

<h2>Opsætning i Google Tag Manager</h2>

I Google Tag Manager skal der laves to ting:

<ul>
<li>En Custom JS variabel som udregner tiden</li>
<li>Et Event Tag hvor resultatet af variablen indsætter som Værdi.</li>
</ul>

<h3>Udregn hvor hurtigt et event udføres</h3>

For at udregne hvor hurtigt et Event udføres, skal der bruges to tal.

<ol>
<li>Et præcist tidspunkt når Event'et udføres.</li>
<li>Et præcist tidspunkt når siden indlæses.</li>
</ol>

Når man skal regne i tid er Unix timestamps geniale. Unix timestamp er den tid der er gået siden 1. januar 1970 - typisk i antal sekunder eller millisekunder.

Og det er super nemt at få det timestamp i millisekunder med JavaScript.

<pre><code class="language-javascript">new Date().getTime()
</code></pre>

Men det har jeg det præcise tidspunkt for hvornår et Event sker.

Så skal jeg bare have tidspunktet hvor siden blev indlæst.

<pre><code class="language-javascript">window.performance.timing.navigationStart
</code></pre>

Ved at trække de to tal fra hinanden, ved du præcist (i millisekuder) hvor lang tid der er gået fra brugeren begyndte at loade siden, til et givent Event bliver udført.

Du laver derfor en Custom JavaScript Variable i GTM, hvor du trækker de to tal fra hinanden. Husk at en Custom JavaScript Variable altid skal være en <code>function</code> som returnerer en værdi.

Funktionen gør følgende pr. linje:

<ol>
<li>Gemmer tiden lige nu i millisekunder</li>
<li>Trækker tiden da siden blev indlæst fra tiden nu i millisekunder. Dividerer med 1000 for at omregne til sekunder</li>
<li>Returnerer tiden hvis den er under 1800 sekunder. Hvis den er over returneres `undefined`</li>
</ol>

Jeg tjekker om der er gået mere end 1800 sekunder (30 minutter) siden dengang siden blev indlæst, for at undgå at tracke nogle meget høje antal sekunder, som vil skævvride data markant. Hvis der er gået mere end 30 minutter er der stor sandsynlighed for at sessionen er udløbet, så det er en god grænse at sætte.

Det smarte ved at returnere undefined som værdi er at <a href="https://www.simoahava.com/gtm-tips/undefined-dimensions-wont-get-sent/" rel="noopener noreferrer">undefined værdier automatisk bliver udeladt</a> af dit request til Google Analytics.

<pre><code class="language-javascript">function() {
  var currentTime = new Date().getTime();
  var timeToEvent = (currentTime - window.performance.timing.navigationStart)/1000;
  return timeToEvent < 1800 ? timeToEvent : undefined;
}
</code></pre>

Jeg bruger altid den samme navngivning når jeg opretter Tags, Variabler eller Triggers i GTM. Fx starter jeg altid en Custom JavaScript Variable med "JS - [navn]" så jeg har dem samlet i oversigten og de er nemme at finde.

Den her kalder jeg "JS - Time to event".

[caption id="attachment_1981" align="alignnone" width="725"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event-725x337.jpg" alt="GTM variabel: JS - Time to event" width="725" height="337" class="size-large wp-image-1981" /></a> GTM variabel: JS - Time to event[/caption]

<h2>Event Tag med tiden som værdi</h2>

Du kan derefter indsætte den nye variabel som Værdi i dine Event tracking Tags.

[caption id="attachment_1980" align="alignnone" width="740"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration.jpg" alt="Indsæt &quot;JS - time to event&quot; som Event Value." width="740" height="702" class="size-full wp-image-1980" /></a> Indsæt "JS - time to event" som Event Value.[/caption]

Det fede ved at tracke tiden som værdien for et Event er at Google Analytics udregner et gennemsnit ud-af-boksen. Dermed får du et hurtigt overblik over hvor hurtigt et Event sker i gennemsnit.

<h3>Use case #1: JavaScript fejl</h3>

En af de ting jeg altid sætter op i GTM er tracking af JavaScript fejl. Det er mega nemt og værdifuldt, fordi det er indbygget i GTM, så der skal ikke kodes noget.

[caption id="attachment_1982" align="alignnone" width="725"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time-725x352.jpg" alt="JavaScript error event med tiden som værdi." width="725" height="352" class="size-large wp-image-1982" /></a> JavaScript error event med tiden som værdi.[/caption]

Ved at tracke tiden indtil der sker en JavaScript fejl, er det meget nemt at se hvilke fejl der sker ved pageload og hvilke der først sker efter brugeren er begyndt at bruge siden. Dét gør det tit meget nemmere at debugge en JavaScript fejl og forstå hvad der gik galt.

<h3>Use case #2: Læsning af indhold</h3>

Jeg tracker min blog med Enhanced Ecommerce, som du kan <a href="https://www.jacobworsoe.dk/indhold-enhanced-ecommerce/">læse meget mere om her</a>. Jeg tracker en række events når brugeren har læst hhv. 33%, 66% samt 100% af et blogindlæg. Her bruger jeg også tiden, til at se hvor hurtigt brugerne læser indholdet og hvor lang tid det tager dem at nå til bunden af siden.

[caption id="attachment_1984" align="alignnone" width="860"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events-860x313.jpg" alt="Den gennemsnitlige tid det tager brugerne af scrolle igennem et blogindlæg." width="860" height="313" class="size-large wp-image-1984" /></a> Den gennemsnitlige tid det tager brugerne af scrolle igennem et blogindlæg.[/caption]

Jeg tracker et "add to cart" event, når brugeren begynder at scrolle ned af indlægget. Det er overraskende at det igennemsnit tager 26,52 sekunder før brugerne begynder at scrolle, men det tager 51,97 sekunder at nå 33% ned gennem indlægget (checkout step 1).

<h3>Use case #3: Klik i menuen</h3>

Mange websites tracker hvad brugeren klikker på i menuen. Særligt i en mega-menu kan det være nyttigt at vide hvor brugerne klikker og hvilke områder der ikke modtager nogen kliks. Her kan tiden også bidrage med ekstra viden, til at se hvor hurtigt brugeren kan danne sig et overblik over menuen og foretage et valg.

Her på bloggen har jeg en hamburger menu, hvor jeg tracker når den åbnes og lukkes.

[caption id="attachment_1986" align="alignnone" width="860"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close-860x246.jpg" alt="I gennemsnit åbnes hamburger menuen efter 116 sekunder og lukkes efter 147 sekunder." width="860" height="246" class="size-large wp-image-1986" /></a> I gennemsnit åbnes hamburger menuen efter 116 sekunder og lukkes efter 147 sekunder.[/caption]

Jeg tracker også når brugeren klikker i menuen. Her er det interessant at se hvor stor forskel der er på hvor hurtigt brugerne klikker på de forskellige kategorier af indlæg. Bemærk at dette er tiden efter siden blev indlæst og ikke tiden efter menuen blev åbnet.

[caption id="attachment_1987" align="alignnone" width="860"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen-860x499.jpg" alt="Tid før klik på de forskellige kategorier i menuen." width="860" height="499" class="size-large wp-image-1987" /></a> Tid før klik på de forskellige kategorier i menuen.[/caption]

Jeg har efterfølgende lavet et stort redesign af min blog og alle beslutningerne var baseret på data, fx at fjerne menuen. <a href="https://www.jacobworsoe.dk/datadrevet-redesign/">Det kan du læse mere om her</a>.

<h3>Use case #4: Brug af drikkevare beregner</h3>

Tilbage i 2015 lavede jeg en <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">infografik over hvor meget der blev drukket til vores bryllup</a>. Det er i øvrigt suverænt det mest blogindlæg jeg har. Jeg skal have skrevet noget mere/bedre om Google Analytics.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009.jpg" alt="" width="844" height="465" class="alignnone size-full wp-image-1993" /></a>

Jeg lavede også en beregner hvor man kan indtaste antal gæster og få at vide hvor meget man skal købe.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster-860x516.jpg" alt="" width="860" height="516" class="alignnone size-large wp-image-1995" /></a>

Der er lavet 18.555 beregninger til dato og der er i gennemsnit gået 110 sekunder fra siden blev indlæst, til der er udført en beregning.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid-860x161.jpg" alt="" width="860" height="161" class="alignnone size-large wp-image-1996" /></a>

Bounteous har også skrevet en fin artikel <a href="https://www.bounteous.com/insights/2018/02/06/average-time-until-event-calculated-metrics/?ns=l">om at tracke tiden op til et event</a> hvis du vil læse mere om emnet.