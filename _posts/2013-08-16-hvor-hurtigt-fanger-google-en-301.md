---
layout: post
title: Hvor hurtigt fanger Google en 301?
date: 2013-08-16 06:38:12
slug: hvor-hurtigt-fanger-google-en-301
wordpress_id: 85
categories:
  - SEO
---

Du har fået et nyt domæne og opsætter en 301 redirect på det gamle domæne over til det nye domæne, for at beholde din trafik og placeringer i søgemaskinerne. Men hvor lang tid tager det egentlig Google at opdage denne viderestilling på <em>hele</em> dit website og opdagere deres indeks? Få svaret her.

Lidt forhistorie: I 2010 supplerede jeg SU'en lidt med at køre taxa, når jeg ikke havde forelæsninger eller sad på læsesalen (læs: optimerede webshops og hang ud på Twitter). Taxa branchen har det med at være lidt hårdt ramt i medierne - der bliver ikke skrevet noget, når det går godt, men medierne elsker at fortælle hvis der har været en uheldig episode hvor en taxa er indblandet. Vi besluttede derfor at skabe lidt god presseomtale. For at medierne vil skrive om det, skal det være lidt sensationelt, lidt nyt og måske lidt skørt. Og noget af det skøreste man kan forestille sig er vel at 40 taxachauffører prøver at cykle til Paris - så det var præcis hvad vi gjorde: <a href="http://www.tourdetaxa.com/">Tour de Taxa</a> var født og flere medier dækkede det online, heriblandt <a href="http://www.tv2fyn.dk/article/305377:Cykelmotionister-tramper-for-gode-formaal" target="_blank" rel="noopener noreferrer">TV2 fyn</a> og <a href="http://www.dr.dk/Regioner/Aarhus/Nyheder/AarhusBy/2010/02/25/132616.htm" target="_blank" rel="noopener noreferrer">DR</a>. I mellemtiden har DR dog valgt at skrotte artiklen - sådan går det når man er så langsom til at publicere sine blogindlæg :)

På et tidspunkt så det dog ud til at vi mistede domænet (tourdetaxa.dk), så for at redde den dyrebare linkjuice der var opbygget på domænet, købe jeg et nyt domæne (tourdetaxa.com) og opsætte en 301 redirect over til det nye domæne.

Da jeg var lidt i tidspres og kunne miste domænet når som helst, fulgte jeg tæt med i hvor hurtig Google var til at fange 301 viderestillingen og udskifte det gamle domæne i deres indeks med det nye domæne.

[caption id="attachment_98" align="alignnone" width="640"]<a href="//www.jacobworsoe.dk/wp-content/uploads/redirect-start1.png"><img class="size-medium wp-image-98 " alt="Da jeg opsatte 301'eren indeholdte sitet 349 url'er." src="//www.jacobworsoe.dk/wp-content/uploads/redirect-start1-640x103.png" width="640" height="103" /></a> Da jeg opsatte 301'eren indeholdte sitet 349 url'er.[/caption]

Sitet var dengang (desværre ikke mere) bygget på Wordpress, så jeg kopierede hele sitet over på det nye webhotel og opsatte en 301 redirect på alle URL'er på det gamle domæne, over til den samme URL på det nye domæne, så jeg hverken mistede trafik eller placeringer i Google. Hvis Google ser en 301 redirect mellem to identiske sider vil de fjerne den gamle URL fra deres indeks og sætte den nye URL ind på den gamles plads, så man beholder sin placering.

Men hvor længe tager det egentlig Google at lave denne øvelse med at bytte rundt på de to URL'er? En 301-redirect betyder en <i>permanent flytning,</i> men betyder det så at Google rent faktisk tror på at indholdet er flyttet permanent første gang de ser en 301, eller skal der lidt mere til, før de begynder at opdatere deres indeks? Det kunne jo være en fejl, så det kan godt være de gerne vil crawle siden et par gange, før de begynder at tro på at sitet rent faktisk er flyttet og begynder at opdatere deres indeks. For at finde ud af det lavede jeg søgningen <i>site:tourdetaxa.dk</i> en gang pr. dag i perioden efter flytningen.

[caption id="attachment_100" align="alignnone" width="640"]<a href="//www.jacobworsoe.dk/wp-content/uploads/chart.png"><img class="size-full wp-image-100" alt="Udvikling i sider i indeks" src="//www.jacobworsoe.dk/wp-content/uploads/chart.png" width="640" height="273" /></a> Udvikling i sider i indeks[/caption]

Som det ses herover tog det faktisk over to måneder før alle siderne på det gamle domæne var fjernet fra indekset. Man kan se at der går 7-8 dage før Google begynder at fjerne de gamle URL'er fra indekset og i starten går det hurtigt, så de første 300 URL'er er faktisk fjernet efter en lille måneds tid. Derefter begynder det så at flade ud, og der gør lang tid før de sidste 50 URL'er er fjernet. Dette hænger sandsynligvis sammen men at der er nogle sider på sitet som bliver crawlet ofte, fx populære blogindlæg og faste sider, som har mange interne links, og hvor Google hurtigt opdager at de er viderestillet. Wordpress er dog også slem til at lave en masse sider med tags, kategorier og arkiver, som ligger dybere ned i sitets struktur og derfor ikke bliver crawlet så ofte, så det er formentlig dem der blev fjernet til sidst.

