class Person:
    def __init__(self,first_name,last_name,domain_name,birthDate):
        self.first_name = first_name,
        self.last_name = last_name,
        self.domain_name = domain_name,
        self.birthDate = birthDate

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def email(self):
        return '{}.{}@{}'.format(self.first_name, self.last_name, self.domain_name)
        
    def DOB(self):
        return '{}'.format(self.birthDate)