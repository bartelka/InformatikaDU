slovo = input("Zadaj slovo bez medzier: ")

if slovo == slovo[::-1]:
    print("Zadane slovo je palindrom.")
else:
    print("Zadane slovo nie je palindrom.")
