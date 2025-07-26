from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/home')
def home():
    return render_template("index.html")

@auth.route('/profile')
def profile():
    return render_template("profile.html")

@auth.route('/accessibility')
def accessibility():
    return render_template("accessibility.html")

@auth.route('/management_supervision_and_coordination_of_construction_works')
def management_supervision():
    return render_template("management_supervision.html")

@auth.route('/Management_of_supervision_and_coordination_of_water_drainage_and_sewerage_infrastructures_in_water_corporations')
def Management_of_supervision_and_coordination_of_water_drainage_and_sewerage_infrastructures_in_water_corporations():
    return render_template("Management_of_supervision_and_coordination_of_water_drainage_and_sewerage_infrastructures_in_water_corporations.html")

@auth.route('/Gardening_works_and_open_public_space')
def Gardening_works_and_open_public_space():
    return render_template("Gardening_works_and_open_public_space.html")

@auth.route('/Construction_of_sewage_plants_and_wastewater_treatment_plants_and_their_ongoing_maintenance')
def Construction_of_sewage_plants_and_wastewater_treatment_plants_and_their_ongoing_maintenance():
    return render_template("Construction_of_sewage_plants_and_wastewater_treatment_plants_and_their_ongoing_maintenance.html")

@auth.route('/Earth_development_works_on_roads')
def Earth_development_works_on_roads():
    return render_template("Earth_development_works_on_roads.html")

@auth.route('/Accompanying_and_supervision_of_urban_development_works')
def Accompanying_and_supervision_of_urban_development_works():
    return render_template("Accompanying_and_supervision_of_urban_development_works.html")

@auth.route('/fuel_and_gas_infrastructures')
def fuel_and_gas_infrastructures():
    return render_template("fuel_and_gas_infrastructures.html")

@auth.route('/requirements')
def requirements():
    return render_template("requirements.html")