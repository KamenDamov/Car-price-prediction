import gradio as gr
import numpy as np
import pandas as pd
import pickle

#Dictionaries to use for the data
asp = dict{
    'Standard':'std',
   'Turbo':'turbo'
}



#Main function to predict price
def predict_price(car, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase, carlength, carwidth, 
                carheight, curbweight, enginetype, cylindernumber, enginesize, fuelsystem, boreratio, horsepower, citympg, highwaympg): 
    car = car.lower()
    print(car)
    fueltype = fueltype.lower()
    print(fueltype)
    doornumber = doornumber.lower()

    
    
    
    #model = pickle.load(open('model.pkl','rb'))

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

fuelsystem = gr.Dropdown(label = "Fuel system", choices = ['mpfi', '2bbl', 'mfi', '1bbl', 'spfi', '4bbl', 'idi', 'spdi'])

boreratio = gr.Slider(label = "Bore ratio (ratio between cylinder bore diameter and piston stroke)", minimum = 1, maximum = 6)

horsepower = gr.Slider(label = "Horse power of the car", minimum = 25, maximum = 400)

citympg = gr.Slider(label = "Mileage in city", minimum = 0, maximum = 100)

highwaympg = gr.Slider(label = "Mileage on highway", minimum = 0, maximum = 100)

output = gr.Textbox()

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
                    outputs=output)

app.launch()
#print(model)