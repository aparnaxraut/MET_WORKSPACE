dictionary={
    "apple":2,
    "banana":3,
    "apricot":4,
    "berry":5
}
product=1
for item in dictionary:
    if item.startswith("a"):
        product*=dictionary[item]
print(product)