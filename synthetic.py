from faker import Faker
import random
import numpy as np
import pandas as pd
import datetime
import config

REGION = config.REGION
NO_OF_CUSTOMER = config.NO_OF_CUSTOMER
NO_OF_MERCHANT = config.NO_OF_MERCHANT
NO_OF_CONCENT = config.NO_OF_CONCENT
NO_OF_SALE = config.NO_OF_SALE
fake = Faker(REGION)

class Customer:
    
    def __init__(self,first_name,last_name,email,gender,dob,image_url,address,mobile,ssn,is_primary_authenticated,is_secondary_authenticated):
        gender_dict = {'True': 'Male','False': 'Female'}
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if(gender):
            self.gender = 'Male'
        else:
            self.gender = 'Female'
        self.dob = dob
        self.image_url = image_url
        self.address = address
        self.contact = mobile
        self.ssn = ssn
        self.is_primary_auth = is_primary_authenticated
        self.is_secondary_auth = is_secondary_authenticated
        
    def get_customer(self):
        d = dict();
        d['first_name'] = self.first_name
        d['last_name'] = self.last_name
        d['email'] = self.email
        d['gender'] = self.gender
        d['dob'] = self.dob
        d['image_url'] = self.image_url
        d['address']= self.address
        d['phone_number'] = self.contact
        d['ssn'] = self.ssn
        d['is_primary_authenticated'] = self.is_primary_auth
        d['is_secondary_authenticated']=self.is_secondary_auth
        return d

class Merchant:
    
    def __init__(self,merchant_name,merchant_website,contact_name,contact_number,merchant_logo,merchant_account_number,merchant_address):
        
        self.merchant_name = merchant_name
        self.merchant_website = merchant_website
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.merchant_logo = merchant_logo
        self.merchant_account_number = merchant_account_number
        self.merchant_address = merchant_address
    
    def get_merchant(self):
        d = dict();
        d['merchant_name'] = self.merchant_name
        d['merchant_website'] = self.merchant_website
        d['contact_name'] = self.contact_name
        d['contact_number'] = self.contact_number
        d['merchant_logo'] = self.merchant_logo
        d['merchant_account_number'] = self.merchant_account_number
        d['merchant_address'] = self.merchant_address
        
        return d

class Product:
    
    def __init__(self,sku,product_name,price,product_description,image_url,merchant_ids,producer,barcode,discount):
        
        self.sku = sku
        self.product_name = product_name
        self.price = price/1000
        self.product_description = product_description
        dimensions = ['S','M','L']
        self.dimensions = random.choice(dimensions)
        self.image_url = image_url
        self.merchant_id = random.choice(merchant_ids)
        self.producer = producer
        self.barcode = barcode
        self.discount = discount
        
    
    def get_product(self):
        d = dict();
        d['sku'] = self.sku
        d['product_name'] = self.product_name
        d['price'] = self.price
        d['product_description'] = self.product_description
        d['product_dimension'] = self.dimensions
        d['image_url'] = self.image_url
        d['merchant_id'] = self.merchant_id
        d['producer'] = self.producer
        d['barcode'] = self.barcode
        d['discount'] = self.discount
        
        return d

class Concent:
    
    def __init__(self,concent_marketing,concent_promotion,customer_ids,merchant_ids):
        
        self.concent_marketing = concent_marketing
        self.concent_promotion = concent_promotion
        self.customer_id = random.choice(customer_ids)
        self.merchant_id = random.choice(merchant_ids)
        
    def get_concent(self):
        d = dict();
        d['concent_marketing'] = self.concent_marketing
        d['concent_promotion'] = self.concent_promotion
        d['customer_id'] = self.customer_id
        d['merchant_id'] = self.merchant_id
        
        return d

class Sale:
    
    def __init__(self,customer_ids,sale_date,sale_time,longitude,latitude):
        self.customer_id = random.choice(customer_ids)
        self.sale_date = sale_date
        self.sale_time = sale_time
        self.longitude = longitude
        self.latitude = latitude
        
    def get_sale(self):
        
        d = dict();
        d['customer_id'] = self.customer_id
        d['sale_date'] = self.sale_date
        d['sale_time'] = self.sale_time
        d['longitude'] = self.longitude
        d['latitude'] = self.latitude
        
        return d

class Transaction:
    def __init__(self,sale_id,item_number,product_id,units,price,discount,product_total):
        self.sale_id = sale_id
        self.item_number = item_number
        self.product_id = product_id
        self.units = units
        self.price = price
        self.discount = discount
        self.product_total = product_total
        
    def get_transaction(self):
        d = dict();
        d['sale_id'] = self.sale_id
        d['item_number'] = self.item_number
        d['product_id'] = self.product_id
        d['units'] = self.units
        d['price'] = self.price
        d['discount'] = self.discount
        d['product_total'] = self.product_total
        
        
        return d

class Invoice:
    def __init__(self,sale_id,total_cost):
        self.sale_id = sale_id
        self.total_cost = total_cost
        
    def get_invoice(self):
        d = dict();
        d['sale_id'] = self.sale_id
        d['total_cost'] = self.total_cost
        
        return d


