
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
