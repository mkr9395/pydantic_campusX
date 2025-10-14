# @model_validator is used to validate multiple fields in one go

from pydantic import BaseModel, EmailStr, model_validator


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]

# create a @model_validator if age is greater than 60 then you must have a contact detail

@model_validator(mode = 'after')
def validate_emergency_conatct(cls, model):
    if model.age > 60 and 'emergency_contact' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency contact')
    return model



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print('inserted')
    
    
patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': '75.2', 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)