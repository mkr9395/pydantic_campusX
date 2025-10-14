from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]
    
    # field validator on email should that it contains 'hdfc' or 'icici'
    
    @field_validator('email')    # we need to specify on which part the field validator will validate
    @classmethod # need to define it as class method
    def email_validator(cls,value) -> str: 
        
        valid_domain_names = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1] # extract domain from the user_input
        
        if domain_name not in  valid_domain_names:
            raise ValueError('Not a valida domain') 
        return value
    
    
    # capitalise the name -> it will capitalize name in after mode
    
    @field_validator('name')
    @classmethod
    def name_capital_transform(cls, value):
        return value.upper()
    
    
    # checks in age datatype in before mode
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 130:
            return value
        else:
            raise ValueError("Invalid value, Age should be in between 0 to 130")
    
    
    
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.married)
    print('inserted')
    
patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': 30, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

insert_patient_data(patient1)