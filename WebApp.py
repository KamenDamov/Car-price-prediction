import gradio as gr
import numpy as np
import pandas as pd
import pickle

def predict_price(input): 
    pass
    #model = pickle.load(open('model.pkl','rb'))

car = gr.Dropdown(label = "Car brand", choices=['Alfa-Romero', 'Audi', 'BMW', 'Chevrolet', 'Dodge', 'Honda',
       'Isuzu', 'Jaguar', 'Mazda', 'Buick', 'Mercury', 'Mitsubishi',
       'Nissan', 'Peugeot', 'Plymouth', 'Porsche', 'Renault',
       'Saab', 'Subaru', 'Toyota', 'Volkswagen', 'Volvo'])

output = gr.Textbox()

app = gr.Interface(title="Predict the price of your car", fn=predict_price,inputs=[car],outputs=output)

app.launch()
#print(model)