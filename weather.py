from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "your_openweathermap_api_key"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city.strip():
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url).json()
            
            if response.get("cod") == 200:
                weather_data = {
                    "city": response["name"],
                    "temperature": response["main"]["temp"],
                    "humidity": response["main"]["humidity"],
                    "condition": response["weather"][0]["description"],
                    "icon": response["weather"][0]["icon"],
                }
            else:
                error = f"City '{city}' not found. Please enter a valid city name."
        else:
            error = "City name cannot be empty. Please enter a valid city."

    return render_template("index.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
