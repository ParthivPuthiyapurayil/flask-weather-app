from flask import Flask, render_template, request
import requests

app = Flask(__name__)
import os

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found. Did you set it in Render environment variables?")


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    temp = None
    city = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code != 200:
                error = "Error fetching data. Please check the city name."
            else:
                data = response.json()
                weather = data['weather'][0]['main']
                temp = data['main']['temp']

    return render_template("index.html", weather=weather, temp=temp, city=city, error=error)

if __name__ == "__main__":
    app.run(debug=True)
