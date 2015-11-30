class Telegrama:
    def __init__(self, line:str):
        parts = line.split(",")
        self.Provincia = int(parts[0])
        self.Departamento = parts[1]
        self.Circuito= parts[2]
        self.Mesa= int(parts[3])
        self.Telegrama= parts[4]
        self.Electores= int(parts[5])
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
    #inconsistentes = filter(telegramaInconsistente, v)
    
    inconsistentes = [t for t in v if (t.VotosCambiemos <= 0 or t.VotosEnBlanco < 0 or t.VotosFPV <= 0 or t.VotosImpugnados < 0 or t.VotosPositivos <= 0 or t.VotosRecurridos < 0 or t.VotosValidos <= 0 or t.TotalVotantes > t.Electores)]
    print ("Telegramas inconsistentes: ", len(inconsistentes))
    for t in inconsistentes:
        print(t)
    
    sumaCambiemos = 0
    sumaFPV = 0
    sumaBlancos = 0
    sumaDesvio = 0
    mesasInconsistentes = 0
    for telegrama in v:
        sumaCambiemos += telegrama.VotosCambiemos
        sumaFPV += telegrama.VotosFPV
        sumaBlancos += telegrama.VotosEnBlanco
        desvio = telegrama.TotalVotantes - (telegrama.VotosValidos + telegrama.VotosImpugnados + telegrama.VotosRecurridos)
        mesasInconsistentes += 1 if desvio != 0 else 0;
        sumaDesvio += desvio 
        
    total = sumaCambiemos + sumaFPV
    porcentajeFPV = sumaFPV * 100/total
    porcentajeCambiemos = sumaCambiemos * 100/total
    porcentajeInconsistencias = mesasInconsistentes * 100 / len(v)
    porcentajeDesvios = abs(sumaDesvio) * 100 / total
    
    print("Total FPV:", sumaFPV, "(", porcentajeFPV ,"%)" )
    print("Total Cambiemos", sumaCambiemos, "(", porcentajeCambiemos ,"%)" )
    print("Total votos desviados", sumaDesvio, "(", porcentajeDesvios, "%)")
    print("Mesas con desvios ", mesasInconsistentes, " (",porcentajeInconsistencias,"%)")


def telegramaInconsistente(t):
    return not((t.VotosFPV + t.VotosCambiemos == t.VotosPositivos) and (t.VotosEnBlanco + t.VotosPositivos == t.VotosValidos) and (t.TotalVotantes == t.VotosValidos + t.VotosImpugnados + t.VotosRecurridos))

def cargar_datos():
    file = open("EscrutinioProvisorio.csv")
    v = []
    for line in file:
        if not line.startswith("Provincia") and not line.startswith(","):
            v.append(Telegrama(line))
            
        # limita la cantidad de telegramas
        #if len(v) == 500:
        #    break
    file.close()
    return v

if __name__ == '__main__':
    main()
