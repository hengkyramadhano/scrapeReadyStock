mylist = ["7RHX58WH","7RHXGPBR","7RHXGPGY"]

copy_mylist = mylist.copy()
carry = []

print(f"Ini isi dari copy_mylist: {copy_mylist}")

for i in range(len(copy_mylist)):
    carry.append(copy_mylist[i])

    if i == 1 :
        for item in carry:
            copy_mylist.remove(item)
        break

print(f"Ini list carry: {carry}")
print(f"Ini list copy_mylist: {copy_mylist}")