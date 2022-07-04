import gradio as gr
import numpy as np
import pandas as pd
import pickle

#Main function to predict price
def predict_price(input): 
    pass
    #model = pickle.load(open('model.pkl','rb'))

car = gr.Dropdown(label = "Car brand", choices=['Alfa-Romero', 'Audi', 'BMW', 'Chevrolet', 'Dodge', 'Honda',
       'Isuzu', 'Jaguar', 'Mazda', 'Buick', 'Mercury', 'Mitsubishi',
       'Nissan', 'Peugeot', 'Plymouth', 'Porsche', 'Renault',
       'Saab', 'Subaru', 'Toyota', 'Volkswagen', 'Volvo'])

fuel = gr.Radio(label = "Fuel Type", choices = ['Gas', 'Diesel'])

aspiration = gr.Radio(label = "Aspiration type", choices = ["Standard", "Turbo"])

door_number = gr.Radio(label = "Number of doors", choices = ["Two", "Four"])

car_body = gr.Dropdown(label ="Car body type", choices = ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'])

output = gr.Textbox()

app = gr.Interface(title="Predict the price of your car", 
                    fn=predict_price,
                    inputs=[car,
                            fuel,
                            aspiration,
                            door_number,
                            car_body,
                            
                            ],
                    outputs=output)

app.launch()
#print(model)