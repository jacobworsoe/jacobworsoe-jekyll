---
layout: post
title: Datadrevet redesign
date: 2020-08-15 22:59:24
slug: datadrevet-redesign
wordpress_id: 1180
categories:
  - Webdesign
---

Jeg startede denne blog i 2009 og <a href="https://www.jacobworsoe.dk/design-versioner/" rel="noopener">den første version</a> var bygget helt fra bunden hvor jeg havde kodet det hele i PHP med MySQL som database.

I 2013 <a href="https://www.jacobworsoe.dk/flyttet-til-wordpress/" rel="noopener noreferrer">flyttede jeg bloggen over på WordPress</a> hvor alt HTML blev konverteret til WordPress templates, men designet forblev nogenlunde uændret.

I 2014 <a href="https://www.jacobworsoe.dk/responsive-design-3-nemme-trin/">lavede jeg designet responsivt</a> så siden blev mobilvenlig.

I 2019 var det så tid til et redesign hvor jeg har brugt data fra Google Analytics, både til at tage beslutninger for at få sitet til at loade så hurtigt som muligt, men også til at forbedre KPI'erne for sitet. Jeg har også testet et råd fra Steve Krug's Dont Make Me Think, for at få brugerne til at læse flere af mine blogindlæg.

Jeg har delt blogindlægget op i to dele, hvor den første del fokuserer på hvordan jeg har kodet sitet (der er brugt GA data to steder, som er markeret med fed herunder).

Den anden del fokuserer på optimering med Google Analytics og opfølgning på effekten af de ændringer jeg har lavet.

<h2>Indhold</h2>

<strong>Part 1:</strong> Det tekniske med fokus på hvordan designet er kodet.

<ul>
<li><a href="#article-header-id-0">Mål med det nye design</a></li>
<li><a href="#article-header-id-1">Workflow</a>

<ul>
<li><a href="#article-header-id-11">GruntJS</a></li>
<li><a href="#article-header-id-2">Kun én JavaScript fil</a></li>
<li><a href="#article-header-id-3">Browser caching og cache busting</a></li>
<li><a href="#article-header-id-4">Gruntfile.js</a></li>
</ul></li>
<li><a href="#article-header-id-5">JavaScript</a>

<ul>
<li><a href="#article-header-id-5">Tracking logik fra GTM til dataLayer</a></li>
<li><a href="#article-header-id-6">Væk med jQuery</a></li>
<li><a href="#article-header-id-7">JavaScript reduceret fra 184 KB til 31 KB</a></li>
</ul></li>
<li><a href="#article-header-id-8">CSS</a>

<ul>
<li><a href="#article-header-id-81">CSS skrevet i Sass</a></li>
<li><a href="#article-header-id-9">Inline CSS eller ekstern fil? <strong>(Baseret på adfærdsdata fra Google Analytics)</strong></a></li>
<li><a href="#article-header-id-10">Inline kun den nødvendige CSS kode</a></li>
<li><a href="#article-header-id-11">CSS reduceret med 45%</a></li>
<li><a href="#article-header-id-12">Væk med !important</a></li>
</ul></li>
<li><a href="#article-header-id-13">Billeder</a></li>
<li><a href="#article-header-id-14">WordPress</a>

<ul>
<li><a href="#article-header-id-141">Væk med unødvendige plugins</a></li>
<li><a href="#article-header-id-15">Tabeller</a></li>
<li><a href="#article-header-id-16">Syntax highlighting</a></li>
<li><a href="#article-header-id-17">Relaterede indlæg <strong>(Baseret på adfærdsdata fra Google Analytics)</strong></a></li>
</ul></li>
</ul>

<strong>Part 2:</strong> Optimering af adfærden på sitet med Google Analytics data.

<ul>
<li><a href="#article-header-id-18">Loadtid og konvertering</a>

<ul>
<li><a href="#article-header-id-181">Google Pagespeed Score hævet fra 86 til 99</a></li>
<li><a href="#article-header-id-19">Er sitet så blevet hurtigere?</a></li>
<li><a href="#article-header-id-20">Hvad med konvertering?</a></li>
<li><a href="#article-header-id-21">Øge sidevisninger pr. besøg (test af råd fra Steve Krug)</a></li>
</ul></li>
<li><a href="#article-header-id-22">Lykkedes målene?</a></li>
</ul>

<h2 id="article-header-id-0">Mål med det nye design</h2>

<ol>
    <li>Mere moderne workflow til udvikling af websitet</li>
    <li>Oprydning i kode og sletning af unødvendige ting</li>
    <li>Hurtigere loadtid</li>
    <li>Højere konvertering</li>
    <li>Øge sidevisninger pr. besøg</li>
</ol>

<h2 id="article-header-id-1">Workflow</h2>

<h3 id="article-header-id-11">GruntJS</h3>

Der er mange (kedelige) opgaver involveret i at optimere front-end kode og jeg bruger <a href="https://gruntjs.com/">GruntJS</a> som task runner, til at udføre alle de opgaver automatisk.

