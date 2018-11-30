import json



totalscore = {}
year = 1958

while year < 2019:
    with open("vglista/vglista_"+str(year)+".json", "r") as read_file:
        data = json.load(read_file)

    print(year)
    totalscore[year] = {}
    for week in data:

        for rank in data[week]:
            print(week)
            tempTitile = data[week][rank]['Artist']+': '+data[week][rank]['Song']
            print(tempTitile)
            if tempTitile not in totalscore[year]:
                totalscore[year][tempTitile] = 41-int(rank)
            else:
                totalscore[year][tempTitile] += 41 - int(rank)
    year += 1

with open('highscore.json', 'w') as outfile:
    json.dump(totalscore, outfile,  ensure_ascii=False, indent=4)

