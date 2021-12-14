

from faker import Faker
class BaseContact():
    def __init__(self, firstname, lastname, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email


    def __repr__(self):
        return f'firstname={self.firstname} lastname={self.lastname} company={self.company} post={self.post} email={self.email}'

    def contact(self):
        print('Kontaktuję się z {} {}, pracującym jako {}, email: {}'.format(self.firstname, self. lastname, self.post, self.email))

    
    @property
    def namelength(self):
        return len(self.firstname + ' ' + self.lastname)

    @namelength.setter
    def namelength(self):
        self._namelength = len(self.firstname + ' ' + self.lastname)

class BusinessContact(BaseContact):
    def __init__(self, firstname, lastname, phone, email, job, company,jobphone):
        super().__init__(firstname, lastname, phone, email)
        self.job = job
        self.company = company
        self.jobphone = jobphone

        


def generate_fake_names():
    names = []
    fake = Faker()
    for i in range(10):
        names.append(BusinessContact(firstname=fake.first_name(),
        lastname=fake.last_name(),
        phone=fake.phone_number(),
        email=fake.email(),
        job = fake.job(),
        company = fake.company(),
        jobphone = fake.phone_number()))
    return names


namelist = generate_fake_names()

for name in namelist:
    print('{} {} {} {}'.format(name.firstname, name.lastname, name.company, name.email))
    print(name.namelength)