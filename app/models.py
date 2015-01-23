from app import db

class Ads(db.Model):
        __tablename__ = 'Ads'
        id = db.Column(db.Integer, primary_key=True)
        ad = db.Column(db.String(10000))

        def __init__(self,ad):
                self.ad = ad
