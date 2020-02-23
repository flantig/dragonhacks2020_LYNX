# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import csv
from werkzeug.exceptions import HTTPException
from html import escape
from flask import Flask, render_template, json, request



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Lynx - Home")


@app.route('/lookup', methods=["GET"])
def lookup():
    # do something with request.data
    city = escape(request.args.get("search"))

    filtered_data = []

    with open("news.csv", "r") as readfile:
        data = csv.reader(readfile)
        for row in data:
            if city.lower() in row[1].lower() and not row[10].lower() == "none":
                filtered_data.append(row)

    title = "Lookup " + city
    if len(filtered_data) == 0:
        city = ""
        title = "Invalid search!"

    img = get_img(city)
    return render_template("lookup_page.html", city=city, title=title,
                           data=filtered_data[:10], img=img)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return render_template("generic_error.html",
                           code=e.code, name=e.name,
                           description=e.description, title=(str(e.code) + " " + e.name))

def get_img(city):
    images = ["Philly", "Philadelphia", "SanDiego",
              "Boston", "Chicago", "Houston",
              "LogAngeles"]

    for image in images:
        if city.lower().replace(" ", "") in image.lower():
            return "/static/img/Avg" + image + "Sent.png"

    return None



if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_flex_quickstart]