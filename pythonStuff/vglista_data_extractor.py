from urllib.request import urlopen
import json
import re
import sys


def writeHTMLFile(tempfile4):


    #print(getPeople(tempfile4))
    newbytefile = replaceStuf(tempfile4, 'td>', '\n', 1, False).encode('utf-8')

    with open('file.html', 'wb') as file:
        file.write(newbytefile)


def gothroughall(firstyear,lastyear,firstweek,lastweek):
    year = firstyear

    maindict = {}
    week = firstweek
    while(year <= lastyear):

        tempdict = {}
        print (year)
        while(week <= 52 and year < lastyear) or (week <= lastweek and year == lastyear):
            #tempString = getSongs(year, week)
            #writeHTMLFile(str(getAndFilterData(year,week)))
            tempdict[week] = getSongs(year, week)
            week += 1;
        maindict[year] = tempdict
        with open('vglista/vglista_'+str(year)+'.json', 'w', encoding='utf-8') as outfile:
            json.dump(tempdict, outfile, ensure_ascii=False, indent=4)
        year += 1;
        week = 1
    return maindict

def getAndFilterData(year,week):
    link = "https://norwegiancharts.com/archiv.asp?sparte=s&woche=" + str(week) + "&jahr=" + str(year) + "&todo=show"

    f = urlopen(link)
    myfile = f.read()
    mystringfile = str(myfile)
    tempfile2 = replaceStuf(mystringfile, '\\\\xf8', 'ø', 0, True)
    tempfile3 = replaceStuf(tempfile2, '\\\\xe5', 'å', 0, True)
    tempfile4 = replaceStuf(tempfile3, '\\\\xe9', 'é', 0, True)
    tempfile5 = replaceStuf(tempfile4, '\\\\', '', 0, True)
    return tempfile5


def getSongs(year, week):
    link = "https://norwegiancharts.com/archiv.asp?sparte=s&woche=" + str(week) + "&jahr=" + str(year) + "&todo=show"

    f = urlopen(link)
    myfile = f.read()
    mystringfile = str(myfile)
    tempfile2 = replaceStuf(mystringfile, '\\\\xf8', 'ø', 0, True)
    tempfile3 = replaceStuf(tempfile2, '\\\\xe5', 'å', 0, True)
    tempfile4 = replaceStuf(tempfile3, '\\\\xe9', 'é', 0, True)
    tempfile5 = replaceStuf(tempfile4, '\\\\', '', 0, True)

    return getPeople(tempfile5)

"""year = '1958'
week = '48'

link = "https://norwegiancharts.com/archiv.asp?sparte=s&woche="+week+"&jahr="+year+"&todo=show"

f = urlopen(link)
myfile = f.read()

print(type(myfile))

#mystringfile = myfile.decode('ISO-8859-1')
mystringfile = str(myfile)"""



def getPeople(mystringfile):
    pattern = '(?<="navb">).*?(?=</a)'
    p = re.compile(pattern)
    iterator = p.finditer(mystringfile)

    count0 = 0
    count1 = 1
    tempdict = {}
    newdict = {}
    for match in iterator:

        #print(match)
        if(count0 % 2 == 0):
            tempdict['Artist'] = mystringfile[match.span()[0]:match.span()[1]]
        else:
            tempdict['Song'] = mystringfile[match.span()[0]:match.span()[1]]
            newdict[count1] = tempdict
            tempdict = {}
            count1 += 1
        count0 += 1
    return newdict


def replaceStuf(mystringfile, pattern, newpattern, int, replace):
    p = re.compile(pattern)
    iterator = p.finditer(mystringfile)
    newfile = ""
    count0 = 0

    for match in iterator:
        #print(match)
        #print(match.span()[int])
        count1 = match.span()[int]
        newfile += mystringfile[count0:count1] + newpattern
        if replace:
            count0 = match.span()[1]
        else:
            count0 = count1
    newfile += mystringfile[count0:]
    return newfile


allsongs = gothroughall(1958,2018,42,46)
print(allsongs)


with open('vglista.json', 'w') as outfile:
    json.dump(allsongs, outfile, indent=4)

sys.exit()

#tempfile = replaceStuf(mystringfile,'\\\\r\\\\n', '\n',0, True)

"""
tempfile2 = replaceStuf(mystringfile,'\\\\xf8', 'ø',0, True)
tempfile3 = replaceStuf(tempfile2,'\\\\xe5', 'å',0, True)
tempfile4 = replaceStuf(tempfile3,'\\\\xe9', 'é',0, True)



print(getPeople(tempfile4))
newbytefile = replaceStuf(tempfile4, 'td>', '\n',1, False).encode('utf-8')

with open('file.html', 'wb') as file:
    file.write(newbytefile)
#print(myfile)"""



