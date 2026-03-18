---
layout: post
title: Tracking af indhold med Enhanced Ecommerce
date: 2020-07-31 23:33:15
slug: indhold-enhanced-ecommerce
wordpress_id: 1700
categories:
  - Analytics
---

Hvilke KPI'er er vigtige for en blog?

Antal månedlige besøg er vigtig.

Trafik fordelt på kanaler er også vigtig at vide. Og måske også om de besøgende tilmelder sig nyhedsbrevet.

<h3>Men hvordan måles konvertering?</h3>

Man kan tracke når nogen skriver en kommentar. Men da diskussionen i høj grad er flyttet over til de sociale medier hvor indlægget deles, så er det ikke et godt mål for konvertering på en blog. Siden jeg startede min blog i 2009 har jeg til dato haft 118.121 besøg og 482 kommentarer, hvilket giver en konverteringsrate på 0,4%.

Det kan også være tilmelding til RSS feed, men selvom det er min foretrukne måde at holde mig opdateret med en lang række blogs, så har jeg på fornemmelsen, at det er meget få der bruger det. Det samme med nyhedsbreve for blogs.

Endelig er der metrics som bounce rate og time on page. Men de er svære at konkludere noget ud fra isoleret set. Jeg har en bounce rate på 85% på dette site. Det er højt, men det betyder ikke nødvendigvis at mine blogindlæg ikke bliver læst grundigt. Det kan sagtens være brugerne er på sitet mange minutter og stadig bouncer. Det betyder bare at de kun læser ét blogindlæg.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent.jpg" alt="85% bounce rate." width="886" height="286" class="size-full wp-image-2300" /></a><figcaption>85% bounce rate.</figcaption></figure>

Time on page bliver ikke målt på den sidste side i et besøg, så med en bounce rate på 85% er det sjældent den bliver målt. Den metric er også farlig at konkludere noget ud fra, da brugeren ikke nødvendigvis forlader siden, men fx blot loader en ny side i en anden tab.

<h2 id="article-header-id-0">Bliver indholdet rent faktisk læst?</h2>

Selvom det er fedt med mange besøg og sidevisninger, så siger det ikke i sig selv noget om kvaliteten af indholdet. Det er vigtigt at vide om brugerne rent faktisk læser indlægget.

Og det er lige præcis den form for konvertering der er vigtig for en blog, så i dette indlæg viser jeg hvordan jeg bruger Google Analytics Enhanced Ecommerce til at tracke mit indhold og den verden af nye indsigter det åbner op for.

<h2 id="article-header-id-1">Inspireret af Simo Ahava</h2>

Jeg elsker at finde nye kreative måder at bruge Google Analytics og Enhanced Ecommerce til at indsamle data og få et nyt indblik i alt fra websites til den fysiske verden.

Det gør Simo Ahava også og mit tracking setup er også kraftigt inspireret af det setup han har lavet på sin egen blog og skrevet om her: <a href="https://www.simoahava.com/analytics/track-content-enhanced-ecommerce/" rel="noopener noreferrer">Track Content With Enhanced Ecommerce</a>

Selve logikken i koden er kopieret fra Simo's <a href="https://github.com/sahava/eec-gtm" rel="noopener noreferrer">Github</a> som er baseret på <a href="http://cutroni.com/blog/2014/02/12/advanced-content-tracking-with-universal-analytics/" rel="noopener noreferrer">Justin Cutroni's scroll script</a>.

Jeg har derefter omskrevet det til ren JavaScript, så det ikke er afhængigt af jQuery, for at slippe for at skulle loade jQuery på sitet. Jeg brugte den her rigtig meget for at konvertere koden: <a href="http://youmightnotneedjquery.com" rel="noopener noreferrer">youmightnotneedjquery.com</a>

Derudover har jeg lavet tre udvidelser af koden:

<ul>
<li>Jeg tracker kun impressions af blogindlæg på forsiden og andre lister, hvis de har været synlige på skærmen</li>
<li>Jeg tracker brugere der kun skimmer artiklen, uden at læse den</li>
<li>Alle data er udstillet i <code>dataLayer</code> og jeg scraper derfor ikke noget indhold med JavaScript</li>
</ul>

Mere om det senere.

<h2>Tracking af læsning af indhold med Enhanced Ecommerce</h2>

Okay, lad os lige starte med at se på hvordan man overhovedet kan bruge Enhanced Ecommerce til at tracke når brugerne læser indholdet på en blog. Det kræver nemlig at man er lidt kreativ med fortolkningerne af Ecommerce og checkout.

Her er definitionerne af Enhanced Ecommerce, som jeg bruger på min blog:

<ul>
<li><strong>Produkt:</strong> Et blogindlæg.</li>
<li><strong>Produkt navn:</strong> Titlen på blogindlægget.</li>
<li><strong>Produkt pris:</strong> Antal ord i blogindlægget.</li>
<li><strong>Produkt kategori:</strong> WordPress kategori, fx "Webanalyse" eller "SEO".</li>
<li><strong>Produkt brand:</strong> Blogindlæggets udgivelsesår.</li>
<li><strong>Produkt impression:</strong> Når et blogindlæg bliver vist på en liste, fx forsiden, kategorisider, tagsider, relateret blogindlæg eller lignende.</li>
<li><strong>Produkt lister:</strong> Alle ovenstående lister.</li>
<li><strong>Produkt click:</strong> Når en bruger klikker på et blogindlæg på en af ovenstående lister.</li>
<li><strong>Produkt detail view:</strong> Når et blogindlæg vises (dvs. sidevisning af et blogindlæg).</li>
<li><strong>Produkt add to cart:</strong> Når brugeren begynder at scrolle og dermed om de er begyndt at læse indlægget.</li>
<li><strong>Produkt checkout:</strong> Der er 3 steps i checkout, som er afhængige af hvor langt brugeren scroller. Step 1 er 33%, step 2 er 66% og step 3 er 100% af indlægget. Her måler jeg kun højden på selve indlægget, dvs. kommentarer er ikke med.</li>
<li><strong>Gennemført købt:</strong> Når brugeren har scrollet 100% af indlægget og været mindst 1 minut på siden. Dermed kan jeg antage at indlægget rent faktisk er læst og ikke bare skimmet.</li>
</ul>

