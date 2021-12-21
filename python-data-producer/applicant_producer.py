import requests
from faker import Faker
from datetime import datetime

def populate_applicant(auth):
    fake = Faker()
    mem_id_array = []
    acc_num_array = []
    applications_url = 'http://localhost:8071/applications'
    
    user_entries = 9
    for i in range(user_entries):
        application_type = fake.random_element(elements=('CHECKING', 'SAVINGS', 'CREDIT_CARD'))
        applicant_info = {
            "applicationType" : application_type,
            "noApplicants" : False,
            "applicants" : [{
                "address" : fake.street_address(),
                "city" : fake.city(),
                "dateOfBirth" : fake.numerify('19##-0%-1#'),
                "driversLicense" : fake.numerify('#########'),
                "email" : fake.email(),
                "firstName" : fake.first_name(),
                "gender" : fake.random_element(elements=('MALE','FEMALE', 'OTHER', 'UNSPECIFIED')),
                "income" : fake.numerify('#%#######'),
                "lastName" : fake.last_name(),
                "mailingAddress" : fake.street_address(),
                "mailingCity" : fake.city(),
                "mailingState" : fake.state(),
                "mailingZipcode" : fake.zipcode(),
                "middleName" : fake.first_name(),
                "phone" : fake.numerify('(###)-###-####'),
                "socialSecurity" : fake.numerify('###-##-') + (str(i+1)*4),
                "state" : fake.state(),
                "zipcode" : fake.zipcode()
            }]
        }
        reg_app = requests.post(applications_url, json=applicant_info, headers=auth)
        mem_id_array.append(reg_app.json()['createdMembers'][0]['membershipId'])
        if application_type != 'CREDIT_CARD':
            acc_num_array.append(reg_app.json()['createdAccounts'][0]['accountNumber'])
    return [mem_id_array, acc_num_array]

# login_info = {
#     'username' : 'adminUser',
#     'password' : 'Password*8'
# }
# login_response = requests.post('http://localhost:8070/login', json=login_info)
# bearer_token = login_response.headers['Authorization']
# auth = {'Authorization' : bearer_token}
# populate_applicant(auth)
