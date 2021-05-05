from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv
import math
from random import choice
#creates an invisible border of stars so that the screeen is always a square
#that is the max location of the stars within
def borderv(s):
    MB = checksize(s)
    border = [["b1",MB,MB,MB,0,'w','o'],
              ["b2",MB,-MB,MB,0,'w','o'],
              ["b3",MB,MB,-MB,0,'w','o'],
              ["b4",MB,-MB,-MB,0,'w','o'],
              ["b5",-MB,MB,MB,0,'w','o'],
              ["b6",-MB,-MB,MB,0,'w','o'],
              ["b7",-MB,MB,-MB,0,'w','o'],
              ["b8",-MB,-MB,-MB,0,'w','o']]
    return border
#object shell for the stars themselves
class star:
    def __init__(self,name,x,y,z,s,c,t):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.size = s
        self.color = c
        self.type = t
#takes the array of the stars and finds the max size to send to the borders  
def checksize(s):
#    s = readall()
    m = max([max(abs(i[1])for i in s),max(abs(i[2])for i in s),max(abs(i[3])for i in s)])
    return m
#a broken function that doesnt server much of a purpose right now
def writestar(star):
    with open('space.csv', mode='a', newline='\n') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([star.name,star.x,star.y,star.z,star.size,star.color,star.type])
#oh shit i didnt need the other function in the shell file...i forgot about this
def printall(s):
#    s = readall()
    for i in s:
        print (i)
#takes the file location and pulls the values from a .csv file and translates them 
#to the star array
def readall(fp):
    stars = []
    with open(fp, mode='r') as file:
        data = csv.reader(file)
        for i,row in enumerate(data):
            stars.append(row)
            for x,col in enumerate(row):
                if (x > 0 and x <5):
                    stars[i][x] = int(col)
    return stars
#a set of functions to create a random star
#the first creates a random star name
def ranname():
	characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	let_ran = 1 + choice(range(3))
	num_ran = 1 + choice(range(3,6))
	start = ''
	for x in range(let_ran):
		start+=characters[choice(range(26))]
	start+='_'
	for y in range(num_ran):
		start+=str(choice(range(10)))
	return(start)
#this creates a random type of object, with different weights for objects
def rantype():
	types=['o','^','s','p']
	typ = 'o'
	t=choice(range(100))
	if t > 84 and t < 95:
		typ = 'p'
	if t > 94 and t < 99:
		typ = '^'
	if t > 98:
		typ = 's'
	return(typ)
#this gives the color based of object type
def rancolor(typ):
	star_colors = ['b','r','y']
	color = 'y'
	if typ == 'o':
		color = star_colors[choice(range(3))]
	if typ == '^':
		color = 'w'
	if typ == 's':
		color = 'k'
	if typ == 'p':
		color = 'm'
	return(color)
#this gives a size based off type and color
def ransize(typ,color):
	size = 0
	if typ == 'o':
		if color == 'b':
			size = choice(range(50,200))
		if color == 'r':
			size = choice(range(10,300))
		if color == 'y':
			size = choice(range(50,100))
	if typ == '^':
		size = 10
	if typ == 's':
		size = 5
	if typ == 'p':
		size = 1000
	return(size)
#the shell for making a random object
def ranstar():
	s = star(0,0,0,0,0,'y','o')
	s.name = ranname()
	s.x = choice(range(-100,100))
	s.y = choice(range(-100,100))
	s.z = choice(range(-100,100))
	s.type = rantype()
	s.color = rancolor(s.type)
	s.size = ransize(s.type,s.color)
	return(s)
#graphs the array given using the border array as a boundry
def graph(s):
    mpl.style.use('dark_background')
    border = borderv(s)
#    s = readall()
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    for i,txt in enumerate(border):
        ax.scatter3D(border[i][1],border[i][2],border[i][3],s=border[i][4],c=border[i][5],marker=border[i][6])
    for i,txt in enumerate(s):
        ax.scatter3D(s[i][1],s[i][2],s[i][3],s=s[i][4],c=s[i][5],marker=s[i][6])
        ax.text(s[i][1],s[i][2],s[i][3],txt[0])
    plt.show()
#given two objects and the full array can give the distance between the two
def distance(name1, name2, s):
#    s = readall()
    xyz = [[],[],[]]
    found = 0
    for i,row in enumerate(s):
        if (row[0] == name1 or row[0] == name2):
            xyz[0].append(s[i][1])
            xyz[1].append(s[i][2])
            xyz[2].append(s[i][3])
            found = found + 1
    if (found < 2):
        print ("stars not found")
        return 0
    elif (found == 2):
        dis = math.sqrt(pow((xyz[0][0]-xyz[0][1]),2)+pow((xyz[1][0]-xyz[1][1]),2)+pow((xyz[2][0]-xyz[2][1]),2))
        return dis
    else:
        print ("how")
        return 1
#the distance from given object to every other object in the array
def distoallstars(name, s):
#    s = readall()
    loc = 0
    for i,row in enumerate(s):
        if (row[0] == name):
            loc = i
    for x,r in enumerate(s):
        if (x != loc):
            print("distance from",s[loc][0],"to",s[x][0],"is:",round(distance(s[loc][0],s[x][0],s),1),"lys and will take:",round(traveltime(distance(s[loc][0],s[x][0],s)),1),"days at max speed")    
#does above using above for every object in the array
#also does this only once for each pairing
def disall(s):
    for i in range(len(s)):
        for x in range(len(s)-(i+1)):
            dis = distance(s[i][0],s[i+x+1][0],s)
            print("distance from",s[i][0],"to",s[i+x+1][0],"is:",round(dis,1),"lys and will take:",round(traveltime(dis),1),"days at max speed")
#a weird function based off my dnd game for travel time between places           
def traveltime(dis):
    c = 9460730472580800
    s = 200000000000
    m = dis * c
    sec = m / s
    mn = sec / 60
    h = mn / 60
    d = h / 24
    return d



        
    
