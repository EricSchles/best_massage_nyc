from app import app
import datetime
import os
from flask import render_template, request, redirect
from models import Ads
from subprocess import call

@app.route("/index",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def index():
	return render_template("index.html")#,show_results=False)

@app.route("/Scraper",methods=["GET","POST"])
def scraping():
        call(["python","../bp_scraper.py"]) #because heroku
        
        return Ads.query.all() #this is a place holder, add subprocess

@app.route("/AdResults",methods=["GET","POST"])
def ad_results():
        return render_template("results.html")#,ads=Ads.query.all())
