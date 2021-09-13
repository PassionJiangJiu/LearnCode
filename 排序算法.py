import math

arr = [5,2,3,15,25,86,34,90,43,65,89,35,78,13,33]

def bubbleSort(arr):
    '''
    冒泡排序
    '''
    if(len(arr)<2):
        print('数组内元素数不能为1')
        return
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
        print('第'+str(i+1)+'次冒泡排序结果为' + str(arr))
             
def selectionSort(arr):
    '''选择排序法'''
    if(len(arr)<2):
        print('数组内元素数不能为1')
        return 
    for i in range(0,len(arr)-1):
        minIndex = i
        for j in range(i,len(arr)-1):
            if (arr[minIndex] > arr[j+1]):
                minIndex = j+1
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        print('第'+str(i+1)+'次选择排序结果为' + str(arr))
        
def insertionSort(arr):
    '''插入排序'''
    if(len(arr)<2):
        print('数组内元素数不能为1')
        return 
    for i in range(0,len(arr)):
        for j in range(0,i):
            if(arr[i]<arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        print('第'+str(i)+'插入排序结果为' + str(arr))
            
def shellSort(arr):
    '''希尔排序'''
    if(len(arr)<2):
        print('数组内元素数不能为1')
        return 
    
    n = len(arr)
    gap = int(n/2)
    count = 1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i 
            while j >= gap and arr[j-gap] > temp :
                arr[j] = arr[j-gap]
                arr[j-gap] = temp
        gap = gap - 1 
        print('第'+str(count)+'次希尔排序结果为' + str(arr))
        count = count + 1

def mergeSort(arr):
    '''归并排序'''
    if(len(arr)<2):
        return arr
    mid = int(len(arr)/2)
    left , right = arr[:mid], arr[mid:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
    print(result)
    return result

def quickSort(arr, pivot, end):
    '''快速排序'''
    if pivot >= end:
        return
    temp = arr[pivot]
    low = pivot
    high = end
    while low < high:
        while low < high and arr[high] >= temp:
            high = high - 1
        arr[low] = arr[high]
        while low < high and arr[low] <= temp:
            low = low + 1
        arr[high] = arr[low]
    arr[low] = temp
    quickSort(arr, pivot, low-1)
    quickSort(arr, low+1, end)
    print(arr)
        
def 
        
    
                  
    

# bubbleSort(arr)#冒泡排序
# selectionSort(arr)#选择排序
# insertionSort(arr)#插入排序
# shellSort(arr)#希尔排序
# mergeSort(arr)#归并排序
# quickSort(arr,0,len(arr)-1)#快速排序