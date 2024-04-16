from flask_sqlalchemy import SQLAlchemy     # ORM used to interface with our SQL db
db = SQLAlchemy()
class Contact(db.Model):
# defining the structure of our database 
    id = db.Column(db.Integer, primary_key=True)    # the databases primary key
    first_name = db.Column(db.String(80),  unique=False, nullable=False) # first name non-unique and required
    last_name = db.Column(db.String(80),  unique=False, nullable=False) # last name non-unique and required
    email = db.Column(db.String(120),  unique=True, nullable=False) # email unique and required
    phone =db.Column(db.String(11), unique =True, nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "phone": self.phone
        }