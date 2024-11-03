import math
def powerSet(set):
    size = len(set)
    setsize = int(math.pow(2, size))
    result = []
    for outer in range(setsize):
        current_subset = []
        for inner in range(size):
            
            if(outer & (1 << inner)) > 0:
                current_subset.append(set[inner])
        result.append(current_subset)
        
    return result

s = int(input("Enter array size: "))
set = []
for i in range(1, s + 1):
    n = int(input(f"Enter elemet {i}: "))
    set.append(n)
power_set_result = powerSet(set)
print("Power Set: ")
for subset in power_set_result:
    print(subset)