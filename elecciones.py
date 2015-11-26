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
        self.VotosEnBlanco= int(parts[9])
        self.VotosPositivos= parts[10]
        self.VotosValidos= parts[11]
        self.VotosCambiemos= int(parts[12])
        self.VotosFPV= int(parts[13])

def main():
    v = cargar_datos()


# previo a mostrar los telegramas filtraría por los que son inconsistentes.
# aplicar uno o varios filter a la colección previo definir qué es inconsistentes
# sugerencia:
#     VotosPositivos = VotosCambiemos + VotosFPV
#     VotosValidos = VotosPositivos + VotosEnBlanco
#     TotalVotantes = VotosRecurridos + VotosImpugnados + VotosEnBlanco + VotosEnPositivo
#    
#    inconsistentes = filter(inconsistencias, v)

    sumaCambiemos = 0
    sumaFPV = 0
    sumaBlancos = 0
    for telegrama in v:
        sumaCambiemos += telegrama.VotosCambiemos
        sumaFPV += telegrama.VotosFPV
        sumaBlancos += telegrama.VotosEnBlanco
        
    total = sumaCambiemos + sumaFPV
    porcentajeFPV = sumaFPV * 100/total
    porcentajeCambiemos = sumaCambiemos * 100/total
    print("Total FPV:", sumaFPV, "(", porcentajeFPV ,"%)" )
    print("Total Cambiemos", sumaCambiemos, "(", porcentajeCambiemos ,"%)" )


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
