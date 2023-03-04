from coachmentor import db


class Mentors(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), unique=True, nullable=False)
    last_name = db.Column(db.String(25), unique=True, nullable=False)
    bookings = db.relationship(
        "bookings", backref="mentor", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.first_name


class Bookings(db.model):
    id = db.column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.column(db.time, nullable=False)
    team_name = db.Column(db.String(25), unique=True, nullable=False)
    coach_first_name = db.Column(db.String(25), unique=True, nullable=False)
    coach_last_name = db.Column(db.String(25), unique=True, nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey(
        "mentor.id", ondelete="CASCADE"), nullable=False)
