{% extends "index.html" %}

{% block content %}
    <div class="container center_text">
        <form action="" method="post">
            <p><input type="text" name="username" maxlength="32" placeholder="Notendanafn" required></p>
            <p><input type="password" name="password" maxlength="32" minlength="4" placeholder="••••" required><p>
            <p><input type="submit" value="Login"></p>
        </form>
        {% if error == True %}
            <p style="color:#ff0000;">Lykilorðið eða Notendanafnið er rangt</p>
        {% else %}
            <p style="color:#ffffff">_</p>
        {% endif %}
    </div>
{% endblock %}