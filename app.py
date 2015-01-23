from flask import Flask, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime
from scraper import Scraper
app = Flask(__name__)

production = False
if 'ON_HEROKU' in os.environ:
        production = True

if production:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
        db = SQLAlchemy(app)

else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///foo.db"
        db = SQLAlchemy(app)
#http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku


class Ads(db.Model):
        __tablename__ = 'Ads'
        id = db.Column(db.Integer, primary_key=True)
        ad = db.Column(db.String(10000))

        def __init__(self,ad):
                self.ad = ad
        
@app.route("/index",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def index():
	return render_template("index.html",show_results=False)

@app.route("/Scraper",methods=["GET","POST"])
def scraping():
        s = Scraper(testing=True)
        ads = s.get_ads()
        #print ads
        for ad in ads:
               ad = Ads(ad)
               db.session.add(ad)
               db.session.commit()
        return render_template("/index",show_results=True)

@app.route("/AdResults",methods=["GET","POST"])
def ad_results():
        return render_template("results.html",ads=Ads.query.all())

if __name__ == '__main__':
	app.run(debug=True)
