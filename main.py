from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def MarsPicture():
    r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key=DEMO_KEY")
    jsondata = json.loads(r.text)
    photos = jsondata['latest_photos']

    enumerated_photos = list(enumerate(photos, 1))

    return render_template('index.html', photos=enumerated_photos)

if __name__ == '__main__':
    app.run(debug=True)