<h2>Lad os få styr på produktdata</h2>

På alle sider hvor der vises et eller flere indlæg, skal der trackes en række produktdata for hvert indlæg.

ID og navnet (titlen) på indlægget kan fanges i Wordpress i <a href="https://codex.wordpress.org/The_Loop" rel="noopener noreferrer" target="_blank">The Loop</a> med de indbyggede funktioner <code>the_title()</code> og <code>the_ID()</code> og gemmes i en JavaScript variabel, så de kan sendes til Google Analytics. Årstallet som gemmes i brand hentes med <code>the_time('Y')</code>.

Et indlæg kan tilhøre flere kategorier og hvis du bruger <a href="https://wordpress.org/plugins/wordpress-seo/" rel="noopener noreferrer" target="_blank">Yoast SEO</a> er der mulighed for at angive en primær kategori. Hvis et indlæg tilhører flere kategorier, bruges kun den primære. Den logik kan kodes således:

<pre><code class="language-php">// SHOW YOAST PRIMARY CATEGORY, OR FIRST CATEGORY
$category = get_the_category();
$useCatLink = true;

// If post has a category assigned.
if ($category){
    $category_display = '';
    $category_link = '';
    if ( class_exists('WPSEO_Primary_Term') )
    {
        // Show the post's 'Primary' category, if this Yoast feature is available, & one is set
        $wpseo_primary_term = new WPSEO_Primary_Term( 'category', get_the_id() );
        $wpseo_primary_term = $wpseo_primary_term->get_primary_term();
        $term = get_term( $wpseo_primary_term );
        if (is_wp_error($term)) { 
            // Default to first category (not Yoast) if an error is returned
            $category_display = $category[0]->name;
            $category_link = get_category_link( $category[0]->term_id );
        } else { 
            // Yoast Primary category
            $category_display = $term->name;
            $category_link = get_category_link( $term->term_id );
        }
    } 
    else {
        // Default, display the first category in WP's list of assigned categories
        $category_display = $category[0]->name;
        $category_link = get_category_link( $category[0]->term_id );
    }

    // Display category
    if ( empty($category_display) ) {
        $category_display = "Ingen kategori";
    }   
}
</code></pre>

Derefter udskrives kategorien med <code><?php echo $category_display; ?></code>.

Prisen er antal ord og der har PHP en indbygget funktion <code>str_word_count</code> som tæller antal ord i en streng - i dette tilfælde den aktuelle artikel. Jeg har lagt det i en funktion i <code>functions.php</code> så jeg nemt kan kalde den med word_count() i <code>single.php</code>.

<pre><code class="language-php">function word_count() {
    $content = get_post_field( 'post_content', $post->ID );
    $word_count = str_word_count( strip_tags( $content ) );
    return $word_count;
}
</code></pre>

I Enhanced Ecommerce er det vigtigt at produktdata er formateret med præcis den rigtige syntaks - ellers vil der ikke blive sendt nogen produktdata til Google Analytics for dét request. Det færdige <code>Product</code> object med den korrekte syntaks ser således ud:

<pre><code class="language-javascript">var product = [{
    name: '<?php the_title(); ?>',
    id: '<?php the_ID(); ?>',
    price: '<?php echo word_count(); ?>',
    brand: '<?php the_time('Y') ?>',
    category: '<?php echo $category_display; ?>',
    variant: '',
    quantity: 1
  }];
</code></pre>

<h2>Product impressions efter 2 sekunder</h2>

Det første trin i kunderejsen er product impressions på en produktliste.

Der vises lister af blogindlæg på forsiden, kategorisider, som relaterede indlæg, etc. Der er primært to ting der er vigtige når der trackes impressions.

<ol>
<li>Der skal kun trackes impressions af blogindlæg som brugeren rent faktisk har set. Det er ikke nok at linket til  blogindlægget har været længere nede på siden (below the fold), eller at brugeren har scrollet lynhurtigt forbi det. Brugeren skal have set blogindlægget og jeg skal være rimelig sikker på at brugeren har set og forholdt sig til det.</p></li>
<li><p>Trackingen må ikke sløve brugerens computer og gøre sitet langsomt. Når jeg skal holde øje med hvor langt brugeren scroller ned af siden og dermed om et givent blogindlæg er blevet synligt på skærmen, kan jeg nemt risikere at der skal køres noget JavaScript kode meget ofte, især hvis brugeren scroller hurtigt ned over siden. Dette kan påvirke hvor gnidningsfrit scrollet opleves for brugeren.</p></li>
</ol>

<p>I værste fald kan det gøre sitet ubrugeligt, som det <a href="https://johnresig.com/blog/learning-from-twitter/" rel="noopener noreferrer" target="_blank">skete for Twitter tilbage i 2011</a>.

<blockquote>Depending upon the browser the scroll event can fire a lot and putting code in the scroll callback will slow down any attempts to scroll the page (not a good idea). Instead it’s much better to use some form of a timer to check every X milliseconds OR to attach a scroll event and only run your code after a delay.<cite><a href="https://johnresig.com/blog/learning-from-twitter/" target="_blank" rel="noopener noreferrer">John Resig, skaberen af jQuery</a></cite></p></blockquote>

<p><strong>Begge ting kan løses med en debounce funktion.</strong>

En debounce funktion siger: “Udfør denne kode når noget ikke er sket i X antal millisekunder”.

<a href="https://css-tricks.com/debouncing-throttling-explained-examples/" rel="noopener noreferrer" target="_blank">Denne artikel fra CSS-Tricks.com</a> har nogle gode visualiseringer og demoer som viser hvordan debounce virker. David Walsh har også <a href="https://davidwalsh.name/javascript-debounce-function" rel="noopener noreferrer" target="_blank">skrevet om det her</a>.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/css-tricks-debounce.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/css-tricks-debounce.png" alt="Kilde: CSS-Tricks.com" width="661" height="133" class="size-full wp-image-2328" /></a> Kilde: <a href="https://css-tricks.com/debouncing-throttling-explained-examples/">CSS-Tricks.com</a></figure>