GruntJS gør følgende ved mine filer:

<ol>
<li>Samler JavaScript filer til én samlet, minificeret fil. Både de forskellige libraries jeg bruger og mine egne JavaScript filer.</li>
<li>Compiler alle <a href="https://sass-lang.com/">Sass</a> filerne til en minificeret CSS fil.</li>
<li>Kopiere alle de færdige optimerede filer over i en mappe, som indeholder de filer der skal uploades til webserveren.</li>
<li>JavaScript filen bliver cachet 1 år i browseren og derfor får den et unikt nyt navn, hvis filen ændres, så browseren downloader den nye fil.</li>
<li>Grunt overvåger mine filer og kører de ovenstående opgaver, når jeg gemmer en ny ændring, fx i en Sass eller JavaScript fil.</li>
</ol>

<h3 id="article-header-id-2">Kun én JavaScript fil</h3>

Det er ikke så vigtigt efter HTTP2 blev lanceret, men det er stadig best practise at lave så få requests som muligt, fx ved at samle alt JavaScript i én fil. Takket være GruntJS bliver dette gjort helt automatisk og derefter bliver filen minificeret.

<h3 id="article-header-id-3">Browser caching og cache busting</h3>

JS filen caches i browseren i 1 år ved at sætte expire-headers til 1 år i <code>.htaccess</code>. Jeg har brugt de anbefalede settings fra <a href="https://html5boilerplate.com/" rel="noopener noreferrer" target="_blank">html5boilerplate</a>.

<pre><code class="language-html">ExpiresByType application/javascript                "access plus 1 year"
ExpiresByType application/x-javascript              "access plus 1 year"
ExpiresByType text/javascript                       "access plus 1 year"
</code></pre>

GruntJS laver et hash baseret på indholdet i filen og det hash bliver tilføjet til filnavnet.

Dvs. denne fil:

<code>bundle.min.js</code>

Kommer til at hedde:

<code>bundle.min.e3d609e4.js</code>

Hvis filen ændrer sig bliver der lavet en ny hash, så filnavnet ændrer sig. Dermed vil browseren se det som en ny fil, så den ikke bruger den fil den allerede har i cache, men downloade den nye fil.

Dermed kan jeg have filen cachet nærmest uendeligt, men stadig sikre at alle browsere får den nyeste fil, hvis jeg ændrer noget.

<h3 id="article-header-id-4">Gruntfile.js</h3>

For de interesserede, så er her min <code>Gruntfile.js</code> som indeholder hele den opsætning af GruntJS som er beskrevet herover. Derudover har den også compile af Sass til CSS som jeg beskriver om lidt.

<pre><code class="language-javascript">module.exports = function(grunt) {
    require("load-grunt-tasks")(grunt);

    // 1. All configuration goes here
    grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),

        // grunt-contrib-concat
        concat: {
            dist: {
                src: [
                    "js/libs/prism.js",
                    "js/SlideUpBox.js",
                    "js/content-as-ecommerce.js",
                    "js/tracking.js",
                    "js/hamburgerNav.js",
                    "js/jacobworsoe.js",
                    "js/drinksberegner.js"
                ],
                dest: "js/build/bundle.js"
            }
        },

        // grunt-contrib-uglify
        uglify: {
            build: {
                files: [
                    {
                        src: "js/build/bundle.js",
                        dest: "js/build/bundle.min.js"
                    }
                ]
            }
        },

        // grunt-contrib-sass
        sass: {
            dist: {
                options: {
                    style: "compressed",
                    sourcemap: "none"
                },
                files: {
                    "css/homepage.css": "scss/homepage-bundle.sass",
                    "css/single.css": "scss/single-bundle.sass"
                }
            }
        },

        // grunt-contrib-copy
        copy: {
            main: {
                files: [
                    {
                        expand: true,
                        src: ["*.php"],
                        dest: "dist/",
                        filter: "isFile"
                    },
                    {
                        expand: true,
                        src: ["*.css"],
                        dest: "dist/",
                        filter: "isFile"
                    },
                    {
                        expand: true,
                        src: ["*.png"],
                        dest: "dist/",
                        filter: "isFile"
                    },
                    {
                        expand: true,
                        src: ["css/*.css"],
                        dest: "dist/",
                        filter: "isFile"
                    },
                    {
                        expand: true,
                        src: ["js/build/*.min.js"],
                        dest: "dist/",
                        filter: "isFile"
                    },
                    {
                        expand: true,
                        src: ["svg/*.svg"],
                        dest: "dist/",
                        filter: "isFile"
                    }
                ]
            }
        },

        // grunt-hashres
        hashres: {
            options: {
                fileNameFormat: "${name}.${hash}.${ext}",
                renameFiles: true
            },
            prod: {
                options: {},
                src: ["dist/js/**/*.min.js"],
                dest: ["dist/footer.php"]
            }
        },

        // grunt-contrib-watch
        watch: {
            options: {
                livereload: true
            },
            scripts: {
                files: ["js/*.js"],
                tasks: ["concat", "uglify"],
                options: {
                    spawn: false
                }
            },
            css: {
                files: ["scss/*.sass", "scss/*.scss"],
                tasks: ["sass"],
                options: {
                    spawn: false
                }
            }
        }

    }); // grunt.initConfig

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    // Development tasks
    grunt.registerTask("default", ["sass", "watch"]);
    grunt.registerTask("stage", ["sass", "concat", "uglify", "copy"]);
    grunt.registerTask("deploy", [
        "sass",
        "concat",
        "uglify",
        "copy",
        "hashres"        
    ]);
};
</code></pre>

