def bubblesort(mylist):
    for i in range(0,len(mylist)-1):
        for j in range(0, len(mylist)-1-i):
            if mylist[j]> mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

thelist=[12,3,4,542,342,54325,654436,13232,2131234,34]
print(bubblesort(thelist))


def bubblesort1(mylist):
    for passnum in range (len(mylist)-1,0,-1):
        for i in range(passnum):
            if mylist[i] >mylist[i+1]:
                temp = mylist[i]
                mylist[i]=mylist[i+1]
                mylist[i+1] =temp
    return mylist

alist=[54,26,93,17,77,31,44,55,20]
print(bubblesort1(alist))
