from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Creates routes to a landing page endpoint and a results endpoint
# Landing page endpoint uses prompts from silly_story and dynamically
# creates form with prompts as fields.

# Results endpoint dynamically creates a story based on 
# answers provided in landing page form. 

@app.route("/")
def form_creation():
    """ creates form for user input for story creation """
    return render_template("questions.html", prompts = silly_story.prompts)

@app.route("/results")
def story_creation():
    """ creates story based off of user input on form """
    generated_story = silly_story.generate(request.args)
    return render_template("story.html", generated_story = generated_story)