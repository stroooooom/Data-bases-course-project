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

from neotime import DateTime as neoDateTime

# username, password = "neo4j", "123" # admin
username, password = "editor", "editor"  # editor

class GetDataQuery:
    def __init__(self):
        self.letters = None
        self.__text = None

    def setWord(self, word: str):
        self.letters = list(set(word))
        self.letters.sort()

    def setLetters(self, letters: list):
        self.letters = letters

    def reset(self):
        self.letters = None
        self.__text = None

    def text(self):
        if not self.letters:
            return self.__text
        self.__text = str()
        returnQueryPart = str()
        for i in range(len(self.letters)):
            letterName = 'ph'+str(i)
            self.__text += "match (p:Person)-[*1]-(r:Record)-[*1]-({letterName}:Phoneme {{notation:'{letter}'}})\n".format(
                letterName=letterName,
                letter=self.letters[i])
            returnQueryPart += "{letterName}.start, {letterName}.end, ".format(letterName=letterName)
        self.__text += "return " + returnQueryPart + "p.fullname, r.description"
        print("query text:")
        print(self.__text)
        return self.__text

    def test_text(self):
        self.letters = ['a', 'b']
        return "match (p:Person)-[*2]-(ph0:Phoneme {notation:'а'})\n" \
               "match (p:Person)-[*2]-(ph1:Phoneme {notation:'б'})\n" \
               "return p.fullname, " \
               "ph0.start, ph0.end, " \
               "ph1.start, ph1.end"


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

    def addPhonemes(self, phonemes: list):
        self.phonemes = phonemes

    def addPhoneme(self, phoneme: Entity.Phoneme): # ??
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
        self.driver = None
        try:
            self.driver = GraphDatabase.driver(
                'bolt://localhost:7687',
                auth=(username, password))  # admin password equals DB password
        except BaseException as e:
            print(e)
            exit(0)
        self.loadQuery = LoadDataQuery()
        self.getQuery = GetDataQuery()

    def loadData(self):
        if not self.loadQuery.text():
            raise ValueError("Cannot run an empty query")
        with self.driver.session() as session:
            return session.write_transaction(self.__createGraph)

    def __createGraph(self, tx):
        return tx.run(self.loadQuery.text()).single()

    def getData(self):
        with self.driver.session() as session:
            return session.read_transaction(self.__getPhonemes)

    def __getPhonemes(self, tx):
        # result = tx.run(self.getQuery.test_text()).records()
        speechSamples = list()
        # records = tx.run(self.getQuery.test_text()).records()
        records = tx.run(self.getQuery.text()).records()
        for record in records:
            d = dict()
            d['filePath'] = record['r.description']
            d['name'] = record['p.fullname']
            for i in range(len(self.getQuery.letters)):
                key = 'ph'+str(i)
                time = (record[key+'.start'].ticks,
                          record[key + '.end'].ticks)
                d[self.getQuery.letters[i]] = time
            speechSamples.append(d)

        # return result
        return speechSamples

    def __del__(self):
        if self.driver:
            self.driver.close()


if __name__ == '__main__':
    graph = Driver()
    # graph.loadQuery.setPerson(Entity.Person('person', 'r', 'city', 'country', 'true', ['abc', 'def']))
    # graph.loadQuery.setRecord("abc.wav")
    # graph.loadQuery.addPhoneme(Entity.Phoneme('a', '00:00:01', '00:00:02', 'r', 'r'))
    # graph.loadQuery.addPhoneme(Entity.Phoneme('b', '00:00:03', '00:00:04', 'r'))
    # graph.loadData()
    # graph.getQuery.setLetters("парк")
    # graph.getQuery.setLetters(['а', 'б', 'в', 'г'])
    graph.getQuery.setLetters(['а', 'б'])
    result = graph.getData()
    for d in result:
        print(d)
    # for record in result:
    #     print(record)
    # print(result[0]['ph0'])
    # records = result.records()
    # for record in records:
    #     print(record['ph0.start'])
        # print("Record:\n", record.data())
    # print(result.records())
    graph.driver.close()
