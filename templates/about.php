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
                    <a class="nav-link" href="/about" style="border-bottom-color: rgba(255, 255, 255, .5)!important;">About</a>
                    <a class="nav-link" href="/credit">Credit</a>
                </nav>
            </div>
        </header>

        <main role="main" class="inner cover px-lg-5 my-auto">

            <h1 class="cover-heading">About Us</h1>
            <div class="row justify-content-md-center">
                <div class="col-md-6 col-sm-12">
                    <p class="lead"><b>Fruity</b> adalah platform yang dapat membantu Anda untuk mengkonsumsi buah-buahan sesuai dengan kebutuhan standar gizi harian</p>
                </div>
            </div>
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


    <div class="modal fade" id="Yayan" tabindex="-1" aria-labelledby="YayanLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="YayanLabel">Modal title</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
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