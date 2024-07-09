from flask import Flask, render_template, request
from weather import get_current_weather
# to remove deployment error
from waitress import serve

app = Flask(__name__) #creating an instance of flask
# define routes to pages

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/weather')

def get_weather():
    city = request.args.get('city')# as it is coming from the city that was entered in form
    # check empty strings or str with spaces only
    if not bool(city.strip()):
        city = 'Kingston'
    weather_data = get_current_weather(city)
    # city not found by API COD is the error code(COD) in the api. if found should be 200; not found is 400
    if not weather_data['cod'] == 200:
        return render_template('cityNotFoundError.html')
        
    return render_template(
        'weather.html',
         title = weather_data['name'], #info coming from the json object
         status = weather_data['weather'][0]['description'].capitalize(),
         temp = f"{weather_data['main']['temp']:.1f}",
         feels_like =f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__== "__main__":
    # app.run(host ="0.0.0.0", port = 8000)
    serve(app, host ="0.0.0.0", port = 8000)
    #use serve from waitress



# to fix WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. as we neeed to deploy app ie put it in production

#pip install waitress 
# serves.. puts it in production