arr = [5,2,3,15,25,86,34,90,43,65,89,35,78]

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
            
    
        
                  
   

# bubbleSort(arr)#冒泡排序
# selectionSort(arr)#选择排序
# insertionSort(arr)#插入排序