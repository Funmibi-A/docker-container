
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Docker Containerization Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Flask Application Running Successfully!</h1>
            <p>This application is containerized using Docker.</p>
            <p>Project: Docker Containerization</p>
            <p>DevOps Engineer on site: Funmibi</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

