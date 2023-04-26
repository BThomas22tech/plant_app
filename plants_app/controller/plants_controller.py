from plants_app import app
from datetime import timedelta,datetime
from plants_app.models.plants_model import Plants
from flask import render_template,session, request,redirect,session,flash
from flask import url_for
@app.route('/')
def show_plants():
    plants = Plants.get_all_plants()
    # for plant in plants:
    #     plant.harvest_date = plant.when_planted + timedelta(days=plant.days_to_maturity)
    # image_file = url_for('static', filename="/hand_plant.jpg")
    return render_template("index.html", plants = plants)

@app.route('/new_plant')
def new_plant():
    return render_template("new_plant.html")

@app.route('/added_plant', methods= ['POST'])
def added_plant():
    when_planted = datetime.strptime(request.form['when_planted'], '%Y-%m-%d')
    days_to_maturity = int(request.form['days_to_maturity'])
    harvest_date = when_planted + timedelta(days=days_to_maturity)
    
    print("harvest date:", harvest_date)

    plant_data = {
        'name': request.form['name'],
        'days_to_maturity': request.form['days_to_maturity'],
        'when_planted': request.form['when_planted'],
        'date_to_harvest': harvest_date,
        'updated_at' : 'updated_at',
        'created_at' :'created_at',
        'number_of_packets': request.form['number_of_packets']
    }
    print("plant info:", plant_data)
    Plants.save(plant_data)
    return redirect('/')

@app.route('/edit_plant/<int:id>')
def edit_plant(id):
    data = {'id': id}

    plant = Plants.get_one_plant(data)
    Plants.edit_plants(request.form)
    return render_template('edit_plant.html', plant = plant)

@app.route('/edited_plant/<int:id>', methods = ['POST'])
def edited_plant(id):
    when_planted = datetime.strptime(request.form['when_planted'], '%Y-%m-%d')
    days_to_maturity = int(request.form['days_to_maturity'])
    harvest_date = when_planted + timedelta(days=days_to_maturity)
    data = {"id":id,
        'name': request.form['name'],
        'days_to_maturity': request.form['days_to_maturity'],
        'when_planted': request.form['when_planted'],
        'date_to_harvest': harvest_date,
        'updated_at' : 'updated_at',
        'created_at' :'created_at',
        'number_of_packets': request.form['number_of_packets']
        }
    
    Plants.edit_plants(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_plant(id):
    data = {
        'id': id
    }
    print(data)
    Plants.delete(data)
    return redirect('/')