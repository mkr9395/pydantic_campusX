from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address
    
    
address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)


# convert pydantic model to python dict

temp = patient1.model_dump()
print(temp)
print(type(temp))

# if you only want to export name to python dict
temp = patient1.model_dump(include=['name']) # type: ignore
print(temp)
print(type(temp))

# want to only exclude address
temp = patient1.model_dump(exclude=['address']) # type: ignore
print(temp)
print(type(temp))
# exclude only city of address
temp = patient1.model_dump(exclude={'address': ['state']}) # type: ignore
print(temp)
print(type(temp))


# exclude_unset excludes where default type is set
temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))

# convert pydantic to json

temp_json = patient1.model_dump_json()
print(temp_json)
print(type(temp_json))