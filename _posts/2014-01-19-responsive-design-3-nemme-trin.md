---
layout: post
title: Responsivt web design i 3 nemme trin
date: 2014-01-19 09:37:49
slug: responsive-design-3-nemme-trin
wordpress_id: 397
categories:
  - Webdesign
---

Når man står og skal igang med sit første responsive website, så kan det godt virke meget kompliceret - sådan havde jeg det i hvert fald. Et website der på magisk vis tilpasser sig til den enhed det bliver vist på og flytter rundt på elementer må da kræve en hulens masse smarte funktioner. Men sandheden er at det slet ikke er så kompliceret. Nutidens teknologier har gjort det uhyre nemt at lave responsive websites. Læs her om mine erfaringer med at gøre denne blog responsive og lær alt hvad du skal vide for at gøre det på din egen blog. Artiklen vil også være interessant for dig, selvom du ikke selv skal igang med at kode, men bare gerne vil kende lidt til fordele/ulemper samt lidt om tilgangen til det og hvad det kræver at gøre det.

Opskriften på et responsive website indeholde tre ingredienser.

<ol>
  <li><a href="#fluid-grids">Fluid grids</a></li>
  <li><a href="#media-queries">Media queries</a></li>
  <li><a href="#viewport-meta-tag">Viewport meta tag</a></li>
</ol>

Og dem gennemgår vi nu.

<h2 id="fluid-grids">1. Fluid grids</h2>

I lang tid har webdesign været defineret i præcise størrelser (særligt bredden på siden), for så var man sikker på at websitet altid så ens ud, uanset hvilken skærmopløsning brugerens computer havde. Denne blog har fx i lang tid haft følgende mål.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/fixed-width-design-web.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/fixed-width-design-web.jpg" alt="Website med statisk bredde." width="750" height="447" class="size-full wp-image-415" /></a><figcaption>Website med statisk bredde.</figcaption></figure>

Jeg var dermed sikker på at det design jeg havde lavet altid så ens ud. I en tid hvor browserkompatibilitet ofte var noget der kunne være svært at få styr på, var det lækkert at nogle ting altid var konstante. Tanken bag mine mål var at 99% af alle dem som besøgte denne blog havde en skærmopløsning på minimum 900px (fx 1024*768 eller derover) og derfor ville det give en god brugeroplevelse for langt de fleste brugere.

Men nu sidder 25% af de besøgende på dette site på mobile enheder, og deres skærme er meget mindre end 900px i bredden. Derudover er der også de få brugere som sidder med en lille desktop skærm, som fx vil se en side hvor kun noget er synligt og de skal scrolle horisontalt, for at se resten af siden.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/desktop-856px.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/desktop-856px.png" alt="Siden set med et desktop vindue mindre end 900px." width="856" height="423" class="size-full wp-image-420" /></a><figcaption>Siden set med et desktop vindue mindre end 900px.</figcaption></figure>

Mobile enheder som fx en iPhone 4S viser dog hele websitet, men det er zoomet så meget ud at teksten er ulæselig, så brugerne er nødt til at zoome ind på teksten = dårlig usability.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2013-11-17-01.32.38.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2013-11-17-01.32.38.png" alt="Siden set med en iPhone 4S." width="640" height="960" class="size-full wp-image-462" /></a><figcaption>Siden set med en iPhone 4S.</figcaption></figure>

<h3>Løsningen er fluid grids</h3>

For at undgå de forfærdelige horisontale scrollbars er vi nødt til at gøre siden fleksibel, så den tilpasser sig browservinduet, uanset størrelse. Dette gøres ved at angive bredden som procent istedet for en statisk bredde i pixels. Hvis man fx angiver at et element har en bredde på 50% så betyder det 50% af bredden af browservinduet hvis det er det "yderste" af sitets elementer, og ellers er det 50% af bredden på det element det er placeret indeni. Hvis man stadig gerne vil have lidt kontrol med <em>hvor</em> bredt sitet bliver, så kan man angivet et max antal pixels med max-width.

