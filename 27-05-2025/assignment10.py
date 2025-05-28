given={
    "name":"alice",
    "city":"new york",
    "hobby":"coding"
}
for item,value in given.items():
    if len(value)>5:
        print(f"{item} : {value.upper()}")
    else:
        print(f"{item} : {value.lower()}")
        