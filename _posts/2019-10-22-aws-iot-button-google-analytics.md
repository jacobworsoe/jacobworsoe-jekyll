---
layout: post
title: Tracking af kaffeforbrug med AWS IoT Button og Google Analytics
date: 2019-10-22 21:48:06
slug: aws-iot-button-google-analytics
categories:
  - Analytics
---

<p>Sidste sommer skrev jeg om hvordan jeg brugte <a href="https://www.jacobworsoe.dk/cola-google-analytics-flic-buttons/">Flic knapper og Google Analytics</a> til at tracke vores forbrug af cola.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-725x495.jpg" alt="" width="725" height="495" class="alignnone size-large wp-image-1389" srcset="https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-725x495.jpg 725w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-690x472.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image-768x525.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/flic-analytics-featured-image.jpg 900w" sizes="auto, (max-width: 725px) 100vw, 725px" /></a></p>
<p>Det gik semi-viralt og Flic spurgte om jeg ville skrive en engelsk version af indlægget, som blev <a href="https://flic.io/blog/track-soda-habits-flic-google-analytics" rel="noopener noreferrer">udgivet det på deres officielle blog</a>.</p>
<p>Det var ret cool.</p>
<p>Men cola er en ting. Det kunne være sjovt at tracke noget der var lidt mere arbejdsrelateret: Kaffe!</p>
<p>Nærmere bestemt vores kaffeforbrug på kontoret.</p>
<p>Udfordringen med Flic er at man skal have en Hub som knapperne forbinder til. Den koster 999,- og jeg kunne godt bruge noget lidt billigere til dette eksperiment.</p>
<div id="attachment_2003" style="width: 855px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Flic-hub-google-shopping.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2003" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Flic-hub-google-shopping.jpg" alt="Flic hub koster pt. 999,-" width="845" height="320" class="size-full wp-image-2003" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Flic-hub-google-shopping.jpg 845w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Flic-hub-google-shopping-690x261.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Flic-hub-google-shopping-768x291.jpg 768w" sizes="auto, (max-width: 845px) 100vw, 845px" /></a><p id="caption-attachment-2003" class="wp-caption-text">Flic hub koster pt. 999,-</p></div>
<p>Man kan faktisk også forbinde knapperne til sin telefon via Bluetooth og sende data via telefonen, men det er heller ikke ideelt at der altid skal være en telefon i nærheden af knapperne.</p>
<h2>AWS IoT Button</h2>
<p>Et af mine yndlingspodcast et <a href="https://shoptalkshow.com/">Shoptalkshow</a>, hvor jeg følger med i nyeste trends indenfor webudvikling. I afsnit 320 snakker de om <a href="https://shoptalkshow.com/episodes/320-internet-things/" rel="noopener noreferrer">Internet of Things</a>.</p>
<p>Her taler de blandt andet om <a href="https://aws.amazon.com/iotbutton/">AWS IoT Button</a> som er en knap ligesom Flic.</p>
<div id="attachment_2004" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-IoT-Button.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2004" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-IoT-Button-860x365.jpg" alt="AWS IoT Button" width="860" height="365" class="size-large wp-image-2004" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-IoT-Button-860x365.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-IoT-Button-690x293.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-IoT-Button-768x326.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-IoT-Button.jpg 1118w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2004" class="wp-caption-text">AWS IoT Button</p></div>
<p>Den fungerer bare uden en hub. Du kobler den direkte på dit Wifi og så kan den sende data via AWS.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Choose-button-wifi.png"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Choose-button-wifi.png" alt="" width="735" height="883" class="alignnone size-full wp-image-2008" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Choose-button-wifi.png 735w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Choose-button-wifi-690x829.png 690w" sizes="auto, (max-width: 735px) 100vw, 735px" /></a></p>
<p>Og den koster kun 22,99 GBP eller cirka 200 kroner.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/23-pund-200-kroner.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/23-pund-200-kroner.jpg" alt="" width="648" height="323" class="alignnone size-full wp-image-2005" /></a></p>
<p>Meget mere simpelt og billigt.</p>
<p>Knappen er den samme hardware som de Dash buttons som Amazon havde på et tidspunkt hvor man kunne bestille fx vaskepulver blot ved et klik på en knap. <a href="https://www.theverge.com/2019/2/28/18245315/amazon-dash-buttons-discontinued">De findes dog ikke mere</a>.</p>
<p>Men IoT knappen kan programmeres via AWS og udføre vilkårlig kode, så alle muligheder er åbne.</p>
<p>Amazon siger selv at IoT knappen er lavet til at udviklere kan have en nem måde at prøve de mange funktioner i AWS.</p>
<blockquote><p>The AWS IoT Button is a programmable button based on the Amazon Dash Button hardware. This simple Wi-Fi device is easy to configure and designed for developers to get started with AWS IoT Core, AWS Lambda, Amazon DynamoDB, Amazon SNS, and many other Amazon Web Services without writing device-specific code.<cite><a href="https://aws.amazon.com/iotbutton/"  rel="noopener noreferrer">Amazon.com</a></cite></p>
</blockquote>
<h2>Funktioner i AWS</h2>
<p>Knappen kan trigger en lang række funktioner i AWS. Når knappen er koblet på Wifi via app&#8217;en, får du en liste med eksempler på små funktioner som knappen kan trigger.</p>
<div id="attachment_2009" style="width: 754px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Eksempler-AWS-functions.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2009" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Eksempler-AWS-functions.png" alt="Eksempler på AWS funktioner." width="744" height="1160" class="size-full wp-image-2009" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Eksempler-AWS-functions.png 744w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Eksempler-AWS-functions-690x1076.png 690w" sizes="auto, (max-width: 744px) 100vw, 744px" /></a><p id="caption-attachment-2009" class="wp-caption-text">Eksempler på AWS funktioner.</p></div>
<p>Og AWS har en lang række af services. I dette tilfælde vil jeg fokusere på Lambda funktioner.</p>
<div id="attachment_2024" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-funktion-oversigt.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2024" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-funktion-oversigt-860x617.jpg" alt="AWS er kæmpe stort og har services til næsten alt." width="860" height="617" class="size-large wp-image-2024" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-funktion-oversigt-860x617.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-funktion-oversigt-690x495.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-funktion-oversigt-768x551.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-funktion-oversigt.jpg 1088w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2024" class="wp-caption-text">AWS er kæmpe stort og har services til næsten alt.</p></div>
<h3>Lambda funktioner</h3>
<p>Lambda funktioner er et stykke kode som kan køres, typisk når en URL kaldes, men i dette tilfælde også ved et klik på knappen.</p>
<p>Koden kan både være Python, Java, Go, Ruby eller Node.js.</p>
<div id="attachment_2026" style="width: 852px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/lambda-funktioner-supported-languages.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2026" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/lambda-funktioner-supported-languages.jpg" alt="Lambda understøtter mange sprog." width="842" height="452" class="size-full wp-image-2026" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/lambda-funktioner-supported-languages.jpg 842w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/lambda-funktioner-supported-languages-690x370.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/lambda-funktioner-supported-languages-768x412.jpg 768w" sizes="auto, (max-width: 842px) 100vw, 842px" /></a><p id="caption-attachment-2026" class="wp-caption-text">Lambda understøtter mange sprog.</p></div>
<p>Det fede ved Node.js er at det egentlig bare er JavaScript, men hvor JavaScript afvikles på klienten, så afvikles Node.js på serveren, ligesom fx PHP.</p>
<h3>Tracking af kaffe i Google Analytics</h3>
<p>For at tracke et Event i Google Analytics skal der laves et <code class="" data-line="">POST</code> request af en URL.</p>
<p>Det er beskrevet i detaljer i <a href="https://www.jacobworsoe.dk/cola-google-analytics-flic-buttons/">indlægget om tracking af cola</a>.</p>
<p>Det kan gøres med Node.js med nedenstående kode.</p>
<p>Koden gør følgende:</p>
<ol>
<li>Der skal laves et HTTPS request, så du starter med at require https module i Node.</li>
<li>ID&#8217;et for den GA property der skal sendes data til gemmes i en variabel.</li>
<li>Jeg opretter variabler til event data og så console.log&#8217;er jeg lige nogle debug data fra knappen. Mere om det senere.</li>
<li>Alt efter om der klikkes 1 gang, 2 gange eller et langt klik, sætter jeg event data med hhv. 1 kop, 2 kopper eller en hel kande kaffe.</li>
<li>Amazon siger at knappen har batteri til 1000 klik, så jeg tracker lige den aktuelle volt på batteriet, så jeg kan se om den er ved at være flad. I skrivende stund har jeg tracket 1538 klik med knappen og der er stadig masser af strøm på batteriet, så den kan meget mere end 1000 klik.</li>
<li>Event value sættes til hhv. 1, 2 eller 10 kopper kaffe i en hel kande.</li>
<li>Jeg laver et <code class="" data-line="">options</code> object som indeholder den URL der skal kaldes, fordelt i hostname, port og path. Port 80 er HTTP webtrafik og port 443 er HTTPS.</li>
<li>Path indeholder de Event data der skal sendes, samt dit GA property ID og et random cookie ID.</li>
<li>Der laves et HTTPS request af URL&#8217;en og den tjekker om den svarer tilbage med en 200 statuskode og hvis der sker en fejl, bliver fejlen logget. Jeg udskriver også lige den endelig path, for at kunne debugge de data der bliver sendt til Google Analytics.</li>
</ol>
<pre><code class="" data-line="">exports.handler = (event, context, callback) =&gt; {
    const https = require(&quot;https&quot;);

    // Payload data
    const GaProperty = &quot;UA-12345-1&quot;;

    var eventCategory;
    var eventAction;
    var eventLabel;
    var eventValue;

        console.log(event.clickType);
        console.log(event.batteryVoltage);

    if (event.clickType === &quot;SINGLE&quot;) {
        eventCategory = &quot;Kaffe&quot;;
        eventAction = &quot;1%20kop&quot;;
        eventLabel = event.batteryVoltage;
        eventValue = &quot;1&quot;;
    } else if (event.clickType === &quot;DOUBLE&quot;) {
        eventCategory = &quot;Kaffe&quot;;
        eventAction = &quot;2%20kopper&quot;;
        eventLabel = event.batteryVoltage;
        eventValue = &quot;2&quot;;
    } else if (event.clickType === &quot;LONG&quot;) {
        eventCategory = &quot;Kaffe&quot;;
        eventAction = &quot;1%20kande&quot;;
        eventLabel = event.batteryVoltage;
        eventValue = &quot;10&quot;;
    }

    var options = {
        hostname: &quot;www.google-analytics.com&quot;,
        port: 443,
        path:
            &quot;/collect?v=1&amp;t=event&amp;tid=&quot; +
            GaProperty +
            &quot;&amp;cid=5b3393c6-dbf2-4e60-a912-c30d7df10f0e&amp;ec=&quot; +
            eventCategory +
            &quot;&amp;ea=&quot; +
            eventAction +
            &quot;&amp;el=&quot; +
            eventLabel +
            &quot;&amp;ev=&quot; +
            eventValue,
        method: &quot;POST&quot;
    };

    var req = https.request(options, res =&gt; {
        console.log(&quot;statusCode:&quot;, res.statusCode);
        if (res.statusCode === 200) {
            console.log(&quot;Data sent!&quot;);
            console.log(options.path);

        }
    });

    req.on(&quot;error&quot;, e =&gt; {
        console.error(e);
    });

    req.end();
};
</code></pre>
<h3>Console.log i node.js</h3>
<p>Normalt vil <code class="" data-line="">console.log()</code> udskrive noget i konsollen i browseren. Node.js køres på serveren så her bliver <code class="" data-line="">console.log()</code> gemt i serverens log.</p>
<p>De ting jeg console.log&#8217;er i koden, når man klikker på knappen, kan ses i AWS.</p>
<div id="attachment_2027" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-CloudWatch-Log-groups.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2027" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-CloudWatch-Log-groups-860x254.jpg" alt="AWS CloudWatch loggen." width="860" height="254" class="size-large wp-image-2027" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-CloudWatch-Log-groups-860x254.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-CloudWatch-Log-groups-690x204.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-CloudWatch-Log-groups-768x227.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/AWS-CloudWatch-Log-groups.jpg 1670w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2027" class="wp-caption-text">AWS CloudWatch loggen.</p></div>
<p>Det er smart til at debugge hvad der er sket.</p>
<h2>Test i Google Analytics real-time</h2>
<p>Så er der bare tilbage at teste at det virker.</p>
<div id="attachment_2036" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-real-time-events.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2036" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-real-time-events-860x197.jpg" alt="Test af knappen i real-time." width="860" height="197" class="size-large wp-image-2036" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-real-time-events-860x197.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-real-time-events-690x158.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-real-time-events-768x176.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/GA-real-time-events.jpg 1385w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2036" class="wp-caption-text">Test af knappen i real-time.</p></div>
<p>Det virker.</p>
<h2>Montering af knappen ved kaffemaskinen</h2>
<p>Jeg satte knappen lige over kaffemaskinen og krydsede fingre for at kollegaerne ville deltage i eksperimentet. For at motivere dem, lavede jeg et <a href="https://datastudio.google.com/u/0/reporting/1CF8o0ir5pZT83E3qQCyzQsHpHBk4trsi/page/77dU" rel="noopener noreferrer">hurtigt dashboard i Data Studio</a>, som viste de spændende data.</p>
<div id="attachment_2039" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Knap-ved-kaffemaskine-860w.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2039" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Knap-ved-kaffemaskine-860w.jpg" alt="Knappen ved kaffemaskinen." width="860" height="1050" class="size-full wp-image-2039" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Knap-ved-kaffemaskine-860w.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Knap-ved-kaffemaskine-860w-690x842.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Knap-ved-kaffemaskine-860w-768x938.jpg 768w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2039" class="wp-caption-text">Knappen ved kaffemaskinen.</p></div>
<h2>Analysen af kaffe-data</h2>
<p>Det første jeg kigger på er kaffe fordelt over dagen. Nogle møder ind før kl. 8 og der kommer tydeligt mange på kontoret kl. 8-9.</p>
<p>Kaffeforbruget peaker kl. 9-10 og begynder derefter at aftage ned mod frokost, hvorefter der kommer en lille spike igen kl. 13 hvor vi lige skal igang igen efter frokost.</p>
<div id="attachment_2016" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kaffe-fordelt-over-dagen.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2016" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kaffe-fordelt-over-dagen-860x497.jpg" alt="Kaffe fordelt over dagen" width="860" height="497" class="size-large wp-image-2016" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kaffe-fordelt-over-dagen-860x497.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kaffe-fordelt-over-dagen-690x399.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kaffe-fordelt-over-dagen-768x444.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kaffe-fordelt-over-dagen.jpg 1432w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2016" class="wp-caption-text">Kaffe fordelt over dagen</p></div>
<p>Hvis vi kigger på det akkumulerede kaffeforbrug over dagen er der også en fast stigning frem til kl. 10 hvor 67% af dagens kaffe er drukket. Derefter flader den lidt ud, men 84% af dagens kaffeforbrug er sket kl. 12.</p>
<div id="attachment_2033" style="width: 1176px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Akkumuleret-kaffeforbrug-v2.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2033" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Akkumuleret-kaffeforbrug-v2.jpg" alt="Akkumuleret kaffeforbrug" width="1166" height="664" class="size-full wp-image-2033" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Akkumuleret-kaffeforbrug-v2.jpg 1166w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Akkumuleret-kaffeforbrug-v2-690x393.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Akkumuleret-kaffeforbrug-v2-768x437.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Akkumuleret-kaffeforbrug-v2-860x490.jpg 860w" sizes="auto, (max-width: 1166px) 100vw, 1166px" /></a><p id="caption-attachment-2033" class="wp-caption-text">Akkumuleret kaffeforbrug</p></div>
<p>Jeg har lavet en Excel skabelon, som gør det super nemt at lave heatmaps, som viser Google Analytics metrics fordelt over ugen. Læs mere om den og hent den gratis lige her: <a href="https://www.jacobworsoe.dk/visualisering-af-google-analytics-data-med-excel-heatmaps/">Visualisering af Google Analytics data med Excel heatmaps</a>.</p>
<p>Med den skabelon kan jeg nemt lave et overblik over kaffe fordelt over ugen. Det er interessant at der igennem et helt år er drukket markant mindre kaffe om torsdagen og man kan også se at der er klart mest brug for kaffe i starten af ugen, til lige at komme igang. Fredag eftermiddag kunne det godt ligne at kaffen er skiftet ud med en velfortjent fyraftensøl.</p>
<div id="attachment_2078" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kopper-kaffe-Excel-heatmap.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2078" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kopper-kaffe-Excel-heatmap-860x580.jpg" alt="Excel heatmap viser kaffeforbrug fordelt på ugen." width="860" height="580" class="size-large wp-image-2078" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kopper-kaffe-Excel-heatmap-860x580.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kopper-kaffe-Excel-heatmap-690x466.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kopper-kaffe-Excel-heatmap-768x518.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Kopper-kaffe-Excel-heatmap.jpg 1211w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2078" class="wp-caption-text">Excel heatmap viser kaffeforbrug fordelt på ugen.</p></div>
<p>En anden ting der er sjov at se ved et eksperiment som det her, er om kollegaerne bliver ved med at klikke når de drikker kaffe. Grafen for events over tid, viser tydeligt at det var sjovest i starten og derefter falder det en del. Der er dog stadig mange der bliver ved med at klikke. Sommerferien ses også tydeligt, hvor der er tomt på kontoret i et par uger.</p>
<div id="attachment_2047" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Total-events-over-tid.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2047" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Total-events-over-tid-860x209.jpg" alt="Kliks på knappen over tid." width="860" height="209" class="size-large wp-image-2047" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Total-events-over-tid-860x209.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Total-events-over-tid-690x168.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Total-events-over-tid-768x187.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/10/Total-events-over-tid.jpg 1319w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2047" class="wp-caption-text">Kliks på knappen over tid.</p></div>
<p>Det viser dog tydeligt at hvis man skal bruge det her til noget seriøst, så er det bedst at brugerne trackes automatisk og ikke som her, hvor de skal huske at trykke på en knap. Det bedste vil være at bygge det sammen med kaffemaskinen, så man automatisk tracker hver gang man løfter kanden eller lignende. Så vil man få mere præcis data over tid.</p>
<h2>Opsummering</h2>
<p>Eksperimentet her viser at det er nemt og billigt at lave knapper til at tracke events i den virkelige verden og gemme dem i Google Analytics til senere analyse. Det koster kun 200,- DKK og knappen, som kun kræver Wifi, har minimum batteri til 1500 klik.</p>
<p>Jeg håber det kan inspirere til at tracke ting i den virkelige verden og samle det i Google Analytics. Er der noget du får lyst til at tracke?</p>

