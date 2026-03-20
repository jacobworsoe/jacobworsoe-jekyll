---
layout: post
title: Tracking af kaffeforbrug med AWS IoT Button og Google Analytics
date: 2019-10-22 21:48:06
slug: aws-iot-button-google-analytics
wordpress_id: 1998
categories:
  - Analytics
---

Sidste sommer skrev jeg om hvordan jeg brugte <a href="{{ '/cola-google-analytics-flic-buttons/' | relative_url }}">Flic knapper og Google Analytics</a> til at tracke vores forbrug af cola.

<a href="{{ '/assets/images/flic-analytics-featured-image.jpg' | relative_url }}"><img src="{{ '/assets/images/flic-analytics-featured-image-725x495.jpg' | relative_url }}" alt="" width="725" height="495" class="alignnone size-large wp-image-1389" /></a>

Det gik semi-viralt og Flic spurgte om jeg ville skrive en engelsk version af indlægget, som blev <a href="https://flic.io/blog/track-soda-habits-flic-google-analytics" rel="noopener noreferrer">udgivet det på deres officielle blog</a>.

Det var ret cool.

Men cola er en ting. Det kunne være sjovt at tracke noget der var lidt mere arbejdsrelateret: Kaffe!

Nærmere bestemt vores kaffeforbrug på kontoret.

Udfordringen med Flic er at man skal have en Hub som knapperne forbinder til. Den koster 999,- og jeg kunne godt bruge noget lidt billigere til dette eksperiment.

<figure><a href="{{ '/assets/images/2019/10/Flic-hub-google-shopping.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/Flic-hub-google-shopping.jpg' | relative_url }}" alt="Flic hub koster pt. 999,-" width="845" height="320" class="size-full wp-image-2003" /></a><figcaption>Flic hub koster pt. 999,-</figcaption></figure>

Man kan faktisk også forbinde knapperne til sin telefon via Bluetooth og sende data via telefonen, men det er heller ikke ideelt at der altid skal være en telefon i nærheden af knapperne.

<h2>AWS IoT Button</h2>

Et af mine yndlingspodcast et <a href="https://shoptalkshow.com/">Shoptalkshow</a>, hvor jeg følger med i nyeste trends indenfor webudvikling. I afsnit 320 snakker de om <a href="https://shoptalkshow.com/episodes/320-internet-things/" rel="noopener noreferrer">Internet of Things</a>.

Her taler de blandt andet om <a href="https://aws.amazon.com/iotbutton/">AWS IoT Button</a> som er en knap ligesom Flic.

<figure><a href="{{ '/assets/images/2019/10/AWS-IoT-Button.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/AWS-IoT-Button-860x365.jpg' | relative_url }}" alt="AWS IoT Button" width="860" height="365" class="size-large wp-image-2004" /></a><figcaption>AWS IoT Button</figcaption></figure>

Den fungerer bare uden en hub. Du kobler den direkte på dit Wifi og så kan den sende data via AWS.

<a href="{{ '/assets/images/2019/10/Choose-button-wifi.png' | relative_url }}"><img src="{{ '/assets/images/2019/10/Choose-button-wifi.png' | relative_url }}" alt="" width="735" height="883" class="alignnone size-full wp-image-2008" /></a>

Og den koster kun 22,99 GBP eller cirka 200 kroner.

<a href="{{ '/assets/images/2019/10/23-pund-200-kroner.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/23-pund-200-kroner.jpg' | relative_url }}" alt="" width="648" height="323" class="alignnone size-full wp-image-2005" /></a>

Meget mere simpelt og billigt.

Knappen er den samme hardware som de Dash buttons som Amazon havde på et tidspunkt hvor man kunne bestille fx vaskepulver blot ved et klik på en knap. <a href="https://www.theverge.com/2019/2/28/18245315/amazon-dash-buttons-discontinued">De findes dog ikke mere</a>.

Men IoT knappen kan programmeres via AWS og udføre vilkårlig kode, så alle muligheder er åbne.

