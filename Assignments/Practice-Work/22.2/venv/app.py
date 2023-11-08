from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import story_happy, story_silly, story_smart, story_sad

app = Flask(__name__)

app.config['SECRET_KEY'] = 'testingbasickey'
toolbar = DebugToolbarExtension(app)


@app.route("/")
def ask_story():
    
    return render_template("base2.html")

@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""
    user_story_choice = request.args.get('story_names')
    prompts = story_sad.prompts

    return render_template("questions.html", prompts=prompts, choice=user_story_choice)


@app.route("/story_sad")
def show_story_sad():
    """Show story result."""
    text = story_sad.generate(request.args)

    return render_template("story.html", text=text)

@app.route("/story_happy")
def show_story_happy():
    """Show story result."""
    text = story_happy.generate(request.args)

    return render_template("story.html", text=text)

@app.route("/story_silly")
def show_story_silly():
    """Show story result."""
    text = story_silly.generate(request.args)

    return render_template("story.html", text=text)

@app.route("/story_smart")
def show_story_smart():
    """Show story result."""
    text = story_smart.generate(request.args)

    return render_template("story.html", text=text)



# COMPLIMENTS_MALE = ["handsome", "beautiful", "amazing", "strong"]
# COMPLIMENTS_FEMALE = ["cute", "beautiful", "amazing", "bootylicious"]

# @app.route('/')
# def home_page():
#     return render_template("base.html")

# @app.route('/hello')
# def say_hello():
#     return render_template("hello.html")

# @app.route('/form')
# def render_form():
#     return render_template("form.html")

# @app.route('/form-2')
# def render_form_2():
#     return render_template("form_2.html")

# @app.route('/greet')
# def get_greeting():
#     username = request.args["username"]
#     compliment = choice(COMPLIMENTS_FEMALE)
#     return render_template("greet.html", username=username, compliment=compliment)

# @app.route('/greet-2')
# def get_greeting_2():
#     username = request.args["username"]
#     wants = request.args.get("wants_compliments")
#     gender = request.args.get("is_girl")
#     nice_things = ""
#     if(gender == "on"):
#         nice_things = sample(COMPLIMENTS_FEMALE, 3)
#     else:
#         nice_things = sample(COMPLIMENTS_MALE, 3)

#     return render_template("greet_2.html",gender=gender, username=username, compliments=nice_things, wants_compliments=wants)

# @app.route('/lucky')
# def show_lucky_num():
#     num = randint(1, 10)
#     return render_template('lucky.html', lucky_num = num, msg = "You are so lucky!")

# @app.route('/spell/<word>')
# def spell_word(word):
#     cap_word = word.upper()
#     return render_template("spell.html", word=cap_word)