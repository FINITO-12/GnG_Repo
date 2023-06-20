from flask import Flask, render_template, flash, redirect, url_for

from forms.forms import RegistrationForm, LogInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '44a2568b40bd2974d01abad1dd4825d9'

# basis = Database("x", "x", "x", "x")
# conn = basis.connect()
# cursor = basis.createCursor(conn=conn)
# basis.insert("soska", "sosochka")
# basis.closeCursor(conn)
# basis.disconnect(conn)

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


@app.route("/userprofile")
def userProfile():
    pass


@app.route("/steam")
def steamTransaction():
    pass


@app.route("/steamtl")
def steamTransactionTL():
    pass


@app.route("/minecraft")
def minecraft():
    pass


@app.route("/playstation")
def psTransaction():
    pass


@app.route("/playstationplus")
def psplusTransaction():
    pass


@app.route("/registration", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LogInForm()
    return render_template('login.html', title='Log in', form=form)
