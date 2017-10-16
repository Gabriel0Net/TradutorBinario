#Texto Para Binario
#By Gabriel
#Scorpi0Net

################## APRESENTAÇÃO ##########################

print('███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗  ██████╗ ███╗   ██╗███████╗████████╗')
print('██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔═══██╗██╔═████╗████╗  ██║██╔════╝╚══██╔══╝')
print('███████╗██║     ██║   ██║██████╔╝██████╔╝██║██║   ██║██║██╔██║██╔██╗ ██║█████╗     ██║   ')
print('╚════██║██║     ██║   ██║██╔══██╗██╔═══╝ ██║██║   ██║████╔╝██║██║╚██╗██║██╔══╝     ██║   ')
print('███████║╚██████╗╚██████╔╝██║  ██║██║     ██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗   ██║   ')
print('╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ')

print("\nwww.scorpio0net.wordpress.com")

################## APRESENTAÇÃO ##########################


################## Imports ##########################

import Binario_Translate

#################### Escolhas #######################

Escolha = input('\n1 - Texto Para Binario \n\n2 - Binario Para Texto \n\nPara Sair : Exit\n\n>>>') # Definindo Opçoes


while Escolha != 'Exit':

    if Escolha == '1': #Se Escolha For Igual A 1

        Binario_Translate.Texto()


    elif Escolha == '2': # Escolha For Igual A 2

        Binario_Translate.Binario()


    elif Escolha != '1' and Escolha != '2' and Escolha != 'Exit':


        Escolha = input('\n1 - Texto Para Binario \n\n2 - Binario Para Texto \n\nPara Sair : Exit\n\n>>>')


    Escolha = input('\n1 - Texto Para Binario \n\n2 - Binario Para Texto \n\nPara Sair : Exit\n\n>>>')



print("\nObrigado por usar esta ferramenta! Nos da Scorpio0Net Agradecemos!! ")