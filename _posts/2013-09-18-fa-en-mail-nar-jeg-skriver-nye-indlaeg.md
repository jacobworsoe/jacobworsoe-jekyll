---
layout: post
title: Få en mail når jeg skriver nye indlæg
date: 2013-09-18 20:36:53
slug: fa-en-mail-nar-jeg-skriver-nye-indlaeg
categories:
  - Wordpress
---

<p>Så kom dagen endelig hvor jeg fik lavet en ordentlig integration til MailChimp fra min blog! Dette betyder at du nu kan tilmelde dig mit nyhedsbrev herunder, så får du automatisk en mail fra mig, næste gang jeg har noget spændende at fortælle &#8211; og du kan selvfølgelig nemt og ganske gebyrfrit framelde dig igen, hvis du ikke længere vil læse mine indlæg.</p>
<h2>Hvordan er det lavet?</h2>
<p>Jeg har brugt et plugin der hedder <a href="http://wordpress.org/plugins/mailchimp-for-wp/" target="_blank" rel="noopener">MailChimp for WP Lite</a> som tilføjer en lille checkbox under kommentarfeltet, hvor de som kommenterer på bloggen let kan tilmelde sig mit nyhedsbrev. Tilmeldingen ryger så automatisk over i MailChimp med single eller double opt-in, og den bruger navnet og e-mailen fra kommentarfeltet, så brugeren skal ikke udfylde noget ekstra for at tilmelde sig nyhedsbrevet.</p>
<p>Det samme plugin kan også lave formularer som man kan indsætte i en sidebar som jeg har ovre til højre eller på en separat landingpage. Jeg synes dog ikke den var så nem at style så den passede ind i mit design, så jeg brugte en af de formularer man kan hente inde fra ens MailChimp administration. Den skulle stadig tilpasses lidt, men HTML koden i den var meget bedre og nemmere at style via CSS så den passede til resten af mit site.</p>
<p>Ovre i MailChimp har jeg så opsat en <a href="http://kb.mailchimp.com/article/what-is-an-rss-to-email-campaign-and-how-to-i-set-one-up" target="_blank" rel="noopener">RSS driven campaign</a> som automatisk sender en mail til min liste når jeg skriver nye indlæg. Man kan også godt vælge at bygge en helt manuel mail og sende til sin liste når man har skrevet et nyt indlæg, men jeg kan godt lide at det kører så automatisk som muligt og så bruge tiden på at fintune de automatiske processor der kører, da det skalerer meget bedre. Og så er det bare sjovere at bruge tiden på optimering fremfor drift :)</p>

