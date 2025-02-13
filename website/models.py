from datetime import datetime
from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# PROXIMOS PASSOS
# CRIAR CLASSES EVENTO E INGRESSO
# INSTALAR A CLASSE FLASK BOOTSTRAP DO VIDEO TEMPLATES E VER SE FAZ ALGUMA DIFERENCA

# Class description
class User(db.Model, UserMixin):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    # Choices (Male = 1, Female = 2, Not applicable = 3)
    gender = db.Column(db.Integer, nullable=False, default=1)

    # user image hash
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    # foreign key = Role (common user = 1)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, default=1)

    # relationship = User | one to Many | Match
    matches = db.relationship('Match', backref='owner', lazy=True)

    '''
     ***** ALTERAR NO FUTURO QUANDO DECIDIRMOS SE VAMOS IMPLEMENTAR MENSAGENS (OU NAO) *****
    # relationship = User | one to Many | Message
    messages = db.relationship('User', backref='role', lazy=True)
    '''

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}', '{self.role.name}')"

'''
 ***** ISSO AQUI FOI SO PRA TESTAR, APAGAR DEPOIS *****
# Class description
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
'''


# Class description
class Role(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), unique=True, nullable=False)

    # relationship = Role | one to Many | User
    users = db.relationship('User', backref='role', lazy=True)

    def __repr__(self):
        return f"Role('{self.id}', '{self.name}')"

'''
# Class description
# Male = 1, Female = 2, Neutral = 3, Not applicable = 4
class Gender(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), unique=True, nullable=False)

    # relationship = Role | one to Many | User
    users = db.relationship('User', backref='gender', lazy=True)

    def __repr__(self):
        return f"Gender('{self.id}', '{self.name}')"
'''

# Class description
class Match(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # ***** MUDAR PARA UM PONTO GEOGRAFICO DEPOIS ?????? *****
    location = db.Column(db.String(50), nullable=False, default='Torino')

    # foreign key = Sport
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)

    # foreign key = User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Match('{self.title}', '{self.date}', '{self.sport.name}')"

# Class description
class Sport(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), unique=True, nullable=False)

    # relationship = Sport | one to Many | Match
    matches = db.relationship('Match', backref='sport', lazy=True)

    def __repr__(self):
        return f"Sport('{self.name}')"



'''
 ***** ALTERAR NO FUTURO QUANDO DECIDIRMOS SE VAMOS IMPLEMENTAR MENSAGENS (OU NAO) *****
#Class description
class Message(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # foreign key = User
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # foreign key = User
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Message('{self.content}', '{self.date_posted}')"

'''