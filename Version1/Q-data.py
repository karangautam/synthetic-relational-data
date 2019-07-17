import json
import pandas as pd
from faker import Faker
import random
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk



def get_first_name(num_records):
    first_name = []
    for i in range(num_records):
        first_name.append(fake.first_name())
    return first_name

def get_last_name(num_records):
    last_name = []
    for i in range(num_records):
        last_name.append(fake.last_name())
    return last_name

def get_middle_name(num_records):
    middle_name = []
    for i in range(num_records):
        middle_name.append(fake.first_name_male())
    return middle_name

def get_full_name(num_records):
    full_name = []
    for i in range(num_records):
        full_name.append(fake.name())
    return full_name

def get_language(num_records):
    language = []
    for i in range(num_records):
        language.append(fake.language_code())
    return language

def get_full_address(num_records):
    full_address = []
    for i in range(num_records):
        full_address.append(fake.locale())
    return full_address

def get_house_number(num_records):
    house_number = []
    for i in range(num_records):
        house_number.append(fake.building_number())
    return house_number

def get_street_number(num_records):
    street_number = []
    for i in range(num_records):
        street_number.append(fake.random_int(min=0, max=99))
    return street_number

def get_person_id_number(num_records):
    person_id_number = []
    for i in range(num_records):
        person_id_number.append(fake.ssn())
    return person_id_number

def get_city(num_records):
    city = []
    for i in range(num_records):
        city.append(fake.city())
    return city

def get_pincode(num_records):
    pincode = []
    for i in range(num_records):
        pincode.append(fake.zipcode())
    return pincode

def get_contact_number(num_records):
    contact_number = []
    for i in range(num_records):
        contact_number.append(fake.phone_number())
    return contact_number

def get_date_of_birth(num_records):
    date_of_birth = []
    for i in range(num_records):
        date_of_birth.append(fake.date_of_birth(tzinfo=None, minimum_age=10, maximum_age=95))
    return date_of_birth

def get_age(num_records):
    age = []
    for i in range(num_records):
        age.append(fake.random_int(min=10, max=95))
    return age

