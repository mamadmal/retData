import mariadb
import matplotlib.pyplot as plt

try:
    connection = mariadb.connect (
    user="root",
    host="127.0.0.1",
    port=3306,
    database="ldrFor"
)
    print("connected!")
except:
    print("ohhh no!")

cur = connection.cursor()

#creat a list for saved datas on that.
data = [()]
#collect data from database
cur.execute(
    "SELECT data FROM felurencet", 
    (data)
)
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
print(total)
#do sum for whole element of list
myList = 1
for i in range(total):
    myList = myList + sdta[i]
print(myList)
#calc of mid.
mid = myList / total
print("the mid:",mid)

#for x-anxis of classter we need to some number
id = []
for i in range(total):
    id.append(i)
    ++i

#plot for the dataset
plt.plot(id, sdta)
plt.show()
