import requests
import logging
import os
from faker import Faker

def populate_applicant(auth, applicant_entries):
    logging.basicConfig(level=logging.INFO, filename="aline_files/core-my/docker-data/aline_log.log", filemode='a', format='%(process)d - [%(levelname)s ] - %(message)s')
    fake = Faker()
    mem_id_array = []
    acc_num_array = []
    # applications_url = 'http://localhost:8071/applications'
    applications_url = f"{os.environ.get('APP_URL')}/applications"
    
    for i in range(applicant_entries):
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
                "socialSecurity" : fake.numerify('###-##-') + (str((i%10)+1)*4),
                "state" : fake.state(),
                "zipcode" : fake.zipcode()
            }]
        }
        logging.info(f'Trying to post {applicant_info}')
        try:
            reg_app = requests.post(applications_url, json=applicant_info, headers=auth)
            mem_id_array.append(reg_app.json()['createdMembers'][0]['membershipId'])
            if application_type != 'CREDIT_CARD':
                acc_num_array.append(reg_app.json()['createdAccounts'][0]['accountNumber'])
            logging.info('Applicant posted')
        except Exception as e:
            logging.error(f'Error entering applicant: ', exc_info=True)
    return [mem_id_array, acc_num_array]

print('', end='')
