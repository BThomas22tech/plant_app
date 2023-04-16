from plants_app import app
from datetime import timedelta
from plants_app.models.plants_model import Plants
from flask import render_template,session, request,redirect,session,flash

@app.route('/')
def show_plants():
    plants = Plants.get_all_plants()
    for plant in plants:
        plant.harvest_date = plant.when_planted + timedelta(days=plant.days_to_maturity)
    return render_template("index.html", plants = plants)
