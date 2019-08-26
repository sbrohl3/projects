
import json

## Addings contents to the database
with open("text_files/customers.json") as customers_json:
    customers = json.load(customers_json)

customers = list(customers)

for key in customers:
    self.first_name = key["first_name"]
    self.last_name = key["last_name"]
    self.crm_company_name = key["company_name"]
    self.company_name = key["company_name"]
    self.address = key["address"]
    self.city = key["city"]
    self.county = key["county"]
    self.state_code = key["state"]
    self.zip_code = key["zip"]
    self.phone_number = key["phone1"]
    self.phone_number_2 = key["phone2"]
    self.email_address = key["email"]