<h2 id="article-header-id-5">JavaScript</h2>

<h3 id="article-header-id-51">Tracking logik fra GTM til dataLayer</h3>

Jeg afprøver og tester en masse forskellig tracking på mit website. Noget af det er tilføjet til sitets JavaScript fil og udstillet i <code>dataLayer</code> som det bør, men noget bliver også hurtigt tilføjet direkte i GTM for at afprøve det.

Jeg gik alt GTM kode igennem og fik det flyttet til sitet, så GTM indeholder så lidt kode og logik som muligt. Det er fint at teste noget hurtigt i GTM, men det skal tilføjes til <code>dataLayer</code> hvis det skal være permanent.

<h3 id="article-header-id-6">Væk med jQuery</h3>

Jeg har omskrevet alt jQuery til ren JavaScript for at slippe for at loade de 87 KB som jQuery fylder når det er minified (274 KB unminified). Her var <a href="http://youmightnotneedjquery.com/" rel="noopener noreferrer" target="_blank">youmightnotneedjquery.com</a> en stor hjælp.

<h3 id="article-header-id-7">JavaScript reduceret fra 184 KB til 31 KB</h3>

JavaScript koden til websitet er reduceret kraftigt med i alt 153 KB hvoraf de 87 KB er jQuery. Men der er også en masse andre ting jeg har skåret væk og skrevet smartere. Fx <a href="http://fitvidsjs.com/">FitVids.JS</a> som jeg brugte da jeg lavede <a href="https://www.jacobworsoe.dk/responsive-design-3-nemme-trin/">sitet responsivt</a> til at gøre YouTube videoer responsive. Det er meget smart, men med lidt simpel HTML og CSS kan man undvære det jQuery plugin.

Jeg indsætter en <code>div</code> rundt om videoen.

```html
<div class="videoWrapper">
    <iframe src="//www.youtube.com/embed/usyYXNNBRjc" frameborder="0" allowfullscreen></iframe>
</div>
```

Og tilføjer lidt styling af den <code>div</code> samt iframen som indeholder videoen, og så er videoen responsiv.

<pre><code class="language-sass">.videoWrapper
    position: relative
    padding-bottom: 56.25%
    padding-top: 25px
    height: 0
    margin: 20px 0 20px 0
    border: 5px solid $lightGrey

.videoWrapper iframe
    position: absolute
    top: 0
    left: 0
    width: 100%
    height: 100%
</code></pre>

Jeg brugte også LunaMetrics' <a href="https://www.bounteous.com/insights/2015/05/11/youtube-tracking-google-analytics-google-tag-manager/?ns=l">script til tracking af visninger af YouTube videoer</a>, men jeg brugte ikke den tracking til noget, så det blev også fjernet.

<h2 id="article-header-id-8">CSS</h2>

<h3 id="article-header-id-81">CSS skrevet i Sass</h3>

I det nye redesign skrev jeg alt CSS fra bunden igen og jeg valgte at skrive det i <a href="https://sass-lang.com/" rel="noopener noreferrer" target="_blank">Sass</a>.

Sass er et sprog som giver nogle ekstra muligheder og Sass filerne skal compiles til almindelige CSS filer inden de ryger ud på websitet.

Her er mine top 3 fedeste ting ved Sass.

<strong>1) Variabler.</strong> Jeg kan definere variabler, fx til farvekoder som er brugt mange steder i koden. Dermed kan du nemt skifte farven overalt i din kode, blot ved at ændre én variabel. Da facebook valgte at rydde op i deres CSS, fandt de 800 næsten ens blå farver i koden. Det sker ikke med Sass.

<figure><a href="{{ '/assets/images/2020/08/Sass-vars-farver.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Sass-vars-farver.jpg' | relative_url }}" alt="Websitets farver defineret i Sass variabler." width="640" height="420" class="size-full wp-image-2372" /></a><figcaption>Websitets farver defineret i Sass variabler.</figcaption></figure>

<strong>2) Imports.</strong> Jeg kan splitte Sass koden op i mindre filer som tilhører en bestemt side eller sektion af sitet. Det hele kan samles til én fil, så browseren stadig kun skal lave et request.

<pre><code class="language-sass">// Base
@import "normalize"
@import "_vars"
@import "_base"
@import "_jetpack"

