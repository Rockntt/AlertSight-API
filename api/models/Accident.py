from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Accident(db.Model):
    type = db.Column(db.String(10), nullable=False)
    source_id = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False, primary_key=True)
    image = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f'<{self.date} - {self.type} - {self.source_id}>'