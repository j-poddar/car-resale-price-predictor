# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)

# Load the Random Forest CLassifier model
filename = 'car_resale_price_prediction_rf.pkl'
model = pickle.load(open(filename, 'rb'))



@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=["GET","POST"])
def predict():
    if request.method == 'POST':
        
        #car_brand
        car_brand = request.form['car_brand']
        # Ambassador = 0
        if(car_brand=='Maruti'):
            Maruti = 1
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0
        elif (car_brand=='Hyndai'):
            Maruti = 0
            Hyundai = 1
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0
        elif (car_brand=='Mahindra'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 1
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0 
        elif (car_brand=='Tata'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 1
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0           
        elif (car_brand=='Honda'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 1
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0   
        elif (car_brand=='Ford'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 1
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0      
        elif (car_brand=='Toyota'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 1
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0  
        elif (car_brand=='Chevrolet'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 1
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='Renault'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 1
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='Volkswagen'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 1
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0  
        elif (car_brand=='Skoda'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 1
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='Nissan'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 1
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='Audi'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 1
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0        
        elif (car_brand=='BMW'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 1
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0  
        elif (car_brand=='Fiat'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 1
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0       
        elif (car_brand=='Mercedes_Benz'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 1
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0       
        elif (car_brand=='Mitsubishi'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 1
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='Jaguar'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 1
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='Land'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 1
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0  
        elif (car_brand=='Volvo'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 1
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0
        elif (car_brand=='Jeep'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 1
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0    
        elif (car_brand=='OpelCorsa'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 1
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0              
        elif (car_brand=='MG'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 1
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0              
        elif (car_brand=='Kia'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 1
            Daewoo = 0
            Isuzu = 0
            Force = 0              
        elif (car_brand=='Daewoo'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 1
            Isuzu = 0
            Force = 0              
        elif (car_brand=='Isuzu'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 1
            Force = 0              
        elif (car_brand=='Force'):
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 1
        else:
            Maruti = 0
            Hyundai = 0
            Mahindra = 0
            Tata = 0
            Honda = 0
            Ford = 0
            Toyota = 0
            Chevrolet = 0
            Renault = 0
            Volkswagen = 0
            Skoda = 0
            Nissan = 0
            Audi = 0
            BMW = 0
            Fiat = 0
            Datsun = 0
            Mercedes_Benz = 0
            Mitsubishi = 0
            Jaguar = 0
            Land = 0
            Volvo = 0
            Jeep = 0
            OpelCorsa = 0
            MG = 0
            Kia = 0
            Daewoo = 0
            Isuzu = 0
            Force = 0       
            
            
        #Fuel    
        fuel = request.form["fuel"]    
        # CNG = 0 (not in column)
        if (fuel=='Petrol'):
            Petrol = 1
            Diesel = 0
            LPG = 0
            Electric = 0
        elif (fuel=='Diesel'):
            Petrol = 0
            Diesel = 1
            LPG = 0
            Electric = 0
        elif (fuel=='LPG'):
            Petrol = 0
            Diesel = 0
            LPG = 1
            Electric = 0   
        elif (fuel=='Electric'):
            Petrol = 0
            Diesel = 0
            LPG = 0
            Electric = 1
        else:
            Petrol = 0
            Diesel = 0
            LPG = 0
            Electric = 0  
              
        #seller_type
        seller_type = request.form['seller_type']
        # Dealer = 0 (not in column)
        if (seller_type == 'Individual'):
              Individual = 1
              Trustmark_Dealer = 0
        elif (seller_type == 'Trustmark_Dealer'):
              Individual = 0
              Trustmark_Dealer = 1    
        else:
              Individual = 0
              Trustmark_Dealer = 0
              
        #owner
        owner = request.form['owner']
        #First_Owner = 0 (Not in column)
        if (owner == 'Fourth_and_Above_Owner'):
            Fourth_and_Above_Owner = 1
            Second_Owner = 0
            Test_Drive_Car = 0
            Third_Owner = 0
        elif (owner == 'Second_Owner'):
            Fourth_and_Above_Owner = 0
            Second_Owner = 1
            Test_Drive_Car = 0
            Third_Owner = 0
        elif (owner == 'Test_Drive_Car'):
            Fourth_and_Above_Owner = 0
            Second_Owner = 0
            Test_Drive_Car = 1
            Third_Owner = 0
        elif (owner == 'Third_Owner'):
            Fourth_and_Above_Owner = 0
            Second_Owner = 0
            Test_Drive_Car = 0
            Third_Owner = 1
        else:
            Fourth_and_Above_Owner = 0
            Second_Owner = 0
            Test_Drive_Car = 0
            Third_Owner = 0
            
        #transmission
        transmission = request.form['transmission']
        #Autometic = 0 (not in column)
        if (transmission == 'Manual'):
            Manual = 1
        else:
            Manual = 0

        
        # km_driven
        
        km_driven = int(request.form['km_driven'])

        # year
        
        year = int(request.form['year'])
              
        data = np.array([[
            Maruti,
            Hyundai,
            Mahindra,
            Tata,
            Honda,
            Ford,
            Toyota,
            Chevrolet,
            Renault,
            Volkswagen,
            Skoda,
            Nissan,
            Audi,
            BMW,
            Fiat,
            Datsun,
            Mercedes_Benz,
            Mitsubishi,
            Jaguar,
            Land,
            Volvo,
            Jeep,
            OpelCorsa,
            MG,
            Kia,
            Daewoo,
            Isuzu,
            Force, 
            Petrol,
            Diesel,
            LPG,
            Electric,
            Individual,
            Trustmark_Dealer,
            Fourth_and_Above_Owner,
            Second_Owner,
            Test_Drive_Car,
            Third_Owner,
            Manual,
            km_driven,
            year
        ]])
        
        my_prediction = model.predict(data)
        output=round(my_prediction[0],2)
            
        return render_template('result.html',prediction_text="The car can be resold at Rs. {}".format(output))
        
    #return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
