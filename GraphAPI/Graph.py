'''

merge (p: Person {name:'Есть в графе'})
Результат - ничего не создается

match (p: Person {name:'Нет в графе'}), (r: Record {id:2})
merge (r)-[:SPOKEN_BY]->(p)
Результат - ничего не создается
________________________________________
CREATE (r: Record {ID: $ID}), 

'''

from neo4j import GraphDatabase
from GraphAPI import Entity

# username, password = "neo4j", "123" # admin
username, password = "editor", "editor"  # editor


class LoadDataQuery:
    def __init__(self):
        self.record = None
        self.person = None
        self.phonemes = list()

        self.__text = None

    def setRecord(self, recordFileName: str):
        self.record = recordFileName

    def setPerson(self, person: Entity.Person):
        self.person = person

    def addPhoneme(self, phoneme: Entity.Phoneme):
        self.phonemes.append(phoneme)

    def reset(self):
        self.person = None
        self.phonemes = list()
        self.__text = None

    def text(self):
        if not self.person or not self.phonemes:
            return self.__text
        self.__text = "create (rec:Record {{description:'{0}'}})\n\n".format(self.record)
        self.__text += \
            "create (person: Person {{fullname:'{fullname}', nativeLanguage:'{nativeLanguage}', " \
            "city:'{city}', country:'{country}', accent:'{accent}'}})\n" \
            "merge (country: Country {{name:'{country}'}})\n" \
            "merge (city: City {{name:'{city}'}})\n\n".format(
                fullname=self.person.fullName,
                nativeLanguage=self.person.nativeLanguage,
                city=self.person.city,
                country=self.person.country,
                accent=self.person.accent,
                disorders=self.person.disorders)
        self.__text += "create (rec)-[:SPOKEN_BY]->(person)\n" \
                       "create (person)-[:LIVES_IN]->(city)\n" \
                       "merge (city)-[:LOCATED_IN]->(country)\n\n"
        for i in range(len(self.person.disorders)):
            disorder = self.person.disorders[i]
            self.__text += "merge (dis{n}: Disorder {{name:'{name}'}})\n" \
                           "create (person)-[:HAS]->(dis{n})".format(n=i, name=disorder)
        for i in range(len(self.phonemes)):
            phoneme = self.phonemes[i]
            self.__text += \
                "create (ph{n}: Phoneme {{notation:'{notation}', start:time('{start}'), end:time('{end}'), \
                language:'{language}', dialect:'{dialect}'}})\n".format(
                    n=i,
                    notation=phoneme.notation,
                    start=phoneme.start,
                    end=phoneme.end,
                    language=phoneme.language,
                    dialect=phoneme.dialect)
            self.__text += "create (ph{n})-[:CONTAINED_IN]->(rec)\n".format(n=i)
        return self.__text


# логику работы UI лучше вынести в отдельный класс
# нужно сохранять Speaker ID, чтобы не искать каждый раз при добавлении фонемы 
class Driver:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            'bolt://localhost:7687',
            auth=(username, password))  # admin password equals DB password
        self.loadQuery = LoadDataQuery()

    def loadData(self):
        if not self.loadQuery.text():
            raise ValueError("Cannot run an empty query")
        with self.driver.session() as session:
            return session.write_transaction(self.__createGraph)

    def __createGraph(self, tx):
        return tx.run(self.loadQuery.text()).single()

    def __del__(self):
        self.driver.close()


if __name__ == '__main__':
    graph = Driver()
    graph.loadQuery.setPerson(Entity.Person('person', 'r', 'city', 'country', 'true', ['abc', 'def']))
    graph.loadQuery.setRecord("abc.wav")
    graph.loadQuery.addPhoneme(Entity.Phoneme('a', '00:00:01', '00:00:02', 'r', 'r'))
    graph.loadQuery.addPhoneme(Entity.Phoneme('b', '00:00:03', '00:00:04', 'r'))
    graph.loadData()
    graph.driver.close()