// Critical
@import "_header"
@import "_videoEmbeds"
@import "_pre"
@import "_button"
@import "_blockquote"

// Below-the-fold
@import "_post-share-follow"
@import "_comments"
@import "_footer"
@import "_slide-up-box"

// Pages
@import "_single"
@import "_highlight"
@import "_tables"
</code></pre>

<strong>3) Nesting.</strong> Med Nesting kan man tilføje underliggende selectors blot ved at indent'e linjen, så man slipper for at gentage selectors mange gange.

Her er et eksempel på Nesting i Sass.

<pre><code class="language-sass">.comment-gravatar
    float: left
    width: 15%
    max-width: 120px
    padding-right: 20px
    margin-top: 10px

    @media(max-width: 500px)
        padding-right: 8px

    img
        border-radius: 5px
</code></pre>

Og her den CSS kode det compiles til.

<pre><code class="language-css">.comment-gravatar {
  float: left;
  width: 15%;
  max-width: 120px;
  padding-right: 20px;
  margin-top: 10px;
}

@media(max-width: 500px) {
  .comment-gravatar {
    padding-right: 8px;
  }
}

.comment-gravatar img {
  border-radius: 5px;
}
</code></pre>

<h3 id="article-header-id-9">Inline CSS eller ekstern fil?</h3>

Normalt er det best practice at have CSS i en ekstern fil, så den kan caches i browseren. Men det kræver et ekstra request at have den i en ekstern fil. Så om det kan betale sig at lave et ekstra request kommer an på hvor stor filen er samt hvor mange sider brugeren ser på sitet.

På første sidevisning vil det nemlig være en ulempe at have CSS i en ekstern fil, da der skal laves et request mere. Men på efterfølgende sider vil filen være cachet og skal ikke hentes igen.

<figure><a href="{{ '/assets/images/2020/07/Bounce-rate-på-85-procent.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/07/Bounce-rate-på-85-procent.jpg' | relative_url }}" alt="Bounce rate på 85% og 1,17 sider pr. session" width="886" height="286" class="size-full wp-image-2300" /></a><figcaption>Bounce rate på 85% og 1,17 sider pr. session</figcaption></figure>

I løbet af det sidste år har der været en bounce rate på 85% på sitet, dvs. langt de fleste læser kun et enkelt blogindlæg. Der bliver også kun set 1,17 sider pr. session. Det betyder altså at 85% af de besøgende ikke ser en efterfølgende side og dermed ikke får gevinsten af en cachet CSS fil.

I hvert fald ikke i det samme besøg. Men det kan jo være de kommer tilbage på sitet igen og dermed stadig har CSS filen i deres cache.

<figure><a href="{{ '/assets/images/2019/11/new-vs.-returning-visitors.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/11/new-vs.-returning-visitors.jpg' | relative_url }}" alt="25% af de besøgende har været på sitet før." width="630" height="453" class="size-full wp-image-2094" /></a><figcaption>25% af de besøgende har været på sitet før.</figcaption></figure>

Det er kun 25% af de besøgende der har været på sitet før, så langt de fleste vil ikke have CSS filen cachet.

<div class="attention"><strong>Bemærk!</strong> Jeg har ekskluderet Safari her, da Safari ikke længere giver korrekte tal for tilbagevendende besøg efter ITP 2.1.</div>

Min konklusion på de ovenstående data bliver at det er bedst at optimere efter at give en hurtig oplevelse på den første sidevisning og derfor lægger jeg CSS'en inline, for at spare det ekstra request.

<h3 id="article-header-id-10">Inline kun den nødvendige CSS kode</h3>

Når man har CSS i en ekstern fil som bliver cachet giver det typisk bedst mening at samle det hele i én fil. Men når jeg inliner min CSS kode, giver det bedre mening kun at inline den CSS kode der skal bruges på den specifikke side.

Min forside er rimelig simpel. I mit tilfælde er det bare en liste af mine blogindlæg med titel, dato og antal kommentarer.

<figure><img src="{{ '/assets/images/2020/08/50466523-B08F-45FF-AE69-A85876863517.jpg' | relative_url }}" alt="Forsiden er meget simpel." width="400" height="437" class="size-full wp-image-2473" /><figcaption>Forsiden er meget simpel.</figcaption></figure>

Et blogindlæg har både billeder og video i indlægget, den har en anderledes header med titlen på indlægget. I bunden er der links til sociale medier, tilmelding til nyhedsbrev og så er der hele kommentar sektionen, som kræver en masse CSS kode.

<figure><img src="{{ '/assets/images/2020/08/716B5771-D030-4214-BF2C-4B0A8DA036D3.jpg' | relative_url }}" alt="Et blogindlæg kræver noget mere CSS." width="400" height="560" class="size-full wp-image-2474" /><figcaption>Et blogindlæg kræver noget mere CSS.</figcaption></figure>

Der er altså en masse CSS kode som er helt overflødig at loade på forsiden og vice versa.