Amazon siger selv at IoT knappen er lavet til at udviklere kan have en nem måde at prøve de mange funktioner i AWS.

<blockquote><p>The AWS IoT Button is a programmable button based on the Amazon Dash Button hardware. This simple Wi-Fi device is easy to configure and designed for developers to get started with AWS IoT Core, AWS Lambda, Amazon DynamoDB, Amazon SNS, and many other Amazon Web Services without writing device-specific code.<cite><a href="https://aws.amazon.com/iotbutton/"  rel="noopener noreferrer">Amazon.com</a></cite></p></blockquote>

<h2>Funktioner i AWS</h2>

Knappen kan trigger en lang række funktioner i AWS. Når knappen er koblet på Wifi via app'en, får du en liste med eksempler på små funktioner som knappen kan trigger.

<figure><a href="{{ '/assets/images/2019/10/Eksempler-AWS-functions.png' | relative_url }}"><img src="{{ '/assets/images/2019/10/Eksempler-AWS-functions.png' | relative_url }}" alt="Eksempler på AWS funktioner." width="744" height="1160" class="size-full wp-image-2009" /></a><figcaption>Eksempler på AWS funktioner.</figcaption></figure>

Og AWS har en lang række af services. I dette tilfælde vil jeg fokusere på Lambda funktioner.

<figure><a href="{{ '/assets/images/2019/10/AWS-funktion-oversigt.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/AWS-funktion-oversigt-860x617.jpg' | relative_url }}" alt="AWS er kæmpe stort og har services til næsten alt." width="860" height="617" class="size-large wp-image-2024" /></a><figcaption>AWS er kæmpe stort og har services til næsten alt.</figcaption></figure>

<h3>Lambda funktioner</h3>

Lambda funktioner er et stykke kode som kan køres, typisk når en URL kaldes, men i dette tilfælde også ved et klik på knappen.

Koden kan både være Python, Java, Go, Ruby eller Node.js.

<figure><a href="{{ '/assets/images/2019/10/lambda-funktioner-supported-languages.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/lambda-funktioner-supported-languages.jpg' | relative_url }}" alt="Lambda understøtter mange sprog." width="842" height="452" class="size-full wp-image-2026" /></a><figcaption>Lambda understøtter mange sprog.</figcaption></figure>

Det fede ved Node.js er at det egentlig bare er JavaScript, men hvor JavaScript afvikles på klienten, så afvikles Node.js på serveren, ligesom fx PHP.

<h3>Tracking af kaffe i Google Analytics</h3>

For at tracke et Event i Google Analytics skal der laves et <code>POST</code> request af en URL.

Det er beskrevet i detaljer i <a href="{{ '/cola-google-analytics-flic-buttons/' | relative_url }}">indlægget om tracking af cola</a>.

Det kan gøres med Node.js med nedenstående kode.

Koden gør følgende:

<ol>
<li>Der skal laves et HTTPS request, så du starter med at require https module i Node.</li>
<li>ID'et for den GA property der skal sendes data til gemmes i en variabel.</li>
<li>Jeg opretter variabler til event data og så console.log'er jeg lige nogle debug data fra knappen. Mere om det senere.</li>
<li>Alt efter om der klikkes 1 gang, 2 gange eller et langt klik, sætter jeg event data med hhv. 1 kop, 2 kopper eller en hel kande kaffe.</li>
<li>Amazon siger at knappen har batteri til 1000 klik, så jeg tracker lige den aktuelle volt på batteriet, så jeg kan se om den er ved at være flad. I skrivende stund har jeg tracket 1538 klik med knappen og der er stadig masser af strøm på batteriet, så den kan meget mere end 1000 klik.</li>
<li>Event value sættes til hhv. 1, 2 eller 10 kopper kaffe i en hel kande.</li>
<li>Jeg laver et <code>options</code> object som indeholder den URL der skal kaldes, fordelt i hostname, port og path. Port 80 er HTTP webtrafik og port 443 er HTTPS.</li>
<li>Path indeholder de Event data der skal sendes, samt dit GA property ID og et random cookie ID.</li>
<li>Der laves et HTTPS request af URL'en og den tjekker om den svarer tilbage med en 200 statuskode og hvis der sker en fejl, bliver fejlen logget. Jeg udskriver også lige den endelig path, for at kunne debugge de data der bliver sendt til Google Analytics.</li>
</ol>