I dette tilfælde køres koden når brugeren stopper med at scrolle i 2 sekunder. Hvis brugeren scroller igen inden de 2 sekunder er gået, nulstilles timeren og når brugeren stopper med at scrolle, starter timeren igen fra 0 og hvis der går 2 sekunder uden scroll, udføres koden.

Og sidst men ikke mindst skal der kun trackes impressions for et produkt én gang på hver side.

Lad os kigge på koden.

Først er der lavet tre funktioner. Den første tjekker om et element er synligt på skærmen.

<pre><code class="language-javascript">function checkVisible(elm) {
  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
  return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
}   
</code></pre>

<p class="attention"><strong>Bemærk!</strong> Jeg lavede dette tilbage i 2016. Hvis det skal laves i dag, kan du med fordel bruge <a href="https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API">Intersection Observer</a> som er et asynkront API til netop at holde øje med hvornår elementer bliver synlige i viewport og den kan også holde styr på hvilke der har været synlige, så man ikke selv skal sørge for at de ikke tracker flere gange. <a href="https://caniuse.com/#feat=intersectionobserver">Browser support</a> er rigtig god i dag, så den bør bruges fremover.
</p>

Den næste laver et Enhanced Ecommerce product object med de relevante produktdata for et blogindlæg som er synligt på skærmen.

<pre><code class="language-javascript">function pushProducts(productElement, i) {
  ga_products.push({
    name: productElement[i].dataset.title,
    id: productElement[i].dataset.id,
    price: productElement[i].dataset.price,
    brand: productElement[i].dataset.year,
    category: productElement[i].dataset.category,
    variant: productElement[i].dataset.author,
    list: pageType,
    position: productElement[i].dataset.position
  });
}
</code></pre>

Produktdataene er placeret i data attributter i HTML koden.

<pre><code class="language-html"><h1 class="home-post-headline">
    <a href="https://www.jacobworsoe.dk/returvarer-google-analytics/" 
        data-title="Tracking af returvarer i Google Analytics (den ultimative guide)" 
        data-id="1597" 
        data-category="Webanalyse" 
        data-year="2019" 
        data-author="2" 
        data-price="3668" 
        data-position="2"
        class="home-post-link">
        Tracking af returvarer i Google Analytics (den ultimative guide)            
    </a>
</h1>
</code></pre>

Den tredje funktion sender impressions til Google Analytics.

<pre><code class="language-javascript">function sendProducts(trigger) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    event: trigger,
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}</code></pre>

Ved pageload bygges et JavaScript <code>object</code> med sidens blogindlæg og der checkes om nogle af sidens blogindlæg er synlige, dvs. dem som er above-the-fold. De synlige blogindlæg pushes til products objectet med <code>pushProducts()</code>.

Hvis der er blogindlæg som ikke er synlige, tilføjes de til <code>ga_products_not_visible</code> objectet som vi derefter kan holde øje med om de bliver synlige i 2 sekunder og tracke en impression for dem.

<pre><code class="language-javascript">// Cache product element
var articles = document.querySelectorAll(".home-post-headline a");

// See if products are in view
if (articles && articles.length > 0) {
  for (var i = 0; i < articles.length; i++) {
    if (checkVisible(articles[i])) {
      pushProducts(articles, i);
    } else {
      ga_products_not_visible.push(articles[i]);
    }
  }
}</code></pre>

Hvis der var nogle synlige blogindlæg, pushes de til dataLayer, så de bliver sendt med, sammen med pageview requestet for siden.

<pre><code class="language-javascript">// If any products was in view on pageload, send those products
if (ga_products.length > 0) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}</code></pre>

Okay, nu har vi styr på blogindlæg som er above-the-fold. Nu skal vi tracke impressions for dem som er below-the-fold.

Fordi det kan være lidt tungt at tracke på scroll, så skal det kun gøres hvis der rent faktisk er nogle produkter below-the-fold, så det starter vi med at tjekke med <code>ga_products_not_visible.length</code>.

Derefter defineres en funktion som køres hver gang der scrolles.

Det første funktionen gør, når der scrolles er <code>clearTimeout</code> som nulstiller timeren.

Derefter startes en ny <code>setTimeout</code> som indeholder den kode som køres efter 2000 millisekunder.

Når de 2000 millisekunder er gået udføres koden, som tjekker om nogle af de blogindlæg der endnu ikke er tracket en impression af, er synlige på skærmen. Hvis det er tilfældet bliver de tilføjet til products objectet og fjernet fra listen over blogindlæg der ikke er tracker en impression for, så de ikke kan trackes igen. Til sidst sendes de til Google Analytics med et event.

<strong>Men!</strong> Hvis der scrolles inden de 2000 millisekunder er gået, så køres hele koden igen og det første i koden er at nulstille timeren og starte den på ny som beskrevet herover.

Dette er “magien” bag en debounce funktion. Den sørger for at koden ikke afvikles med det samme der scrolles, men først efter en pause på 2000 millisekunder, hvilket både gør sitet mere flydende, men også sikrer at brugeren skal stoppe med at scrolle i 2000 millisekunder (og dermed formentlig har vurderet om de vil klikke på linket) før vi tracker en impression.

<pre><code class="language-javascript">// If page contained products not in view, start the scroll tracker
if (ga_products_not_visible.length > 0) {
  var scrollTimeout;

  function checkProductsInViewOnScroll() {
    clearTimeout(scrollTimeout);

    scrollTimeout = setTimeout(function() {
      for (var i = ga_products_not_visible.length - 1; i >= 0; i--) {
        if (checkVisible(ga_products_not_visible[i])) {
          pushProducts(ga_products_not_visible, i);

          // Remove the product in view from ga_products_not_visible
          ga_products_not_visible.splice(i, 1);
        }
      }

      if (ga_products.length > 0) {
        sendProducts("moreImpressionsSent");
      }
    }, 2000);
  }

  // Start scroll listener
  window.addEventListener("scroll", checkProductsInViewOnScroll);
}</code></pre>

Her er den samlede kode til at tracke impressions på lister.

<pre><code class="language-javascript">// Set objects to store posts
window.ga_products = window.ga_products || [];
window.ga_products_not_visible = window.ga_products_not_visible || [];

function checkVisible(elm) {
  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(
    document.documentElement.clientHeight,
    window.innerHeight
  );
  return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
}

