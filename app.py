from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput 
from Model.predict import predict_output, model

app = FastAPI()

        
# Machiine readable      
@app.get('/health') # whenever you deploye your plat form on the kubernative or aws platform so it need the health check where they can search and know about the website is live or not 
def health_check(): # Mandentory 
    return {
        'status': 'OK',
        'model_loaded': model is not None 
    }# we are declearing that if model is not so it's came true or if it's so false 
# human Readable       
@app.get('/') # this dwfine because we want to display some output on the home 
def home():
    return {'message':'Insurance Premium'}
        
@app.post('/predict')
def predict_premium(data: UserInput):

    User_Input = {
        'bmi': data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk' : data.lifestyle_risk,
        'city_tier' : data.city_tier,
        'income_lpa' : data.income_lpa,
        'occupation' : data.occupation
    }

    try:
        prediction = predict_output(User_Input)
        return JSONResponse(status_code = 200, content = {'predicted_category': prediction })
    except Exception as e :
        return JSONResponse(Status_code=500,Content=str(e))

    
    



    
    


