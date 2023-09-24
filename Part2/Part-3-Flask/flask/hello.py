from flask import Flask
from flask import render_template

from markupsafe import escape
app = Flask(__name__)

#-----------------------------------------------------------------------------------------

# @app.route("/")
# def hello_world():
#     # return "<script>alert('Boom')</script>"
#     return f"Hello, {escape('<script>alert(Boom)</script>')}!"

#------------------------------------------------------------------------------------------

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

#-------------------------------------------------------------------------------------------

# from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

#-------------------------------------------------------------------------------------------

# from markupsafe import escape

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

# from flask import url_for

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

#-------------------------------------------------------------------------------------------

# from flask import request

# def do_the_login():
#     return 'login OK'

# def show_the_login_form():
#     return 'show login form'  

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

#-------------------------------------------------------------------------------------------
# def do_the_login():
#     return 'login OK'

# def show_the_login_form():
#     return 'show login form' 

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

#-------------------------------------------------------------------------------------------
# from flask import url_for
# @app.route('/')
# def index():
#     return url_for('static', filename='style\styles.css')

#-------------------------------------------------------------------------------------------



@app.route('/tags/')
def hello(name='Bob'):
    return render_template('stas.html', name=name)

#-------------------------------------------------------------------------------------------

@app.route('/train/from/<FromCity>/to/<ToCity>')
def timelist(FromCity,ToCity):
    # Select * from database
    return render_template('hello.html', cityA = FromCity, cityB = ToCity)

#-------------------------------------------------------------------------------------------
# from flask import request, render_template


# def valid_login(user, passw):
#     # select * from users where user_name like user
#     user_db = 'kovalyuk'
#     pass_db = '1234'

#     return (user == user_db) and (pass_db == passw)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['passw']):
#             return 'OK, Hello'
#         else:
#             error = 'Invalid username/password'

#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error_desc=error)

#-------------------------------------------------------------------------------------------

@app.route('/train/list')

def train_list():
    return render_template('train.html')