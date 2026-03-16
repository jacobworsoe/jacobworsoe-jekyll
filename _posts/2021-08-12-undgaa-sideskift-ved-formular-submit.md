---
layout: post
title: Undgå sideskift ved formular submit
date: 2021-08-12 16:46:31
slug: undgaa-sideskift-ved-formular-submit
categories:
  - Analytics
---

Her er et lille trick som jeg bruger når jeg skal teste tracking af en formular. Du kan affyre denne kode i konsollen og undgå at side skifter når formularen submittes. Dermed mister du ikke debug information i konsollen eller i diverse tracking debug extensions.

Det eneste du skal gøre er at udskifte <code>#formId</code> med ID eller class på formularen og affyre koden i konsollen, inden du submitter formularen.

<pre><code class="language-javascript">window.addEventListener('beforeunload', function(e) {
    e.preventDefault();
    e.returnValue = '';
});

document.querySelector("#formId").addEventListener("submit", function(e){    
    e.preventDefault();
    console.log("form submitted");    
});
</code></pre>