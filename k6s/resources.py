import base64
from flask import make_response, render_template
from flask_classful import FlaskView, route
from .env import Env

class Instructions(FlaskView):

    def _make_html(self, instructions: str):
        return """
        <!DOCTYPE html>
<html lang="pl">
	<head>
		<title>Hitechwoman</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="/static/css/font.css" type="text/css" rel="stylesheet">
		<link href="/static/css/bootstrap.css" type="text/css" rel="stylesheet">
		<link href="/static/css/base.css" type="text/css" rel="stylesheet">
		<link href="/static/css/page.css" type="text/css" rel="stylesheet">
	</head>
	<body>
		<!-- Header section start Here -->
		<header class="header">
			<div class="container">
				<div class="head-logo">
					<a href="#">
						<img src="/static/images/logo.svg" alt="">
					</a>
				</div>
			</div>
		</header>
		<!-- Header section End Here -->
		<!-- Block section Start Here -->
		<section class="sec-content">
			<div class="content-block">
			    <div class="content-details">
        """ + instructions + """
        </div>
				<div class="content-img">
					<img src="/static/images/woman.png" alt="">
				</div>
			</div>
			<div class="full-shape"></div>
		</section>
		<!-- Block section End Here -->
	</body>
</html>
        """

    @route('/')
    def index(self):
        if Env().is_k8s():
            with open('ins3', 'r') as f:
                ins = base64.b64decode(f.read()).decode('utf-8')
        elif Env().is_docker():
            with open('ins2', 'r') as f:
                ins = base64.b64decode(f.read()).decode('utf-8')
        else:
            with open('ins1', 'r') as f:
                ins = base64.b64decode(f.read()).decode('utf-8')

        response = make_response(self._make_html(ins), 200)
        return response