<pre><code class="language-javascript">exports.handler = (event, context, callback) =&gt; {
    const https = require("https");

    // Payload data
    const GaProperty = "UA-12345-1";

    var eventCategory;
    var eventAction;
    var eventLabel;
    var eventValue;

        console.log(event.clickType);
        console.log(event.batteryVoltage);

    if (event.clickType === "SINGLE") {
        eventCategory = "Kaffe";
        eventAction = "1%20kop";
        eventLabel = event.batteryVoltage;
        eventValue = "1";
    } else if (event.clickType === "DOUBLE") {
        eventCategory = "Kaffe";
        eventAction = "2%20kopper";
        eventLabel = event.batteryVoltage;
        eventValue = "2";
    } else if (event.clickType === "LONG") {
        eventCategory = "Kaffe";
        eventAction = "1%20kande";
        eventLabel = event.batteryVoltage;
        eventValue = "10";
    }

    var options = {
        hostname: "www.google-analytics.com",
        port: 443,
        path:
            "/collect?v=1&amp;t=event&amp;tid=" +
            GaProperty +
            "&amp;cid=5b3393c6-dbf2-4e60-a912-c30d7df10f0e&amp;ec=" +
            eventCategory +
            "&amp;ea=" +
            eventAction +
            "&amp;el=" +
            eventLabel +
            "&amp;ev=" +
            eventValue,
        method: "POST"
    };

    var req = https.request(options, res =&gt; {
        console.log("statusCode:", res.statusCode);
        if (res.statusCode === 200) {
            console.log("Data sent!");
            console.log(options.path);

        }
    });

    req.on("error", e =&gt; {
        console.error(e);
    });

    req.end();
};
</code></pre>

<h3>Console.log i node.js</h3>

Normalt vil <code>console.log()</code> udskrive noget i konsollen i browseren. Node.js køres på serveren så her bliver <code>console.log()</code> gemt i serverens log.

De ting jeg console.log'er i koden, når man klikker på knappen, kan ses i AWS.

<figure><a href="{{ '/assets/images/2019/10/AWS-CloudWatch-Log-groups.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/AWS-CloudWatch-Log-groups-860x254.jpg' | relative_url }}" alt="AWS CloudWatch loggen." width="860" height="254" class="size-large wp-image-2027" /></a><figcaption>AWS CloudWatch loggen.</figcaption></figure>

Det er smart til at debugge hvad der er sket.

<h2>Test i Google Analytics real-time</h2>

Så er der bare tilbage at teste at det virker.

<figure><a href="{{ '/assets/images/2019/10/GA-real-time-events.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/GA-real-time-events-860x197.jpg' | relative_url }}" alt="Test af knappen i real-time." width="860" height="197" class="size-large wp-image-2036" /></a><figcaption>Test af knappen i real-time.</figcaption></figure>

Det virker.

<h2>Montering af knappen ved kaffemaskinen</h2>

Jeg satte knappen lige over kaffemaskinen og krydsede fingre for at kollegaerne ville deltage i eksperimentet. For at motivere dem, lavede jeg et <a href="https://datastudio.google.com/u/0/reporting/1CF8o0ir5pZT83E3qQCyzQsHpHBk4trsi/page/77dU" rel="noopener noreferrer">hurtigt dashboard i Data Studio</a>, som viste de spændende data.

<figure><a href="{{ '/assets/images/2019/10/Knap-ved-kaffemaskine-860w.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/Knap-ved-kaffemaskine-860w.jpg' | relative_url }}" alt="Knappen ved kaffemaskinen." width="860" height="1050" class="size-full wp-image-2039" /></a><figcaption>Knappen ved kaffemaskinen.</figcaption></figure>

<h2>Analysen af kaffe-data</h2>

