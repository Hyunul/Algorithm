while True:
    name, age, weight = input().split(" ")
    if name == "#" or age == "0" or weight == "0":
        break
    
    if int(age) > 17 or int(weight) >= 80:
        club = "Senior"
    else:
        club = "Junior"
    
    print(name, club)