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


    return render_template('index.html', bedrooms=bedrooms, bathrooms=bathrooms, floors=floors, views=views, cities=cities, streets=streets, zipcode=zipcode)


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


if __name__ == '__main__':
    app.run(debug=True)
