from flask import Flask, request, render_template, redirect, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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
    created_at = db.Column(db.String, default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("new_users.id"))

    users = db.relationship('New_User', backref='posts')
    tags = db.relationship('Tag', secondary = 'poststags', backref = 'posts')

    def create_post(new_post):
        db.session.add(new_post)
        db.session.commit()


class PostTag(db.Model):
    __tablename__ = 'poststags'

    post_id= db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key = True)
    tag_id= db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key = True)

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), unique = True)


with app.app_context():
    db.create_all()



@app.route("/")
def user_form():
    all_users = New_User.query.all()
    tag = Tag.query.get(1)
    return render_template("landing.html", all_users = all_users, tag = tag)

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
    tags = Tag.query.all()
    return render_template("add_post.html", user = user, tags = tags)

@app.route("/add_post/<id>", methods = ["POST"])
def add_post(id):
    user = New_User.query.get(id)
    if (user):
        post_content = request.form['content']
        post_title = request.form['title']
        post_created_at = datetime.now()
        tags = request.form.getlist('tags')
        new_post = Post(title = post_title, content = post_content, created_at = post_created_at, user_id = id)
        Post.create_post(new_post)
        if tags:
            for tag in tags:
                temp_post_tag = PostTag(post_id = new_post.id, tag_id = tag)
                db.session.add(temp_post_tag)
                db.session.commit()
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
    tags = request.form.getlist('tag_name')
    if(request.method == 'GET'):
        
        return render_template("all_posts.html", posts=posts, tags=tags)
    else:
        return render_template("all_posts.html", posts=posts, tags=tags)

@app.route("/edit_post_form/<id>")
def edit_post_form(id):
     post = Post.query.get(id)
     tags = Tag.query.all()
     return render_template("edit_post_form.html", post = post, tags = tags)

@app.route("/edit_post/<id>", methods = ['POST'])
def edit_post(id):
    post = Post.query.get(id)
    post.title = request.form['title']
    post.content = request.form['content']
    all_post_tag = PostTag.query.filter_by(post_id = post.id).all()
    tags = request.form.getlist('tags')
    for tag in all_post_tag:
        db.session.delete(tag)
        db.session.commit()
    for tag in tags:
            temp_post_tag = PostTag(post_id = post.id, tag_id = tag)
            db.session.add(temp_post_tag)
            db.session.commit()

    return redirect(f"/view_all_posts/{post.user_id}")

@app.route("/delete_post/<id>")
def delete_post(id):
     post = Post.query.get(id)
     db.session.delete(post)
     db.session.commit()
     return redirect(f"/user{post.user_id}")

@app.route("/tags")
def tags_detail():
    all_tags = Tag.query.all()
    return render_template("all_tags.html", all_tags = all_tags)

@app.route("/tags/<id>")
def tag_detail(id):
    tag = Tag.query.get(id)
    return render_template("show_tag.html", tag = tag)

@app.route("/tags/new", methods = ['POST', 'GET'])
def create_tag():
    if (request.method == 'GET'):
        return render_template("create_tag.html")
    else:
        tag_name = request.form['tag_name']
        db.session.add(Tag(name = tag_name))
        db.session.commit()
        return redirect("/")

@app.route("/tags/<id>/edit", methods = ['GET', 'POST'])
def show_edit_form(id):
    tag = Tag.query.get(id)
    if(request.method == "GET"):
        return render_template("tag_edit_form.html", tag = tag)
    else:
        tag.name = request.form['tag_name']
        db.session.add(tag)
        db.session.commit()
        return redirect('/')
    
@app.route("/tags/<id>/delete")
def delete_tag(id):
    tag = Tag.query.get(id)
    db.session.delete(tag)
    db.session.commit()
    return redirect('/')