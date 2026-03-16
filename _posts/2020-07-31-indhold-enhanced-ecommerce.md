---
layout: post
title: Tracking af indhold med Enhanced Ecommerce
date: 2020-07-31 23:33:15
slug: indhold-enhanced-ecommerce
categories:
  - Analytics
---

<p>Hvilke KPI&#8217;er er vigtige for en blog?</p>
<p>Antal månedlige besøg er vigtig.</p>
<p>Trafik fordelt på kanaler er også vigtig at vide. Og måske også om de besøgende tilmelder sig nyhedsbrevet.</p>
<h3>Men hvordan måles konvertering?</h3>
<p>Man kan tracke når nogen skriver en kommentar. Men da diskussionen i høj grad er flyttet over til de sociale medier hvor indlægget deles, så er det ikke et godt mål for konvertering på en blog. Siden jeg startede min blog i 2009 har jeg til dato haft 118.121 besøg og 482 kommentarer, hvilket giver en konverteringsrate på 0,4%.</p>
<p>Det kan også være tilmelding til RSS feed, men selvom det er min foretrukne måde at holde mig opdateret med en lang række blogs, så har jeg på fornemmelsen, at det er meget få der bruger det. Det samme med nyhedsbreve for blogs.</p>
<p>Endelig er der metrics som bounce rate og time on page. Men de er svære at konkludere noget ud fra isoleret set. Jeg har en bounce rate på 85% på dette site. Det er højt, men det betyder ikke nødvendigvis at mine blogindlæg ikke bliver læst grundigt. Det kan sagtens være brugerne er på sitet mange minutter og stadig bouncer. Det betyder bare at de kun læser ét blogindlæg.</p>
<div id="attachment_2300" style="width: 896px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2300" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent.jpg" alt="85% bounce rate." width="886" height="286" class="size-full wp-image-2300" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent.jpg 886w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent-690x223.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent-768x248.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Bounce-rate-på-85-procent-860x278.jpg 860w" sizes="auto, (max-width: 886px) 100vw, 886px" /></a><p id="caption-attachment-2300" class="wp-caption-text">85% bounce rate.</p></div>
<p>Time on page bliver ikke målt på den sidste side i et besøg, så med en bounce rate på 85% er det sjældent den bliver målt. Den metric er også farlig at konkludere noget ud fra, da brugeren ikke nødvendigvis forlader siden, men fx blot loader en ny side i en anden tab.</p>
<h2 id="article-header-id-0">Bliver indholdet rent faktisk læst?</h2>
<p>Selvom det er fedt med mange besøg og sidevisninger, så siger det ikke i sig selv noget om kvaliteten af indholdet. Det er vigtigt at vide om brugerne rent faktisk læser indlægget.</p>
<p>Og det er lige præcis den form for konvertering der er vigtig for en blog, så i dette indlæg viser jeg hvordan jeg bruger Google Analytics Enhanced Ecommerce til at tracke mit indhold og den verden af nye indsigter det åbner op for.</p>
<h2 id="article-header-id-1">Inspireret af Simo Ahava</h2>
<p>Jeg elsker at finde nye kreative måder at bruge Google Analytics og Enhanced Ecommerce til at indsamle data og få et nyt indblik i alt fra websites til den fysiske verden.</p>
<p>Det gør Simo Ahava også og mit tracking setup er også kraftigt inspireret af det setup han har lavet på sin egen blog og skrevet om her: <a href="https://www.simoahava.com/analytics/track-content-enhanced-ecommerce/" rel="noopener noreferrer">Track Content With Enhanced Ecommerce</a></p>
<p>Selve logikken i koden er kopieret fra Simo&#8217;s <a href="https://github.com/sahava/eec-gtm" rel="noopener noreferrer">Github</a> som er baseret på <a href="http://cutroni.com/blog/2014/02/12/advanced-content-tracking-with-universal-analytics/" rel="noopener noreferrer">Justin Cutroni&#8217;s scroll script</a>.</p>
<p>Jeg har derefter omskrevet det til ren JavaScript, så det ikke er afhængigt af jQuery, for at slippe for at skulle loade jQuery på sitet. Jeg brugte den her rigtig meget for at konvertere koden: <a href="http://youmightnotneedjquery.com" rel="noopener noreferrer">youmightnotneedjquery.com</a></p>
<p>Derudover har jeg lavet tre udvidelser af koden:</p>
<ul>
<li>Jeg tracker kun impressions af blogindlæg på forsiden og andre lister, hvis de har været synlige på skærmen</li>
<li>Jeg tracker brugere der kun skimmer artiklen, uden at læse den</li>
<li>Alle data er udstillet i <code class="" data-line="">dataLayer</code> og jeg scraper derfor ikke noget indhold med JavaScript</li>
</ul>
<p>Mere om det senere.</p>
<h2>Tracking af læsning af indhold med Enhanced Ecommerce</h2>
<p>Okay, lad os lige starte med at se på hvordan man overhovedet kan bruge Enhanced Ecommerce til at tracke når brugerne læser indholdet på en blog. Det kræver nemlig at man er lidt kreativ med fortolkningerne af Ecommerce og checkout.</p>
<p>Her er definitionerne af Enhanced Ecommerce, som jeg bruger på min blog:</p>
<ul>
<li><strong>Produkt:</strong> Et blogindlæg.</li>
<li><strong>Produkt navn:</strong> Titlen på blogindlægget.</li>
<li><strong>Produkt pris:</strong> Antal ord i blogindlægget.</li>
<li><strong>Produkt kategori:</strong> WordPress kategori, fx &#8220;Webanalyse&#8221; eller &#8220;SEO&#8221;.</li>
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
<p>På alle sider hvor der vises et eller flere indlæg, skal der trackes en række produktdata for hvert indlæg.</p>
<p>ID og navnet (titlen) på indlægget kan fanges i WordPress i <a href="https://codex.wordpress.org/The_Loop" rel="noopener noreferrer" target="_blank">The Loop</a> med de indbyggede funktioner <code class="" data-line="">the_title()</code> og <code class="" data-line="">the_ID()</code> og gemmes i en JavaScript variabel, så de kan sendes til Google Analytics. Årstallet som gemmes i brand hentes med <code class="" data-line="">the_time(&#039;Y&#039;)</code>.</p>
<p>Et indlæg kan tilhøre flere kategorier og hvis du bruger <a href="https://wordpress.org/plugins/wordpress-seo/" rel="noopener noreferrer" target="_blank">Yoast SEO</a> er der mulighed for at angive en primær kategori. Hvis et indlæg tilhører flere kategorier, bruges kun den primære. Den logik kan kodes således:</p>
<pre><code class="" data-line="">// SHOW YOAST PRIMARY CATEGORY, OR FIRST CATEGORY
$category = get_the_category();
$useCatLink = true;

// If post has a category assigned.
if ($category){
    $category_display = &#039;&#039;;
    $category_link = &#039;&#039;;
    if ( class_exists(&#039;WPSEO_Primary_Term&#039;) )
    {
        // Show the post&#039;s &#039;Primary&#039; category, if this Yoast feature is available, &amp; one is set
        $wpseo_primary_term = new WPSEO_Primary_Term( &#039;category&#039;, get_the_id() );
        $wpseo_primary_term = $wpseo_primary_term-&gt;get_primary_term();
        $term = get_term( $wpseo_primary_term );
        if (is_wp_error($term)) { 
            // Default to first category (not Yoast) if an error is returned
            $category_display = $category[0]-&gt;name;
            $category_link = get_category_link( $category[0]-&gt;term_id );
        } else { 
            // Yoast Primary category
            $category_display = $term-&gt;name;
            $category_link = get_category_link( $term-&gt;term_id );
        }
    } 
    else {
        // Default, display the first category in WP&#039;s list of assigned categories
        $category_display = $category[0]-&gt;name;
        $category_link = get_category_link( $category[0]-&gt;term_id );
    }

    // Display category
    if ( empty($category_display) ) {
        $category_display = &quot;Ingen kategori&quot;;
    }   
}
</code></pre>
<p>Derefter udskrives kategorien med <code class="" data-line="">&lt;?php echo $category_display; ?&gt;</code>.</p>
<p>Prisen er antal ord og der har PHP en indbygget funktion <code class="" data-line="">str_word_count</code> som tæller antal ord i en streng &#8211; i dette tilfælde den aktuelle artikel. Jeg har lagt det i en funktion i <code class="" data-line="">functions.php</code> så jeg nemt kan kalde den med word_count() i <code class="" data-line="">single.php</code>.</p>
<pre><code class="" data-line="">function word_count() {
    $content = get_post_field( &#039;post_content&#039;, $post-&gt;ID );
    $word_count = str_word_count( strip_tags( $content ) );
    return $word_count;
}
</code></pre>
<p>I Enhanced Ecommerce er det vigtigt at produktdata er formateret med præcis den rigtige syntaks &#8211; ellers vil der ikke blive sendt nogen produktdata til Google Analytics for dét request. Det færdige <code class="" data-line="">Product</code> object med den korrekte syntaks ser således ud:</p>
<pre><code class="" data-line="">var product = [{
    name: &#039;&lt;?php the_title(); ?&gt;&#039;,
    id: &#039;&lt;?php the_ID(); ?&gt;&#039;,
    price: &#039;&lt;?php echo word_count(); ?&gt;&#039;,
    brand: &#039;&lt;?php the_time(&#039;Y&#039;) ?&gt;&#039;,
    category: &#039;&lt;?php echo $category_display; ?&gt;&#039;,
    variant: &#039;&#039;,
    quantity: 1
  }];
</code></pre>
<h2>Product impressions efter 2 sekunder</h2>
<p>Det første trin i kunderejsen er product impressions på en produktliste.</p>
<p>Der vises lister af blogindlæg på forsiden, kategorisider, som relaterede indlæg, etc. Der er primært to ting der er vigtige når der trackes impressions.</p>
<ol>
<li>Der skal kun trackes impressions af blogindlæg som brugeren rent faktisk har set. Det er ikke nok at linket til  blogindlægget har været længere nede på siden (below the fold), eller at brugeren har scrollet lynhurtigt forbi det. Brugeren skal have set blogindlægget og jeg skal være rimelig sikker på at brugeren har set og forholdt sig til det.</p>
</li>
<li>
<p>Trackingen må ikke sløve brugerens computer og gøre sitet langsomt. Når jeg skal holde øje med hvor langt brugeren scroller ned af siden og dermed om et givent blogindlæg er blevet synligt på skærmen, kan jeg nemt risikere at der skal køres noget JavaScript kode meget ofte, især hvis brugeren scroller hurtigt ned over siden. Dette kan påvirke hvor gnidningsfrit scrollet opleves for brugeren.</p>
</li>
</ol>
<p>I værste fald kan det gøre sitet ubrugeligt, som det <a href="https://johnresig.com/blog/learning-from-twitter/" rel="noopener noreferrer" target="_blank">skete for Twitter tilbage i 2011</a>.</p>
<blockquote><p>Depending upon the browser the scroll event can fire a lot and putting code in the scroll callback will slow down any attempts to scroll the page (not a good idea). Instead it’s much better to use some form of a timer to check every X milliseconds OR to attach a scroll event and only run your code after a delay.<cite><a href="https://johnresig.com/blog/learning-from-twitter/" target="_blank" rel="noopener noreferrer">John Resig, skaberen af jQuery</a></cite></p>
</blockquote>
<p><strong>Begge ting kan løses med en debounce funktion.</strong></p>
<p>En debounce funktion siger: “Udfør denne kode når noget ikke er sket i X antal millisekunder”.</p>
<p><a href="https://css-tricks.com/debouncing-throttling-explained-examples/" rel="noopener noreferrer" target="_blank">Denne artikel fra CSS-Tricks.com</a> har nogle gode visualiseringer og demoer som viser hvordan debounce virker. David Walsh har også <a href="https://davidwalsh.name/javascript-debounce-function" rel="noopener noreferrer" target="_blank">skrevet om det her</a>.</p>
<div id="attachment_2328" style="width: 671px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/css-tricks-debounce.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2328" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/css-tricks-debounce.png" alt="Kilde: CSS-Tricks.com" width="661" height="133" class="size-full wp-image-2328" /></a><p id="caption-attachment-2328" class="wp-caption-text">Kilde: <a href="https://css-tricks.com/debouncing-throttling-explained-examples/">CSS-Tricks.com</a></p></div>
<p>I dette tilfælde køres koden når brugeren stopper med at scrolle i 2 sekunder. Hvis brugeren scroller igen inden de 2 sekunder er gået, nulstilles timeren og når brugeren stopper med at scrolle, starter timeren igen fra 0 og hvis der går 2 sekunder uden scroll, udføres koden.</p>
<p>Og sidst men ikke mindst skal der kun trackes impressions for et produkt én gang på hver side.</p>
<p>Lad os kigge på koden.</p>
<p>Først er der lavet tre funktioner. Den første tjekker om et element er synligt på skærmen.</p>
<pre><code class="" data-line="">function checkVisible(elm) {
  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
  return !(rect.bottom &lt; 0 || rect.top - viewHeight &gt;= 0);
}   
</code></pre>
<p class="attention"><strong>Bemærk!</strong> Jeg lavede dette tilbage i 2016. Hvis det skal laves i dag, kan du med fordel bruge <a href="https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API">Intersection Observer</a> som er et asynkront API til netop at holde øje med hvornår elementer bliver synlige i viewport og den kan også holde styr på hvilke der har været synlige, så man ikke selv skal sørge for at de ikke tracker flere gange. <a href="https://caniuse.com/#feat=intersectionobserver">Browser support</a> er rigtig god i dag, så den bør bruges fremover.
</p>
<p>Den næste laver et Enhanced Ecommerce product object med de relevante produktdata for et blogindlæg som er synligt på skærmen.</p>
<pre><code class="" data-line="">function pushProducts(productElement, i) {
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
<p>Produktdataene er placeret i data attributter i HTML koden.</p>
<pre><code class="" data-line="">&lt;h1 class=&quot;home-post-headline&quot;&gt;
    &lt;a href=&quot;https://www.jacobworsoe.dk/returvarer-google-analytics/&quot; 
        data-title=&quot;Tracking af returvarer i Google Analytics (den ultimative guide)&quot; 
        data-id=&quot;1597&quot; 
        data-category=&quot;Webanalyse&quot; 
        data-year=&quot;2019&quot; 
        data-author=&quot;2&quot; 
        data-price=&quot;3668&quot; 
        data-position=&quot;2&quot;
        class=&quot;home-post-link&quot;&gt;
        Tracking af returvarer i Google Analytics (den ultimative guide)            
    &lt;/a&gt;
&lt;/h1&gt;
</code></pre>
<p>Den tredje funktion sender impressions til Google Analytics.</p>
<pre><code class="" data-line="">function sendProducts(trigger) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    event: trigger,
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}</code></pre>
<p>Ved pageload bygges et JavaScript <code class="" data-line="">object</code> med sidens blogindlæg og der checkes om nogle af sidens blogindlæg er synlige, dvs. dem som er above-the-fold. De synlige blogindlæg pushes til products objectet med <code class="" data-line="">pushProducts()</code>.</p>
<p>Hvis der er blogindlæg som ikke er synlige, tilføjes de til <code class="" data-line="">ga_products_not_visible</code> objectet som vi derefter kan holde øje med om de bliver synlige i 2 sekunder og tracke en impression for dem.</p>
<pre><code class="" data-line="">// Cache product element
var articles = document.querySelectorAll(&quot;.home-post-headline a&quot;);

// See if products are in view
if (articles &amp;&amp; articles.length &gt; 0) {
  for (var i = 0; i &lt; articles.length; i++) {
    if (checkVisible(articles[i])) {
      pushProducts(articles, i);
    } else {
      ga_products_not_visible.push(articles[i]);
    }
  }
}</code></pre>
<p>Hvis der var nogle synlige blogindlæg, pushes de til dataLayer, så de bliver sendt med, sammen med pageview requestet for siden.</p>
<pre><code class="" data-line="">// If any products was in view on pageload, send those products
if (ga_products.length &gt; 0) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}</code></pre>
<p>Okay, nu har vi styr på blogindlæg som er above-the-fold. Nu skal vi tracke impressions for dem som er below-the-fold.</p>
<p>Fordi det kan være lidt tungt at tracke på scroll, så skal det kun gøres hvis der rent faktisk er nogle produkter below-the-fold, så det starter vi med at tjekke med <code class="" data-line="">ga_products_not_visible.length</code>.</p>
<p>Derefter defineres en funktion som køres hver gang der scrolles.</p>
<p>Det første funktionen gør, når der scrolles er <code class="" data-line="">clearTimeout</code> som nulstiller timeren.</p>
<p>Derefter startes en ny <code class="" data-line="">setTimeout</code> som indeholder den kode som køres efter 2000 millisekunder.</p>
<p>Når de 2000 millisekunder er gået udføres koden, som tjekker om nogle af de blogindlæg der endnu ikke er tracket en impression af, er synlige på skærmen. Hvis det er tilfældet bliver de tilføjet til products objectet og fjernet fra listen over blogindlæg der ikke er tracker en impression for, så de ikke kan trackes igen. Til sidst sendes de til Google Analytics med et event.</p>
<p><strong>Men!</strong> Hvis der scrolles inden de 2000 millisekunder er gået, så køres hele koden igen og det første i koden er at nulstille timeren og starte den på ny som beskrevet herover.</p>
<p>Dette er “magien” bag en debounce funktion. Den sørger for at koden ikke afvikles med det samme der scrolles, men først efter en pause på 2000 millisekunder, hvilket både gør sitet mere flydende, men også sikrer at brugeren skal stoppe med at scrolle i 2000 millisekunder (og dermed formentlig har vurderet om de vil klikke på linket) før vi tracker en impression.</p>
<pre><code class="" data-line="">// If page contained products not in view, start the scroll tracker
if (ga_products_not_visible.length &gt; 0) {
  var scrollTimeout;

  function checkProductsInViewOnScroll() {
    clearTimeout(scrollTimeout);

    scrollTimeout = setTimeout(function() {
      for (var i = ga_products_not_visible.length - 1; i &gt;= 0; i--) {
        if (checkVisible(ga_products_not_visible[i])) {
          pushProducts(ga_products_not_visible, i);

          // Remove the product in view from ga_products_not_visible
          ga_products_not_visible.splice(i, 1);
        }
      }

      if (ga_products.length &gt; 0) {
        sendProducts(&quot;moreImpressionsSent&quot;);
      }
    }, 2000);
  }

  // Start scroll listener
  window.addEventListener(&quot;scroll&quot;, checkProductsInViewOnScroll);
}</code></pre>
<p>Her er den samlede kode til at tracke impressions på lister.</p>
<pre><code class="" data-line="">// Set objects to store posts
window.ga_products = window.ga_products || [];
window.ga_products_not_visible = window.ga_products_not_visible || [];

function checkVisible(elm) {
  var rect = elm.getBoundingClientRect();
  var viewHeight = Math.max(
    document.documentElement.clientHeight,
    window.innerHeight
  );
  return !(rect.bottom &lt; 0 || rect.top - viewHeight &gt;= 0);
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
var articles = document.querySelectorAll(&quot;.home-post-headline a&quot;);

// See if products are in view
if (articles &amp;&amp; articles.length &gt; 0) {
  for (var i = 0; i &lt; articles.length; i++) {
    if (checkVisible(articles[i])) {
      pushProducts(articles, i);
    } else {
      ga_products_not_visible.push(articles[i]);
    }
  }
}

// If any products was in view on pageload, send those products
if (ga_products.length &gt; 0) {
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    ecommerce: {
      impressions: window.ga_products
    }
  });
  window.ga_products = [];
}

// If page contained products not in view, start the scroll tracker
if (ga_products_not_visible.length &gt; 0) {
  var scrollTimeout;

  function checkProductsInViewOnScroll() {
    clearTimeout(scrollTimeout);

    scrollTimeout = setTimeout(function() {
      for (var i = ga_products_not_visible.length - 1; i &gt;= 0; i--) {
        if (checkVisible(ga_products_not_visible[i])) {
          pushProducts(ga_products_not_visible, i);

          // Remove the product in view from ga_products_not_visible
          ga_products_not_visible.splice(i, 1);
        }
      }

      if (ga_products.length &gt; 0) {
        sendProducts(&quot;moreImpressionsSent&quot;);
      }
    }, 2000);
  }

  // Start scroll listener
  window.addEventListener(&quot;scroll&quot;, checkProductsInViewOnScroll);
}
</code></pre>
<p>Antal impressions falder dermed jo længere ned på forsiden man kommer og de første to positioner har stort set samme antal impressions, da de er above-the-fold, både på mobile og desktop.</p>
<div id="attachment_2315" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2315" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden-860x477.png" alt="Impressions fordelt på positioner på forsiden." width="860" height="477" class="size-large wp-image-2315" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden-860x477.png 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden-690x383.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden-768x426.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Impressions-fordelt-på-positioner-på-forsiden.png 1163w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2315" class="wp-caption-text">Impressions fordelt på positioner på forsiden.</p></div>
<h2>Produkt click med et callback</h2>
<p>Når brugeren klikker på et blogindlæg, skal klikket trackes. Udfordringen er at siden skifter når man klikker og derfor er der risiko for at requestet ikke når at blive sendt til Google Analytics, før siden er skiftet og dermed bliver det aldrig sendt.</p>
<p>Løsningen er at annullere sideskiftet med JavaScript og istedet få GTM til at <a href="https://www.simoahava.com/gtm-tips/hitcallback-eventcallback/" rel="noopener noreferrer" target="_blank">lave sideskiftet i et callback</a> efter requestet er succesfuldt sendt til Google Analytics.</p>
<p>Der er særligt to ting der er vigtige at tage højde for når man annullerer et sideskift.</p>
<ol>
<li>Hvis requestet til Google Analytics fejler eller GTM ikke bliver loaded korrekt på siden, kan det betyde at sideskiftet aldrig bliver lavet.</p>
</li>
<li>
<p>Hvis brugeren holder CTRL (eller CMD på Mac) nede mens der klikkes på linket for at åbne det i en ny tab, skal der ikke laves et sideskift, da brugeren jo netop gerne vil blive på siden.</p>
</li>
</ol>
<p>Den første kan løses ved at lave et <a href="https://www.simoahava.com/gtm-tips/use-eventtimeout-eventcallback/" rel="noopener noreferrer" target="_blank">timeout på fx 2 sekunder</a>, så sideskiftet bliver lavet uanset hvad, hvis requestet til Google Analytics ikke er gennemført efter 2 sekunder.</p>
<p>Den anden kan løses ved at tjekke om click eventet har enten <code class="" data-line="">event.ctrlKey</code> (Windows) eller <code class="" data-line="">event.metaKey</code> (Mac) for at tjekke om brugeren holder CTRL/CMD nede mens der klikkes.</p>
<p>Alt logikken tilføjes til det <code class="" data-line="">dataLayer.push</code> som udføres når brugeren klikker på et blogindlæg på en liste, fx forsiden.</p>
<pre><code class="" data-line="">dataLayer.push({
  event: &quot;productClick&quot;,
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
    if (!e.ctrlKey &amp;&amp; !e.metaKey) {
      window.location = href;
    }
  },
  eventTimeout: 2000
});
</code></pre>
<h2>Brugbar CTR på produktlister</h2>
<p>Når der er styr på tracking af blogindlæg som har været på brugerens skærm i 2 sekunder, samt kliks, fås en meget mere brugbar CTR for de enkelte blogindlæg på de forskellige lister.</p>
<p>Brugbar fordi jeg ved at brugeren har haft tid til at læse overskriften og vurdere om blogindlægget er spændende og relevant. Det er helt afgørende for at man faktisk kan konkludere noget på baggrund af CTR.</p>
<h2>Brugerne klikker ikke på relaterede og nyeste indlæg</h2>
<p>Jeg har brugt Enhanced Ecommerce til at tracke min blog siden 2016. Da jeg gav bloggen et redesign i starten af 2019 undersøgte jeg hvor mange der klikker, når der vises relaterede indlæg i bunden af et indlæg eller klikker på listen af nyeste blogindlæg.</p>
<div id="attachment_1828" style="width: 1280px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1828" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png" alt="Sidebar med nyeste blogindlæg - men klikker folk på dem?" width="1270" height="526" class="size-full wp-image-1828" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png 1270w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR-690x286.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR-768x318.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR-725x300.png 725w" sizes="auto, (max-width: 1270px) 100vw, 1270px" /></a><p id="caption-attachment-1828" class="wp-caption-text">Sidebar med nyeste blogindlæg &#8211; men klikker folk på dem?</p></div>
<div id="attachment_1829" style="width: 951px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1829" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg.png" alt="I bunden af alle blogindlæg vises links til relaterede blogindlæg." width="941" height="595" class="size-full wp-image-1829" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg.png 941w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg-690x436.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg-768x486.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Relaterede-blogindlæg-725x458.png 725w" sizes="auto, (max-width: 941px) 100vw, 941px" /></a><p id="caption-attachment-1829" class="wp-caption-text">I bunden af alle blogindlæg vises links til relaterede blogindlæg.</p></div>
<p>Det gør de ikke.</p>
<p>Slet ikke.</p>
<div id="attachment_1830" style="width: 1104px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1830" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png" alt="CTR på 0,05% og 0,42% viser at meget få klikker på de links." width="1094" height="485" class="size-full wp-image-1830" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png 1094w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg-690x306.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg-768x340.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg-725x321.png 725w" sizes="auto, (max-width: 1094px) 100vw, 1094px" /></a><p id="caption-attachment-1830" class="wp-caption-text">CTR på 0,05% og 0,42% viser at meget få klikker på de links.</p></div>
<p>Bemærk de meget forskellige antal impressions. Som beskrevet ovenfor tracker jeg kun impressions når links er synlige på skærmen og brugeren ikke har scrollet i 2 sekunder.</p>
<p>Nyeste indlæg vises i højre side højt oppe på siden, mens relaterede indlæg vises i bunden af blogindlæg, så der er langt færre der scroller helt ned til dem.</p>
<p>Fordi der er meget få kliks er det svært at optimere ud fra. Men hvis der havde været nogle flere kliks, ville det være oplagt at kigge på hvilke blogindlæg der fungerer godt når de vises som relaterede indlæg:</p>
<div id="attachment_1833" style="width: 900px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1833" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products.png" alt="CTR for de enkelte blogindlæg når de vises som relaterede indlæg." width="890" height="610" class="size-full wp-image-1833" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products.png 890w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products-690x473.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products-768x526.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-products-725x497.png 725w" sizes="auto, (max-width: 890px) 100vw, 890px" /></a><p id="caption-attachment-1833" class="wp-caption-text">CTR for de enkelte blogindlæg når de vises som relaterede indlæg.</p></div>
<p>CTR på de links var dermed så lav, at de for langt de fleste brugere ikke er brugbare links, og dermed blot støj. Jeg valgte derfor at fjerne dem i det nye design og dermed få et mere clean design.</p>
<blockquote><p>Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.<cite>Antoine de Saint-Exupery</cite></p></blockquote>
<p>Til sammenligning har links på forsiden en CTR på 4,92%.</p>
<div id="attachment_1844" style="width: 828px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1844" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden.png" alt="CTR på forsiden." width="818" height="313" class="size-full wp-image-1844" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden.png 818w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden-690x264.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden-768x294.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Product-list-performance-homepage-og-forsiden-725x277.png 725w" sizes="auto, (max-width: 818px) 100vw, 818px" /></a><p id="caption-attachment-1844" class="wp-caption-text">CTR på forsiden.</p></div>
<p>Screenshottet viser i øvrigt en kritisk vigtig ting i Enhanced Ecommerce og analytics generelt: <strong>Konsistent data</strong>.</p>
<p>Da jeg redesignede bloggen omskrev jeg alt JavaScript fra bunden, så det var skrevet i ren JavaScript (dvs. uden jQuery) og samtidig fulgte <a href="https://css-tricks.com/how-do-you-structure-javascript-the-module-pattern-edition/" rel="noopener noreferrer" target="_blank">den samme gode kodestruktur</a>.</p>
<p>Det betød desværre at jeg kom til at omdøbe Forsidens <code class="" data-line="">product list name</code> fra Forsiden til homepage og dermed er data nu splittet.</p>
<p>Doh!</p>
<p>Lesson learned.</p>
<h2>Produkt detaljevisning, add to cart og checkout</h2>
<p>Okay, nu skal vi videre ned gennem tragten. Næste skridt fra <code class="" data-line="">product click</code> er <code class="" data-line="">detail view</code>. Nu gennemgår jeg alt det der sker på et blogindlæg.</p>
<p>Når et blogindlæg vises starter jeg med at sætte en række variabler, som bruges til at styre scroll trackingen. Der sættes det samme scrollTimeout på 2000 millisekunder som ved impressions og jeg sætter at brugeren mindst skal scrolle 150 pixels før de er begyndt at læse indlægget.</p>
<p>Derefter sættes en variabel til <code class="" data-line="">false</code> for hvert event/state ned gennem siden. Når brugeren scroller til et punkt affyres et event og det sættes derefter til <code class="" data-line="">true</code> så det samme event ikke trackes igen, hvis brugeren scrolle op igen.</p>
<p>Derefter vælges den <code class="" data-line="">div</code> som indeholder blogindlægget, så jeg kan måle højden på den <code class="" data-line="">div</code> og holde øje med hvor langt brugeren scroller. Bemærk at kommentarerne under indlægget ikke er med i denne <code class="" data-line="">div</code>, så det er kun selve indlægget jeg kigger på.</p>
<p>Til sidst gemmes det aktuelle tidspunkt, som bruges til at afgøre hvor længe brugeren har været aktiv på siden.</p>
<pre><code class="" data-line="">// Default time delay before checking location
var scrollTimeout = 2000;

// # px before tracking a reader
var readerLocation = 150;

// Set some flags for tracking &amp; execution
var timer = 0;
var scroller = false;
var oneThird = false;
var twoThirds = false;
var endContent = false;
var didComplete = false;
var purchase = false;

// Content area DIV class
var contentArea = document.querySelector(&quot;.post-content&quot;);

// Set some time variables to calculate reading time
var startTime = new Date();
var beginning = startTime.getTime();
var totalTime = 0;
</code></pre>
<p>Derefter pushes en Enhanced Ecommerce action sat til <code class="" data-line="">detail</code> som sendes med sidevisningen når brugeren lander på blogindlægget. Konsistens er vigtig i Enhanced Ecommerce, så de produktdata der sendes med her, skal være identiske med dem som bruges ved <code class="" data-line="">impressions</code> og <code class="" data-line="">click</code>.</p>
<pre><code class="" data-line="">// Track the article load as a Product Detail View
dataLayer.push({
   ecommerce: {
     detail: {
       products: product
     }
   }
});
</code></pre>
<p>Derefter defineres den funktion som affyres når brugeren ikke har scrollet i 2000 millisekunder.</p>
<pre><code class="" data-line="">// Check the location and track user
function trackLocation() {
  clearTimeout(scrollTimeout);

  scrollTimeout = setTimeout(function() {
// Herinde placeres alt koden som affyres efter 2000 millisekunder

    }
  }, 2000);
}

// Track the scrolling and track location
window.addEventListener(&quot;scroll&quot;, trackLocation);
},
</code></pre>
<p>Når brugeren begynder at scrolle på siden og dermed begynder at læse indholdet, trackes dette med et <code class="" data-line="">add to cart</code> event. Her bruger jeg samme debounce funktion som tidligere, sat til 2 sekunder.</p>
<pre><code class="" data-line="">scrollTimeout = setTimeout(function() {
    bottom = window.innerHeight + window.pageYOffset;

    // If user starts to scroll send an event
    if (bottom &gt; readerLocation &amp;&amp; !scroller) {
      dataLayer.push({
        event: &quot;addToCart&quot;,
        ecommerce: {
          add: {
            products: product
          }
        }
      });
      scroller = true;          
    }
</code></pre>
<p>Når brugeren lander på siden måles højden på artiklen i pixels, som bruges til at tracke hvor meget af artiklen der læses. Hvis brugeren scroller 33% af artiklen, trackes checkout step 1.</p>
<p>Ved 66% trackes step 2 og ved 100% af artiklen trackes step 3.</p>
<pre><code class="" data-line="">// If one third is reached
if (
  bottom &gt;= contentArea.offsetTop + contentArea.clientHeight / 3 &amp;&amp;
  !oneThird
) {
  dataLayer.push({
    event: &quot;checkout&quot;,
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
  bottom &gt;= contentArea.offsetTop + contentArea.clientHeight / 3 * 2 &amp;&amp;
  !twoThirds
) {
  dataLayer.push({
    event: &quot;checkout&quot;,
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
  bottom &gt;= contentArea.offsetTop + contentArea.clientHeight &amp;&amp;
  (!endContent || !purchase)
) {
  if (!endContent) {
    dataLayer.push({
      event: &quot;checkout&quot;,
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
<p>Hvis brugeren har været på siden mere end 1 minut, når der er scrollet 100% af artiklen, antages det at brugeren har læst artiklen og ikke bare skimmet den og den handling trackes som et køb. Prisen på ordren er antal ord i blogindlægget og dermed kan man se hvor mange artikler og ord der bliver læst på bloggen.</p>
<pre><code class="" data-line="">// If user has reached end of funnel, check if 60 seconds is passed
if (endContent &amp;&amp; !purchase) {
  currentTime = new Date();
  contentScrollEnd = currentTime.getTime();
  timeToContentEnd = Math.round((contentScrollEnd - beginning) / 1000);
  if (timeToContentEnd &gt; 60 &amp;&amp; !purchase) {
    // Track purchase
    dataLayer.push({
      event: &quot;purchase&quot;,
      ecommerce: {
        purchase: {
          actionField: {
            id:
              new Date().getTime() +
              &quot;_&quot; +
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
      event: &quot;scrollToEndBeforeOneMinute&quot;,
      product: product[0].name
    });
  }
}
</code></pre>
<p>Den samlede kode for tracking af læsning af et blogindlæg ser dermed således ud:</p>
<pre><code class="" data-line="">// Track single post as product
trackSinglePostAsProduct: function(product) {
  // Default time delay before checking location
  var scrollTimeout = 2000;

  // # px before tracking a reader
  var readerLocation = 150;

  // Set some flags for tracking &amp; execution
  var timer = 0;
  var scroller = false;
  var oneThird = false;
  var twoThirds = false;
  var endContent = false;
  var didComplete = false;
  var purchase = false;

  // Content area DIV class
  var contentArea = document.querySelector(&quot;.post-content&quot;);

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
      if (bottom &gt; readerLocation &amp;&amp; !scroller) {
        dataLayer.push({
          event: &quot;addToCart&quot;,
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
        bottom &gt;= contentArea.offsetTop + contentArea.clientHeight / 3 &amp;&amp;
        !oneThird
      ) {
        dataLayer.push({
          event: &quot;checkout&quot;,
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
        bottom &gt;= contentArea.offsetTop + contentArea.clientHeight / 3 * 2 &amp;&amp;
        !twoThirds
      ) {
        dataLayer.push({
          event: &quot;checkout&quot;,
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
        bottom &gt;= contentArea.offsetTop + contentArea.clientHeight &amp;&amp;
        (!endContent || !purchase)
      ) {
        if (!endContent) {
          dataLayer.push({
            event: &quot;checkout&quot;,
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
      if (endContent &amp;&amp; !purchase) {
        currentTime = new Date();
        contentScrollEnd = currentTime.getTime();
        timeToContentEnd = Math.round((contentScrollEnd - beginning) / 1000);
        if (timeToContentEnd &gt; 60 &amp;&amp; !purchase) {
          // Track purchase
          dataLayer.push({
            event: &quot;purchase&quot;,
            ecommerce: {
              purchase: {
                actionField: {
                  id:
                    new Date().getTime() +
                    &quot;_&quot; +
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
            event: &quot;scrollToEndBeforeOneMinute&quot;,
            product: product[0].name
          });
        }
      }
    }, 2000);
  }

  // Track the scrolling and track location
  window.addEventListener(&quot;scroll&quot;, trackLocation);
},
</code></pre>
<p>Dataene kan blandt andet ses i Product Performance rapporten.</p>
<div id="attachment_2329" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2329" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance-860x452.jpg" alt="Top 10 mest læste blogindlæg og deres gennemsnitspris (antal ord)." width="860" height="452" class="size-large wp-image-2329" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance-860x452.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance-690x363.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance-768x403.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Product-performance.jpg 1380w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2329" class="wp-caption-text">Top 10 mest læste blogindlæg og deres gennemsnitspris (antal ord).</p></div>
<h2>Analyse af Ecommerce data for min blog</h2>
<p>Okay, lad os kigge på det data jeg kan få ud af alt det her.</p>
<h3>Shopping behaviour</h3>
<p>En af de fedeste rapporter i Enhanced Ecommerce er Shopping Behaviour, som viser en komplet funnel over hele websitet fra total antal sessioner til antal køb.</p>
<p>Her ses frafaldet i hvert step mod læste blogindlæg.</p>
<div id="attachment_1926" style="width: 1566px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1926" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour.png" alt="Shopping behaviour" width="1556" height="724" class="size-full wp-image-1926" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour.png 1556w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour-690x321.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour-768x357.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Shopping-behaviour-725x337.png 725w" sizes="auto, (max-width: 1556px) 100vw, 1556px" /></a><p id="caption-attachment-1926" class="wp-caption-text">Shopping behaviour</p></div>
<p>Jeg kan se at en stor del af de besøgende ser blogindlæg (faktisk hele 96%) og rigtige mange begynder at scrolle (add to cart). 85% af dem der scroller når også ned til den første 1/3 af indlægget (checkout) men kun 20% af dem læser et blogindlæg. Der er et stort frafald på det sidste step.</p>
<p>Det kigger vi lige nærmere på med <code class="" data-line="">Checkout behaviour</code>.</p>
<div id="attachment_1927" style="width: 1295px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1927" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour.png" alt="Checkout behaviour" width="1285" height="719" class="size-full wp-image-1927" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour.png 1285w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour-690x386.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour-768x430.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Checkout-behaviour-725x406.png 725w" sizes="auto, (max-width: 1285px) 100vw, 1285px" /></a><p id="caption-attachment-1927" class="wp-caption-text">Checkout behaviour</p></div>
<p>Antal sessioner bliver cirka halveret i hvert step, men dog er 78% af dem som scroller helt til bunden også på siden længe nok, til at de læser blogindlægget og tracket som et køb.</p>
<h3>Ekskludering af irrelevante blogindlæg</h3>
<p>Mit mest besøgte blogindlæg er uden sammenligning min <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">infografik over hvor meget der blev drukket til vores bryllup</a>.</p>
<div id="attachment_1887" style="width: 833px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1887" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart.png" alt="Mest besøgte sider siden 2009." width="823" height="415" class="size-full wp-image-1887" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart.png 823w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart-690x348.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart-768x387.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Mest-viste-sider-GDS-chart-725x366.png 725w" sizes="auto, (max-width: 823px) 100vw, 823px" /></a><p id="caption-attachment-1887" class="wp-caption-text">Mest besøgte sider siden 2009.</p></div>
<p>Jeg har brugt Enhanced Ecommerce til at tracke min blog siden december 2016 og siden da har den infografik stået for 77% af alle sidevisninger.</p>
<div id="attachment_1888" style="width: 751px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1888" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016.png" alt="Infografikken står for 77% af alle sidevisninger på sitet." width="741" height="351" class="size-full wp-image-1888" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016.png 741w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016-690x327.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/drinksregnskab-77-procent-sidevisninger-siden-2016-725x343.png 725w" sizes="auto, (max-width: 741px) 100vw, 741px" /></a><p id="caption-attachment-1888" class="wp-caption-text">Infografikken står for 77% af alle sidevisninger på sitet.</p></div>
<p>Målgruppen og adfærden på det blogindlæg er markant anderledes end de andre blogindlæg jeg skriver om digital marketing, så derfor udelukker jeg den med et segment, i alle de nedenstående analyser.</p>
<h3>Top 10 blogindlæg</h3>
<p>Herunder ses top 10 blogindlæg baseret på sidevisninger (detail views) samt deres Buy-to-Detail Rate.</p>
<p>Eller sagt på en anden måde: En vanity metric mod en engagement metric.</p>
<p>Bemærk de kæmpe forskelle i engagement!</p>
<div id="attachment_2331" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2331" src="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate-860x380.jpg" alt="Der er kæmpe forskel på hvor mange der rent faktisk læser blogindlæggene." width="860" height="380" class="size-large wp-image-2331" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate-860x380.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate-690x305.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate-768x339.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2020/07/Top-10-blogposts-buy-to-detail-rate.jpg 1696w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2331" class="wp-caption-text">Der er kæmpe forskel på hvor mange der rent faktisk læser blogindlæggene.</p></div>
<h3>Konverteringsrate pr. trafikkilder</h3>
<p>Med infografikken fjernet, kan jeg se om besøg fra forskellige kilder egentlig læser mine blogindlæg.</p>
<p>Gennemsnittet for sitet er en konverteringsrate på 26,58% hvilket vil sige at 27% af trafikken læser mindst ét blogindlæg. Det er jeg egentlig godt tilfreds med.</p>
<ul>
<li>Organisk trafik har en konvertering på 24,33% dvs. tæt på gennemsnittet.</li>
<li>Social er høj hvor 34% læser blogindlægget når det bliver delt.</li>
<li>E-mail er ekstremt høj hvor 43% læser blogindlægget. Næsten dobbelt så højt som gennemsnittet. Jeg sender kun e-mails ud, når jeg skriver nye blogindlæg, så det giver god mening at folk kun klikker på links i de e-mails, hvis de synes blogindlægget ser spændende ud. Men alligevel :)</li>
</ul>
<div id="attachment_1893" style="width: 1286px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1893" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping.png" alt="Konvertering fordelt på trafikkilder." width="1276" height="511" class="size-full wp-image-1893" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping.png 1276w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping-690x276.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping-768x308.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Konvertering-for-default-channel-grouping-725x290.png 725w" sizes="auto, (max-width: 1276px) 100vw, 1276px" /></a><p id="caption-attachment-1893" class="wp-caption-text">Konvertering fordelt på trafikkilder.</p></div>
<p>Lad os først lige kigge nærmere på social og de posts jeg selv laver, når jeg har skrevet et nyt blogindlæg.</p>
<div id="attachment_1892" style="width: 1278px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1892" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts.png" alt="Konvertering er markant højere end gennemsnittet på 27%." width="1268" height="351" class="size-full wp-image-1892" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts.png 1268w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts-690x191.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts-768x213.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Source-medium-sociale-posts-725x201.png 725w" sizes="auto, (max-width: 1268px) 100vw, 1268px" /></a><p id="caption-attachment-1892" class="wp-caption-text">Konvertering er markant højere end gennemsnittet på 27%.</p></div>
<p>Konverteringen her er markant højere end gennemsnittet på 27% men det er interessant at facebook konvertere lavere end de andre. Jeg poster typisk kun i <a href="https://www.facebook.com/groups/googleanalytics/" rel="noopener noreferrer" target="_blank">Analytics-nørder &#8211; den hårde kerne</a> hvor alle er interesseret i Analytics. På <a href="https://www.linkedin.com/in/jacobworsoe/" rel="noopener noreferrer" target="_blank">LinkedIn</a> og <a href="https://twitter.com/jacobworsoe" rel="noopener noreferrer" target="_blank">Twitter</a> ryger den bredt ud til mit netværk, som nok er en lidt mere blandet skare, men til trods for det, så er der flere der læser hele indlægget.</p>
<h2>Bliver blogindlæg læst eller bare skimmet?</h2>
<p>Hvis brugeren scroller helt til bunden af et blogindlæg inden der er gået 60 sekunder, har brugeren kun skimmet blogindlægget. Der er ikke noget godt Enhanced Ecommerce event der passer til det, så det derfor tracker jeg det blot som et normalt Event.</p>
<p>Jeg laver 3 segmenter, som allesammen har en detaljevisning i deres session:</p>
<ol>
<li>Sessioner som kun skimmer</li>
<li>Sessioner som kun læser</li>
<li>Sessioner som både skimmer og læser</li>
</ol>
<p>De tre segmenter kan brydes ned på device og dermed se adfærden.</p>
<div id="attachment_1919" style="width: 1460px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1919" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices.png" alt="Andel der skimmer og læser fordelt på devices" width="1450" height="715" class="size-full wp-image-1919" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices.png 1450w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices-690x340.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices-768x379.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Andel-der-skimmer-eller-læser-fordelt-på-devices-725x358.png 725w" sizes="auto, (max-width: 1450px) 100vw, 1450px" /></a><p id="caption-attachment-1919" class="wp-caption-text">Andel der skimmer og læser fordelt på devices</p></div>
<ul>
<li>Der er altså <strong>26% der kun skimmer et blogindlæg</strong>, mens hele <strong>63% læser blogindlægget</strong> uden at skimme det først. Det er overraskende. Jeg havde egentlig forventet at langt flere startede med at skimme og derefter læse, hvis det så spændende ud &#8211; fx. masser af billede og ikke bare wall of text. Men det er faktisk kun 11% der først skimmer og derefter læser indlægget.</li>
<li>Det er dem som scroller helt til bunden inden der er gået et minut, og derefter bliver på siden og stadig er aktive (dvs. scroller) når der er gået et minut.</li>
<li>Det er derimod ikke overraskende at der er næsten <strong>dobbelt så mange der skimmer på desktop</strong> i forhold til mobile devices, da det er meget nemmere at scrolle ned i bunden på en desktop, fx med scroll-hjulet på musen eller &#8220;page down&#8221;-tasten. Det er lidt tungere at scrolle et langt indlæg igennem med swipe på en telefon.</li>
</ul>
<h2>Bliver lange blogindlæg læst mere end korte blogindlæg?</h2>
<p>I <code class="" data-line="">Product Performance</code> rapporten kan du se <code class="" data-line="">Average price</code> og <code class="" data-line="">But-to-detail rate</code>. Med de to tal kan du se sammenhængen mellem blogindlæggets længde (prisen) og sandsynligheden for at det bliver læst.</p>
<p>Du plotter tallene på et Scatter Plot i Excel og tilføjer en trendlinje, som viser sammenhængen.</p>
<div id="attachment_1922" style="width: 1033px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering.png"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-1922" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering.png" alt="Korrelationen mellem pris og konvertering er -0,32" width="1023" height="703" class="size-full wp-image-1922" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering.png 1023w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering-690x474.png 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering-768x528.png 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/08/Korrelation-mellem-pris-og-konvertering-725x498.png 725w" sizes="auto, (max-width: 1023px) 100vw, 1023px" /></a><p id="caption-attachment-1922" class="wp-caption-text">Korrelationen mellem pris og konvertering er -0,32</p></div>
<p>Trendlinjen viser en tydelig nedadgående sammenhæng mellem pris og konvertering, så jo længere blogindlægget er, jo mindre sandsynlighed er der for at det bliver læst til ende.</p>
<h3>Antal ord i buckets</h3>
<p>Du kan også inddele blogindlæggene i buckets af antal ord, fx 0-500, 501-1000, etc. og finde den optimale længde på et blogindlæg hvor brugerne oftest læser det hele.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord-860x513.jpg" alt="" width="860" height="513" class="alignnone size-large wp-image-2121" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord-860x513.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord-690x412.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord-768x458.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-vs.-Antal-ord.jpg 1243w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<p>Overraskende nok er det de helt korte indlæg på mindre end 500 ord hvor færrest læser det hele. Der er et sweetspot omkring 500-1500 ord og ligesom det ses i ovenstående Scatter Plot, så falder fastholdelsen i de lange indlæg.</p>
<h2>Der er STOR forskel på blogindlæg</h2>
<p>Okay, lad os kigge på mine to seneste blogindlæg som eksempler.</p>
<p>Baseret på antal pageviews er de cirka lige populære.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-pageviews.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-pageviews.jpg" alt="" width="637" height="371" class="alignnone size-full wp-image-2110" /></a></p>
<p>Men pageviews er bare en vanity metric. Den fortæller intet om kvaliteten eller evnen til at fastholde brugeren.</p>
<p>Og de to blogindlæg er meget forskellige.</p>
<ul>
<li><a href="https://www.jacobworsoe.dk/returvarer-google-analytics/">Tracking af returvarer i Google Analytics (den ultimative guide 2019)</a> er en inspiration, men også noget som er en reference til senere brug og den er på 3668 ord.</li>
<li><a href="https://www.jacobworsoe.dk/aws-iot-button-google-analytics/">Tracking af kaffeforbrug med AWS IoT Button og Google Analytics</a> er en sjov use-case for Google Analytics, den er rimelig letlæst og man skal læse (eller skimme) det hele for at den er sjov. Den er kun på 1571 ord.</li>
</ul>
<h3>Buy-to-Detail Rate</h3>
<p>Den store forskel på de to blogindlæg ses tydeligt i Buy-to-Detail rate som er 11,69% for returvarer-indlægget mens den er hele 46,26% på AWS IoT-indlægget!</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail-860x230.jpg" alt="" width="860" height="230" class="alignnone size-large wp-image-2113" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail-860x230.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail-690x185.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail-768x206.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/retur-vs-aws-buy-to-detail.jpg 1308w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<p>Dvs. næsten halvdelen af alle dem som ser indlægget om AWS scroller helt til bunden og er mindst 1 minut på siden.</p>
<p>Men hvornår falder folk fra på returvarer-indlægget?</p>
<p>Men hey! Tabeller med rå data er måske fede for data scientists, men de dur ikke til at gøre data nemme at forstå. Så lad os lige lave en graf inden vi går videre.</p>
<div id="attachment_2112" style="width: 870px" class="wp-caption alignnone"><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg.jpg"><img loading="lazy" decoding="async" aria-describedby="caption-attachment-2112" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg-860x437.jpg" alt="Fastholdelse af brugeren i et blogindlæg" width="860" height="437" class="size-large wp-image-2112" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg-860x437.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg-690x351.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg-768x390.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Fastholdelse-af-brugeren-i-et-blogindlæg.jpg 1241w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a><p id="caption-attachment-2112" class="wp-caption-text">Fastholdelse af brugeren i et blogindlæg</p></div>
<p>Meget bedre.</p>
<p>Herover ses en tydelig forskel hvor mange brugere på returvarer-indlægget starter med at scrolle (Add to cart) men meget få læser ned til 33% af indlægget (Checkout). Så de fleste har lige skimmet toppen og (forhåbentlig) bogmærket siden og så videre til andre ting.</p>
<p>På kaffe-indlægget er der slet ikke samme frafald, så det indlæg fastholder brugerne meget bedre. Det er godt at vide til fremtiden.</p>
<h2>Blog kategorier</h2>
<p>Der er også kæmpe forskel i fastholdelse af brugerne fordelt på kategorier. Indlæg om <a href="https://www.jacobworsoe.dk/category/nethandel/">Nethandel</a> bliver læst meget.</p>
<p>Heldigvis bliver mine indlæg om <a href="https://www.jacobworsoe.dk/category/webanalyse/">Webanalyse</a>, som jeg lægger meget arbejde i, også læst meget, hvor 24% læser hele indlægget.</p>
<p>Til gengæld skal jeg vidst tage mig lidt sammen, når jeg skriver om <a href="https://www.jacobworsoe.dk/category/seo/">SEO</a>, som umiddelbart ikke er så interessante indlæg. Her har jeg også lige taget <a href="https://www.jacobworsoe.dk/category/hverdagsstatistik/">Hverdagsstatisk</a> med, som er mit indlæg om <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">drikkevarer til et bryllup</a>.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier-860x597.jpg" alt="" width="860" height="597" class="alignnone size-large wp-image-2117" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier-860x597.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier-690x479.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier-768x533.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-rate-for-kategorier.jpg 1197w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<h2>Udgivelsesår</h2>
<p>Jeg skrev mit første blogindlæg på denne blog i 2009 og jeg har skrevet 35 indlæg i alt. Lad os se om jeg er blevet bedre til at skrive spændende indlæg igennem årene.</p>
<p><a href="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår.jpg"><img loading="lazy" decoding="async" src="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår-860x502.jpg" alt="" width="860" height="502" class="alignnone size-large wp-image-2119" srcset="https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår-860x502.jpg 860w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår-690x403.jpg 690w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår-768x448.jpg 768w, https://www.jacobworsoe.dk/wp-content/uploads/2019/11/Buy-to-Detail-Rate-pr.-udgivelsesår.jpg 1281w" sizes="auto, (max-width: 860px) 100vw, 860px" /></a></p>
<p>Jeg startede ret godt ud i 2009 og 2010 og havde derefter nogle knap så gode år, særligt 2014-2017. Men 2018 og 2019 har begge været rigtig gode år, så jeg skal vidst bare fortsætte med den type indlæg.</p>
<h2>Opsummering</h2>
<p>I det ovenstående har jeg gennemgået step-by-step hvordan jeg bruger Enhanced Ecommerce til at få et langt mere detaljeret billede af hvordan mit indhold performer.</p>
<p>Ikke bare vanity metrics, som pageviews, bounce rate og time on page.</p>
<p>Men metrics som viser præcist hvad brugerne gør på sitet, hvor lang tid de (korrekte) er på siden, samt hvor meget af indholdet de læser.</p>
<h2>Hvor mange procent tror du læser dette indlæg?</h2>
<p>Smid dit svar herunder og deltag i lodtrækning om en&#8230; ej pjat, du kan ikke vinde noget, men giv gerne et bud alligevel :)</p>