Jeg havde dog regnet med at grafen ville se omvendt ud, hvor den i starten crawler sitet og ser at siderne er viderestillet, men gerne lige vil give det et par dage, for at se om viderestillingen nu også er permanent inden de opdaterer deres indeks. Jeg havde så regnet med at Google ville opdage at der var igang med at ske noget med det her domæne og derfor lige ville løbe resten af sitet igennem for at se om det nu også var gældende for resten af sitet. Men det lader ikke til at de skruer op for deres crawl frekvens på sitet.

<h2>Hvad siger Google om det?</h2>
Imens testen kørte, åbnede Matt Cutts op for en ny omgang spørgsmål og jeg sendte derfor dette spørgsmål ind til ham, for at høre hvad Googles officielle holdning til "ventetid" ved en 301 redirect er:

<div class="videoWrapper">
<iframe src="//www.youtube.com/embed/QyQs3tz7ZKo?enablejsapi=1" height="360" width="640" allowfullscreen="" frameborder="0"></iframe>
</div>

Som man kan høre, så bekræfter han at Google gerne vil se en 301 redirect et par gange før de begynder at tro på den, hvilket stemmer meget godt overens med min graf, hvor der ikke rigtig bliver flyttet nogle URL'er den første uges tid.

<h2>Kan det gøres hurtigere?</h2>
Matt Cutts nævner også at det er vigtigt ikke at sende <em>mixed signals</em> hvor kun nogle URL'er på sitet er viderestillet, men denne "forudsætning" er opfyldt her. Til et WAW arrangement i Århus snakkede jeg blandt andet med <a href="http://www.henrik-bondtofte.dk/" target="_blank" rel="noopener noreferrer">Henrik Bondtofte</a> om dette og han nævnte at det også var vigtigt med et godt HTML sitemap, for at Google bedre kan finde alle URL'er på sitet og få dem crawlet.  Sitet er flyttet over på en anden platform nu, men jeg har beholdt en <a href="http://tourdetaxa.jacobworsoe.dk" target="_blank" rel="noopener noreferrer">kopi af sitet</a> (som selvfølgelig er blokeret i robots.txt), hvor du kan se hvordan det så ud, da jeg flyttede det. Sitet havde et <a href="http://tourdetaxa.jacobworsoe.dk/sitemap/" target="_blank" rel="noopener noreferrer">HTML sitemap</a> da det blev flyttet, men det indeholdte kun 236 sider ud af de 349 sider som Google havde i deres indeks, så sitemappet var ikke komplet. Blandt andet havde jeg ikke <a href="http://tourdetaxa.jacobworsoe.dk/tag/cykling-paris/" target="_blank" rel="noopener noreferrer">tags</a> og <a href="http://tourdetaxa.jacobworsoe.dk/category/%C3%B8st/" target="_blank" rel="noopener noreferrer">kategori</a> sider med, så det kunne have hjulpet med at få dem crawlet og fjernet.

Derudover ville det have hjulpet, hvis sitet havde flere indgående links, da det vil gøre at sitet bliver crawlet oftere, men også at Google vil crawle flere sider på sitet ved hvert besøg. Da jeg flyttede sitet havde forsiden en PageRank på 3 og havde blandt andet nedenstående indgående links, hvor der var nogle gode imellem, men endnu flere ville selvfølgelig ikke have skadet.
<ul>
	<li><a href="http://www.tv2fyn.dk/article/305377:Cykelmotionister-tramper-for-gode-formaal" target="_blank" rel="noopener noreferrer">http://www.tv2fyn.dk/article/305377:Cykelmotionister-tramper-for-gode-formaal</a></li>
	<li>http://www.tv2fyn.dk/article/305377?autoplay=1&amp;video_id=41866</li>
	<li><a href="http://www.fuglebjergcykling.dk/soeen-rundt/soeen-rundt-2011.aspx" target="_blank" rel="noopener noreferrer">http://www.fuglebjergcykling.dk/soeen-rundt/soeen-rundt-2011.aspx</a></li>
	<li><a href="http://www.denjyskepigegarde.dk/tour-de-taxa/" target="_blank" rel="noopener noreferrer">http://www.denjyskepigegarde.dk/tour-de-taxa/</a></li>
	<li><a href="http://picykel.dk/node/616" target="_blank" rel="noopener noreferrer">http://picykel.dk/node/616</a></li>
	<li><a href="http://dansketidende.dk/skrifter/02/02d/rejser.html" target="_blank" rel="noopener noreferrer">http://dansketidende.dk/skrifter/02/02d/rejser.html</a></li>
</ul>
<h2>Kunne jeg have gjort mere?</h2>
Det endte dog ikke med at vi mistede domænet, men jeg synes alligevel at to måneder var lang tid for at flytte et forholdsvis lille website. Har du erfaring med at flytte et site? Har du prøvet at bruge funktionen i Google Webmaster Tools som Matt Cutts snakker om?

Jeg er forresten igang med at holde øje med et væsentligt større site for at se, hvor lang tid det tager at flytte det. Det er et site på over 200.000 sider, men til gengæld et site hvor der er 100% styr på det tekniske setup, så det bliver spændende, men mere om det senere :)