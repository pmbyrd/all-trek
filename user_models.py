
from datetime import datetime
from models import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
# db = SQLAlchemy()

# def connect_db(app):
#     """Connection to the database that is called in app.py for the Flask app to use."""
#     db.app = app
#     db.init_app(app)
DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"

"""This module contains the user model for the database."""

class User(db.Model):
    """Creates a user model for the database."""
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.Text, nullable=False, unique=True)
    
    first_name= db.Column(db.Text, nullable=False)
    
    last_name = db.Column(db.Text, nullable=False)
    
    email = db.Column(db.Text, nullable=False, unique=True)
    
    avatar = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    password = db.Column(db.Text, nullable=False)
    
    bio = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    
    # comments = db.relationship("Comment", backref="user", cascade="all, delete-orphan")
    
    # posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
    
    # tags = db.relationship("Tag", backref="user", cascade="all, delete-orphan")
    
    
    
    @classmethod
    def signup(cls, username, email, password, first_name, last_name, avatar, bio):
        """Signs up a user: hashes their password and adds user to system."""
        
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')
        
        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            bio=bio
        )
        
        db.session.add(user)
        return user
    
    
    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`. If found, return user, else return False."""
        
        user = cls.query.filter_by(username=username).first()
        
        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                bcrypt.check_password_hash(user.password, password)
                if is_auth:
                    return user
                
        return False
    

class Post(db.Model):
    """A post's model for the database."""
    
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True) 
    
    title = db.Column(db.String(80),
                      nullable = False)

    content = db.Column(db.Text,
                         nullable=False)

    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

    
    def __repr__(self):
        return f"<Post #{self.id}: {self.title}, {self.user_id}>"
    

class Tag(db.Model):
    """Generates a table for post tags"""
    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(40), unique=True)
    
    posts = db.relationship('Post',
                            secondary="post_tags",
                            backref="tags")
    
    def __repr__(self):
        return f"<Tag #{self.id}, {self.name}>"
    
    
class PostTag(db.Model):
    """Generates a table for many-to-many relationships"""
    __tablename__ = "post_tags"
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
  
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
    def __repr__(self):
        return f"<Post Tag post_id=#{self.post_id} tag_id=#{self.tag_id}>"
    
    
    
    
    