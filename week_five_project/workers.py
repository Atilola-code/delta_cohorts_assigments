class Worker:
    def __init__(self, name, gender, job, qualification, years_of_experience, location, is_active=False):
        self.name = name
        self.gender = gender
        self.job = job
        self.qualification = qualification
        self.years_of_experience = years_of_experience
        self.location = location
        self.is_active = is_active


    def __str__(self):
        return f"Worker{self.name}, {self.gender}, {self.job}, {self.qualification}, {self.years_of_experience},{self.is_active}"
        



