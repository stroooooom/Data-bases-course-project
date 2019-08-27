from neo4j import GraphDatabase
from Graph import Entity

class Query:
    def __init__(self):
        self.person_init = False
        self.record_init = False
        self.text = ""

class Graph:
    def __init__(self):
        self.driver = GraphDatabase.driver('bolt://localhost:7687',
                                           auth=(username, password))  # admin password equals DB password

    def add_person(self, person):
        return
        # with self.driver.session() as session:
        # return session.write_transaction(self.create_person_node, person)

    def _add_person_node(self, tx, person):
        return tx.run("MERGE (a:Person {fullName: $fullName, nativeLanguage: $nativeLanguage})",
                      fullName=person.fullName, nativeLanguage=person.nativeLanguage).single().value()

    def _add_city_node(self, tx, person):
        return tx.run("MERGE (a:City {name: $name}", name=person.city)

    def _add_country_node(self, tx, person):
        return tx.run("MERGE (a:Country {name: $name}", name=person.country)

    def add_record(self, record):
        # empty
        return

    def _add_record_node(self, tx, record):
        return tx.run("MERGE (a:Record {description: $description}", description=record.description)

    def add_phoneme(self, record):
        # empty
        return

    def _add_phoneme(self, tx, phoneme):
        return tx.run("MERGE (a:Phoneme {notation: $notation, start: $start, end: $end, language: $language})",
                      notation=phoneme.notation, start=phoneme.start, end=phoneme.end, language=phoneme.language)

    def _add_disorder(self, tx, disorderName):
        return tx.run("MERGE (a:Disorder {name: $name})", name=disorderName)

