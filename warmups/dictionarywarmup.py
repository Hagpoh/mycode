jedi = {
        'name':'Obi-Wan Kenobi',
        'age':57,
        'lightsaber color':'blue',
        'apprentices':['Anakin Skywalker','Luke Skywalker'],
        'alias':'Ben Kenobi'
        }

jedi["girlfriend"] = "Satine Kryze"

x = 1
for key in jedi:
    print(f"{x}. {key}")
    x += 1

choice = input("Please input a key from above: ") 

if choice in jedi:
    print (jedi.get(choice))
else:
    print("Not an option")