function pushProducts(productElement, i) {
  ga_products.push({
    name: productElement[i].dataset.title,
    id: productElement[i].dataset.id,
    price: productElement[i].dataset.price,
    brand: productElement[i].dataset.year,
    category: productElement[i].dataset.category,
    variant: productElement[i].dataset.author,
    list: pageType,
    position: productElement[i].dataset.position
  });
}

function sendProducts(trigger) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    event: trigger,
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}

// Cache product element
var articles = document.querySelectorAll(".home-post-headline a");

// See if products are in view
if (articles && articles.length > 0) {
  for (var i = 0; i < articles.length; i++) {
    if (checkVisible(articles[i])) {
      pushProducts(articles, i);
    } else {
      ga_products_not_visible.push(articles[i]);
    }
  }
}

// If any products was in view on pageload, send those products
if (ga_products.length > 0) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}

// If page contained products not in view, start the scroll tracker
if (ga_products_not_visible.length > 0) {
  var scrollTimeout;

  function checkProductsInViewOnScroll() {
    clearTimeout(scrollTimeout);

    scrollTimeout = setTimeout(function() {
      for (var i = ga_products_not_visible.length - 1; i >= 0; i--) {
        if (checkVisible(ga_products_not_visible[i])) {
          pushProducts(ga_products_not_visible, i);

          // Remove the product in view from ga_products_not_visible
          ga_products_not_visible.splice(i, 1);
        }
      }

      if (ga_products.length > 0) {
        sendProducts("moreImpressionsSent");
      }
    }, 2000);
  }

  // Start scroll listener
  window.addEventListener("scroll", checkProductsInViewOnScroll);
}
</code></pre>

Antal impressions falder dermed jo længere ned på forsiden man kommer og de første to positioner har stort set samme antal impressions, da de er above-the-fold, både på mobile og desktop.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden-860x477.png" alt="Impressions fordelt på positioner på forsiden." width="860" height="477" class="size-large wp-image-2315" /></a><figcaption>Impressions fordelt på positioner på forsiden.</figcaption></figure>

<h2>Produkt click med et callback</h2>

Når brugeren klikker på et blogindlæg, skal klikket trackes. Udfordringen er at siden skifter når man klikker og derfor er der risiko for at requestet ikke når at blive sendt til Google Analytics, før siden er skiftet og dermed bliver det aldrig sendt.

Løsningen er at annullere sideskiftet med JavaScript og istedet få GTM til at <a href="https://www.simoahava.com/gtm-tips/hitcallback-eventcallback/" rel="noopener noreferrer" target="_blank">lave sideskiftet i et callback</a> efter requestet er succesfuldt sendt til Google Analytics.

Der er særligt to ting der er vigtige at tage højde for når man annullerer et sideskift.

<ol>
<li>Hvis requestet til Google Analytics fejler eller GTM ikke bliver loaded korrekt på siden, kan det betyde at sideskiftet aldrig bliver lavet.</p></li>
<li><p>Hvis brugeren holder CTRL (eller CMD på Mac) nede mens der klikkes på linket for at åbne det i en ny tab, skal der ikke laves et sideskift, da brugeren jo netop gerne vil blive på siden.</p></li>
</ol>

<p>Den første kan løses ved at lave et <a href="https://www.simoahava.com/gtm-tips/use-eventtimeout-eventcallback/" rel="noopener noreferrer" target="_blank">timeout på fx 2 sekunder</a>, så sideskiftet bliver lavet uanset hvad, hvis requestet til Google Analytics ikke er gennemført efter 2 sekunder.

Den anden kan løses ved at tjekke om click eventet har enten <code>event.ctrlKey</code> (Windows) eller <code>event.metaKey</code> (Mac) for at tjekke om brugeren holder CTRL/CMD nede mens der klikkes.

Alt logikken tilføjes til det <code>dataLayer.push</code> som udføres når brugeren klikker på et blogindlæg på en liste, fx forsiden.

<pre><code class="language-javascript">dataLayer.push({
  event: "productClick",
  ecommerce: {
    click: {
      actionField: { list: pageType },
      products: [
        {
          name: title,
          id: id,
          price: price,
          brand: author,
          category: category,
          variant: year,
          position: position
        }
      ]
    }
  },
  eventCallback: function() {
    if (!e.ctrlKey && !e.metaKey) {
      window.location = href;
    }
  },
  eventTimeout: 2000
});
</code></pre>

<h2>Brugbar CTR på produktlister</h2>

Når der er styr på tracking af blogindlæg som har været på brugerens skærm i 2 sekunder, samt kliks, fås en meget mere brugbar CTR for de enkelte blogindlæg på de forskellige lister.

Brugbar fordi jeg ved at brugeren har haft tid til at læse overskriften og vurdere om blogindlægget er spændende og relevant. Det er helt afgørende for at man faktisk kan konkludere noget på baggrund af CTR.

<h2>Brugerne klikker ikke på relaterede og nyeste indlæg</h2>

Jeg har brugt Enhanced Ecommerce til at tracke min blog siden 2016. Da jeg gav bloggen et redesign i starten af 2019 undersøgte jeg hvor mange der klikker, når der vises relaterede indlæg i bunden af et indlæg eller klikker på listen af nyeste blogindlæg.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png" alt="Sidebar med nyeste blogindlæg - men klikker folk på dem?" width="1270" height="526" class="size-full wp-image-1828" /></a><figcaption>Sidebar med nyeste blogindlæg - men klikker folk på dem?</figcaption></figure>

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg.png" alt="I bunden af alle blogindlæg vises links til relaterede blogindlæg." width="941" height="595" class="size-full wp-image-1829" /></a><figcaption>I bunden af alle blogindlæg vises links til relaterede blogindlæg.</figcaption></figure>

Det gør de ikke.

Slet ikke.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png" alt="CTR på 0,05% og 0,42% viser at meget få klikker på de links." width="1094" height="485" class="size-full wp-image-1830" /></a><figcaption>CTR på 0,05% og 0,42% viser at meget få klikker på de links.</figcaption></figure>

Bemærk de meget forskellige antal impressions. Som beskrevet ovenfor tracker jeg kun impressions når links er synlige på skærmen og brugeren ikke har scrollet i 2 sekunder.

