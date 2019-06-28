from tkinter import *
from faker import Faker
import random
import numpy as np
import pandas as pd
import datetime
import numpy.core._methods
import numpy.lib.format

fake = Faker('de_CH')
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
   root = Tk()
   fName = Checkbar(root, ['First Name'])
   lName = Checkbar(root,['Last Name'])
   ssn= Checkbar(root,['ssn'])
   streetAddress = Checkbar(root,['Street Address'])
   licencePlate = Checkbar(root,['Licence Plate Number'])
   phoneNumber = Checkbar(root,['Phone Number'])
   company = Checkbar(root,['Company'])
   job = Checkbar(root,['Job'])
   email = Checkbar(root,['email'])
   numRecordsText=Label(root, text="Enter Number of Records")
   numRecords= Entry(root,width=10)

   fName.pack(side=TOP,  anchor=W)
   lName.pack(side=TOP,  anchor=W)
   ssn.pack(side=TOP,  anchor=W)
   streetAddress.pack(side=TOP,  anchor=W)
   licencePlate.pack(side=TOP,  anchor=W)
   phoneNumber.pack(side=TOP,  anchor=W)
   company.pack(side=TOP,  anchor=W)
   job.pack(side=TOP,  anchor=W)
   email.pack(side=TOP,  anchor=W)
   numRecordsText.pack(side=LEFT)
   numRecords.pack(side=LEFT)
   

   def get_details():
      d = dict();
      if fName.state():
         d['First_name'] = fake.first_name()
      if lName.state():
         d['Last_name'] = fake.last_name()
      if ssn.state():
         d['ssn'] = fake.ssn()
      if streetAddress.state():
         d['streetAddress'] = fake.street_address()
      if licencePlate.state():
         d['license_plate'] = fake.license_plate()
      if phoneNumber.state():
         d['Phone'] = fake.phone_number()
      if company.state():
         d['Company'] = fake.company()
      if job.state():
         d['Job'] = fake.job()
      if email.state():
         d['email'] = fake.email()

      return d

   def gen_data(): 
      data = []
      for iterations in range(int(numRecords.get())):
         data.append(get_details())

      fake_data = pd.DataFrame.from_dict(data=data)
      curretdatetime=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
      file_name = 'fake_data'+str(curretdatetime)+'.csv'
      fake_data.to_csv(file_name,index=False)

#   def exit_out():
#      root.quit()

   Button(root, text='Quit', command=exit_out).pack(side=RIGHT)
 #  Button(root, text='Submit', command=gen_data).pack(side=RIGHT)
   root.mainloop()