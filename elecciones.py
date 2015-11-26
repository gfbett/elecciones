class Telegrama:
    def __init__(self, line:str):
        parts = line.split(",")
        self.Provincia = int(parts[0])
        self.Departamento = parts[1]
        self.Circuito= parts[2]
        self.Mesa= int(parts[3])
        self.Telegrama= parts[4]
        self.Electores= parts[5]
        self.TotalVotantes= int(parts[6])
        self.VotosRecurridos= int(parts[7])
        self.VotosImpugnados= int(parts[8])
        self.VotosEnBlanco= int(parts[9])
        self.VotosPositivos= int(parts[10])
        self.VotosValidos= int(parts[11])
        self.VotosCambiemos= int(parts[12])
        self.VotosFPV= int(parts[13])
        
    def __str__(self):
        return "Provincia:{0},Departamento:{1},Circuito:{2},Mesa:{3},Electores:{4},TotalVotantes:{5},VotosRecurridos:{6},VotosImpugnados:{7},VotosEnBlanco:{8},VotosPositivos:{9},VotosValidos:{10},VotosCambiemos:{11},VotosFPV:{12}".format(self.Provincia, self. Departamento, self. Circuito, self. Mesa, self. Electores, self. TotalVotantes, self.VotosRecurridos, self.VotosImpugnados, self.VotosEnBlanco, self.VotosPositivos, self.VotosValidos, self.VotosCambiemos, self.VotosFPV)
        
def main():
    v = cargar_datos()
    inconsistentes = filter(telegramaConsistente, v)

    for telegrama in inconsistentes:
        print(telegrama)
    print("fin")

def telegramaConsistente(t):
    return not((t.VotosFPV + t.VotosCambiemos == t.VotosPositivos) and (t.VotosEnBlanco + t.VotosPositivos == t.VotosValidos) and (t.TotalVotantes == t.VotosValidos + t.VotosImpugnados + t.VotosRecurridos))

def cargar_datos():
    file = open("EscrutinioProvisorio.csv")
    v = []
    for line in file:
        if not line.startswith("Provincia") and not line.startswith(","):
            v.append(Telegrama(line))
            
        # limita la cantidad de telegramas
        if len(v) == 500:
            break
    file.close()
    return v

if __name__ == '__main__':
    main()
