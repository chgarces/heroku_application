list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 0]
dict1 = {"PASSED": list_1, "FAILED": list_2}

print("CHECK : {}".format(dict1))

dict2 = {"key": [], "key2": []}
for sc in dict1.get("PASSED"):
    if sc == 1:
        dict1.get("PASSED").remove(sc)
        dict1.get("FAILED").append(sc)


print("CHECK : {}".format(dict1))
print("CHECK : {}".format(dict2))

for k in dict2.keys():
    for kid in dict2.get(k):
        print("CHECK VALUES : {}".format(kid))
