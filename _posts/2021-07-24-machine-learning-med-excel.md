---
layout: post
title: Machine Learning med Excel
date: 2021-07-24 16:11:16
slug: machine-learning-med-excel
wordpress_id: 652
categories:
  - Analytics
---

<blockquote>Mennesker lærer af erfaring. Maskiner lærer af data.</blockquote>

Interessen for Machine Learning er steget markant i løbet af de sidste år, men for mange er det stadig mest et buzz word. Her vil jeg prøve at bringe det lidt ned på et niveau som de fleste kan relatere til, nemlig ved at lave lidt Machine Learning i Excel. Machine Learning behøver ikke være mere kompleks end det.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2021/07/machine-learning-google-trends.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2021/07/machine-learning-google-trends-860x264.png" alt="machine learning google trends" width="860" height="264" class="aligncenter size-large wp-image-2692" /></a>

<h2>Antal ord og organisk trafik</h2>

Som eksempel på machine learning der kan laves i Excel, vil jeg analysere forholdet mellem længden på blogindlæg og mængden af organisk SEO trafik. Sammenhængen er bevist flere gange tidligere, fx af Backlinko:

[caption id="attachment_1297" align="alignnone" width="690"]<a href="http://www.jacobworsoe.dk/wp-content/uploads/backlinko-content-total-word-count.png"><img src="http://www.jacobworsoe.dk/wp-content/uploads/backlinko-content-total-word-count-690x475.png" alt="Kilde: https://backlinko.com/search-engine-ranking" width="690" height="475" class="size-medium wp-image-1297" /></a> Kilde: <a href="https://backlinko.com/search-engine-ranking">https://backlinko.com/search-engine-ranking</a>[/caption]

Rand Fiskin har dog et helt andet take på det i denne Whiteboard Friday:

[caption id="attachment_1297" align="alignnone" width="690"]<a href="https://moz.com/blog/blog-post-length-frequency?wvideo=vhkmto6gk4"><img src="https://embedwistia-a.akamaihd.net/deliveries/e39d34732ebc9dda5f64d76e5e4d4a60b97e6703.jpg?image_play_button_size=2x&amp;image_crop_resized=960x540&amp;image_play_button=1&amp;image_play_button_color=2299dbe0" alt="The perfect blog post length and frequency is bullshit" width="690" height="475" class="size-medium wp-image-1297" /></a> The perfect blog post length and frequency is bullshit[/caption]

Her vil jeg derfor analysere hvor meget længden af indlægget betyder for trafikken på min personlige blog og endnu mere spændende: Om man kan forudsige hvor meget trafik et blogindlæg vil få, baseret på antal ord = prædiktiv analyse.

<h2>Først har vi brug for noget data</h2>

Vi skal bruge et datasæt som indeholder antal ord i hvert blogindlæg samt antal organiske sessioner der er startet på hvert blogindlæg. Der er flere måder at få antal ord på. Man kan gøre det manuelt, men det gider vi ikke, så vi får Wordpress til at gøre det for os, ved at indsætte denne funktion i <code>functions.php</code>:

<pre><code class="language-php">function word_count() {
    $content = get_post_field( 'post_content', $post->ID );
    $word_count = str_word_count( strip_tags( $content ) );
    return $word_count;
}
</code></pre>

Derefter kan antal ord i hver blogindlæg nemt udstilles i <code>dataLayer</code> sådan her:

<pre><code class="language-php">window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'words': '<?php echo word_count(); ?>'
});
</code></pre>

I Google Analytics har jeg så opsat en hit-scoped Custom Dimension, hvor jeg kan opsamle antal ord for blogindlægget, når det bliver besøgt.

[caption id="attachment_1307" align="alignnone" width="481"]<a href="http://www.jacobworsoe.dk/wp-content/uploads/word-count-hit-scoped-custom-dimension.png"><img src="http://www.jacobworsoe.dk/wp-content/uploads/word-count-hit-scoped-custom-dimension.png" alt="Antal ord i hit-scoped custom dimension" width="481" height="330" class="size-full wp-image-1307" /></a> Antal ord i hit-scoped custom dimension[/caption]

Derefter vælger jeg rapporten Acquisition -> All traffic -> Channels og vælger Organic Search. Jeg vælger Landing Page som primær dimension og den nye custom dimension Word Count, som sekundær dimension og får dermed dette udtræk, som eksporteres til Excel.

