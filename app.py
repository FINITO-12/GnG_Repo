from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': "Rasul",
        'title': "Blog Post 1",
        'content': "First post content",
        'date_posted': 'May 19, 2016'
    },

    {
        'author': "Aqil",
        'title': "Blog Post 2",
        'content': "Second post content",
        'date_posted': 'May 20, 2016'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')