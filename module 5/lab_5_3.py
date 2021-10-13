word = "Found name:"
ids = {'name': 'Alice', 'age': '27'}


def get_person(name, *args, age='None'):
    print(word, name)
    print('Age:', age)
    print(args)


get_person(**ids)

get_person(ids['name'], list(range(1, 10)))