Det nemmeste er at sætte alle dine nuværende width's til max-width og så sætte width til den procentdel, det nu skal være. Min side var 900px bred, og det vil jeg gerne fortsætte med. Jeg sætter derfor at headeren skal have en max-width på 900px og en width på 100%. Derved vil headeren maksimalt være samme bredde som browservinduet og aldrig bredere end 900px. Sitet vil dermed se uforandret ud på store skærme, men på små skærme vil det kunne blive mindre og tilpasse sig brugerens browservindue. Mit content område var 600px i bredden, så 600/900*100 giver 66,66%. Mit nye fluid grid ser nu således ud:

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/fluid-grids-max-width.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/fluid-grids-max-width.jpg" alt="Websitet er nu konverteret til fluid grids." width="750" height="447" class="size-full wp-image-425" /></a><figcaption>Websitet er nu konverteret til fluid grids.</figcaption></figure>

Det der er vigtigt når man konverterer til fluid grids er at <span style="text-decoration: underline;">alt</span> skal være angivet med en width angivet i procent. Det betyder ikke noget med højden, men bredden skal altid være angivet i procent. Dette gælder bl.a. for:

<ul>
  <li>Div elementer</li>
  <li>Padding</li>
  <li>Margin</li>
  <li>Billeder</li>
  <li>Video</li>
</ul>

Hvis der havde været padding eller margin mellem mine elementer skulle disse også angives i procent. Hvis der fx havde været en <em>padding-right: 10px; </em>på mit #content element skulle jeg først fratrække de 10px fra de 600px på mit content element og udregne procenterne igen. De ville så blive:

<pre><code class="language-css">#header {
  width: 100%;
  max-width: 900px;
}

#content {
  width: 65.55%;
  max-width: 590px;
  padding-left: 1.11%; /* 10px / 900px * 100 = 1.11% */
}

#sidebar {
  width: 33.33%;
  max-width: 300px;
}
</code></pre>

<h3>Box-sizing redder dagen - nogen gange</h3>

En af de nye properties i CSS3 er box-sizing som ændrer på den normale Box Model i CSS, så den i de fleste tilfælde bliver nemmere at arbejde med. Du skal starte med at indsætte følgende i din CSS fil.

<pre><code class="language-css">* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
</code></pre>

Når du har gjort dette vil padding og border ikke blive lagt til bredden af et element, men istedet tilføjet inde i elementet. Det vil sige at hvis du i den normale box model har et element på 600px og du tilføjer 10px padding i hver side, så bliver bredden på elementet 620px. Med <em>box-sizing: border-box; </em>vil den padding du angiver istedet blive fratrukket den plads der er inde i elementet, så du nu kun har 580px inde i elementet, men det bliver ved med at være 600px i bredden.

Det betyder at du ikke længere skal lave regnestykket ovenfor, med at fratrække padding og udregne nye procenter - 600px vil altid være 600px. Men det gælder kun for padding og border - ikke margin. Hvilket også giver meget god mening, da padding er noget der ligger inde i elementet og margin er noget rundt om elementet.

Der er dog et lille men - hvis jeg fx har et website som er 900px i bredden og jeg smider et content element på 600px og en sidebar på 300px ind i det element, så fungerer det fint. Det gør det også hvis jeg tilføjer padding til mit content element, da det stadig vil være 600px bred. Men, hvis jeg tilføjer 10px padding til hele sitet, så breaker det. For nu er der pludselig ikke længere plads til de to elementer, da sitets indvendige mål nu kun er 880px (900px - 10px padding i hver side). Så du kan altid stole på elementernes udvendige mål, men du kan ikke stole på deres indvendige mål længere. Så det er svært at sige hvad der er bedst, men jeg synes det er nemmere at arbejde med den nye box model som box-sizing giver.

Men nu skulle vi gerne stå med et site hvor alle elementers bredde (inkl. padding, margin og borders) er angivet i procent. Sitet vil dermed aldrig overstige browservinduets størrelse og teksten inde i elementerne vil automatisk justere sig efter bredden på elementerne. Hvis du har nogle meget lange ord, typisk URL'er, kan du gøres sådan her, hvorefter den automatisk vil opdele lange ord, så de ikke bryder ud af rammen.

