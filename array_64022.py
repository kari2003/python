import array as arr

e=[1,2,3,4,5,6,7,8,9,10]


a=arr.array('i',e)

print("initial array")

for i in a:
    print(i,end=" ")

sliced_array=a[3:8]

print("slicing elements in a range 3-8")
print(sliced_array)

sliced_array=a[5:]
print("elements sliced from 5th element till the end")
print(sliced_array)


sliced_array=a[:]
print("printing all elements using slice operation")
print(sliced_array)
