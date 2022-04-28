import controller
from models.LinkedList import LinkedList
def main():
    minha_lista = LinkedList()
    while True:
        comando=input().split()
        if comando[0]=="RPI" and len(comando)==2: 
            controller.RPI(minha_lista, comando)
            minha_lista.traverse_list()
        if comando[0]=="RPF" and len(comando)==2:
            controller.RPF(minha_lista, comando)
            minha_lista.traverse_list()
        if comando[0]=="RPDE" and len(comando)==3:
            controller.RPDE(minha_lista, comando)
            minha_lista.traverse_list()
        if comando[0]=="RPAE" and len(comando)==3:
            controller.RPAE(minha_lista, comando)
            minha_lista.traverse_list()
        if comando[0]=="RPII" and len(comando)==3: 
            controller.RPII(minha_lista, comando)
            minha_lista.traverse_list()
        if comando[0]=="VNE" and len(comando)==1:
            print(f"O número de elementos são {controller.VNE(minha_lista, comando)}.")
        if comando[0]=="VP" and len(comando)==2: 
            if controller.VP(minha_lista, comando)==True:
                print(f"O país {comando[1]} encontra-se na lista.")
            else:
                print(f"O país {comando[1]} não se encontra na lista.")
        if comando[0]=="EPE" and len(comando)==1: 
            controller.EPE(minha_lista, comando)
        if comando[0]=="EUE" and len(comando)==1: 
            minha_lista.get_last_node()
            controller.EUE(minha_lista, comando)
        if comando[0]=="EP" and len(comando)==2: 
            controller.EP(minha_lista, comando)


        


        

