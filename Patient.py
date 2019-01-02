"""Patient Class will be used to generate individual patient objects for triage of exposures"""


class Patient():
    def __init__(self, identifier, age, weight, gender):
        """
        A model for the person exposed,
        attributes will be used to determine
        exposure doses for triage if applicable
        """
        self.identifier = identifier
        self.age = age
        self.weight = weight
        self.gender = gender

    def show_patient(self):
        demographics = self.identifier.title() + ' ' + str(self.age) + ' ' + str(self.weight) + ' ' + self.gender
        return demographics


new_patient = Patient('harold lichtman', 45, 135, 'male')

print(new_patient.show_patient())
