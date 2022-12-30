import mariadb
import matplotlib.pyplot as plt
import sys

try:
    connection = mariadb.connect (
    user="root",
    host="127.0.0.1",
    port=3306,
    database="ldrFor"
)
    print("connected to DB!")
except:
    print("ohhh no!")
    sys.exit()

cur = connection.cursor()

data = [()] #define a list for store data that come from DB
print("please select the place to record data: \n(1): out-day\n(2): out-night\n(3): ind-day\n(14): ind-night")
def inDay():
    cur.execute("SELECT data FROM felurencet", (data))
    print("in-day added...\n")

def outDay():
    cur.execute("SELECT outDay FROM felu-outday",(data))
    print("out-day added...\n")

def outNight():
    cur.execute("SELECT outNight FROM felu-outNight",(data))
    print("out-night added...\n")

def inNight():
    cur.execute("SELECT inDay FROM felu-indoNight",(data))
    print("in-night added...\n")

print("typre yours:")
x = input()
if x == '1':
    inDay()
elif x == '2':
    outDay()
elif x == '3':
    outNight()
elif x == '4':
    inNight()
else:
    print("invalid number. you should choose 1-4")
    sys.exit()

#saved deformed data in new list.
sdta = []
#loops for add data to new list one by one
for data in cur:
    data = data[0]
    sdta.append(data)
#and then print whole datas
print(sdta[1:])
#give the number of list
total = len(sdta)
print("the total number: ",total)
#do sum for whole element of list
myList = 1
for i in range(total):
    myList = myList + sdta[i]
print("sum: ",myList)
#calc of mid.
mid = myList / total
print("the mid:",mid)

#for x-anxis of plot we need to some numbers
id = []
for i in range(total):
    id.append(i)
    ++i

#plot for the dataset
plt.plot(id, sdta)
plt.show()