Nyeste indlæg vises i højre side højt oppe på siden, mens relaterede indlæg vises i bunden af blogindlæg, så der er langt færre der scroller helt ned til dem.

Fordi der er meget få kliks er det svært at optimere ud fra. Men hvis der havde været nogle flere kliks, ville det være oplagt at kigge på hvilke blogindlæg der fungerer godt når de vises som relaterede indlæg:

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products.png" alt="CTR for de enkelte blogindlæg når de vises som relaterede indlæg." width="890" height="610" class="size-full wp-image-1833" /></a><figcaption>CTR for de enkelte blogindlæg når de vises som relaterede indlæg.</figcaption></figure>

CTR på de links var dermed så lav, at de for langt de fleste brugere ikke er brugbare links, og dermed blot støj. Jeg valgte derfor at fjerne dem i det nye design og dermed få et mere clean design.

<blockquote>Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.<cite>Antoine de Saint-Exupery</cite></blockquote>

Til sammenligning har links på forsiden en CTR på 4,92%.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden.png" alt="CTR på forsiden." width="818" height="313" class="size-full wp-image-1844" /></a><figcaption>CTR på forsiden.</figcaption></figure>

Screenshottet viser i øvrigt en kritisk vigtig ting i Enhanced Ecommerce og analytics generelt: <strong>Konsistent data</strong>.

Da jeg redesignede bloggen omskrev jeg alt JavaScript fra bunden, så det var skrevet i ren JavaScript (dvs. uden jQuery) og samtidig fulgte <a href="https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/" rel="noopener noreferrer" target="_blank">den samme gode kodestruktur</a>.

Det betød desværre at jeg kom til at omdøbe Forsidens <code>product list name</code> fra Forsiden til homepage og dermed er data nu splittet.

Doh!

Lesson learned.

<h2>Produkt detaljevisning, add to cart og checkout</h2>

Okay, nu skal vi videre ned gennem tragten. Næste skridt fra <code>product click</code> er <code>detail view</code>. Nu gennemgår jeg alt det der sker på et blogindlæg.

Når et blogindlæg vises starter jeg med at sætte en række variabler, som bruges til at styre scroll trackingen. Der sættes det samme scrollTimeout på 2000 millisekunder som ved impressions og jeg sætter at brugeren mindst skal scrolle 150 pixels før de er begyndt at læse indlægget.

Derefter sættes en variabel til <code>false</code> for hvert event/state ned gennem siden. Når brugeren scroller til et punkt affyres et event og det sættes derefter til <code>true</code> så det samme event ikke trackes igen, hvis brugeren scrolle op igen.

Derefter vælges den <code>div</code> som indeholder blogindlægget, så jeg kan måle højden på den <code>div</code> og holde øje med hvor langt brugeren scroller. Bemærk at kommentarerne under indlægget ikke er med i denne <code>div</code>, så det er kun selve indlægget jeg kigger på.

Til sidst gemmes det aktuelle tidspunkt, som bruges til at afgøre hvor længe brugeren har været aktiv på siden.

<pre><code class="language-javascript">// Default time delay before checking location
var scrollTimeout = 2000;

// # px before tracking a reader
var readerLocation = 150;

// Set some flags for tracking & execution
var timer = 0;
var scroller = false;
var oneThird = false;
var twoThirds = false;
var endContent = false;
var didComplete = false;
var purchase = false;

// Content area DIV class
var contentArea = document.querySelector(".post-content");

// Set some time variables to calculate reading time
var startTime = new Date();
var beginning = startTime.getTime();
var totalTime = 0;
</code></pre>

Derefter pushes en Enhanced Ecommerce action sat til <code>detail</code> som sendes med sidevisningen når brugeren lander på blogindlægget. Konsistens er vigtig i Enhanced Ecommerce, så de produktdata der sendes med her, skal være identiske med dem som bruges ved <code>impressions</code> og <code>click</code>.

<pre><code class="language-javascript">// Track the article load as a Product Detail View
dataLayer.push({
   ecommerce: {
     detail: {
       products: product
     }
   }
});
</code></pre>

Derefter defineres den funktion som affyres når brugeren ikke har scrollet i 2000 millisekunder.

<pre><code class="language-javascript">// Check the location and track user
function trackLocation() {
  clearTimeout(scrollTimeout);

  scrollTimeout = setTimeout(function() {
// Herinde placeres alt koden som affyres efter 2000 millisekunder

    }
  }, 2000);
}

// Track the scrolling and track location
window.addEventListener("scroll", trackLocation);
},
</code></pre>

Når brugeren begynder at scrolle på siden og dermed begynder at læse indholdet, trackes dette med et <code>add to cart</code> event. Her bruger jeg samme debounce funktion som tidligere, sat til 2 sekunder.

