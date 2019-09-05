"""
Entities for the graph model
"""


class Person:
    def __init__(self, fullname, native_language, city, country,
                 accent=False, disorders=None):
        if not fullname:
            raise ValueError("Person.fullName is not initialised")
        if not native_language:
            raise ValueError("Person.firstLanguage is not initialised")
        if not city:
            raise ValueError("Person.city is not initialised")
        if not country:
            raise ValueError("Person.country is not initialised")
        if disorders == []: # None means person doesn't have any disorders
            raise ValueError("Disorders can not be an empty list")
        self.fullName = fullname
        self.nativeLanguage = native_language
        self.city = city
        self.country = country
        self.accent = accent
        self.disorders = disorders

    def setAccent(self):
        self.accent = True

    def setDisorders(self, disorders):
        if disorders == []:  # None means person doesn't have any disorders
            raise ValueError("Disorders can not be an empty list")
        self.disorders = list(disorders)


class Phoneme:
    def __init__(self, notation, start, end, language, dialect=None):
        if not notation:
            raise ValueError("Phoneme.notation is not initialised")
        if not start:
            raise ValueError("Phoneme.start is not initialised")
        if not end:
            raise ValueError("Phoneme.end is not initialised")
        if not language:
            raise ValueError("Phoneme.language is not initialised")
        self.notation = notation
        self.start = start
        self.end = end
        self.language = language
        self.dialect = dialect if dialect else None