<pre><code class="language-css">body {
  word-wrap: break-word;
}
</code></pre>

Men hvad med billeder og videoer? Hvad sker der med dem når websitet bliver mindre? Det kigger vi på nu.

<h3>Billeder</h3>

På billeder skal vi sikre at billederne aldrig er større end det element de er placeret i. Det vil sige 100%. Men hvis billederne er små skal de samtidig ikke forstørres, så de bliver grimme, så de skal samtidig heller ikke være større end de rigtigt er. Den sidste ting er at størrelsesforholdet mellem højde og bredde på billedet altid skal være den samme, så billedet ikke bliver "strukket" eller mast sammen. Alt dette klares nemt med følgende CSS.

<pre><code class="language-css">img {
  max-width: 100%;
  height: auto;
}
</code></pre>

Smart ik? :)

Det geniale i dette, er at CSS overskriver, hvis der angivet height og width parametre på billedet ovre i HTML'en. Det er best practice at gøre dette og Wordpress indsætter det også som standard og det er altså fint nok, da vi bare overskriver disse mål med CSS værdierne ovenfor. Browsere er desuden blevet meget bedre til at resize billederne uden at ødelægge kvaliteten, så du kan sagtens gøre dine billeder mindre via CSS - til en vis grænse.

Du skal fx ikke smide et kæmpe 4000*3000px billede ind, direkte fra dit kamera og resize det via CSS. Det kan godt være det bliver pænt nok, men det vil tage alt for lang tid at downloade for brugeren. Lav hellere en version af billedet som passer til max-width på content elementet - i dette tilfælde 600px - og så brug CSS til at gøre dette billede mindre, så det passer til mindre skærme. Så har du godt styr på både usability og loadtid, især hvis du lige køre billedet gennem værktøjer som Smush.it, som laver tabsfri komprimering af billederne inden du uploader dem.

<h3>Video - FitVids to the rescue!</h3>

Så har vi styr på billederne, det var jo nemt nok. Så gælder det videoerne, og det er faktisk endnu nemmere! For uanset om du har embedded videoer fra Youtube, Vimeo eller noget helt tredje, så klarer <a href="http://fitvidsjs.com" target="_blank" rel="noopener noreferrer">FitVids.js</a> det hele for dig. Det er et jQuery plugin, som du henter og indsætter på dit site. Derefter fortæller du hvilket element videoerne er placeret i og dermed hvilket element de skal holde sig inden for og så tilpasser de selv størrelsen. Koden du skal indsætte på sitet ser således ud.

<pre><code class="language-html"><script src="path/to/jquery.min.js" type="text/javascript"></script>
<script src="path/to/jquery.fitvids.js" type="text/javascript"></script>
<script type="text/javascript">// <![CDATA[
$(document).ready(function(){
    // Target your .container, .wrapper, .post, etc.
    $("#thing-with-videos").fitVids();
  });
// ]]></script>
</code></pre>

Og det var faktisk det. Sitet er nu responsivt, forstået på den måde at det automatisk tilpasser sig til den skærmstørrelse det bliver vist på. Og i princippet skal der faktisk ikke mere til. Et godt eksempel på det er <a title="Sprinklertesten.dk" href="http://sprinklertesten.jacobworsoe.dk/" target="_blank" rel="noopener noreferrer">dette lille site</a> jeg har lavet for nyligt. Det indeholder ingen media queries eller lignende, men er stadig 100% responsivt, alene fordi det er lavet fleksibelt med de teknikker der er beskrevet ovenfor.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/Screenshot-2013-11-12-23.13.12.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/Screenshot-2013-11-12-23.13.12.png" alt="Websitet vil tilpasse sig skærmstørrelsen og er dermed &quot;responsivt&quot;." width="476" height="582" class="size-full wp-image-449" /></a><figcaption>Websitet vil tilpasse sig skærmstørrelsen og er dermed "responsivt".</figcaption></figure>

Men nu er det tid til at putte lidt icing on the cake i form af media queries.

