given=("sam","john","alex","bob")
for item in given:
    if len(item)==3:
        print(item.upper())
    else:
        print(item.capitalize())