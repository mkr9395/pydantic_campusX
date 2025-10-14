from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Optional, Annotated

# creating pydantic model/class
class Patient(BaseModel):
    
    name : str = Field(default = 'No name', max_length = 50) # name should not be greater than 50 character and default is no_name
    
    email : EmailStr # email will be validated as it should have @
    
    linkedIn_url : AnyUrl  # url should have https:// and .com
    
    age : Annotated[int, Field(gt=0, strict=True)] # age should always be greater than 0 using Field and can only have int
    
    weight : Annotated[float, Field(ge=0, description = "This field contains weight of patient in decimals")]
    
    married : Optional[bool] = None # optional will always have default value as None
    
    allergies : list[str] = ['no allegries'] # default value will no allergies
    
    contact_details : dict[str, str] # in dict both key & values are str
    



def insert_patient_data(patient : Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.linkedIn_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details,"\n")
    print(patient,"\n")
    
    print("patient inserted")
    
       
# creating the dictionary
patient_info = {'name':'mohit', 'email':'abc@gmadail.com', 'linkedIn_url' : 'https://www.mkr935.com' ,'age':30 , 'weight': 96.5, 'married': True,'allergies' : ['cough','coold'], 'contact_details':{'mob_no': '943174499'}}

# inantiate the pydantic with raw dictionary
patient1 = Patient(**patient_info) # unpack the dictionary

insert_patient_data(patient=patient1)


