people = [
    ('이호준', '01050442903'),
    ('이호상', '01051442904'),
    ('이준호', '01053442904'),
    ('이호준', '01050442903'),
    ('이준', '01050412904'),
    ('이호', '01050443904'),
    ('이호준', '01050442903'),         
]
people

new_people = set(people)
len(new_people)

dict_people = {}
for i in new_people: 
    dict_people[i[1]] = i[0]
dict_people
len(dict_people)
dict_people = {}
for i in new_people: 
    dict_people[i[1]] = i[0]
dict_people
len(dict_people)