<pre><code class="language-javascript">scrollTimeout = setTimeout(function() {
    bottom = window.innerHeight + window.pageYOffset;

    // If user starts to scroll send an event
    if (bottom > readerLocation && !scroller) {
      dataLayer.push({
        event: "addToCart",
        ecommerce: {
          add: {
            products: product
          }
        }
      });
      scroller = true;          
    }
</code></pre>

Når brugeren lander på siden måles højden på artiklen i pixels, som bruges til at tracke hvor meget af artiklen der læses. Hvis brugeren scroller 33% af artiklen, trackes checkout step 1.

Ved 66% trackes step 2 og ved 100% af artiklen trackes step 3.

<pre><code class="language-javascript">// If one third is reached
if (
  bottom >= contentArea.offsetTop + contentArea.clientHeight / 3 &&
  !oneThird
) {
  dataLayer.push({
    event: "checkout",
    ecommerce: {
      checkout: {
        actionField: { step: 1, option: product[0].variant },
        products: product
      }
    }
  });
  oneThird = true;
}

// If two thirds is reached
if (
  bottom >= contentArea.offsetTop + contentArea.clientHeight / 3 * 2 &&
  !twoThirds
) {
  dataLayer.push({
    event: "checkout",
    ecommerce: {
      checkout: {
        actionField: { step: 2, option: product[0].variant },
        products: product
      }
    }
  });
  twoThirds = true;          
}

// If user has hit the bottom of the content send an event
if (
  bottom >= contentArea.offsetTop + contentArea.clientHeight &&
  (!endContent || !purchase)
) {
  if (!endContent) {
    dataLayer.push({
      event: "checkout",
      ecommerce: {
        checkout: {
          actionField: { step: 3, option: product[0].variant },
          products: product
        }
      }
    });
    endContent = true;
  }
}
</code></pre>

<h2>Tracking af læste blogindlæg som køb</h2>

Hvis brugeren har været på siden mere end 1 minut, når der er scrollet 100% af artiklen, antages det at brugeren har læst artiklen og ikke bare skimmet den og den handling trackes som et køb. Prisen på ordren er antal ord i blogindlægget og dermed kan man se hvor mange artikler og ord der bliver læst på bloggen.

<pre><code class="language-javascript">// If user has reached end of funnel, check if 60 seconds is passed
if (endContent && !purchase) {
  currentTime = new Date();
  contentScrollEnd = currentTime.getTime();
  timeToContentEnd = Math.round((contentScrollEnd - beginning) / 1000);
  if (timeToContentEnd > 60 && !purchase) {
    // Track purchase
    dataLayer.push({
      event: "purchase",
      ecommerce: {
        purchase: {
          actionField: {
            id:
              new Date().getTime() +
              "_" +
              Math.random()
                .toString(36)
                .substring(5),
            revenue: product[0].price
          },
          products: product
        }
      }
    });

    // Only do this once!
    purchase = true;
  } else {
    dataLayer.push({
      event: "scrollToEndBeforeOneMinute",
      product: product[0].name
    });
  }
}
</code></pre>

Den samlede kode for tracking af læsning af et blogindlæg ser dermed således ud:

<pre><code class="language-javascript">// Track single post as product
trackSinglePostAsProduct: function(product) {
  // Default time delay before checking location
  var scrollTimeout = 2000;

  // # px before tracking a reader
  var readerLocation = 150;

  // Set some flags for tracking & execution
  var timer = 0;
  var scroller = false;
  var oneThird = false;
  var twoThirds = false;
  var endContent = false;
  var didComplete = false;
  var purchase = false;

  // Content area DIV class
  var contentArea = document.querySelector(".post-content");

  // Set some time variables to calculate reading time
  var startTime = new Date();
  var beginning = startTime.getTime();
  var totalTime = 0;

  // Track the article load as a Product Detail View
  dataLayer.push({
    ecommerce: {
      detail: {
        products: product
      }
    }
  });

  // Check the location and track user
  function trackLocation() {
    clearTimeout(scrollTimeout);

    scrollTimeout = setTimeout(function() {
      bottom = window.innerHeight + window.pageYOffset;

      // If user starts to scroll send an event
      if (bottom > readerLocation && !scroller) {
        dataLayer.push({
          event: "addToCart",
          ecommerce: {
            add: {
              products: product
            }
          }
        });
        scroller = true;          
      }

      // If one third is reached
      if (
        bottom >= contentArea.offsetTop + contentArea.clientHeight / 3 &&
        !oneThird
      ) {
        dataLayer.push({
          event: "checkout",
          ecommerce: {
            checkout: {
              actionField: { step: 1, option: product[0].variant },
              products: product
            }
          }
        });
        oneThird = true;
      }

      // If two thirds is reached
      if (
        bottom >= contentArea.offsetTop + contentArea.clientHeight / 3 * 2 &&
        !twoThirds
      ) {
        dataLayer.push({
          event: "checkout",
          ecommerce: {
            checkout: {
              actionField: { step: 2, option: product[0].variant },
              products: product
            }
          }
        });
        twoThirds = true;          
      }

      // If user has hit the bottom of the content send an event
      if (
        bottom >= contentArea.offsetTop + contentArea.clientHeight &&
        (!endContent || !purchase)
      ) {
        if (!endContent) {
          dataLayer.push({
            event: "checkout",
            ecommerce: {
              checkout: {
                actionField: { step: 3, option: product[0].variant },
                products: product
              }
            }
          });
          endContent = true;
        }
      }

      // If user has reached end of funnel, check if 60 seconds is passed
      if (endContent && !purchase) {
        currentTime = new Date();
        contentScrollEnd = currentTime.getTime();
        timeToContentEnd = Math.round((contentScrollEnd - beginning) / 1000);
        if (timeToContentEnd > 60 && !purchase) {
          // Track purchase
          dataLayer.push({
            event: "purchase",
            ecommerce: {
              purchase: {
                actionField: {
                  id:
                    new Date().getTime() +
                    "_" +
                    Math.random()
                      .toString(36)
                      .substring(5),
                  revenue: product[0].price
                },
                products: product
              }
            }
          });

          // Only do this once!
          purchase = true;
        } else {
          dataLayer.push({
            event: "scrollToEndBeforeOneMinute",
            product: product[0].name
          });
        }
      }
    }, 2000);
  }

  // Track the scrolling and track location
  window.addEventListener("scroll", trackLocation);
},
</code></pre>

Dataene kan blandt andet ses i Product Performance rapporten.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance-860x452.jpg" alt="Top 10 mest læste blogindlæg og deres gennemsnitspris (antal ord)." width="860" height="452" class="size-large wp-image-2329" /></a><figcaption>Top 10 mest læste blogindlæg og deres gennemsnitspris (antal ord).</figcaption></figure>

<h2>Analyse af Ecommerce data for min blog</h2>

Okay, lad os kigge på det data jeg kan få ud af alt det her.

<h3>Shopping behaviour</h3>

En af de fedeste rapporter i Enhanced Ecommerce er Shopping Behaviour, som viser en komplet funnel over hele websitet fra total antal sessioner til antal køb.

Her ses frafaldet i hvert step mod læste blogindlæg.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour.png" alt="Shopping behaviour" width="1556" height="724" class="size-full wp-image-1926" /></a><figcaption>Shopping behaviour</figcaption></figure>

Jeg kan se at en stor del af de besøgende ser blogindlæg (faktisk hele 96%) og rigtige mange begynder at scrolle (add to cart). 85% af dem der scroller når også ned til den første 1/3 af indlægget (checkout) men kun 20% af dem læser et blogindlæg. Der er et stort frafald på det sidste step.

Det kigger vi lige nærmere på med <code>Checkout behaviour</code>.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour.png" alt="Checkout behaviour" width="1285" height="719" class="size-full wp-image-1927" /></a><figcaption>Checkout behaviour</figcaption></figure>

Antal sessioner bliver cirka halveret i hvert step, men dog er 78% af dem som scroller helt til bunden også på siden længe nok, til at de læser blogindlægget og tracket som et køb.

<h3>Ekskludering af irrelevante blogindlæg</h3>

Mit mest besøgte blogindlæg er uden sammenligning min <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">infografik over hvor meget der blev drukket til vores bryllup</a>.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart.png" alt="Mest besøgte sider siden 2009." width="823" height="415" class="size-full wp-image-1887" /></a><figcaption>Mest besøgte sider siden 2009.</figcaption></figure>

Jeg har brugt Enhanced Ecommerce til at tracke min blog siden december 2016 og siden da har den infografik stået for 77% af alle sidevisninger.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016.png" alt="Infografikken står for 77% af alle sidevisninger på sitet." width="741" height="351" class="size-full wp-image-1888" /></a><figcaption>Infografikken står for 77% af alle sidevisninger på sitet.</figcaption></figure>

Målgruppen og adfærden på det blogindlæg er markant anderledes end de andre blogindlæg jeg skriver om digital marketing, så derfor udelukker jeg den med et segment, i alle de nedenstående analyser.

<h3>Top 10 blogindlæg</h3>

Herunder ses top 10 blogindlæg baseret på sidevisninger (detail views) samt deres Buy-to-Detail Rate.

Eller sagt på en anden måde: En vanity metric mod en engagement metric.

Bemærk de kæmpe forskelle i engagement!

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate-860x380.jpg" alt="Der er kæmpe forskel på hvor mange der rent faktisk læser blogindlæggene." width="860" height="380" class="size-large wp-image-2331" /></a><figcaption>Der er kæmpe forskel på hvor mange der rent faktisk læser blogindlæggene.</figcaption></figure>

<h3>Konverteringsrate pr. trafikkilder</h3>

Med infografikken fjernet, kan jeg se om besøg fra forskellige kilder egentlig læser mine blogindlæg.

Gennemsnittet for sitet er en konverteringsrate på 26,58% hvilket vil sige at 27% af trafikken læser mindst ét blogindlæg. Det er jeg egentlig godt tilfreds med.

<ul>
<li>Organisk trafik har en konvertering på 24,33% dvs. tæt på gennemsnittet.</li>
<li>Social er høj hvor 34% læser blogindlægget når det bliver delt.</li>
<li>E-mail er ekstremt høj hvor 43% læser blogindlægget. Næsten dobbelt så højt som gennemsnittet. Jeg sender kun e-mails ud, når jeg skriver nye blogindlæg, så det giver god mening at folk kun klikker på links i de e-mails, hvis de synes blogindlægget ser spændende ud. Men alligevel :)</li>
</ul>

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping.png" alt="Konvertering fordelt på trafikkilder." width="1276" height="511" class="size-full wp-image-1893" /></a><figcaption>Konvertering fordelt på trafikkilder.</figcaption></figure>

Lad os først lige kigge nærmere på social og de posts jeg selv laver, når jeg har skrevet et nyt blogindlæg.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts.png" alt="Konvertering er markant højere end gennemsnittet på 27%." width="1268" height="351" class="size-full wp-image-1892" /></a><figcaption>Konvertering er markant højere end gennemsnittet på 27%.</figcaption></figure>

Konverteringen her er markant højere end gennemsnittet på 27% men det er interessant at facebook konvertere lavere end de andre. Jeg poster typisk kun i <a href="https://www.facebook.com/groups/googleanalytics/" rel="noopener noreferrer" target="_blank">Analytics-nørder - den hårde kerne</a> hvor alle er interesseret i Analytics. På <a href="https://www.linkedin.com/in/jacobworsoe/" rel="noopener noreferrer" target="_blank">LinkedIn</a> og <a href="https://twitter.com/jacobworsoe" rel="noopener noreferrer" target="_blank">Twitter</a> ryger den bredt ud til mit netværk, som nok er en lidt mere blandet skare, men til trods for det, så er der flere der læser hele indlægget.

<h2>Bliver blogindlæg læst eller bare skimmet?</h2>

Hvis brugeren scroller helt til bunden af et blogindlæg inden der er gået 60 sekunder, har brugeren kun skimmet blogindlægget. Der er ikke noget godt Enhanced Ecommerce event der passer til det, så det derfor tracker jeg det blot som et normalt Event.

Jeg laver 3 segmenter, som allesammen har en detaljevisning i deres session:

<ol>
<li>Sessioner som kun skimmer</li>
<li>Sessioner som kun læser</li>
<li>Sessioner som både skimmer og læser</li>
</ol>

De tre segmenter kan brydes ned på device og dermed se adfærden.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices.png" alt="Andel der skimmer og læser fordelt på devices" width="1450" height="715" class="size-full wp-image-1919" /></a><figcaption>Andel der skimmer og læser fordelt på devices</figcaption></figure>

<ul>
<li>Der er altså <strong>26% der kun skimmer et blogindlæg</strong>, mens hele <strong>63% læser blogindlægget</strong> uden at skimme det først. Det er overraskende. Jeg havde egentlig forventet at langt flere startede med at skimme og derefter læse, hvis det så spændende ud - fx. masser af billede og ikke bare wall of text. Men det er faktisk kun 11% der først skimmer og derefter læser indlægget.</li>
<li>Det er dem som scroller helt til bunden inden der er gået et minut, og derefter bliver på siden og stadig er aktive (dvs. scroller) når der er gået et minut.</li>
<li>Det er derimod ikke overraskende at der er næsten <strong>dobbelt så mange der skimmer på desktop</strong> i forhold til mobile devices, da det er meget nemmere at scrolle ned i bunden på en desktop, fx med scroll-hjulet på musen eller "page down"-tasten. Det er lidt tungere at scrolle et langt indlæg igennem med swipe på en telefon.</li>
</ul>

<h2>Bliver lange blogindlæg læst mere end korte blogindlæg?</h2>

I <code>Product Performance</code> rapporten kan du se <code>Average price</code> og <code>But-to-detail rate</code>. Med de to tal kan du se sammenhængen mellem blogindlæggets længde (prisen) og sandsynligheden for at det bliver læst.

Du plotter tallene på et Scatter Plot i Excel og tilføjer en trendlinje, som viser sammenhængen.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering.png"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering.png" alt="Korrelationen mellem pris og konvertering er -0,32" width="1023" height="703" class="size-full wp-image-1922" /></a><figcaption>Korrelationen mellem pris og konvertering er -0,32</figcaption></figure>

Trendlinjen viser en tydelig nedadgående sammenhæng mellem pris og konvertering, så jo længere blogindlægget er, jo mindre sandsynlighed er der for at det bliver læst til ende.

<h3>Antal ord i buckets</h3>

Du kan også inddele blogindlæggene i buckets af antal ord, fx 0-500, 501-1000, etc. og finde den optimale længde på et blogindlæg hvor brugerne oftest læser det hele.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord-860x513.jpg" alt="" width="860" height="513" class="alignnone size-large wp-image-2121" /></a>

Overraskende nok er det de helt korte indlæg på mindre end 500 ord hvor færrest læser det hele. Der er et sweetspot omkring 500-1500 ord og ligesom det ses i ovenstående Scatter Plot, så falder fastholdelsen i de lange indlæg.

<h2>Der er STOR forskel på blogindlæg</h2>

Okay, lad os kigge på mine to seneste blogindlæg som eksempler.

Baseret på antal pageviews er de cirka lige populære.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-pageviews.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-pageviews.jpg" alt="" width="637" height="371" class="alignnone size-full wp-image-2110" /></a>

Men pageviews er bare en vanity metric. Den fortæller intet om kvaliteten eller evnen til at fastholde brugeren.

Og de to blogindlæg er meget forskellige.

<ul>
<li><a href="https://www.jacobworsoe.dk/returvarer-google-analytics/">Tracking af returvarer i Google Analytics (den ultimative guide 2019)</a> er en inspiration, men også noget som er en reference til senere brug og den er på 3668 ord.</li>
<li><a href="https://www.jacobworsoe.dk/aws-iot-button-google-analytics/">Tracking af kaffeforbrug med AWS IoT Button og Google Analytics</a> er en sjov use-case for Google Analytics, den er rimelig letlæst og man skal læse (eller skimme) det hele for at den er sjov. Den er kun på 1571 ord.</li>
</ul>

<h3>Buy-to-Detail Rate</h3>

Den store forskel på de to blogindlæg ses tydeligt i Buy-to-Detail rate som er 11,69% for returvarer-indlægget mens den er hele 46,26% på AWS IoT-indlægget!

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail-860x230.jpg" alt="" width="860" height="230" class="alignnone size-large wp-image-2113" /></a>

Dvs. næsten halvdelen af alle dem som ser indlægget om AWS scroller helt til bunden og er mindst 1 minut på siden.

Men hvornår falder folk fra på returvarer-indlægget?

Men hey! Tabeller med rå data er måske fede for data scientists, men de dur ikke til at gøre data nemme at forstå. Så lad os lige lave en graf inden vi går videre.

<figure><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg-860x437.jpg" alt="Fastholdelse af brugeren i et blogindlæg" width="860" height="437" class="size-large wp-image-2112" /></a><figcaption>Fastholdelse af brugeren i et blogindlæg</figcaption></figure>

Meget bedre.

Herover ses en tydelig forskel hvor mange brugere på returvarer-indlægget starter med at scrolle (Add to cart) men meget få læser ned til 33% af indlægget (Checkout). Så de fleste har lige skimmet toppen og (forhåbentlig) bogmærket siden og så videre til andre ting.

På kaffe-indlægget er der slet ikke samme frafald, så det indlæg fastholder brugerne meget bedre. Det er godt at vide til fremtiden.

<h2>Blog kategorier</h2>

Der er også kæmpe forskel i fastholdelse af brugerne fordelt på kategorier. Indlæg om <a href="https://www.jacobworsoe.dk/category/nethandel/">Nethandel</a> bliver læst meget.

Heldigvis bliver mine indlæg om <a href="https://www.jacobworsoe.dk/category/webanalyse/">Webanalyse</a>, som jeg lægger meget arbejde i, også læst meget, hvor 24% læser hele indlægget.

Til gengæld skal jeg vidst tage mig lidt sammen, når jeg skriver om <a href="https://www.jacobworsoe.dk/category/seo/">SEO</a>, som umiddelbart ikke er så interessante indlæg. Her har jeg også lige taget <a href="https://www.jacobworsoe.dk/category/hverdagsstatistik/">Hverdagsstatisk</a> med, som er mit indlæg om <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">drikkevarer til et bryllup</a>.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier-860x597.jpg" alt="" width="860" height="597" class="alignnone size-large wp-image-2117" /></a>

<h2>Udgivelsesår</h2>

Jeg skrev mit første blogindlæg på denne blog i 2009 og jeg har skrevet 35 indlæg i alt. Lad os se om jeg er blevet bedre til at skrive spændende indlæg igennem årene.

<a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår.jpg"><img src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår-860x502.jpg" alt="" width="860" height="502" class="alignnone size-large wp-image-2119" /></a>

Jeg startede ret godt ud i 2009 og 2010 og havde derefter nogle knap så gode år, særligt 2014-2017. Men 2018 og 2019 har begge været rigtig gode år, så jeg skal vidst bare fortsætte med den type indlæg.

<h2>Opsummering</h2>

I det ovenstående har jeg gennemgået step-by-step hvordan jeg bruger Enhanced Ecommerce til at få et langt mere detaljeret billede af hvordan mit indhold performer.

Ikke bare vanity metrics, som pageviews, bounce rate og time on page.

Men metrics som viser præcist hvad brugerne gør på sitet, hvor lang tid de (korrekte) er på siden, samt hvor meget af indholdet de læser.

<h2>Hvor mange procent tror du læser dette indlæg?</h2>

Smid dit svar herunder og deltag i lodtrækning om en... ej pjat, du kan ikke vinde noget, men giv gerne et bud alligevel :)