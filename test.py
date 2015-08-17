import time
import random
def heapSort(hlist):
  
  for start in range((len(hlist)-2)//2, -1, -1):
    siftdown(hlist, start, len(hlist)-1)
 
  for end in range(len(hlist)-1, 0, -1):
    hlist[end], hlist[0] = hlist[0], hlist[end]
    siftdown(hlist, 0, end - 1)
  
 
def siftdown(hlist, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and hlist[child] < hlist[child + 1]:
      child += 1
    if hlist[root] < hlist[child]:
      hlist[root], hlist[child] = hlist[child], hlist[root]
      root = child
    else:
      break
    
def mergeSort(alist):
    
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)
    
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quicksort(myList, start, end):
    
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    
    return(myList)


def insertion(list3,n):
    start = time.time()
    for i in range(1,n):
        key=list3[i]
        j=i-1
        while(j>=0)&(list3[j]>key):
            list3[j+1]=list3[j]
            j=j-1
        list3[j+1]=key
    end = time.time()
    print("Time taken for insertion sort",end-start)
    #print(list3)
def selection(list2,n):
   
    start = time.time()
    for i in range(n-1):
       min=i
       for j in range(i+1,n):
           if(list2[j]<list2[min]):
               min=j
       temp=list2[i]
       list2[i]=list2[min]
       list2[min]=temp
    end = time.time()
    print("Time taken for selection sort",end-start)
    #print("selection sort output",list2)
def bubble(list1,n):
    start = time.time()
    for i in range(n-1):
       for j in range(n-i-1):
           if(list1[j]>list1[j+1]):
               temp=list1[j+1]
               list1[j+1]=list1[j]
               list1[j]=temp
    end = time.time()
    print("Time taken for  bubble sort",end-start)
    #print("bubble sort output   ",list1)
    
    
def main():
    list=[]
    list1=[]
    list2=[]
    myList=[]
    alist=[]
    n=int(input("enter the LIMIT"))
    for i in range(n):    
        list.append(random.randint(0,n))
    
    #print ("Unsorted list is\n",list)
    list1=list[:]
    bubble(list1,n)
    list2=list[:]
    selection(list2,n)
    list3=list[:]
    insertion(list3,n)
    myList =list[:]
    list4=list[:]
    start = time.time()
    sortedList = quicksort(myList,0,len(myList)-1)
    end = time.time()
    print("Time taken for quicksort",end-start)
    alist=list[:]
    start = time.time()     
    mergeSort(alist)
    end = time.time()
    print("Time taken for mergesort",end-start)
    start = time.time()
    heapSort(list4)
    end = time.time()
    print("Time taken for heapsort",end-start)
    #print("Sorted list is\n",sortedList)
   
main()
