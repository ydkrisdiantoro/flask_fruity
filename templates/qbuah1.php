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

            <!-- <form action="#"> -->
            <h2 class="cover-heading">Sudah Makan Buah Hari Ini?</h2>

            <a href="qbuah2" class="btn btn-light">Sudah</a>
            <a href="qbuah3" class="btn btn-light">Belum</a>
            <!-- </form> -->

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