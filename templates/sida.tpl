{% extends "index.html" %}

{% block content %}
    <div class="container center_text">
        <h2>{{ user['name'] }}</h2>
        <h3>Username: {{ user['username'] }}</h3>
        <h3>Password: <button class="secret">{{ user['password'] }}</button></h3>
        <a href="/" class="button">Til baka</a> <a href="/utskraning" class="button">Útskráning</a>
    </div>
{% endblock %}