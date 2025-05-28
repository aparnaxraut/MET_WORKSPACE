list=["python","code","loop","if","python","else","if"]
stopwords={"if","else"}
for item in list:
    if item in stopwords:
        continue
    print(item)