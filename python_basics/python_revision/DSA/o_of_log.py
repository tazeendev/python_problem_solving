def find_name(name,target):
    left=0
    right=len(name)-1
    while left<=right:
        mid_value=(left+right)//2
        if name[mid_value]==target:
            return mid_value
        elif name[mid_value]<target:
            left=mid_value+1
        else:
            right=mid_value-1
    return -1
names=['Tazeen','Shawana','Ayesha','Sadia','Sabah','Ali','Ahmad']
names.sort()
target_name='Sabah'
result=find_name(names,target_name)
if result!=-1:
    print(f'{target_name} found at index {result}')
else:
    print(f'{target_name} not found in the list')