#######################################
customer_list = []
for i in range(NO_OF_CUSTOMER):
    customer = Customer(fake.first_name(),fake.last_name(),fake.email(),fake.boolean(chance_of_getting_true=60),fake.date_of_birth(),
                                 fake.image_url(),fake.address(),fake.phone_number(),fake.ssn(),fake.boolean(chance_of_getting_true=60),
                                 fake.boolean(chance_of_getting_true=60))
    customer_list.append(customer.get_customer())
customer_data = pd.DataFrame.from_dict(data=customer_list)
customer_data.insert(0, 'customer_id', range(100001 , 100001 + len(customer_data)))
customer_data = customer_data[['customer_id','first_name','last_name','email','gender','dob','image_url','address','phone_number','ssn','is_primary_authenticated','is_secondary_authenticated']]

######################################
merchant_list = []

for _ in range(NO_OF_MERCHANT):
    merchant = Merchant(fake.company(),fake.hostname(),fake.name(),fake.phone_number(),fake.image_url(),fake.iban(),fake.address())
    merchant_list.append(merchant.get_merchant())
merchant_data = pd.DataFrame.from_dict(data=merchant_list)
merchant_data.insert(0, 'merchant_id', range(100001 , 100001 + len(merchant_data)))

merchant_data = merchant_data[['merchant_id','merchant_name','merchant_website','merchant_address','merchant_account_number','merchant_logo','contact_name','contact_number']]

#####################################
sample_product = pd.read_csv('sample_products.csv')
product_list = []

for i in range(len(sample_product)):
    discount = random.randint(0,50)
    product = Product(sample_product['sku (unique id)'].loc[i],sample_product['product_name'].loc[i],sample_product['price_cents'].loc[i],fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),fake.image_url(),merchant_data['merchant_id'].values,sample_product['producer'].loc[i],sample_product['barcode'].loc[i],discount)
    product_list.append(product.get_product())
product_data = pd.DataFrame.from_dict(data=product_list)
product_data.insert(0, 'product_id', range(100001 , 100001 + len(product_data)))
product_data=product_data[['product_id','sku','product_name','price','barcode','product_description','product_dimension','producer','merchant_id','image_url','discount']]

####################################
concent_list = []

for _ in range(NO_OF_CONCENT):
    
    concent = Concent(fake.boolean(),fake.boolean(),customer_data['customer_id'].values,merchant_data['merchant_id'].values)
    concent_list.append(concent.get_concent())

concent_data = pd.DataFrame.from_dict(data=concent_list)
concent_data.insert(0, 'concent_id', range(100001 , 100001 + len(concent_data)))

####################################
sale_list = []

for _ in range(NO_OF_SALE):
    date =fake.date_this_decade(before_today=True, after_today=False)
    time = fake.time_object(end_datetime=None)
    sale = Sale(customer_data['customer_id'].values,date,time,fake.longitude(),fake.latitude())
    sale_list.append(sale.get_sale())
sale_data = pd.DataFrame.from_dict(data=sale_list)
sale_data.insert(0, 'sale_id', range(100001 , 100001 + len(sale_data)))

###################################
transaction_list = []

for i in range(len(sale_data)):
    sale_id = sale_data['sale_id'][i]
    items = random.randint(1,10)
    for j in range(1,items):
        item_number = j
        product_index = random.randint(0,len(product_data)-1)
        product_id = product_data['product_id'][product_index]
        product_price = product_data['price'][product_index]
        units = random.randint(1,10)
        product_discount = product_data['discount'][product_index]
        product_total = product_price*units * (1 - product_discount/100)
        
        transaction = Transaction(sale_id,item_number,product_id,units,product_price,product_discount,product_total)
        transaction_list.append(transaction.get_transaction())
transaction_data = pd.DataFrame.from_dict(data=transaction_list)
transaction_data.insert(0, 'transaction_id', range(100001 , 100001 + len(transaction_data)))
transaction_data = transaction_data[['transaction_id','sale_id','item_number','product_id','units','price','discount','product_total']]

###################################
invoice_list = []

temp_data = transaction_data.groupby(["sale_id"])[["product_total"]].sum()
temp_data.reset_index(level=0,inplace=True)

for i in range(len(temp_data)):
    
    invoice = Invoice(temp_data['sale_id'][i],temp_data['product_total'][i])
    invoice_list.append(invoice.get_invoice())
invoice_data = pd.DataFrame.from_dict(data=invoice_list)


##################################
customer_data.to_csv('customer_data.csv',index=False)
merchant_data.to_csv('merchant_data.csv',index=False)
product_data.to_csv('product_data.csv',index=False)
concent_data.to_csv('concent_data.csv',index=False)
sale_data.to_csv('sale_data.csv',index=False)
transaction_data.to_csv('transaction_data.csv',index=False)
invoice_data.to_csv('invoice_data.csv',index=False)
