---
layout: page
title: Archives
---
<ul class="archive" id="group">
  {% for post in site.posts %}
    {% unless post.next %}
      <h3>{{ post.date | date: '%Y' }}</h3>
    {% else %}
      {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
      {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
      {% if year != nyear %}
        <h3>{{ post.date | date: '%Y' }}</h3>
      {% endif %}
    {% endunless %}

    <li>    
        <div class="month">{{ post.date | date:"%b %-d" }}</div>
        <div class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></div>
    </li>
  {% endfor %}
</ul>