Når jeg bruger Sass til at samle de enkelte .sass filer til en færdig CSS fil laver jeg derfor to filer:

<ol>
<li>En til forsiden og kategorisider, hvor der blot vises en liste af indlæg.</li>
<li>En til <code>single.php</code> som viser hele indlægget.</li>
</ol>

De to filer har alt den generelle styling til fælles, som jeg har brudt ud i logiske moduler.

<pre><code class="language-sass">// Base
@import "normalize" // https://necolas.github.io/normalize.css/
@import "_vars" // Sass variabler med alle de farver jeg bruger
@import "_base" // Site-wide styling, fx box-sizing: border-box og H1, H2, H3 og overordnet font-family
@import "_jetpack" // Jetpack tilføjer en lille statistik box, som jeg sjuler med CSS

// Critical - Above-the-fold
@import "_header" // SVG logo, sidens titel, hamburger menuen og selve menuen som åbnes

// Below-the-fold
@import "_footer" // Footer med sociale links, mit billede og en række links
</code></pre>

Ovenstående CSS kode inkluderes i begge filer og derudover inkluderer jeg så den kode som er relevant for hhv. forsiden og blogindlægget.

Jeg har i alt 19 KB CSS kode.

<a href="{{ '/assets/images/2019/11/Frodeling-af-bytes-i-CSS-koden.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/11/Frodeling-af-bytes-i-CSS-koden-860x503.jpg' | relative_url }}" alt="" width="860" height="503" class="alignnone size-large wp-image-2099" /></a>

<ul>
<li>41% er Normalize, som jeg måske skal overveje om jeg kan undvære.</li>
<li>38% er specifikt til blogindlæg som jeg derved ikke behøver at loade på forsiden.</li>
<li>18% er den globale CSS til header og footer.</li>
<li>3% er til forsiden, der som sagt er meget simpel.</li>
</ul>

I WordPress inkluderer jeg de to CSS filer så de ligger inline, baseret på et check for om siden er <code>single.php</code> eller andre sider.

<pre><code class="language-php"><style>
<?php if ( is_single() || is_page() ) {
    include("css/single.css");
} else {
    include("css/homepage.css");
}
?>
</style>
</code></pre>

<h3 id="article-header-id-11">CSS reduceret med 45%</h3>

CSS kode har det med at vokse over tid og man får sjældent ryddet op løbende. Her skrev jeg alt fra bunden og jeg er nok også blevet bedre til at skrive CSS så det fylder mindre. Resultatet er en 45% reduktion af CSS fra 34,5 KB på i det gamle design til 19 KB i det nye design.

<a href="{{ '/assets/images/2019/11/CSS-kode-KB-jacobworsoe-v2-vs.-v3.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/11/CSS-kode-KB-jacobworsoe-v2-vs.-v3.jpg' | relative_url }}" alt="" width="1002" height="601" class="alignnone size-full wp-image-2103" /></a>

<h3 id="article-header-id-12">Væk med !important</h3>

Når jeg skriver !important i min CSS kode er det et tegn på at jeg har malet mig op i et hjørne.

Det er en sidste udvej. Og det kommer til at bide mig i røven senere hen.

Det gamle design brugte !important 35 gange.

Derfor har jeg fokuseret på at få gennemtænkt mine CSS selectors så jeg undgår at bruge !important i det nye design.

Jeg har også tænkt over at min styling skal cascade så meget som muligt, så jeg definerer mest muligt CSS kode på de øverste selectors (dem med lavest specificity) og derefter nedarves de bare til alt det øvrige. Det betyder også at jeg ikke overskriver min egen kode eller laver den samme styling flere gange på forskellige selectors.

Et eksempel er at jeg styler min font på <code>html</code> elementet og derefter nedarves det bare til resten af sitet, så jeg ikke skal style min font igen - lige bortset fra <code>input</code> elementer som ikke nedarver styling og derfor skal styling skrives specifikt på dem.

<pre><code class="language-sass">html
    background: $grey-dark
    color: $lightGrey
    font-family: -system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"
    -webkit-font-smoothing: antialiased
    -moz-osx-font-smoothing: grayscale
    letter-spacing: 0.02em
    font-size: 20px
    line-height: 1.75
</code></pre>

Tit bruges !important også for at overskrive noget andet styling, fx noget CSS der kommer med et plugin. Det betyder dermed overflødig kode, som blot overskrives.

Det giver også browseren mere arbejde med at finde ud af hvad der skal overskrive noget andet.

Jeg har, så vidt det er muligt, deaktiveret den medfølgende CSS fra de enkelte plugins, så jeg blot får den rå HTML og selv skrevet alt styling. Dermed er jeg sikker på at der ikke kommer noget overflødig CSS kode med.

<h2 id="article-header-id-13">SVG til grafik</h2>

SVG er super fedt til grafiske elementer fordi det er kode og ikke et billede. Dermed kan det skalere uendeligt uden at blive grimt og det fylder meget lidt.

