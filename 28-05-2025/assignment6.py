fruits={
    "mango":50,
    "apple":60,
    "banana":70
}
fruits.update({"grapes":80})
print(fruits)
fruits["apple"]=90
print(fruits)
del fruits["banana"]
print(fruits)
print(fruits.items())