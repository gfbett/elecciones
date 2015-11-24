class Telegrama:
    def __init__(self, line:str):
        parts = line.split(",")
        self.Provincia = parts[0]
        self.Departamento = parts[1]
        self.Circuito= parts[2]
        self.Mesa= parts[3]
        self.Telegrama= parts[4]
        self.Electores= parts[5]
        self.TotalVotantes= parts[6]
        self.VotosRecurridos= parts[7]
        self.VotosImpugnados= parts[8]
        self.VotosEnBlanco= parts[9]
        self.VotosPositivos= parts[10]
        self.VotosValidos= parts[11]
        self.votosCambiemos= parts[12]
        self.votosFPV= parts[13]


def main():
    v = cargar_datos()

    for telegrama in v:
        print(telegrama.TotalVotantes)


def cargar_datos():
    file = open("EscrutinioProvisorio.csv")
    v = []
    for line in file:
        if not line.startswith("Provincia") and not line.startswith(","):
            v.append(Telegrama(line))
    file.close()
    return v


if __name__ == '__main__':
    main()
