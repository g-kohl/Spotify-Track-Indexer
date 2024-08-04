class User:
    def __init__(self, id, name, country, email):
        self.id = id
        self.name = name
        self.country = country
        self.email = email

    def __str__(self):
        return self.id + '*' + self.name + '*' + self.country + '*' + self.email