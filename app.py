from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Create a route to the landing page that displays a dropdown menu
# of the two story options for the user to choose from 

# Creates routes to a landing page endpoint and a results endpoint
# Landing page endpoint uses prompts from silly_story and dynamically
# creates form with prompts as fields.

# Results endpoint dynamically creates a story based on 
# answers provided in landing page form. 


@app.route("/")
def choose_story():
    return render_template('story_choice.html', 
                            silly_story_class = silly_story,
                            excited_story_class = excited_story
        )


@app.route("/question")
def form_creation():
    """ creates form for user input for story creation """
    selected_story = request.args["stories"]
    return render_template("questions.html", prompts = selected_story.prompts)


@app.route("/results")
def story_creation():
    """ creates story based off of user input on form """
    generated_story = silly_story.generate(request.args)
    return render_template("story.html", generated_story = generated_story)