<h2 id="media-queries">2. Media queries</h2>

Når man snakker om responsivt web design og hjemmesider der automatisk tilpasser sig til mobile enheder, tænker mange nok på media queries. Så du føler måske jeg har spildt din tid lidt indtil videre? Men sandheden er at fluid grids er det grundlæggende element i responsivt web design. Du kan nemlig ikke lave et responsivt web design kun ved brug af media queries - det skal også være fleksibelt (fluid), for at være 100% responsivt, så det kan bruges på alle enheder.

Media queries er en slags betingelser, vi kan indsætte i vores CSS og gøre noget hvis betingelserne er opfyldt. En betingelse kan være:

<pre><code class="language-css">@media (max-width: 790px) {
  h1 {
    font-size: 30px;
  }
}
</code></pre>

Ovenstående betingelse betyder, at hvis browservinduet maksimalt er 790 pixels i bredden, dvs. mindre end 791 pixels, så skal alle H1 på sitet have en skriftstørrelse på 30px. Denne betingelse kaldes også et breakpoint og det er disse breakpoints vi kan bruge til at flytte rundt på elementer, ændre deres design eller måske fjerne dem helt fra designet.

<h3>Valg af breakpoints</h3>

Der er overordnet to forskellige måder at vælge sine breakpoints på - en rigtig og en forkert. Den første er at kigge i Google Analytics og se hvilke skærmopløsninger brugerne har og vælge breakpoints efter dette. Derved vil man fx få en liste som denne:

<pre><code class="language-css">@media (max-width: 320px) { } /* iPhone i portrait mode */
@media (max-width: 480px) { } /* iPhone i landscape mode */
@media (max-width: 768px) { } /* iPad i portrait mode */
@media (max-width: 1024px) { } /* iPad i landscape mode */
</code></pre>

Derved kan man designe site website så det giver en god brugeroplevelse på alle ovenstående enheder uanset hvordan de vender. Denne tilgang har dog en stor ulempe: Formålet med et responsivt website er nemlig ikke at få det til at virke på nogle enheder, men derimod på <em>alle</em> enheder. Det gælder ikke kun iPhones og iPads, for de er snart forældet og i morgen kommer der en ny model, som måske har en helt andet skærmopløsning. Og vi skal også tænke på alle de andre smartphones og tablets der findes på markedet og alle de modeller der kommer næste år. Og det stopper ikke her, for hvad med smartwatches, smartTV, biler og måske også køleskabet som nok også snart kan gå på nettet? Det lyder som en fuldstændig umulig opgave med flere hundrede forskellige media queries som konstant skal opdateres når der kommer nye modeller.

Men vent... Jeg lovede dig jo at det var nemt at lave responsive webdesign? Bare rolig, det er det stadig. Tricket er at glemme alt om enheder og i stedet lade dit design diktere dine breakpoints! Dette gøres ved at gøre dit browservindue mindre og mindre indtil du ikke længere synes designet er pænt eller virker som det skal. Her måler du så bredden på vinduet og dermed har du dit første breakpoint.

Hvis du åbner Developer Tools i Chrome så viser den størrelsen på vinduet i øverste højre hjørne mens du trækker. For mig var det første breakpoint ved 788px hvor jeg synes linjerne begyndte at blive for korte og designet så i det hele taget lidt klemt ud. Det anbefales at holde linjernes længde på mellem 40 og 70 tegn, for at det er nemmest at læse. Hvis de bliver kortere skal man skifte linje for ofte og længere begynder det at blive svært for øjnene at finde tilbage til den rigtige linje ved linjeskift.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/first-breakpoint-788px.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/first-breakpoint-788px.png" alt="Ved 788px begynder designet at se lidt klemt ud." width="787" height="747" class="size-full wp-image-453" /></a><figcaption>Ved 788px begynder designet at se lidt klemt ud.</figcaption></figure>

Jeg indsætter derfor dette breakpoint som media query:

<pre><code class="language-css">@media (max-width: 788px) {}
</code></pre>

