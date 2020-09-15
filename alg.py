def merge(arr, l, m, r, tracker): 
    n1 = m - l + 1
    n2 = r - m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0, n1): 
        L[i] = arr[l + i] 
  
    for j in range(0, n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0    
    j = 0 
    k = l  
  
    while i < n1 and j < n2:
        tracker.add(str(i), j)
        tracker.add(str(k), l)
        #tracker.add(str(j), i)
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def mergeSort(arr,l,r, tracker): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m, tracker) 
        mergeSort(arr, m+1, r, tracker) 
        merge(arr, l, m, r, tracker) 

def bubbleSort(arr, tracker): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                tracker.add(str(arr[j+1]), arr[j])
            else:
                tracker.add(str(arr[j]), arr[j+1])
  
