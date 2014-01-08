import flask, flask.views
import sayings

app = flask.Flask(__name__)

app.secret_key = "bacon"

class Page1(flask.views.MethodView):
	def get(self):
		
		phrase = sayings.say_it()		

		return flask.render_template("index.html", phrase = phrase)

app.add_url_rule("/Jo", view_func=Page1.as_view("base"), methods=["GET"])

if __name__ == '__main__':
#app.debug = True
app.run()
