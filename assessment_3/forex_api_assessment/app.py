from flask import Flask, request, render_template, redirect, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime, timezone


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "donttellanyone123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

db = SQLAlchemy(app)

class New_User(db.Model):
    __tablename__ = "new_users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    image_url = db.Column(db.String, unique = True)

    posts = db.relationship('Post')


    def greet(self):
        return f"Hi my name is {self.first_name} {self.last_name}"

    def create_user(new_user):
        db.session.add(new_user)
        db.session.commit()

    def delete_user(user):
         db.session.delete(user)
         db.session.commit()

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50))
    content = db.Column(db.String)
    created_at = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("new_users.id"))

    user_info = db.relationship('New_User')

    def create_post(new_post):
        db.session.add(new_post)
        db.session.commit()

with app.app_context():
    db.create_all()



@app.route("/")
def user_form():
    all_users = New_User.query.all()
    return render_template("landing.html", all_users = all_users)

@app.route("/add_user_form")
def add_user_form():
     return render_template("add_user.html")

@app.route("/add_user", methods = ["POST"])
def add_user():
        new_user = New_User(
                first_name = request.form['first_name'],
                last_name = request.form['last_name'], 
                image_url = request.form['image_url'],
                )              
        New_User.create_user(new_user)
        user = New_User.query.filter_by(image_url = new_user.image_url).first()
        return redirect(f"/confirmation/{user.id}")

@app.route('/confirmation/<id>')
def confirmation_page(id):
    user = New_User.query.filter_by(id = id).first()
    return render_template("confirmation.html", user = user)

@app.route('/all_users')
def all_users():
     all_users = New_User.query.all()
     return render_template('all_users.html', all_users = all_users)

@app.route('/delete_user/<id>',methods = ["POST"])  
def delete_user(id):
     user = New_User.query.get(id)
     New_User.delete_user(user)
     return redirect(f"/delete_confirmation/{user.id}")

@app.route('/edit_user_form/<id>')
def edit_user_form(id):
     user = New_User.query.get(id)
     return render_template("/edit_user_form.html", user = user)

@app.route('/edit_user/<id>', methods = ["POST"])
def edit_user(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    user = New_User.query.get(id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.add(user)
    db.session.commit()
    return redirect("/")

@app.route('/delete_confirmation/<id>')
def delete_confirmation_page(id):
    return render_template("delete_confirmation.html", id = id)

@app.route('/user<id>')
def user_page(id):
     user = New_User.query.get(id)
     return render_template("user.html", user = user)

@app.route("/add_post_form/<id>")
def add_post_form(id):
    user = New_User.query.get(id)
    return render_template("add_post.html", user = user)

@app.route("/add_post/<id>", methods = ["POST"])
def add_post(id):
    user = New_User.query.get(id)
    if (user):
        post_content = request.form['content']
        post_title = request.form['title']
        post_created_at = datetime.now()
        new_post = Post(title = post_title, content = post_content, created_at = post_created_at, user_id = id)
        Post.create_post(new_post)
        return redirect(f'/view_all_posts/{id}')
    else:
         return redirect("/error.html")

@app.route("/view_post/<id>")
def view_post(id):
     post = Post.query.get(id)
     return render_template("post.html", post = post)

@app.route("/view_all_posts/<id>", methods = ["GET", "POST"])
def view_all_posts(id):
    posts = Post.query.filter_by(user_id = id).all()
    if(request.method == 'GET'):
        return render_template("all_posts.html", posts=posts)
    else:
        return render_template("all_posts.html", posts=posts)

@app.route("/edit_post_form/<id>")
def edit_post_form(id):
     post = Post.query.get(id)
     return render_template("edit_post_form.html", post = post)

@app.route("/edit_post/<id>", methods = ['POST'])
def edit_post(id):
    post = Post.query.get(id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.add(post)
    db.session.commit()
    return redirect(f"/view_all_posts/{post.user_id}")

@app.route("/delete_post/<id>")
def delete_post(id):
     post = Post.query.get(id)
     db.session.delete(post)
     db.session.commit()
     return redirect(f"/user{post.user_id}")
