from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Accident(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    source_id = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return (f'<{self.r} - {self.type} - {self.source_id}>')