Jeg bruger det fx til den lille graf i mit logo.

Der er forskellige måder at indsætte et SVG billede på og jeg lytter til <a href="https://css-tricks.com/">Chris Coyiers</a> enorme erfaring om SVG (han har skrevet en bog om det: <a href="https://abookapart.com/products/practical-svg" rel="noopener noreferrer" target="_blank">Practical SVG</a>). Hans anbefaling er blot at inline SVG koden direkte i HTML'en. Det har han skrevet om her: <a href="https://css-tricks.com/pretty-good-svg-icon-system/" rel="noopener noreferrer" target="_blank">A Pretty Good SVG Icon System</a>

Jeg har alle mine SVG filer liggende i koden og selve koden til grafen i logoet kan ses herunder. Den fylder kun 848 bytes som SVG fil.

<figure><a href="{{ '/assets/images/2019/10/SVG-filer.jpg' | relative_url }}"><img src="{{ '/assets/images/2019/10/SVG-filer-860x247.jpg' | relative_url }}" alt="SVG koden til grafen som fylder under 1 KB" width="860" height="247" class="size-large wp-image-2060" /></a><figcaption>SVG koden til grafen som fylder under 1 KB</figcaption></figure>

Indholdet af SVG filen indsætter jeg i <code>header.php</code> med følgende kode. Når SVG filen ligger i koden, skal der ikke laves et ekstra request for at hente den og færre requests er med til at gøre sitet hurtigt.

<pre><code class="language-php"><a href="https://www.jacobworsoe.dk/" title="jacobworsoe.dk" rel="home" class="blog-title">
   <span class="logo"><?php include("svg/logo.svg"); ?></span>
   <span class="title"><?php bloginfo( 'name' ); ?></span>
</a>
</code></pre>

<h2 id="article-header-id-14">WordPress</h2>

<h3 id="article-header-id-141">Væk med unødvendige plugins</h3>

Jeg har fået fjernet en del plugins, så det bliver mere simpelt, fjerner mulige sikkerhedshuller og gør sitet hurtigere.

<h3 id="article-header-id-15">Tabeller</h3>

<a href="https://wordpress.org/plugins/tablepress/" rel="noopener noreferrer" target="_blank">TablePress</a> er et fedt plugin, men de få simple tabeller jeg har i mine indlæg, kan jeg sagtens skrive i hånden, så væk med det.

<h3 id="article-header-id-16">Syntax highlighting</h3>

Jeg brugte <a href="https://github.com/googlearchive/code-prettify">Code Prettify</a> til syntax highlighting af kode. Jeg er skiftet til at bruge <a href="https://prismjs.com/" rel="noopener noreferrer" target="_blank">Prism.js</a> hvor jeg vælger præcis de kodesprog jeg skal bruge og så får jeg en CSS fil og en JavaScript fil. CSS filen inkluderer jeg i min SCSS fil og JavaScript filen bliver bundlet sammen med min øvrige JS kode i én samlet fil. Og så er dét plugin overflødigt :)

Jeg kan i øvrigt anbefale <a href="https://css-tricks.com/posting-code-blocks-wordpress-site/" rel="noopener noreferrer" target="_blank">denne artikel</a> med alle de forskellige muligheder for at skrive og vise kode i WordPress.

<h3 id="article-header-id-17">Relaterede indlæg</h3>

Jeg har brugt Yet Another Related Posts Plugin til at vise relaterede indlæg i bunden af hvert blogindlæg.

<figure><a href="{{ '/assets/images/2019/08/Relaterede-blogindlæg.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/Relaterede-blogindlæg.png' | relative_url }}" alt="I bunden af alle blogindlæg vises links til relaterede blogindlæg." width="941" height="595" class="size-full wp-image-1829" /></a><figcaption>I bunden af alle blogindlæg vises links til relaterede blogindlæg.</figcaption></figure>

Jeg brugte Enhanced Ecommerce til at tracke impressions og clicks på dem og fandt ud af at de links havde en CTR på 0,42% så for 99,58% var de bare ligegyldigt støj på siden. Så jeg fjernede dem inklusiv det plugin.

<figure><a href="{{ '/assets/images/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/Product-list-performance-nyeste-og-relaterede-indlæg.png' | relative_url }}" alt="CTR på 0,42% viser at meget få klikker på de links." width="1094" height="485" class="size-full wp-image-1830" /></a><figcaption>CTR på 0,42% viser at meget få klikker på de links.</figcaption></figure>

Jeg fjernede i øvrigt også links til de seneste blogindlæg, da de havde en endnu lavere CTR på 0,05% - disse blev ikke lavet med et plugin, men det er altid godt at få fjernet unødvendigt støj.

<figure><a href="{{ '/assets/images/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png' | relative_url }}"><img src="{{ '/assets/images/2019/08/Nyeste-blogindlæg-imressions-clicks-CTR.png' | relative_url }}" alt="Sidebar med nyeste blogindlæg." width="1270" height="526" class="size-full wp-image-1828" /></a><figcaption>Sidebar med nyeste blogindlæg.</figcaption></figure>

