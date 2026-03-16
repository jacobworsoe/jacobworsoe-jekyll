---
layout: post
title: Undgå sideskift ved formular submit
date: 2021-08-12 16:46:31
slug: undgaa-sideskift-ved-formular-submit
categories:
  - Analytics
---

<p>Her er et lille trick som jeg bruger når jeg skal teste tracking af en formular. Du kan affyre denne kode i konsollen og undgå at side skifter når formularen submittes. Dermed mister du ikke debug information i konsollen eller i diverse tracking debug extensions.</p>
<p>Det eneste du skal gøre er at udskifte <code class="" data-line="">#formId</code> med ID eller class på formularen og affyre koden i konsollen, inden du submitter formularen.</p>
<pre><code class="" data-line="">window.addEventListener(&#039;beforeunload&#039;, function(e) {
    e.preventDefault();
    e.returnValue = &#039;&#039;;
});

document.querySelector(&quot;#formId&quot;).addEventListener(&quot;submit&quot;, function(e){    
    e.preventDefault();
    console.log(&quot;form submitted&quot;);    
});
</code></pre>