Det første jeg kigger på er kaffe fordelt over dagen. Nogle møder ind før kl. 8 og der kommer tydeligt mange på kontoret kl. 8-9.

Kaffeforbruget peaker kl. 9-10 og begynder derefter at aftage ned mod frokost, hvorefter der kommer en lille spike igen kl. 13 hvor vi lige skal igang igen efter frokost.

<figure><a href="{{ '/assets/images/2019/10/Kaffe-fordelt-over-dagen.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/Kaffe-fordelt-over-dagen-860x497.jpg' | relative_url }}" alt="Kaffe fordelt over dagen" width="860" height="497" class="size-large wp-image-2016" /></a><figcaption>Kaffe fordelt over dagen</figcaption></figure>

Hvis vi kigger på det akkumulerede kaffeforbrug over dagen er der også en fast stigning frem til kl. 10 hvor 67% af dagens kaffe er drukket. Derefter flader den lidt ud, men 84% af dagens kaffeforbrug er sket kl. 12.

<figure><a href="{{ '/assets/images/2019/10/Akkumuleret-kaffeforbrug-v2.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/Akkumuleret-kaffeforbrug-v2.jpg' | relative_url }}" alt="Akkumuleret kaffeforbrug" width="1166" height="664" class="size-full wp-image-2033" /></a><figcaption>Akkumuleret kaffeforbrug</figcaption></figure>

Jeg har lavet en Excel skabelon, som gør det super nemt at lave heatmaps, som viser Google Analytics metrics fordelt over ugen. Læs mere om den og hent den gratis lige her: <a href="{{ '/visualisering-af-google-analytics-data-med-excel-heatmaps/' | relative_url }}">Visualisering af Google Analytics data med Excel heatmaps</a>.

Med den skabelon kan jeg nemt lave et overblik over kaffe fordelt over ugen. Det er interessant at der igennem et helt år er drukket markant mindre kaffe om torsdagen og man kan også se at der er klart mest brug for kaffe i starten af ugen, til lige at komme igang. Fredag eftermiddag kunne det godt ligne at kaffen er skiftet ud med en velfortjent fyraftensøl.

<figure><a href="{{ '/assets/images/2019/10/Kopper-kaffe-Excel-heatmap.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/Kopper-kaffe-Excel-heatmap-860x580.jpg' | relative_url }}" alt="Excel heatmap viser kaffeforbrug fordelt på ugen." width="860" height="580" class="size-large wp-image-2078" /></a><figcaption>Excel heatmap viser kaffeforbrug fordelt på ugen.</figcaption></figure>

En anden ting der er sjov at se ved et eksperiment som det her, er om kollegaerne bliver ved med at klikke når de drikker kaffe. Grafen for events over tid, viser tydeligt at det var sjovest i starten og derefter falder det en del. Der er dog stadig mange der bliver ved med at klikke. Sommerferien ses også tydeligt, hvor der er tomt på kontoret i et par uger.

<figure><a href="{{ '/assets/images/2019/10/Total-events-over-tid.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/Total-events-over-tid-860x209.jpg' | relative_url }}" alt="Kliks på knappen over tid." width="860" height="209" class="size-large wp-image-2047" /></a><figcaption>Kliks på knappen over tid.</figcaption></figure>

Det viser dog tydeligt at hvis man skal bruge det her til noget seriøst, så er det bedst at brugerne trackes automatisk og ikke som her, hvor de skal huske at trykke på en knap. Det bedste vil være at bygge det sammen med kaffemaskinen, så man automatisk tracker hver gang man løfter kanden eller lignende. Så vil man få mere præcis data over tid.

<h2>Opsummering</h2>

Eksperimentet her viser at det er nemt og billigt at lave knapper til at tracke events i den virkelige verden og gemme dem i Google Analytics til senere analyse. Det koster kun 200,- DKK og knappen, som kun kræver Wifi, har minimum batteri til 1500 klik.

Jeg håber det kan inspirere til at tracke ting i den virkelige verden og samle det i Google Analytics. Er der noget du får lyst til at tracke?