<strong>Vigtigt:</strong> Det er vigtigt at media queries indsættes nederst i CSS filen. De har ikke en højere CSS specificity, så de vil blive overskrevet at den almindelige styling, hvis de står øverst i filen.

Nu skal vi så finde ud af hvordan vi fixer designet, så det stadig er pænt og brugervenligt ved denne skærmstørrelse.

Et af de populære tricks at lave med media queries er at gøre designet smallere ved at fjerne kolonner fra designet. Det kan fx være man starter med tre kolonner og går først ned på to kolonner og til sidst en kolonne på de helt små skærme. I mit design har jeg kun to kolonner; et content område og en sidebar, som vist på tegningen længere oppe. De er sat op således:

<pre><code class="language-css">#wrapper {
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
}

#content {
  max-width: 600px;
  width: 66.66%;
  float: left;
}

#sidebar {
  max-width: 300px;
  width: 33.33%;
  float: right;
}
</code></pre>

For at lave dette to-kolonne design om til en kolonne laver jeg en media query som overskriver noget af ovenstående CSS når browservinduet er mindre end 788px. Mere præcist skal alle elementer have en bredde på 100% og deres float skal fjernes. Derudover skal max-width også sættes til 100% så vi fx overskriver de 600px som max-width er sat til på #content elementet. Da websitet kan ses i et browservindue på 788px skal det ikke længere begrænses til 600px som det er nu. Derfor sættes det op således:

<pre><code class="language-css">#wrapper {
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
}

#content {
  max-width: 600px;
  width: 66.66%;
  float: left;
}

#sidebar {
  max-width: 300px;
  width: 33.33%;
  float: right;
}

@media (max-width: 788px) {

#content {
  width: 100%;
  max-width: 100%;
  float: none;
}

#sidebar {
  width: 100%;
  max-width: 100%;
  float: none;
}
}
</code></pre>

Sitet ser nu således ud ved 786px. Meget bedre.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/first-media-query-786px.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/first-media-query-786px.jpg" alt="Websitet med en kolonne." width="783" height="625" class="size-full wp-image-456" /></a><figcaption>Websitet med en kolonne.</figcaption></figure>

Sidebaren ligger nu nederst på siden under kommentarerne. Bemærk at den fylder hele bredden ud, men at billedet ikke bliver større end det rigtigt er, hvilket skyldes den måde vi lavede billederne fleksible på tidligere.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/Screenshot-2013-11-16-02.11.50.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/Screenshot-2013-11-16-02.11.50.png" alt="Sidebaren skubbet ned under det primære indhold." width="770" height="649" class="size-full wp-image-457" /></a><figcaption>Sidebaren skubbet ned under det primære indhold.</figcaption></figure>

Men vi kan godt gøre lidt mere. Min tagline i headeren er blevet skubbet ned på tre linjer og det er ikke så pænt. Derudover begynder hele min header med logo og tagline også at fylde lidt for meget af siden, når sitet bliver set på en så lille skærm. Jeg vil derfor gerne gøre det mindre og mere simpelt, så man kan bruge pladsen til at vise det rigtige indhold. Jeg fjerner derfor min tagline og gør logoet (som bare er en H1 med teksten jacobworsoe.dk) lidt mindre og så skal logoet kunne bruge hele bredden, dvs. width: 100%. Derudover gør jeg også mine H1'ere lidt mindre, så de heller ikke bliver for voldsomme på små skærme. Jeg tilføjer dette til min media query:

<pre><code class="language-css">#logo {
  float: none;
  max-width: 100%;
  width: 100%;
  font-size: 26px;
  text-align: center;
}

#tagline {
  display: none;
}

h1 {
  font-size: 30px;
}
</code></pre>

Derved ser sitet nu sådan ud:

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/Screenshot-2013-11-16-02.16.18.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/Screenshot-2013-11-16-02.16.18.png" alt="Header, logo og tagline tilpasset til små skærme." width="783" height="580" class="size-full wp-image-458" /></a><figcaption>Header, logo og tagline tilpasset til små skærme.</figcaption></figure>

<h3>Flere media queries?</h3>

