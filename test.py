import pandas

bestand = pandas.read_csv("Pokemon.csv")

# print(bestand.columns)
go = bestand["Generation"] == 6
print(bestand[go]["Name"])


lijst = []
for i, pok in bestand.iterrows():
    if (pok["HP"] > 100 and pok["HP"] < 200):
        print(pok["NAME"])
