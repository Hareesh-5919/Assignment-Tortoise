def rotate(array_list,length_n):
    x = array_list[length_n-1]
    for i in range(length_n-1,0,-1):
        array_list[i] = array_list[i-1]
        array_list[0] = x

array_list= [1, 3, 5, 2, 6, 2]
length_n = len(array_list)
print ("Given array_list is")
for i in range(0, length_n): 
    print (array_list[i], end = ' ')

rotate(array_list, length_n)
print ("\nRotated array_list is") 
for j in range(0, length_n): 
    print (array_list[j], end = ' ')