Jeg prøver nu at gøre browseren endnu mindre, men synes faktisk at designet virker glimrende uanset hvor småt vinduet bliver. Og det er netop fluid grid, der gør at designet virker selvom vi gør browseren mindre. Vi har kun en media query som ændre på designet, resten af tilpasningen til utallige skærmstørrelser klares fordi designet er fluid og dermed fleksibelt.

<h2 id="viewport-meta-tag">3. Viewport meta tag</h2>

Nu har jeg et design som virker på alle enheder, så vi kan da lige prøve at teste det på en iPhone. Desværre er resultatet ikke helt som forventet - mit responsive website virker slet ikke...

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2013-11-17-01.32.38.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2013-11-17-01.32.38.png" alt="Siden set med en iPhone 4S." width="640" height="960" class="size-full wp-image-462" /></a><figcaption>Siden set med en iPhone 4S.</figcaption></figure>

Grunden til dette er at der - især da iPhonen blev lanceret, men også nu til dags - findes mange websites som ikke er optimeret til mobile enheder, så derfor er enhederne nødt til at lave nogle tricks for at give den bedst mulige brugeroplevelse på alle websites. De mobile enheder viser derfor websites som om de havde en stor desktop skærm, så man kan se hele websitet når man lander på det. Hvis de ikke gjorde det, ville de bare vise det øverste venstre hjørne af websitet. Med dette trick giver de dig det fulde overblik over websitet, hvorefter du så kan zoome ind på den tekst du vil læse.

iPhonen viser fx websitet som om den havde en skærmbredde på 980px og derfor bliver den ikke påvirket af vores media query. Men nu har vi lavet et website som er optimeret til alle slags enheder, og vi kan dermed fortælle browseren at den skal vise siden i den størrelse som enheden i virkeligheden har. Dette gøres ved at indsætte dette tag i din header:

<pre><code class="language-html"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
</code></pre>

Nu vil iPhonen vise websitet med en skærmbredde på 320px og dermed blive påvirket af vores media query, som siger at designet kun har én kolonne. Derudover siger den at der skal være zoomet helt ud og at der ikke må kunne zoomes ind på teksten. Derved ser sitet nu således ud:

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2013-11-27-20.43.01.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2013-11-27-20.43.01.png" alt="Websitet på en iPhone med en bredde på 320px." width="640" height="960" class="size-full wp-image-470" /></a><figcaption>Websitet på en iPhone med en bredde på 320px.</figcaption></figure>

Og det var faktisk det. Det var de tre trin der skal til for at omdanne websitet til at være 100% responsivt, uanset hvilken enhed det bliver vist på.

<h2>Mobile first - mere end en ideologi</h2>

Måske har du hørt udtrykket mobile first? Men hvad er det? Det er vel hvad man kan kalde en ideologi eller tilgang til webdesign. Men det er mere end webdesign. For snart fire år siden sagde Eric Schmidt fra Google at de skiftede til at <a href="http://www.pcmag.com/article2/0,2817,2359752,00.asp" target="_blank" rel="noopener noreferrer">lave alting mobile first</a>. Grundlæggende går det ud på at man starter med at lave sit projekt til mobile enheder og derefter skalerer det op til desktop og ikke den anden vej. Det har nogle klare fordele. Jeg ser primært to fordele som jeg har valgt at kalde <em>den ideologiske fordel</em> og <em>den tekniske fordel</em>.

<h3>Den ideologiske fordel</h3>

Hvor mange gange er du ikke kommet ind på et mobilt website og har en følelse af at du går glip af noget. Noget af det de har ovre på "det fulde website". Den følelse sidder jeg i hvert fald tit med. En skrabet oplevelse, hvor man kun har adgang til få udvalgte sektioner af sitet og stærkt begrænset funktionalitet. Man bliver nærmest straffet for at besøge websitet fra sin mobiltelefon. Dette kan man også sagtens komme ud for ved responsivt webdesign og jeg har faktisk skudt mig selv i foden, for jeg valgte jo at fjerne min tagline oppe i headeren på små skærme. Jeg giver dermed brugerne et begrænset website, selvom mine intentioner måske var gode nok - nemlig at fjerne overflødige ting og gøre det mere simpelt. Men hvis taglinen er overflødig på mobile enheder, hvorfor skal desktop brugere så se på den? Og det er netop det der er tankegangen bag mobile first.

