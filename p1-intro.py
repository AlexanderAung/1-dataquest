from csv import reader

with open('artworks.csv') as file:
    read_file = reader(file)
    children = list(read_file)

print(children[0])
print(children[1])
