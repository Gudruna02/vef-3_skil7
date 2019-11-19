{% extends "index.html" %}

{% block content %}
    <div class="container center_text">
        {% if user['name'] != "none" %}
            <h3>you are logged in as {{ user['username'] }}</h3>
            <a href="/utskraning" class="button">Útskráning</a> <a href="/sida" class="button">Þín síða</a>
        {% else %}
            <a href="/innskraning" class="button">Innskráning</a>
            <a href="/nyrnotandi" class="button">Gera nýan notanda</a>
        {% endif %}
    </div>
{% endblock %}