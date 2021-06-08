<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous"> -->

    <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/cover.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/style.css') }}">

    <title>Fruity</title>

    <style>
        body {
            background: #efefef;
        }
    </style>
</head>

<body>


    <div class="container d-flex h-100 p-3 mx-auto flex-column text-center">
        <header class="masthead mb-auto">
            <div class="inner">
                <!-- <h3 class="masthead-brand">Fruity</h3> -->
                <nav class="nav nav-masthead justify-content-center">
                    <a class="nav-link" href="/">Home</a>
                    <a class="nav-link" href="/about">About</a>
                    <a class="nav-link" href="/credit" style="border-bottom-color: rgba(255, 255, 255, .5)!important;">Credit</a>
                </nav>
            </div>
        </header>

        <main role="main" class="inner cover px-lg-5 my-auto">

            <h1 class="cover-heading">Credit</h1>
            <p class="lead">Sistem ini dibuat oleh TIM Bangkit B21-CAP0456</p>

            <div class="card-group text-dark mt-5">
                <div class="card">
                    <img src="{{ url_for('static', filename='assets/img/yayan.jpg') }}" class="card-img-top" alt="Yayan Dwi Krisdiantoro">
                    <div class="card-body">
                        <h5 class="card-title" >Yayan Dwi Krisdiantoro</h5>
                        <p class="card-text">Universitas Negeri Semarang<br>Cloud Computing</p>
                        <p class="card-text bg-dark text-white"><small><a href="http://wa.me/6285156107936 " target="_blank" rel="noopener noreferrer">phone</a> - <a href="https://www.linkedin.com/in/yayan-dwi-krisdiantoro-1258b6163" target="_blank" rel="noopener noreferrer">linkedin</a></small></p>
                    </div>
                </div>
                <div class="card">
                    <img src="{{ url_for('static', filename='assets/img/fauza.jpg') }}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Ahmad Fauza Aulia</h5>
                        <p class="card-text">Universitas Negeri Semarang<br>Cloud Computing</p>
                        <p class="card-text bg-dark text-white"><small><a href="http://wa.me/6281215212066" target="_blank" rel="noopener noreferrer">phone</a> - <a href="https://www.linkedin.com/in/fauzaaulia/" target="_blank" rel="noopener noreferrer">linkedin</a></small></p>
                    </div>
                </div>
                <div class="card">
                    <img src="{{ url_for('static', filename='assets/img/dimitri.jpg') }}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Akhmad Dimitri Baihaqi</h5>
                        <p class="card-text">Universitas Brawijaya<br>Machine Learning</p>
                        <p class="card-text bg-dark text-white"><small><a href="http://wa.me/6281335485425" target="_blank" rel="noopener noreferrer">phone</a> - <a href="https://www.linkedin.com/in/dimitribaihaqi/" target="_blank" rel="noopener noreferrer">linkedin</a></small></p>
                    </div>
                </div>
                <div class="card">
                    <img src="{{ url_for('static', filename='assets/img/wildan.jpg') }}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Muhammad Wildan Oktavian</h5>
                        <p class="card-text">Universitas Brawijaya<br>Machine Learning</p>
                        <p class="card-text bg-dark text-white"><small><a href="http://wa.me/6287846055293" target="_blank" rel="noopener noreferrer">phone</a> - <a href="https://www.linkedin.com/in/wildan-oktavian-b93858178/" target="_blank" rel="noopener noreferrer">linkedin</a></small></p>
                    </div>
                </div>
            </div>

            <h5 class="cover-heading mt-5">Terimakasih Kepada</h5>
            <p class="lead">Pembimbing TIM Bangkit B21-CAP0456</p>

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


    <!-- Optional JavaScript; choose one of the two! -->

    <script type="text/javascript" src="{{ url_for('static', filename='assets/js/feather.min.js') }}"></script>
    <script>
        feather.replace()
    </script>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <!-- <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script> -->

    <!-- Offline JS -->
    <script src="{{ url_for('static', filename='assets/js/jquery.min.js') }}"></script>
    <script src="{{ url_for('static', filename='assets/js/popper.min.js') }}"></script>
    <script src="{{ url_for('static', filename='assets/js/bootstrap.min.js') }}"></script>
</body>

</html>