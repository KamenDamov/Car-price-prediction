import gradio as gr
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

#Dictionaries to use for the data
asp = {
    'Standard':'std',
   'Turbo':'turbo'
}

drivew = {
    'Rear wheel drive': 'rwd',
    'Front wheel drive': 'fwd', 
    '4 wheel drive': '4wd'
}

cylnum = {
    2: 'two',
    3: 'three', 
    4: 'four',
    5: 'five', 
    6: 'six', 
    8: 'eight',
    12: 'twelve'
}

#Function to model data to fit the model
def transform(data):
    #Scale the data
    sc= StandardScaler()

    lasso_reg = pickle.load(open('model.pkl','rb'))

    #Columns of the df
    cols = ['CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'wheelbase', 'carlength', 'carwidth', 'carheight', 
    'curbweight', 'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'horsepower', 'citympg', 'highwaympg']

    #Dummy columns of the dummy df
    cols_to_use = ['wheelbase', 'carlength', 'carwidth', 'carheight',\
         'curbweight', 'enginesize', 'boreratio', 'horsepower', \
             'citympg', 'highwaympg', 'CarName_alfa-romero',\
                  'CarName_audi', 'CarName_bmw', 'CarName_buick',\
                       'CarName_chevrolet', 'CarName_dodge', 'CarName_honda',\
                            'CarName_isuzu', 'CarName_jaguar', 'CarName_mazda', 'CarName_mercury', \
                                'CarName_mitsubishi', 'CarName_nissan', 'CarName_peugeot', 'CarName_plymouth', \
                                    'CarName_porsche', 'CarName_renault', 'CarName_saab', 'CarName_subaru', 'CarName_toyota',\
                                         'CarName_volkswagen', 'CarName_volvo', 'fueltype_diesel', 'fueltype_gas', 'aspiration_std',\
                                              'aspiration_turbo', 'doornumber_four', 
                                              'doornumber_two', 'carbody_convertible',
                                               'carbody_hardtop', 'carbody_hatchback', 
                                               'carbody_sedan', 'carbody_wagon',
                                                'drivewheel_4wd', 'drivewheel_fwd', 
                                                'drivewheel_rwd', 'enginelocation_front',
                                                 'enginelocation_rear', 'enginetype_dohc',
                                                  'enginetype_dohcv', 'enginetype_l',
                                                   'enginetype_ohc', 'enginetype_ohcf',
                                                    'enginetype_ohcv', 'enginetype_rotor',
                                                     'cylindernumber_eight', 'cylindernumber_five',
                                                      'cylindernumber_four', 'cylindernumber_six',
                                                       'cylindernumber_three', 'cylindernumber_twelve',
                                                        'cylindernumber_two', 'fuelsystem_1bbl',
                                                         'fuelsystem_2bbl', 'fuelsystem_4bbl',
                                                          'fuelsystem_idi', 'fuelsystem_mfi',
                                                           'fuelsystem_mpfi', 'fuelsystem_spdi', 'fuelsystem_spfi']

    #Dataframe with the new data
    new_df = pd.DataFrame([data],columns = cols)

    cat = []
    num = []
    for col in new_df.columns: 
        if new_df[col].dtypes == 'object': 
            cat.append(col)
        else: 
            num.append(col)

    #Creating the values to feed the model
    x1_new = pd.get_dummies(new_df[cat], drop_first = False)
    x2_new = new_df[num]
    X_new = pd.concat([x2_new,x1_new], axis = 1)

    final_df = pd.DataFrame(columns = cols_to_use)
    final_df = pd.concat([final_df, X_new])
    final_df = final_df.fillna(0)

    X_new = final_df.values
    
    X_new[:, :(len(x1_new.columns))]= sc.fit_transform(X_new[:, :(len(x1_new.columns))])

    output = lasso_reg.predict(X_new)
    return "The price of the car " + str(round(np.exp(output)[0],2)) + "$"

#Main function to predict price
def predict_price(car, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase, carlength, carwidth, 
                carheight, curbweight, enginetype, cylindernumber, enginesize, fuelsystem, boreratio, horsepower, citympg, highwaympg): 

    new_data = [car.lower(), fueltype.lower(), asp[aspiration], doornumber.lower(), carbody, drivew[drivewheel], enginelocation.lower(),
                wheelbase, carlength, carwidth, carheight, curbweight, enginetype, cylnum[cylindernumber], enginesize, fuelsystem, 
                boreratio, horsepower, citympg, highwaympg]
    
    return transform(new_data)
    

car = gr.Dropdown(label = "Car brand", choices=['Alfa-Romero', 'Audi', 'BMW', 'Chevrolet', 'Dodge', 'Honda',
       'Isuzu', 'Jaguar', 'Mazda', 'Buick', 'Mercury', 'Mitsubishi',
       'Nissan', 'Peugeot', 'Plymouth', 'Porsche', 'Renault',
       'Saab', 'Subaru', 'Toyota', 'Volkswagen', 'Volvo'])

fueltype = gr.Radio(label = "Fuel Type", choices = ['Gas', 'Diesel'])

aspiration = gr.Radio(label = "Aspiration type", choices = ["Standard", "Turbo"])

doornumber = gr.Radio(label = "Number of doors", choices = ["Two", "Four"])

carbody = gr.Dropdown(label ="Car body type", choices = ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'])

drivewheel = gr.Radio(label = "Drive wheel", choices = ['Rear wheel drive', 'Front wheel drive', '4 wheel drive'])

enginelocation = gr.Radio(label = "Engine location", choices = ['Front', 'Rear'])

wheelbase = gr.Slider(label = "Distance between the wheels on the side of the car (in inches)", minimum = 50, maximum = 300)

carlength = gr.Slider(label = "Length of the car (in inches)", minimum = 50, maximum = 300)

carwidth = gr.Slider(label = "Width of the car (in inches)", minimum = 50, maximum = 300)

carheight = gr.Slider(label = "Height of the car (in inches)", minimum = 50, maximum = 300)

curbweight = gr.Slider(label = "Weight of the car (in pounds)", minimum = 500, maximum = 6000)

enginetype = gr.Dropdown(label = "Engine type", choices = ['dohc', 'ohcv', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'])

cylindernumber = gr.Radio(label = "Cylinder number", choices = [2, 3, 4, 5, 6, 8, 12])

enginesize = gr.Slider(label = "Engine size (swept volume of all the pistons inside the cylinders)", minimum = 50, maximum = 500)

fuelsystem = gr.Dropdown(label = "Fuel system (link to ressource: ", choices = ['mpfi', '2bbl', 'mfi', '1bbl', 'spfi', '4bbl', 'idi', 'spdi'])

boreratio = gr.Slider(label = "Bore ratio (ratio between cylinder bore diameter and piston stroke)", minimum = 1, maximum = 6)

horsepower = gr.Slider(label = "Horse power of the car", minimum = 25, maximum = 400)

citympg = gr.Slider(label = "Mileage in city (in km)", minimum = 0, maximum = 100)

highwaympg = gr.Slider(label = "Mileage on highway (in km)", minimum = 0, maximum = 100)

Output = gr.Textbox()

app = gr.Interface(title="Predict the price of a car based on its specs", 
                    fn=predict_price,
                    inputs=[car,
                            fueltype,
                            aspiration,
                            doornumber,
                            carbody,
                            drivewheel, 
                            enginelocation, 
                            wheelbase,
                            carlength, 
                            carwidth, 
                            carheight, 
                            curbweight,
                            enginetype, 
                            cylindernumber, 
                            enginesize,
                            fuelsystem,
                            boreratio,
                            horsepower, 
                            citympg, 
                            highwaympg
                            ],
                    outputs=Output)

app.launch()