from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/profile/<name>')
# def profile(name):
#     return render_template("profile.html", name=name)
#
# @app.route('/')
# def index():
#     return '<h3>method used: %s</h3>' % request.method
#
#
# @app.route('/bacon', methods=['GET','POST'])
# def bacon():
#     if request.method == 'POST':
#         return "you are using POST"
#     else:
#         return "you are using GET"

# @app.route('/profile/<username>') #<var>
# def profile(username):
#     return 'hello %s' % username
#
#
# @app.route('/post/<int:post_id>') #<var> integer
# def show_post(post_id):
#     return 'post id is  %s' % post_id
#
@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html",user=user)

@app.route('/shopping')
def shopping():
    food = ["cheese","tuna","beef"]
    return render_template("shopping.html",food=food)

if __name__ == "__main__":
    app.run(debug=True)