Start med at designe til mobile enheder, for så tvingen du dig selv til kun medtage ting i designet som er absolut nødvendige for brugeren. Så for du skåret overflødige ting fra med det samme og du skal ikke længere bekymre dig om, hvilke brugere der skal se dem, og hvem der ikke skal, og alle enheder har adgang til det samme indhold, blot præsenteret på forskellige måder.

Rent praktisk vil det så sige at du starter med et design i en kolonne og når skærmen så bliver stor nok, så skriver du en media query som laver designet om til to kolonne. I det ovenstående har vi brugt max-width som media query, og det skal nu ændres til min-width, dvs. reglen er opfyldt når skærmen minimum er X antal pixel bred:

<pre><code class="language-css">@media (min-width: 788px) {
// CSS til to-kolonne design
}
</code></pre>

Det var den mere bløde fordel. Nu til den hårde.

<h3>Den tekniske fordel</h3>

Måden disse media queries fungerer på, er at de overskriver den normale CSS, hvis reglen er opfyldt. Dette betyder altså at vi først fortæller browseren at websitet skal se ud på en bestemt måde og derefter beder browseren om at lave det om til noget helt andet. Når vi designer <em>desktop first</em>, så beder vi dermed små mobiltelefoner om at lave en masse arbejde før de kan vise siden til brugeren. Problemet er tydeligt, ik? Vi beder altså den enhed med den mindste hardware og den dårligste internetforbindelse om at hente en masse overflødig information, blot for at overskrive dem gennem en masse ekstra beregninger. Og problemet kunne være meget større end på min blog, hvor der trods alt kun laves små justeringer. Tænk bare hvis vi havde 5-6 breakpoints og ændrede en masse ting i designet hver gang.

Hvis vi lavede designet mobile first, så kunne de mindste enheder nøjes med at læse den normale CSS og springe over alle media queries og overlade alle de ekstra beregninger til de større enheder. Det virker som en meget mere fair arbejdsfordeling :)

<h2>Det handler ikke kun om små skærme</h2>

I et <a title="Husk 301 når du får ny hjemmeside" href="https://www.jacobworsoe.dk/husk-301-nar-du-far-ny-hjemmeside/" target="_blank" rel="noopener noreferrer">tidligere blogindlæg</a> var jeg lidt ude efter HiFi-Klubben, men det er faktisk et ret lækkert website de har fået lavet hvor de bruger media queries rigtig meget. Responsivt design, handler nemlig ikke kun om at lave mobilvenlige websites, men om hele tiden at udnytte den tilgængelige skærmplads bedst muligt. Et eksempel er at HiFi-Klubben bruger nedenstående media query til vise 5 kolonner med produkter på meget store skærme (over 1611 pixel). Det kunne jeg fx godt lære noget af på denne blog, hvor mit design maksimalt er 900px bredt, hvilket giver en masse spildplads hvis man fx sidder på en Full HD skærm som er 1920 pixels i bredden.

Her er den media query som HiFi-Klubben bruger til at vise 5 kolonner (ved at sætte deres width til 20% er der plads til 5 produkter) på store skærme:

<pre><code class="language-css">@media only screen and (min-width: 1611px)
{
    .product-teaser-list .product-teaser--large
    {
        width: 20%;
    }
}
</code></pre>

<h2>Så er det din tur</h2>

Så er der vist ikke mere at sige om responsive web design i denne omgang. Jeg håber dette har vist at der ikke er noget magisk bag responsive design og at det faktisk er til at overskue, så du nu er klar til at lave dit eget website responsivt. Hvilket website skal du igang med? Har du allerede lavet det responsivt? Vis det endelig frem i kommentarerne herunder!

Og skulle du sidde tilbage med nogle spørgsmål, inden du kaster dig ud i det, så skal du også være velkommen til at skrive det herunder.