def get_sentence(num_records):
    sentence = []
    for i in range(num_records):
        sentence.append(fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
    return sentence

def get_canton(num_records):
    canton = []
    for i in range(num_records):
        canton.append(fake.street_address())
    return canton

def get_gender(num_records):
    gender_dict = {'True': 'Male','False': 'Female'}
    gender_list = []
    for i in range(num_records):
        out=fake.boolean(chance_of_getting_true=60)
        if(out):
            gender = 'Male'
        else:
            gender = 'Female'
            
        gender_list.append(gender)
    return gender_list

def get_email(num_records):
    email = []
    for i in range(num_records):
        email.append(fake.email())
    return email

def get_home_phone_number(num_records):
    home_phone_number = []
    for i in range(num_records):
        home_phone_number.append(fake.phone_number())
    return home_phone_number

def get_office_number(num_records):
    office_number = []
    for i in range(num_records):
        office_number.append(fake.phone_number())
    return office_number

def get_civil_status(num_records):
    civil_status_list = []
    civil_status_dict = ['Single','Married','Divorsed']
    for i in range(num_records):
        civil_status = random.choice(civil_status_dict)
        civil_status_list.append(civil_status)
    return civil_status_list

def get_personal_record_date(num_records):
    personal_record_date = []
    for i in range(num_records):
        personal_record_date.append(fake.date_this_decade(before_today=True, after_today=False))
    return personal_record_date

def get_personal_amount(num_records):
    mu, sigma = 1000,200
    personal_amount = []
    for i in range(num_records):
        personal_amount.append(np.round(np.random.normal(mu, sigma),2))
    return personal_amount

def get_country(num_records):
    country = []
    for i in range(num_records):
        country.append(fake.country())
    return country

def get_state(num_records):
    state = []
    for i in range(num_records):
        state.append(fake.state())
    return state


def get_birth_place(num_records):
    birth_place = []
    for i in range(num_records):
        birth_place.append(fake.city())
    return birth_place


def get_account_number(num_records):
    account_number = []
    for i in range(num_records):
        account_number.append(fake.iban())
    return account_number


def get_user_name(num_records):
    user_name = []
    for i in range(num_records):
        user_name.append(fake.user_name())
    return user_name


def gen_data(field_type,num_records):
    
    if field_type == 'First-Name':
        d = get_first_name(num_records)
    elif field_type == 'Last-Name':
        d = get_last_name(num_records)
    elif field_type == 'Middle-Name':
        d = get_middle_name(num_records)
    elif field_type == 'Full-Name':
        d = get_full_name(num_records)
    elif field_type == 'Language':
        d = get_language(num_records)
    elif field_type == 'Full-Address':
        d = get_full_address(num_records)
    elif field_type == 'House-Number':
        d = get_house_number(num_records)
    elif field_type == 'Street-Number':
        d = get_street_number(num_records)
    elif field_type == 'Personal-ID-Number':
        d = get_person_id_number(num_records)
    elif field_type == 'City':
        d = get_city(num_records)
    elif field_type == 'Pincode':
        d = get_pincode(num_records)
    elif field_type == 'Contact-Number':
        d = get_contact_number(num_records)
    elif field_type == 'Date-Of-Birth':
        d = get_date_of_birth(num_records)
    elif field_type == 'Age':
        d = get_age(num_records)
    elif field_type == 'Gender':
        d = get_gender(num_records)  
    elif field_type == 'Email':
        d = get_email(num_records)
    elif field_type == 'Home-Phone-Number':
        d = get_home_phone_number(num_records)
    elif field_type == 'Office-Number':
        d = get_office_number(num_records)
    elif field_type == 'Civil-Status':
        d = get_civil_status(num_records)  
    elif field_type == 'Personal-Record-Date':
        d = get_personal_record_date(num_records) 
    elif field_type == 'Personal-Amount':
        d = get_personal_amount(num_records) 
    elif field_type == 'Country':
        d = get_country(num_records)
    elif field_type == 'State':
        d = get_state(num_records)
    elif field_type == 'Canton':
        d = get_canton(num_records)
    elif field_type == 'Birth-Place':
        d = get_birth_place(num_records)
    elif field_type == 'Account-Number':
        d = get_account_number(num_records)
    elif field_type == 'User-Name':
        d = get_user_name(num_records)
    elif field_type == 'Sentence':
        d = get_sentence(num_records)
    elif field_type == 'Canton':
        d = get_canton(num_records)
    else:
        pass
    return d

def generate_data(file_path):
    with open(file_path) as data_file:
        data = json.load(data_file)
    
    Region = data['region']
    global fake
    fake = Faker(Region)

    for i in range(len(data['database'])):
        table_name = data['database'][i]['table']['name']
        file_location = data['database'][i]['table']['location']
        table_data = pd.read_csv(file_location)
        num_records = table_data.shape[0]
        for j in range(len(data['database'][i]['fields'])):
            field_name = data['database'][i]['fields'][j]['field-name']
            field_type = data['database'][i]['fields'][j]['field-type']
            synthetic = gen_data(field_type,num_records)
            table_data[field_name] = pd.DataFrame(synthetic)
        table_data.to_csv('amended{}.csv'.format(table_name))


if __name__ == '__main__':
    def import_csv_data():
        global v
        global json_file_path
        json_file_path = askopenfilename()
    #    print(csv_file_path)
        v.set(json_file_path)
    #    print(v)
        #df = pd.read_csv(csv_file_path)
        
    def get_data():
        generate_data(json_file_path)
        root.destroy()

    root = tk.Tk()
##    image = Image.open("logo.jpg")
##    photo = ImageTk.PhotoImage(image)
##    logo = tk.Label(image=photo)
##    logo.image = photo
##    logo.pack()
##  #  logo = tk.PhotoImage(file="logo.jpg")
##
##    w1 = tk.Label(root, image=logo).pack(side="right")
##
##    explanation = """Create Synthetic Data for Personal Identifiable fields.
##                    Input - data.json
##                    Output - table csv files with prefix amended"""
##
##    w2 = tk.Label(root, 
##                  justify=tk.LEFT,
##                  padx = 10, 
##                  text=explanation).pack(side="left")

    tk.Label(root, text='File Path').grid(row=0, column=0)
    v = tk.StringVar()
    
    entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
    tk.Button(root,text='Generate Data',command=get_data).grid(row=1, column=1)
    tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=2)
    root.mainloop()







