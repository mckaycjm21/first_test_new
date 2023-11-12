from flask import Flask, render_template, request, redirect, flash, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey, personality_quiz as p_survey, surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = 'testingbasickey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

SESSION_RES = "session_responses"
SESSION_SURVEY = "session_survey"


@app.route('/', methods=['GET', 'POST'])
def pick_survey():

    if request.method == 'POST':
        choice = request.form['survey_choice']
        return redirect(url_for('survey_start', choice=choice))
    return render_template('index.html')

@app.route('/survey_start/<string:choice>')
def survey_start(choice):
    sess = session[SESSION_SURVEY]
    sess = choice
    session[SESSION_SURVEY] = sess
    if choice == "personality":
        sess = p_survey
    else:
        sess = survey
    title = sess.title
    instructions = sess.instructions
    return render_template('survey_start.html',title=title, instructions=instructions)

@app.route('/begin', methods=["POST"])
def begin_survey():
    session[SESSION_RES] = []
    return redirect("/questions/0")

@app.route('/user_response', methods=["POST"])
def handle_user_response():
    surve = session[SESSION_SURVEY]
    sur = surveys[surve]
    choice = request.form['answer']
    responses = session[SESSION_RES]
    responses.append(choice)
    session[SESSION_RES] = responses

    if (len(responses) == len(sur.questions)):

        return redirect("/survey_complete")

    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:sesid>')
def show_question(sesid):
    surve = session[SESSION_SURVEY]
    sur = surveys[surve]
    responses = session.get(SESSION_RES)

    if (responses is None):

        return redirect("/")
    if (len(responses) == len(sur.questions)):

        return redirect("/survey_complete")

    if (len(responses) != sesid):

        flash(f"Invalid question id: {sesid}.")
        return redirect(f"/questions/{len(responses)}")

    question = sur.questions[sesid]
    return render_template(
        "survey_question.html", question_num=sesid, question=question)




@app.route('/survey_complete')
def survey_complete():
    surve = session[SESSION_SURVEY]
    sur = surveys[surve]
    return render_template('survey_complete.html', survey=sur)