<h2 id="article-header-id-18">Loadtid og konvertering</h2>

Okay, det var en lang teknisk snak. Nu skal vi se om det har givet de ønskede resultater.

<h3 id="article-header-id-181">Google Pagespeed Score hævet fra 86 til 99</h3>

Det gamle design havde en pagespeed score på 86 for desktop. <a href="https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fwww.jacobworsoe.dk%2F&tab=desktop" rel="noopener noreferrer" target="_blank">Den er nu 99</a>.

<figure><a href="{{ '/assets/images/2020/08/pagespeed_score_99_desktop.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/pagespeed_score_99_desktop.jpg' | relative_url }}" alt="Pagespeed score på 99 for desktop." width="701" height="467" class="size-full wp-image-2337" /></a><figcaption>Pagespeed score på 99 for desktop.</figcaption></figure>

Den vigtige metric er dog mobile nu og <a href="https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fwww.jacobworsoe.dk%2F&tab=mobile" rel="noopener noreferrer" target="_blank">den er 96</a>.

<figure><a href="{{ '/assets/images/2020/08/pagespeed_score_96_mobile.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/pagespeed_score_96_mobile.jpg' | relative_url }}" alt="Pagespeed score på 96 for mobile." width="687" height="477" class="size-full wp-image-2338" /></a><figcaption>Pagespeed score på 96 for mobile.</figcaption></figure>

<h3 id="article-header-id-19">Er sitet så blevet hurtigere?</h3>

Ja, det er det. I gennemsnit er loadtiden blevet forbedret 29%.

<figure><a href="{{ '/assets/images/2020/08/Average-pageload-times.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Average-pageload-times.jpg' | relative_url }}" alt="Den gennemsnitlige loadtid er forbedret 29%." width="592" height="327" class="size-full wp-image-2367" /></a><figcaption>Den gennemsnitlige loadtid er forbedret 29%.</figcaption></figure>

Men gennemsnit kan snyde meget og skjule sandheden.

Ikke alle sider loader lige hurtigt.

Jeg har blogindlæg på mere end <a href="https://www.jacobworsoe.dk/indhold-enhanced-ecommerce/">6000 ord med masser af billeder</a>. Jeg har meget populære blogindlæg som står for <a href="https://www.jacobworsoe.dk/hvor-meget-drikker-gaesterne-til-et-bryllup/">70% af sidevisningerne</a> som kun har få, men til gengæld meget store billeder. Og så er der <a href="https://www.jacobworsoe.dk">forsiden</a> som stort set kun er tekst.

Især det faktum at de har meget forskellige antal sidevisninger gør at de fylder meget forskelligt i gennemsnittet.

Lad os derfor kigge på top 10 mest populære sider hver for sig, samt et vægtet gennemsnit for de sider. Alle top 10 sider er blevet hurtigere, men der er stor forskel på hvor meget de er forbedret.

<figure><a href="{{ '/assets/images/2020/08/Udvikling-i-loadtid-top-10-sider.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Udvikling-i-loadtid-top-10-sider-860x496.jpg' | relative_url }}" alt="Top 10 sider er i gennemsnit blevet 22% hurtigere - men der er store forskelle!" width="860" height="496" class="size-large wp-image-2368" /></a><figcaption>Top 10 sider er i gennemsnit blevet 22% hurtigere - men der er store forskelle!</figcaption></figure>

22% er et mere retvisende gennemsnit for udviklingen i loadtid.

<h3 id="article-header-id-20">Hvad med konvertering?</h3>

Jeg har tidligere skrevet om hvordan jeg bruger Enhanced Ecommerce til at <a href="https://www.jacobworsoe.dk/indhold-enhanced-ecommerce/">tracke om brugerne læser mine blogindlæg</a>.

Kort fortalt tracker jeg hvor mange der scroller helt til bunden af et blogindlæg og har været mindst 1 minut på siden. Det er den vigtigste KPI for min blog. Hvor mange læser hele blogindlægget?

For hvert blogindlæg har jeg en Buy-to-detail Rate, som er forholdet mellem antal sidevisninger og antal læsninger.

På trods af at loadtiden er markant forbedret for alle blogindlæg, så er konverteringen desværre ikke steget - tværtimod.

Jeg tror den store årsag til den lavere konvertering skyldes designet. Jeg har skruet op for <code>font-size</code> fra <code>17px</code> til <code>20px</code> i det nye design og gjort overskrifter markant større og givet det hele lidt mere "luft". Det gør det nemmere at læse, men siden bliver også markant længere. Måske føles det som et længere blogindlæg at tygge sig igennem?

