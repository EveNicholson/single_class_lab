class Student:


    def __init__ (self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        return  "I can talk!"

    def favourite_language(self, language):
        return f"I love {language}"
    