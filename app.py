from flask import Flask, render_template

posts = [
            {
                'Author': 'Harshit Sharma',
                'title': 'First Blog Post',
                'content': 'This is the body of the post!!!',
                'date_posted': '11th December 2019'
            },
            {
                'Author': 'Tony Stark',
                'title': 'About me',
                'content': 'Genius, Playboy, Billionaire, Philanthropist',
                'date_posted': '10th December 2019'
            }

        ]

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html', posts = posts)


@app.route("/about")
def about():
	return "About Page"


if __name__ == "__main__":
	app.run(debug=True)
