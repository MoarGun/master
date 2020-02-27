
from app.forms import LoginForm
@app.route('/login')

def login():
    form = LoginForm()
    return render_template('login.html', title="Sign in', form=form)

