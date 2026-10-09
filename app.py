from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import List, Optional, Literal, Annotated
import pickle
from fastapi.responses import JSONResponse
import pandas as pd
import sklearn
import numpy as np

# ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

tier1cities = ['Mumbai', 'Delhi', 'Banglore', 'Chennai', 'Kolkata', 'Hydrabad', 'Pune']
tier2cities = ['Jaipur', 'Chandigarh', 'Indore', 'Kota', 'Lucknow']

# new pydantic model:
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user in years")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kilograms")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user in meters")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the user in lakhs per annum")]
    smoker: Annotated[bool, Field(..., description="Whether the user is a smoker or not")]
    city: Annotated[str, Field(..., description="City type of the user")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner',
                                  'unemployed', 'private_job'], Field(..., description="Occupation type of the user")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high'
        elif self.smoker and self.bmi > 27:
            return 'medium'
        else:
            return 'low'
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'senior'
    
    @computed_field
    @property
    def city_tier(self) -> str:
        if self.city in tier1cities:
            return 'tier1'
        elif self.city in tier2cities:
            return 'tier2'
        else:
            return 'tier3'
        
@app.post('/predict')
def predict_premium(data: UserInput):
    
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])
    
    prediction = model.predict(input_df)[0]
    
    return JSONResponse(status_code=200, content={"predicted_category": prediction})
# @app.post('/predict')
# def predict_premium(data: UserInput):

#     input_df = pd.DataFrame([{
#         'bmi': data.bmi,
#         'age_group': data.age_group,
#         'lifestyle_risk': data.lifestyle_risk,
#         'city_tier': data.city_tier,
#         'income_lpa': data.income_lpa,
#         'occupation': data.occupation
#     }])

#     # Debugging information
#     print("\n--- Input DataFrame ---")
#     print(input_df)

#     print("\n--- Input Data Types ---")
#     print(input_df.dtypes)

#     print("\n--- Model Expected Features ---")
#     if hasattr(model, "feature_names_in_"):
#         print(model.feature_names_in_)
#     else:
#         print("Model does not expose feature_names_in_")

#     try:
#         prediction = model.predict(input_df)[0]

#         # Convert NumPy scalar types to standard Python types
#         if hasattr(prediction, "item"):
#             prediction = prediction.item()

#         return JSONResponse(
#             status_code=200,
#             content={"predicted_category": prediction}
#         )

#     except Exception as e:
#         print("\n--- Prediction Error ---")
#         print(repr(e))
#         raise