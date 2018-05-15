---
layout: page
title: Category
---
<ul class="category" id="group">
{% for category in site.categories %}
  <h3>{{ category | first }}</h3> 
    {% for posts in category %}
      {% for post in posts %}
      	{% if post.url %}
        <li>    
          <div class="month">{{ post.date | date:"%Y %b" }}</div>
          <div class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></div>
        </li>
        {% endif %}
      {% endfor %}
    {% endfor %}
    
  
{% endfor %}
</ul>
