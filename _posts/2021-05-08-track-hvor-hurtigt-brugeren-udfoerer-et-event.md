---
layout: post
title: Track hvor hurtigt brugeren udfører et event
date: 2021-05-08 16:21:41
slug: track-hvor-hurtigt-brugeren-udfoerer-et-event
categories:
  - Analytics
---

<p>En af de ting jeg næsten altid tracker sammen med Event Tracking er time to event.</p>
<p>Dermed kan jeg se hvor lang tid der går fra brugeren lander på siden til et Event udføres.</p>
<p>Det tilføjer også en spændende dimension til dine data, som ikke er tilgængelig i en standard Google Analytics opsætning, nemlig tid mellem forskellige events indenfor en session.</p>
<p>Google Analytics er god til at vise hvor mange sessioner, transaktioner, etc. du har haft på en given dag eller time, samt den gennemsnitlige varighed for de sessioner. Men der er ikke noget data på rækkefølgen af events eller tiden mellem de enkelte events. Det tilføjer vi noget af i dag.</p>
<p>Her viser jeg hvordan du sætter det op og eksempler på hvordan det kan forbedre dine analyser.</p>
<h2>Opsætning i Google Tag Manager</h2>
<p>I Google Tag Manager skal der laves to ting:</p>
<ul>
<li>En Custom JS variabel som udregner tiden</li>
<li>Et Event Tag hvor resultatet af variablen indsætter som Værdi.</li>
</ul>
<h3>Udregn hvor hurtigt et event udføres</h3>
<p>For at udregne hvor hurtigt et Event udføres, skal der bruges to tal.</p>
<ol>
<li>Et præcist tidspunkt når Event&#8217;et udføres.</li>
<li>Et præcist tidspunkt når siden indlæses.</li>
</ol>
<p>Når man skal regne i tid er Unix timestamps geniale. Unix timestamp er den tid der er gået siden 1. januar 1970 &#8211; typisk i antal sekunder eller millisekunder.</p>
<p>Og det er super nemt at få det timestamp i millisekunder med JavaScript.</p>
<pre><code class="" data-line="">new Date().getTime()
</code></pre>
<p>Men det har jeg det præcise tidspunkt for hvornår et Event sker.</p>
<p>Så skal jeg bare have tidspunktet hvor siden blev indlæst.</p>
<pre><code class="" data-line="">window.performance.timing.navigationStart
</code></pre>
<p>Ved at trække de to tal fra hinanden, ved du præcist (i millisekuder) hvor lang tid der er gået fra brugeren begyndte at loade siden, til et givent Event bliver udført.</p>
<p>Du laver derfor en Custom JavaScript Variable i GTM, hvor du trækker de to tal fra hinanden. Husk at en Custom JavaScript Variable altid skal være en <code class="" data-line="">function</code> som returnerer en værdi.</p>
<p>Funktionen gør følgende pr. linje:</p>
<ol>
<li>Gemmer tiden lige nu i millisekunder</li>
<li>Trækker tiden da siden blev indlæst fra tiden nu i millisekunder. Dividerer med 1000 for at omregne til sekunder</li>
<li>Returnerer tiden hvis den er under 1800 sekunder. Hvis den er over returneres `undefined`</li>
</ol>
<p>Jeg tjekker om der er gået mere end 1800 sekunder (30 minutter) siden dengang siden blev indlæst, for at undgå at tracke nogle meget høje antal sekunder, som vil skævvride data markant. Hvis der er gået mere end 30 minutter er der stor sandsynlighed for at sessionen er udløbet, så det er en god grænse at sætte.</p>
<p>Det smarte ved at returnere undefined som værdi er at <a href="https://www.simoahava.com/gtm-tips/undefined-dimensions-wont-get-sent/" rel="noopener noreferrer">undefined værdier automatisk bliver udeladt</a> af dit request til Google Analytics.</p>
<pre><code class="" data-line="">function() {
  var currentTime = new Date().getTime();
  var timeToEvent = (currentTime - window.performance.timing.navigationStart)/1000;
  return timeToEvent &lt; 1800 ? timeToEvent : undefined;
}
</code></pre>
<p>Jeg bruger altid den samme navngivning når jeg opretter Tags, Variabler eller Triggers i GTM. Fx starter jeg altid en Custom JavaScript Variable med &#8220;JS &#8211; [navn]&#8221; så jeg har dem samlet i oversigten og de er nemme at finde.</p>
<p>Den her kalder jeg &#8220;JS &#8211; Time to event&#8221;.</p>
<div id="attachment_1981" style="width: 735px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1981" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event-725x337.jpg" alt="GTM variabel: JS - Time to event" width="725" height="337" class="size-large wp-image-1981" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event-725x337.jpg 725w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event-690x320.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event-768x357.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-variabel-JS-time-to-event.jpg 1327w" sizes="auto, (max-width: 725px) 100vw, 725px" /></a><p id="caption-attachment-1981" class="wp-caption-text">GTM variabel: JS &#8211; Time to event</p></div>
<h2>Event Tag med tiden som værdi</h2>
<p>Du kan derefter indsætte den nye variabel som Værdi i dine Event tracking Tags.</p>
<div id="attachment_1980" style="width: 750px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1980" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration.jpg" alt="Indsæt &quot;JS - time to event&quot; som Event Value." width="740" height="702" class="size-full wp-image-1980" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration.jpg 740w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration-690x655.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GTM-tag-JavaScript-error-configuration-725x688.jpg 725w" sizes="auto, (max-width: 740px) 100vw, 740px" /></a><p id="caption-attachment-1980" class="wp-caption-text">Indsæt &#8220;JS &#8211; time to event&#8221; som Event Value.</p></div>
<p>Det fede ved at tracke tiden som værdien for et Event er at Google Analytics udregner et gennemsnit ud-af-boksen. Dermed får du et hurtigt overblik over hvor hurtigt et Event sker i gennemsnit.</p>
<h3>Use case #1: JavaScript fejl</h3>
<p>En af de ting jeg altid sætter op i GTM er tracking af JavaScript fejl. Det er mega nemt og værdifuldt, fordi det er indbygget i GTM, så der skal ikke kodes noget.</p>
<div id="attachment_1982" style="width: 735px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1982" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time-725x352.jpg" alt="JavaScript error event med tiden som værdi." width="725" height="352" class="size-large wp-image-1982" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time-725x352.jpg 725w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time-690x335.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time-768x373.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/JavaScript-error-events-with-time.jpg 1406w" sizes="auto, (max-width: 725px) 100vw, 725px" /></a><p id="caption-attachment-1982" class="wp-caption-text">JavaScript error event med tiden som værdi.</p></div>
<p>Ved at tracke tiden indtil der sker en JavaScript fejl, er det meget nemt at se hvilke fejl der sker ved pageload og hvilke der først sker efter brugeren er begyndt at bruge siden. Dét gør det tit meget nemmere at debugge en JavaScript fejl og forstå hvad der gik galt.</p>
<h3>Use case #2: Læsning af indhold</h3>
<p>Jeg tracker min blog med Enhanced Ecommerce, som du kan <a href="https://www.jacobworsoe.dk/indhold-enhanced-ecommerce/">læse meget mere om her</a>. Jeg tracker en række events når brugeren har læst hhv. 33%, 66% samt 100% af et blogindlæg. Her bruger jeg også tiden, til at se hvor hurtigt brugerne læser indholdet og hvor lang tid det tager dem at nå til bunden af siden.</p>
<div id="attachment_1984" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1984" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events-860x313.jpg" alt="Den gennemsnitlige tid det tager brugerne af scrolle igennem et blogindlæg." width="860" height="313" class="size-large wp-image-1984" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events-860x313.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events-690x251.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events-768x279.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Content-with-ecommerce-time-to-events.jpg 1347w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-1984" class="wp-caption-text">Den gennemsnitlige tid det tager brugerne af scrolle igennem et blogindlæg.</p></div>
<p>Jeg tracker et &#8220;add to cart&#8221; event, når brugeren begynder at scrolle ned af indlægget. Det er overraskende at det igennemsnit tager 26,52 sekunder før brugerne begynder at scrolle, men det tager 51,97 sekunder at nå 33% ned gennem indlægget (checkout step 1).</p>
<h3>Use case #3: Klik i menuen</h3>
<p>Mange websites tracker hvad brugeren klikker på i menuen. Særligt i en mega-menu kan det være nyttigt at vide hvor brugerne klikker og hvilke områder der ikke modtager nogen kliks. Her kan tiden også bidrage med ekstra viden, til at se hvor hurtigt brugeren kan danne sig et overblik over menuen og foretage et valg.</p>
<p>Her på bloggen har jeg en hamburger menu, hvor jeg tracker når den åbnes og lukkes.</p>
<div id="attachment_1986" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1986" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close-860x246.jpg" alt="I gennemsnit åbnes hamburger menuen efter 116 sekunder og lukkes efter 147 sekunder." width="860" height="246" class="size-large wp-image-1986" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close-860x246.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close-690x197.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close-768x220.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Hamburger-menu-open-close.jpg 1311w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-1986" class="wp-caption-text">I gennemsnit åbnes hamburger menuen efter 116 sekunder og lukkes efter 147 sekunder.</p></div>
<p>Jeg tracker også når brugeren klikker i menuen. Her er det interessant at se hvor stor forskel der er på hvor hurtigt brugerne klikker på de forskellige kategorier af indlæg. Bemærk at dette er tiden efter siden blev indlæst og ikke tiden efter menuen blev åbnet.</p>
<div id="attachment_1987" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1987" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen-860x499.jpg" alt="Tid før klik på de forskellige kategorier i menuen." width="860" height="499" class="size-large wp-image-1987" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen-860x499.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen-690x400.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen-768x445.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Klik-i-hamburger-menuen.jpg 1312w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-1987" class="wp-caption-text">Tid før klik på de forskellige kategorier i menuen.</p></div>
<p>Jeg har efterfølgende lavet et stort redesign af min blog og alle beslutningerne var baseret på data, fx at fjerne menuen. <a href="https://www.jacobworsoe.dk/datadrevet-redesign/">Det kan du læse mere om her</a>.</p>
<h3>Use case #4: Brug af drikkevare beregner</h3>
<p>Tilbage i 2015 lavede jeg en <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">infografik over hvor meget der blev drukket til vores bryllup</a>. Det er i øvrigt suverænt det mest blogindlæg jeg har. Jeg skal have skrevet noget mere/bedre om Google Analytics.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009.jpg" alt="" width="844" height="465" class="alignnone size-full wp-image-1993" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009.jpg 844w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009-690x380.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Mest-besøgte-indlæg-siden-2009-768x423.jpg 768w" sizes="auto, (max-width: 844px) 100vw, 844px" /></a></p>
<p>Jeg lavede også en beregner hvor man kan indtaste antal gæster og få at vide hvor meget man skal købe.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster-860x516.jpg" alt="" width="860" height="516" class="alignnone size-large wp-image-1995" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster-860x516.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster-690x414.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster-768x461.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-50-gæster.jpg 917w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<p>Der er lavet 18.555 beregninger til dato og der er i gennemsnit gået 110 sekunder fra siden blev indlæst, til der er udført en beregning.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid-860x161.jpg" alt="" width="860" height="161" class="alignnone size-large wp-image-1996" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid-860x161.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid-690x129.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid-768x144.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Drikkevare-beregner-gns-tid.jpg 1346w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<p>Bounteous har også skrevet en fin artikel <a href="https://www.bounteous.com/insights/2018/02/06/average-time-until-event-calculated-metrics/?ns=l">om at tracke tiden op til et event</a> hvis du vil læse mere om emnet.</p>