<figure><a href="{{ '/assets/images/2020/08/Udvikling-i-konvertering-top-10-sider.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Udvikling-i-konvertering-top-10-sider.jpg' | relative_url }}" alt="Udvikling i konvertering - top 10 sider" width="1058" height="645" class="size-full wp-image-2377" /></a><figcaption>Udvikling i konvertering - top 10 sider</figcaption></figure>

Bounce Rate er ligeledes uændret, på trods af den hurtigere loadtid.

<figure><a href="{{ '/assets/images/2020/08/Bounce-Rate-comparison.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Bounce-Rate-comparison.jpg' | relative_url }}" alt="Bounce Rate før/efter designet." width="915" height="497" class="size-full wp-image-2378" /></a><figcaption>Bounce Rate før/efter designet.</figcaption></figure>

Så det nye design har ikke haft den ønskede effekt på konverteringen. Det må jeg gøre bedre i næste design.

<h3 id="article-header-id-21">Øge sidevisninger pr. besøg</h3>

Jeg har læst <a href="https://www.saxo.com/dk/dont-make-me-think-revisited_steve-krug_paperback_9780321965516">Don't Make Me Think</a> mange gange og den kan anbefales til alle der arbejder med noget digitalt.

<figure><a href="{{ '/assets/images/2020/08/Dont_make_me_think.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Dont_make_me_think.jpg' | relative_url }}" alt="Don&#039;t Make Me Think af Steve Krug" width="622" height="622" class="size-full wp-image-2383" /></a><figcaption>Don't Make Me Think af Steve Krug</figcaption></figure>

Her er en god pointe fra bogen omkring navigation.

<figure><a href="{{ '/assets/images/2020/08/The-overlooked-purpose-of-navigation.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/The-overlooked-purpose-of-navigation-860x486.jpg' | relative_url }}" alt="Navigation reveals content!" width="860" height="486" class="size-large wp-image-2384" /></a><figcaption>Navigation reveals content!</figcaption></figure>

Som tidligere vist, så har sitet en Bounce Rate på 85% og der bliver kun set 1,17 sider pr. session.

<figure><a href="{{ '/assets/images/2020/07/Bounce-rate-på-85-procent.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/07/Bounce-rate-på-85-procent.jpg' | relative_url }}" alt="Bounce rate på 85% og 1,17 sider pr. session" width="886" height="286" class="size-full wp-image-2300" /></a><figcaption>Bounce rate på 85% og 1,17 sider pr. session</figcaption></figure>

Jeg vil gerne at brugerne fortsætter rundt på sitet og ser nogle flere blogindlæg.

Det gamle design havde ikke en menu, så jeg tilføjede en burger menu som viser sitets kategorier, som Steve Krug anbefaler i Don't Make Me Think.

<figure><a href="{{ '/assets/images/2020/08/burger-menu-open.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/burger-menu-open.jpg' | relative_url }}" alt="Burger menu med kategorier." width="798" height="552" class="size-full wp-image-2386" /></a><figcaption>Burger menu med kategorier.</figcaption></figure>

Jeg tracker både hvor mange der åbner burger menuen og hvor mange der klikker i den.

<ul>
    <li>1,6% af alle besøg åbner menuen.</li>
    <li>0,4% af alle besøg klikker på noget i menuen.</li>
</ul>

Her er de kategorier der bliver klikket på.

<figure><a href="{{ '/assets/images/2020/08/Click-in-hamburger-navigation.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Click-in-hamburger-navigation.jpg' | relative_url }}" alt="Mest klikkede kategorier i burger menuen." width="762" height="587" class="size-full wp-image-2385" /></a><figcaption>Mest klikkede kategorier i burger menuen.</figcaption></figure>

Umiddelbart en ret lav konverteringsrate og sider pr. besøg er dog også uændret.

<figure><a href="{{ '/assets/images/2020/08/Pages-per-session.jpg' | relative_url }}"><img src="{{ '/assets/images/2020/08/Pages-per-session.jpg' | relative_url }}" alt="Pages per session er uændret." width="463" height="266" class="size-full wp-image-2388" /></a><figcaption>Pages per session er uændret.</figcaption></figure>

Så selvom Steve Krug har ret i mange ting, så virker en burger menu altså ikke på dette site. Jeg må i tænkeboks.

Til sammenligning er der 0,47% der klikker på et internt link når jeg i et blogindlæg, linker til et andet af mine blogindlæg.

<h2 id="article-header-id-22">Lykkedes målene?</h2>

Lad os se.

<ol>
<li>Mere moderne workflow til udvikling af websitet - <span class="task-status-completed">Tjek!</span></li>
<li>Oprydning i kode og sletning af unødvendige ting - <span class="task-status-completed">Tjek!</span></li>
<li>Hurtigere loadtid - <span class="task-status-completed">Tjek!</span></li>
<li>Højere konvertering - <span class="task-status-failed">Nope!</span></li>
<li>Øge sidevisninger pr. besøg - <span class="task-status-failed">Nope!</span></li>
</ol>

<style>
.task-status-completed { color: #48e0a4 }
.task-status-failed { color: #ffafaf }
</style>