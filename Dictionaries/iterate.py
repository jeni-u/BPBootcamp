students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for list in students:
        for key, val in list.items():
            print(key, "-" ,val , " ", end="\n")

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for x in some_list:
        if key_name in x:
            print(x[key_name])
        
iterateDictionary2('last_name',students)