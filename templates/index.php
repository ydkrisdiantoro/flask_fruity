{% extends "page.html" %}
{% block content %}

    <div class="container d-flex h-100 p-3 mx-auto flex-column text-center">
        <header class="masthead mb-auto">
            <div class="inner">
                <!-- <h3 class="masthead-brand">Fruity</h3> -->
                <nav class="nav nav-masthead justify-content-center">
                    <a class="nav-link" href="/" style="border-bottom-color: rgba(255, 255, 255, .5)!important;">Home</a>
                    <a class="nav-link" href="/about">About</a>
                    <a class="nav-link" href="/credit">Credit</a>
                </nav>
            </div>
        </header>

        <main role="main" class="inner cover px-lg-5 my-auto">

            <h1 class="cover-heading">Selamat Datang di Fruity!</h1>
            <p class="lead">Ketahui infomasi kebutuhan Buah dan Sayur Anda untuk memenuhi Standar Gizi!</p>
            <p class="lead">
                <a href="qbuah1" class="btn btn-light">Mulai Sekarang</a>
            </p>

        </main>

        <footer class="mastfoot mt-auto">
            <div class="inner">
                <small>
                    <p class="mb-0">Bangkit 2021</p>
                    Capstone Project - <a href="mailto:y.d.krisdiantoro@gmail.com">B21-CAP0456</a>
                </small>
            </div>
        </footer>
    </div>

{% endblock %}