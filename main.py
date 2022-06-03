import utils
# Create an instance of the class Flask:
import flask

app = flask.Flask(__name__)


# Create view for route "/":
@app.route("/")
def main_page():
    return flask.render_template('main_page.html', list_candidates=utils.candidates_list())


# Create view for route "/candidate/<uid>":
@app.route("/candidate/<uid>")
def candidates_name(uid):
    return flask.render_template('candidates_name.html', list_candidates=utils.candidates_list(), name=str(uid))


# Create view for route "/skills/<uid>":
@app.route("/skills/<uid>")
def candidates_skills(uid):
    return flask.render_template('candidates_skills.html', list_candidates=utils.candidates_list(), skills=str(uid))


# Run main.py in this file:
if __name__ == "__main__":
    app.run(debug=True)
