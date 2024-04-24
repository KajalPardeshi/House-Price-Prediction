from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('HousePricePrediction.pkl', 'rb'))

df = pd.read_csv('Cleaned_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    bedrooms = sorted(df['bedrooms'].unique())
    bathrooms = sorted(df['bathrooms'].unique())
    floors = sorted(df['floors'].unique())
    views = sorted(df['view'].unique())
    cities = sorted(df['city'].unique())
    streets = sorted(df['street'].unique())
    zipcode = sorted(df['statezip'].unique())


    return render_template('ind.html', bedrooms=bedrooms, bathrooms=bathrooms, floors=floors, views=views, cities=cities, streets=streets, zipcode=zipcode)


@app.route('/predict', methods=['POST'])
def predict():
    bedrooms = float(request.form.get('bedrooms'))
    bathrooms = float(request.form.get('bathrooms'))
    sqft_liv = int(request.form.get('sqft_living'))
    floors = float(request.form.get('floors'))
    views = int(request.form.get('view'))
    sqft_ab = int(request.form.get('sqft_above'))
    sqft_base = int(request.form.get('sqft_basement'))
    cities = request.form.get('city')
    street = request.form.get('street')
    zip = request.form.get('statezip')

    print(bedrooms,bathrooms,sqft_liv,floors,views,sqft_ab,sqft_base,cities,street,zip)

    input = pd.DataFrame([[bedrooms,bathrooms,sqft_liv,floors,views,sqft_ab,sqft_base,cities,street,zip]], columns=['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'view', 'sqft_above', 'sqft_basement', 'street', 'city', 'statezip'])

    prediction = model.predict(input)[0]

    return f"Predicted Price of House is: ₹ {str(prediction)}"
    

    # prediction=model.predict(pd.DataFrame(columns=['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'view', 'sqft_above', 'sqft_basement', 'street', 'city', 'statezip'], data=np.array([bedrooms,bathrooms,sqft_liv,floors,views,sqft_ab,sqft_base,cities,street,zip]).reshape(1, 10)))

    # print(prediction)

    # return render_template('ind.html', prediction_text='Predicted Price of House is {}'.format(prediction))


if __name__ == '__main__':
    app.run(debug=True)






# Import Libraries
# from flask import Flask, request, render_template
 
# import model # load model.py
 
# app = Flask(__name__)
 
# # render htmp page
# @app.route('/')
# def home():
#     return render_template('index.html')
 
# # get user input and the predict the output and return to user
# @app.route('/predict',methods=['POST'])
# def predict():
     
#     #take data from form and store in each feature    
#     input_features = [x for x in request.form.values()]
#     bath = input_features[0]
#     balcony = input_features[1]
#     total_sqft_int = input_features[2]
#     bhk = input_features[3]
#     price_per_sqft = input_features[4]
#     area_type = input_features[5]
#     availability = input_features[6]
#     location = input_features[7]
     
#     # predict the price of house by calling model.py
#     predicted_price = model.predict_house_price(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)       
 
 
#     # render the html page and show the output
#     return render_template('index.html', prediction_text='Predicted Price of Bangalore House is {}'.format(predicted_price))
 
# # if __name__ == "__main__":
# #     app.run(host="0.0.0.0", port="8080")
     
# if __name__ == "__main__":
#     app.run()