[caption id="attachment_1308" align="alignnone" width="677"]<a href="http://www.jacobworsoe.dk/wp-content/uploads/word-count-secondary-dimension.png"><img src="http://www.jacobworsoe.dk/wp-content/uploads/word-count-secondary-dimension.png" alt="Datasættet med landingpage, antal ord og organiske sessioner." width="677" height="432" class="size-full wp-image-1308" /></a> Datasættet med landingpage, antal ord og organiske sessioner.[/caption]

<div class="attention"><strong>Bemærk:</strong> Det er vigtigt at vælge en tidsperiode hvor alle blogindlæg har været online i hele perioden. Hvis der kigges tilbage på det sidste år (for at få et godt datagrundlag) men nogle blogindlæg, kun har været online den sidste uge, vil det give et forkert billede på, hvor meget trafik de blogindlæg har fået, sammenlignet med de andre.</div>

Okay, så nu har vi styr på datasættet. Så skal vi igang med noget Machine Learning.

<h2>Der er tre typer af Machine Learning</h2>

Indenfor Machine Learning er der tre primære grupper af analyser du kan lave:

<ul>
    <li><strong>Unsupervised learning:</strong> Kan der findes nogle interessante mønstre i datasættet?</li>
    <li><strong>Supervised learning:</strong> Kan man forudsige noget på baggrund af disse data?</li>
    <li><strong>Reinforcement learning:</strong> Analyse der automatisk bliver klogere af sig selv på baggrund af en række regler, fx, find den optimale strategi i skak</li>
</ul>

I dette indlæg kigger vi på de to første. Lad os starte med den første:

<h2>Unsupervised learning</h2>

Det første skridt er at undersøge om der er en sammenhæng mellem de to variabler. I statistik kaldes de to to variable for den uafhængige variabel (antal ord) og den afhængige variabel (organisk trafik). Vi prøver altså at undersøge om organisk trafik er <em>afhængig</em> af antal ord.

<h3>Er der en sammenhæng? (Scatter Plot)</h3>

Det kan være svært at se om der er en sammenhæng ud fra en tabel med data, så lad os lave lidt simpelt data visualisering med et Scatter Plot.

Hver prik er et blogindlæg og akserne er hhv. antal ord i artikel og organisk trafik til blogindlægget.

[caption id="attachment_1677" align="alignnone" width="1054"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-organisk-trafik-scatter.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-organisk-trafik-scatter.png" alt="Scatter plot af alle mine indlæg." width="1054" height="601" class="size-full wp-image-1677" /></a> Scatter plot af alle mine indlæg.[/caption]

I første omgang er det svært at se om der er en sammenhæng, da de fleste er klumpet sammen nede i hjørnet. Det skyldes <code>outliers</code>, dvs. observationer i datasættet, som ligger markant uden for normalen. Ekstreme tilfælde er svære at arbejde med, da de vil få alt for stor indflydelse på modellen. Vi ønsker primært at arbejde med data indenfor normal-området.

De to outliers er:

1) Mit indlæg om <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">drikkevarer til et bryllup</a>, som får ekstremt meget trafik, sammenlignet med mine normale indlæg om digital marketing, så derfor fjernes den fra modellen.

2) Den anden outlier er mit indlæg om <a href="https://www.jacobworsoe.dk/responsive-design-3-nemme-trin/">responsivt web design i 3 nemme trin</a> som er på 4253 ord, som er markant længere end mine øvrige indlæg, så derfor fjerner jeg også den.

