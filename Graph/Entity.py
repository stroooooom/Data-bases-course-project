"""
Entities for the graph model
"""


class Record:
    def __init__(self, description):
        self.description = description


class Person:
    def __init__(self, fullname, native_language, city, country,
                 accent=False, disorders=[]):
        if not fullname:
            raise ValueError("Person.fullName is not initialised")
        if not native_language:
            raise ValueError("Person.firstLanguage is not initialised")
        if not city:
            raise ValueError("Person.city is not initialised")
        if not country:
            raise ValueError("Person.country is not initialised")
        self.fullName = fullname
        self.nativeLanguage = native_language
        self.city = city
        self.country = country
        self.accent = accent
        self.disorders = disorders

    def setAccent(self):
        self.accent = True

    def setDisorders(self, disorders):
        self.disorders = list(disorders)


class Phoneme:
    def __init__(self, notation, start, end, language):
        if not notation:
            raise ValueError("Phoneme.notation is not initialised")
        if not start:
            raise ValueError("Phoneme.start is not initialised")
        if not end:
            raise ValueError("Phoneme.cendity is not initialised")
        if not language:
            raise ValueError("Phoneme.language is not initialised")
        self.notation = notation
        self.start = start
        self.end = end
        self.language = language

class Feature:
    def __init__(self, name, type):
        self.name = name
        self.type = type
