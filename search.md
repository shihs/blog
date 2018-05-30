---
layout: page
title: Search
---
<ul class="archive" id="group">
  

  

  
  <h1 class="page-title"><i class="fa fa-search" style="font-size:1em;"></i>&nbsp;Search</h1>


<br/>&nbsp;
<form action="get" id="site_search" autocomplete="on">
<center>
  <input style="font-size:20px;" type="text" id="search_box">
  <input style="font-size:20px;" type="submit" value="Go!">
</center>
</form>
<br/>&nbsp;
<br/>&nbsp;

<ul id="search_results"></ul>

<script src="{{ "/js/lunr.min.js" | relative_url }}"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="{{ "/js/search.js" | relative_url }}"></script>