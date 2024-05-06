capitals = {"USA": "Washington D.C.",
            "Turkey": "Ankara",
            "Japan": "Tokyo"}


print(capitals.get("USA"))


if capitals.get("asdasdasd"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
# capitals.update({"USA" : "try"})

# capitals.pop("Turkey")
# capitals.popitem()
# capitals.clear()

print(capitals)

keys = capitals.keys()

print(keys)

for key in capitals.keys():
    print(key)
    
    
values = capitals.values()

print(values)

for value in capitals.values():
    print(value)
    
    
items = capitals.items()

print(items)    

for item in capitals.items():
    print(item)
    
    
for key, value in capitals.items():
    print(f"{key}: {value}")    