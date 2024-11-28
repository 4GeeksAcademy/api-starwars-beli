from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "name": self.name
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "population": self.population,
            "name": self.name
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    age = db.Column(db.Integer)
    eye_color = db.Column(db.String(250))

    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "age": self.age,
            "name": self.name,
            "eye_color": self.eye_color
        }

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    person= db.relationship("User")
    planet_id= db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet= db.relationship("Planet")
    people_id= db.Column(db.Integer, db.ForeignKey("people.id"))
    people= db.relationship("People")

    def __repr__(self):
        return '<Favoritos %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id

        }

