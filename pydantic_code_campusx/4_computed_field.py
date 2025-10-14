# fields computed from other fields but not passed in input.

from pydantic import BaseModel, EmailStr, computed_field


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]
    
    # will calculate bmi with height and weight

    @computed_field
    @property
    def bmi(self)-> float: # whatever this function name will be that will become the new field/column
        bmi = round(self.weight/(self.height **2), 2)
        return bmi


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('created new value')
    
    
patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)


