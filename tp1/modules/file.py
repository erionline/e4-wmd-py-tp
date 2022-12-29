def writeToFile(data, filename):
    with open(filename, 'w') as file:
        file.write("nom,prenom,age,ville")
        for d in data:
            file.write(f"\n{d['nom']},{d['prenom']},{d['age']},{d['ville']}")

def readFromFile(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        data = data[1:]
        for i in range(len(data)):
            data[i] = data[i].strip().split(',')
    return data