[caption id="attachment_1679" align="alignnone" width="1053"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-outliers.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-outliers.png" alt="De to outliers der forvrænger data." width="1053" height="597" class="size-full wp-image-1679" /></a> De to outliers der forvrænger data.[/caption]

Nu er det mere tydeligt at se en sammenhæng, hvor blogindlæg med flere ord også har mere organisk trafik.

[caption id="attachment_1680" align="alignnone" width="1050"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-outliers-fjernet.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-outliers-fjernet.png" alt="Scatter plot uden outliers." width="1050" height="596" class="size-full wp-image-1680" /></a> Scatter plot uden outliers.[/caption]

Vi kan gøre det lidt tydeligere, ved at tilføje en tendenslinje.

[caption id="attachment_1681" align="alignnone" width="1049"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-tendenslinje.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-tendenslinje.png" alt="En tendenslinje fremhæver sammenhængen." width="1049" height="599" class="size-full wp-image-1681" /></a> En tendenslinje fremhæver sammenhængen.[/caption]

En tendenslinje gør for det første sammenhængen tydeligere, men den viser også hvor konsistent sammenhængen er i datasættet. Jo tættere alle prikkerne er på linjen, jo mere konsistent er relationen mellem tekstlængden og trafikken. Jo længere prikkerne er fra linjen, jo mere tilfældigt er det og dermed vil dataene typisk ikke være gode at bygge en model på.

<h2>Hvor stærk er sammenhængen? (Korrelation)</h2>

Hvis der er perfekt korrelation, kan man forudsige værdien af den ene variabel, kun ved at kende den anden.

Korrelation udtrykkes som et tal mellem -1 og 1. Jo tættere på yderpunkterne, dvs. -1 eller 1, jo stærkere er korrelationen.

Lad os tage et par eksempler.

Her er først et datasæt med en korrelation på 1, dvs. når den ene stiger, så stiger den anden også.

[caption id="attachment_1682" align="alignnone" width="594"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-korrelation-1.00.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-korrelation-1.00.png" alt="Datasæt med korrelation på 1." width="594" height="357" class="size-full wp-image-1682" /></a> Datasæt med korrelation på 1.[/caption]

Det kan for eksempel være personers højde og vægt som ofte følges ad. I den virkelige verden vil man dog typisk aldrig opnå en korrelation på 1,0  da der vil altid være outliers.

Den omvendte er et datasæt med en korrelation på -1, dvs. en negativ korrelation. Det vil altså sige når den ene stiger, så falder en anden.

[caption id="attachment_1687" align="alignnone" width="593"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-korrelation-minus-1.00.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-korrelation-minus-1.00.png" alt="Datasæt med korrelation på -1." width="593" height="356" class="size-full wp-image-1687" /></a> Datasæt med korrelation på -1.[/caption]

Det kan fx være sammenhængen mellem hvor koldt det er og hvor mange penge man bruger på at opvarme sit hus.

Det sidste eksempel er et datasæt med en korrelation tæt på 0, dvs. der er ingen sammenhæng mellem de to variabler. Dermed er det umuligt at forudsige hvad den ene værdi vil være hvis man kender den anden værdi.

[caption id="attachment_1688" align="alignnone" width="593"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-korrelation-0.03.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-korrelation-0.03.png" alt="Datasæt med korrelation på 0,03." width="593" height="354" class="size-full wp-image-1688" /></a> Datasæt med korrelation på 0,03.[/caption]

Det kan fx være en persons højde og karakter i skolen, hvor der formentlig ikke er nogen som helst sammenhæng, og det er dermed helt tilfældigt hvor prikkerne er placeret, som det ses herover.

<h3>Korrelation mellem antal ord og organisk trafik</h3>

I disse data er korrelationen mellem antal ord og organisk trafik på 0,63.

[caption id="attachment_1681" align="alignnone" width="1049"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-tendenslinje.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-tendenslinje.png" alt="Korrelation på 0,63." width="1049" height="599" class="size-full wp-image-1681" /></a> Korrelation på 0,63.[/caption]

<h3>Årsag eller sammenhæng?</h3>

Okay, så nu har vi fundet ud af at der er en sammenhæng mellem de to variabler. Årsag er en helt anden ting.

Det vi gerne vil undersøge her er nemlig ikke blot om der er en sammenhæng mellem antal ord og organisk trafik, men også om antallet af ord kan forårsage (eller forklare) trafikken og dermed om man kan konkludere at hvis man skriver flere ord, så får man også mere trafik og omvendt.

Når vi snakker årsag så er der tre muligheder:

<ol>
    <li><strong>Antal ord påvirker mængden af organisk trafik.</strong> Det er en sandsynlig forklaring.</li>
    <li><strong>Organisk trafik påvirker antal ord.</strong> Det giver ikke nogen mening. Der kommer ikke flere ord i en artikel, hvis den begynder at modtage mere organisk trafik, så væk med den.</li>
    <li><strong>Både antal ord og organisk trafik bliver påvirket samtidig af en helt 3. faktor.</strong> Den kan også være en sandsynlig forklaring. Forklaringen kan være at årsagen bare er gode velskrevne blogindlæg, som både får meget trafik og at velskrevne blogindlæg også ofte er længere. Dvs. man kan ikke bare skrive længere blogindlæg. Man skal skrive bedre blogindlæg, for at få mere trafik.</li>
</ol>

Ingen kan forklare korrelation bedre end hende her, så lad os give hende 5 minutter og så fortsætter vi derefter.

<div class="videoWrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/8B271L3NtAw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<h3>Giver det mening?</h3>

Det bedste du kan gøre for at afgøre om den ene variabel forårsager den anden variabel eller der blot er en sammenhæng er at spørge dig selv om det giver mening?

<ul>
    <li>Lange tekster indeholder meget information om et givent emne og er derfor gode at henvise til.</li>
    <li>Lange tekster kommer i bund med et emne.</li>
    <li>Lange tekster dækker mange aspekter af et emne og brugeren skal dermed kun søge information ét sted.</li>
</ul>

Alle sammen er faktorer som gør at Google gerne vil ranke indholdet højt.

<a href="http://blog.serpiq.com/how-important-is-content-length-why-data-driven-seo-trumps-guru-opinions/">Tidligere undersøgelser</a> har vist en sammenhæng mellem lange tekster og deres placering i Google.

<h2>Supervised learning</h2>

For at lave en model som kan forudsige organisk trafik baseret på antal ord kan vi lave en regressionsanalyse.

<h2>Regression</h2>

En regressionsanalyse kan laves <a href="https://statisticsbyjim.com/regression/regression-analysis-excel/">direkte i Excel</a> og giver følgende resultat for vores data.

[caption id="attachment_1692" align="alignnone" width="1151"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-linear-regression.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-linear-regression.png" alt="Resultatet af den linære regression." width="1151" height="446" class="size-full wp-image-1692" /></a> Resultatet af den linære regression.[/caption]

Den blå kasse hedder R squared på engelsk, også kaldet forklaringsgraden. Den viser at 17,5% af variationen i den afhængige variabel (organisk trafik) kan forklares af modellen. Og eftersom der kun er én uafhængig variabel i modellen (antal ord), så kan vi altså sige at antal ord forklarer 17,5% af variationen i organisk trafik. Eller sagt på lidt mere dansk: Antal ord forklarer 17,5% af den organiske trafik et blogindlæg har. Resten af variationen (82,5%) kan ikke forklares af modellen, og skyldes dermed andre faktorer, som er alle de andre ting Google kigger på, når de ranker indhold.

<h2>Hov hov, nu ikke så hurtigt!</h2>

Men husk at vi ikke kan konkludere at antal ord <em><strong>alene</strong></em> forklarer 17,5% af trafikken. Som tidligere nævnt kan det sagtens være en andre ting, som dog korrelerer stærkt med antal ord, fx en velskrevet artikel, som får mange sociale delinger, links, høj CTR, etc.

<h2>Forudsige organisk trafik</h2>

Okay, nu skal vi lige et smut ned af memory lane. Vi skal tilbage til linoleumsgulve og folkeskolens matematiktimer. Kan du huske <em>linjens ligning</em>?

Altså den her: <strong>Y = A * X + B</strong>

Hvor A er hældningen på linjen og B er skæringen med Y-aksen. Det er de to tal regressionsanalysen kan udregne for os.

Når vi kander A og B kan vi indsætte antal ord som X og udregne den forventede organisk trafik. Vi skal derfor have linjens ligning for tendenslinjen herunder.

[caption id="attachment_1681" align="alignnone" width="1049"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-tendenslinje.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-scatter-tendenslinje.png" alt="Linjens ligning for tendenslinje kan forudsige trafikken." width="1049" height="599" class="size-full wp-image-1681" /></a> Linjens ligning for tendenslinje kan forudsige trafikken.[/caption]

De to tal vi skal bruge til at indsætte istedet for A og B i ligningen får vi altså som en del af resultatet af den linære regression. Det er de to tal i den orange boks.

[caption id="attachment_1692" align="alignnone" width="1151"]<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-linear-regression.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/06/machine-learning-linear-regression.png" alt="De to orange tal er A og B i linjens ligning." width="1151" height="446" class="size-full wp-image-1692" /></a> De to orange tal er A og B i linjens ligning.[/caption]

Det første tal er skæringen med Y-aksen som er -13,95.

Det næste tal er hældningen på linjen som er 0,067.

Dermed bliver linjens ligning: <strong>Y = 0,067 * X - 13,95</strong>

Hvis vi fx indsætter X = 5000, får vi følgende: <strong>321,05</strong> = 0,067 * 5000 - 13,95.

Det vil altså sige at den forventede organiske trafik til et blogindlæg på 5000 ord er 321 besøg i samme periode som de øvrige tal er udtrukket for. I dette tilfælde har jeg trukket 1 års besøg ud, så perioden er 1 år.

Hældningen på linjen fortæller desuden at hver gang X stiger med 1, så stiger Y med 0,067.

Sagt på dansk: Hver gang vi skriver et ord mere, så kan vi forvente 0,067 flere besøg om året.