
import Binario_Library

Text = []

Add = [] #Adicionando Lista Vazia

Binary = []

Carac = "[,']"

#J = 0  # Definindo Variaveis

#W = 8

P = 0

D = 0

def Texto():

    Entrada = str(input('Digite o Texto >>>:'))  # Recenbendo string

    for I in Entrada:  # Para I em Distancia De Entrada, O I vai esta sendo definido letra por letra!

        ###################### Abecedario ##########################

        if I == 'a':  # Se I for em algum momento igual a ('a')

            Text.append(Binario_Library.a)

        if I == 'b':

            Text.append(Binario_Library.b)

        if I == 'c':

            Text.append(Binario_Library.c)

        if I == 'd':

            Text.append(Binario_Library.d)

        if I == 'e':

            Text.append(Binario_Library.e)

        if I == 'f':

            Text.append(Binario_Library.f)

        if I == 'g':

            Text.append(Binario_Library.g)

        if I == 'h':

            Text.append(Binario_Library.h)

        if I == 'i':

            Text.append(Binario_Library.i)

        if I == 'j':

            Text.append(Binario_Library.j)

        if I == 'k':

            Text.append(Binario_Library.k)

        if I == 'l':

            Text.append(Binario_Library.l)

        if I == 'm':

            Text.append(Binario_Library.m)

        if I == 'n':

            Text.append(Binario_Library.n)

        if I == 'o':

            Text.append(Binario_Library.o)

        if I == 'p':

            Text.append(Binario_Library.p)

        if I == 'q':

            Text.append(Binario_Library.q)

        if I == 'r':

            Text.append(Binario_Library.r)

        if I == 's':

            Text.append(Binario_Library.s)

        if I == 't':

            Text.append(Binario_Library.t)

        if I == 'u':

            Text.append(Binario_Library.u)

        if I == 'v':

            Text.append(Binario_Library.v)

        if I == 'w':

            Text.append(Binario_Library.w)

        if I == 'x':

            Text.append(Binario_Library.x)

        if I == 'y':

            Text.append(Binario_Library.y)

        if I == 'z':

            Text.append(Binario_Library.z)

            ###################### Abecedario Maiusculo ################

        if I == 'A':

            Text.append(Binario_Library.A1)

        if I == 'B':

            Text.append(Binario_Library.B1)


        if I == 'C':

            Text.append(Binario_Library.C1)

        if I == 'D':

            Text.append(Binario_Library.D1)

        if I == 'E':

            Text.append(Binario_Library.E1)

        if I == 'F':

            Text.append(Binario_Library.F1)

        if I == 'G':

            Text.append(Binario_Library.G1)

        if I == 'H':

            Text.append(Binario_Library.H1)

        if I == 'I':

            Text.append(Binario_Library.I1)

        if I == 'J':

            Text.append(Binario_Library.J1)

        if I == 'K':

            Text.append(Binario_Library.K1)

        if I == 'L':

            Text.append(Binario_Library.L1)

        if I == 'M':

            Text.append(Binario_Library.M1)

        if I == 'N':

            Text.append(Binario_Library.N1)

        if I == 'O':

            Text.append(Binario_Library.O1)

        if I == 'P':

            Text.append(Binario_Library.P1)

        if I == 'Q':

            Text.append(Binario_Library.Q1)

        if I == 'R':

            Text.append(Binario_Library.R1)

        if I == 'S':

            Text.append(Binario_Library.S1)

        if I == 'T':

            Text.append(Binario_Library.T1)

        if I == 'U':

            Text.append(Binario_Library.U1)

        if I == 'V':

            Text.append(Binario_Library.V1)

        if I == 'W':

            Text.append(Binario_Library.W1)

        if I == 'X':

            Text.append(Binario_Library.X1)

        if I == 'Y':

            Text.append(Binario_Library.Y1)

        if I == 'Z':

            Text.append(Binario_Library.Z1)

            ###################### Letras Acentuadas ####################

        if I == 'á':

            Text.append(Binario_Library.á)

        if I == 'ã':

            Text.append(Binario_Library.ã)

        if I == 'é':

            Text.append(Binario_Library.é)

        if I == 'ê':

            Text.append(Binario_Library.ê)

        if I == 'ü':

            Text.append(Binario_Library.ü)

        if I == 'ó':

            Text.append(Binario_Library.ó)

        if I == 'õ':

            Text.append(Binario_Library.õ)

        if I == 'ç':

            Text.append(Binario_Library.ç)

        if I == 'ñ':

            Text.append(Binario_Library.ñ)

            ###################### Caracteres ##########################

        if I == '!':

            Text.append(Binario_Library.exclamação)

        if I == '?':

            Text.append(Binario_Library.interrogação)

        if I == '/':

            Text.append(Binario_Library.barra)

        if I == ":":

            Text.append( Binario_Library.doisposto)

        if I == ';':

            Text.append( Binario_Library.pontovirgula)

        if I == ',':

            Text.append( Binario_Library.virgula)

        if I == '.':

            Text.append( Binario_Library.ponto)

        if I == '>':

            Text.append( Binario_Library.maior)

        if I == '<':

            Text.append( Binario_Library.menor)

        if I == '|':

            Text.append( Binario_Library.barrareta)

        if I == '@':

            Text.append( Binario_Library.arroba)

        if I == '#':

            Text.append( Binario_Library.hastag)

        if I == '$':

            Text.append( Binario_Library.cifrão)

        if I == '%':

            Text.append( Binario_Library.porcento)

        if I == '&':

            Text.append( Binario_Library.ecomercial)

        if I == '*':

            Text.append( Binario_Library.asterisco)

        if I == '{':

            Text.append( Binario_Library.Acolchetes)

        if I == '}':

            Text.append( Binario_Library.Fcolchetes)

        if I == '(':

            Text.append( Binario_Library.Aparenteses)

        if I == ')':

            Text.append( Binario_Library.Fparenteses)

        if I == '[':

            Text.append( Binario_Library.Achave)

        if I == ']':

            Text.append( Binario_Library.Fchave)

        if I == '_':

            Text.append( Binario_Library.underline)

        if I == '-':

            Text.append( Binario_Library.negativo)

        if I == '+':

            Text.append( Binario_Library.mais)

        if I == '=':

            Text.append( Binario_Library.igual)

        if I == ' ':

            Text.append( Binario_Library.espaço)

            ###################### numeros ##########################

        if I == '1':

            Text.append( Binario_Library.um)

        if I == '2':

            Text.append( Binario_Library.dois)

        if I == '3':

            Text.append( Binario_Library.tres)

        if I == '4':

            Text.append( Binario_Library.quatro)

        if I == '5':

            Text.append( Binario_Library.cinco)

        if I == '6':

            Text.append( Binario_Library.seis)

        if I == '7':

            Text.append( Binario_Library.sete)

        if I == '8':

            Text.append( Binario_Library.oito)

        if I == '9':

            Text.append( Binario_Library.nove)

        if I == '0':

            Text.append( Binario_Library.zero)


    print('\n',str.join(' ', Text))

    Text.clear()


def Binario():

    ##################################################################################################

    """Bloco para colocar espaçamento no binario no binario"""

    Binary.clear()#Limpar lista de binario!

    Entrada1 = input('Binario >>>;')  # Recebendo Binario

    for var in range(0, len(Carac)):  # Para cada numeros de caracteres

        Entrada1 = Entrada1.replace(Carac[var], "")  # trocar os caracteres para um espaço vazio!

    N = len(Entrada1)  # Ler Quantidade De Binario

    D = N // 8  # Divida A Quantidade De Binario Por 8!!! Ex: 01100001 01100001 // 16 = 2 Binarios

    J = 0

    W = 8

    ###################################################################################################

    """Bloco para transformar os binarios que estão em string para inteiros."""

    for O in range(D):  # Para Letra O em Distancia Da Variavel D

        S = Entrada1[J:W]  # Fazendo Slice Com Lista!, Issu é Oque Fara Str Em Int

        Add.append(S)  # Adiciona O Slice A Uma Lista, Ex: Add = ['01100001','01100001']

        J += 9  # Variaveis do Slice, A cada vez que o loop for feito Adicionara mais 9 no Slice!

        W += 9

    ###################################################################################################


    """Bloco para tradução dos binarios em letra"""

    for X in Add:  # Para X em uma Distancia de Add!, Ex: Add = ['01100001','01100001']

        if X ==  Binario_Library.a:  # Se X por algum momento for igual a '01100001'

            Binary.append('a')

        if X ==  Binario_Library.b:

            Binary.append('b')

        if X ==  Binario_Library.c:

            Binary.append('c')

        if X ==  Binario_Library.d:

            Binary.append('d')

        if X ==  Binario_Library.e:

            Binary.append('e')

        if X ==  Binario_Library.f:

            Binary.append('f')

        if X ==  Binario_Library.g:

            Binary.append('g')

        if X ==  Binario_Library.h:

            Binary.append('h')

        if X ==  Binario_Library.i:

            Binary.append('i')

        if X ==  Binario_Library.j:

            Binary.append('j')

        if X ==  Binario_Library.k:

            Binary.append('k')

        if X ==  Binario_Library.l:

            Binary.append('l')

        if X ==  Binario_Library.m:

            Binary.append('m')

        if X ==  Binario_Library.n:

            Binary.append('n')

        if X ==  Binario_Library.o:

            Binary.append('o')

        if X ==  Binario_Library.p:

            Binary.append('p')

        if X ==  Binario_Library.q:

            Binary.append('q')

        if X ==  Binario_Library.r:

            Binary.append('r')

        if X ==  Binario_Library.s:

            Binary.append('s')

        if X ==  Binario_Library.t:

            Binary.append('t')

        if X ==  Binario_Library.u:

            Binary.append('u')

        if X ==  Binario_Library.v:

            Binary.append('v')

        if X ==  Binario_Library.w:

            Binary.append('w')

        if X ==  Binario_Library.x:

            Binary.append('x')

        if X ==  Binario_Library.y:

            Binary.append('y')

        if X ==  Binario_Library.z:

            Binary.append('z')

        ###################### Abecedario Maiusculo ##########################

        if X ==  Binario_Library.A1:

            Binary.append('A')

        if X ==  Binario_Library.B1:

            Binary.append('B')

        if X ==  Binario_Library.C1:

            Binary.append('C')

        if X ==  Binario_Library.D1:

            Binary.append('D')

        if X ==  Binario_Library.E1:

            Binary.append('E')

        if X ==  Binario_Library.F1:

            Binary.append('F')

        if X ==  Binario_Library.G1:

            Binary.append('G')

        if X ==  Binario_Library.H1:

            Binary.append('H')

        if X ==  Binario_Library.I1:

            Binary.append('I')

        if X ==  Binario_Library.J1:

            Binary.append('J')

        if X ==  Binario_Library.K1:

            Binary.append('K')

        if X ==  Binario_Library.L1:

            Binary.append('L')

        if X ==  Binario_Library.M1:

            Binary.append('M')

        if X ==  Binario_Library.N1:

            Binary.append('N')

        if X ==  Binario_Library.O1:

            Binary.append('O')

        if X ==  Binario_Library.P1:

            Binary.append('P')

        if X ==  Binario_Library.Q1:

            Binary.append('Q')

        if X ==  Binario_Library.R1:

            Binary.append('R')

        if X ==  Binario_Library.S1:

            Binary.append('S')

        if X ==  Binario_Library.T1:

            Binary.append('T')

        if X ==  Binario_Library.U1:

            Binary.append('U')

        if X ==  Binario_Library.V1:

            Binary.append('V')

        if X ==  Binario_Library.W1:

            Binary.append('W')

        if X ==  Binario_Library.X1:

            Binary.append('X')

        if X ==  Binario_Library.Y1:

            Binary.append('Y')

        if X ==  Binario_Library.Z1:

            Binary.append('Z')

        ###################### Letras Acentuadas ####################

        if X ==  Binario_Library.á:

            Binary.append('á')

        if X ==  Binario_Library.ã:

            Binary.append('ã')

        if X ==  Binario_Library.é:

            Binary.append('é')

        if X ==  Binario_Library.ê:

            Binary.append('ê')

        if X ==  Binario_Library.ü:

            Binary.append('ü')

        if X ==  Binario_Library.ó:

            Binary.append('ó')

        if X ==  Binario_Library.õ:

            Binary.append('õ')

        if X ==  Binario_Library.ç:

            Binary.append('ç')

        if X ==  Binario_Library.ñ:

            Binary.append('ñ')

        ###################### Caracteres ############################


        if X ==  Binario_Library.exclamação:

            Binary.append('!')

        if X ==  Binario_Library.interrogação:

            Binary.append('?')

        if X ==  Binario_Library.barra:

            Binary.append('/')

        if X ==  Binario_Library.doisposto:

            Binary.append(':')

        if X ==  Binario_Library.pontovirgula:

            Binary.append(';')

        if X ==  Binario_Library.virgula:

            Binary.append(',')

        if X ==  Binario_Library.ponto:

            Binary.append('.')

        if X ==  Binario_Library.maior:

            Binary.append('>')

        if X ==  Binario_Library.menor:

            Binary.append('<')

        if X ==  Binario_Library.barrareta:

            Binary.append('|')

        if X ==  Binario_Library.arroba:

            Binary.append('@')

        if X ==  Binario_Library.hastag:

            Binary.append('#')

        if X ==  Binario_Library.cifrão:

            Binary.append('$')

        if X ==  Binario_Library.porcento:

            Binary.append('%')

        if X ==  Binario_Library.ecomercial:

            Binary.append('&')

        if X ==  Binario_Library.asterisco:

            Binary.append('*')

        if X ==  Binario_Library.Acolchetes:

            Binary.append('{')

        if X ==  Binario_Library.Fcolchetes:

            Binary.append('}')

        if X ==  Binario_Library.Aparenteses:

            Binary.append('(')

        if X ==  Binario_Library.Fparenteses:

            Binary.append(')')

        if X ==  Binario_Library.Achave:

            Binary.append('[')

        if X ==  Binario_Library.Fchave:

            Binary.append(']')

        if X ==  Binario_Library.underline:

            Binary.append('_')

        if X ==  Binario_Library.negativo:

            Binary.append('-')

        if X ==  Binario_Library.mais:

            Binary.append('+')

        if X ==  Binario_Library.igual:

            Binary.append('=')

        if X ==  Binario_Library.espaço:

            Binary.append(' ')

        ###################### numeros ##########################

        if X ==  Binario_Library.um:

            Binary.append('1')

        if X ==  Binario_Library.dois:

            Binary.append('2')

        if X ==  Binario_Library.tres:

            Binary.append('3')

        if X ==  Binario_Library.quatro:

            Binary.append('4')

        if X ==  Binario_Library.cinco:

            Binary.append('5')

        if X ==  Binario_Library.seis:

            Binary.append('6')

        if X ==  Binario_Library.sete:

            Binary.append('7')

        if X ==  Binario_Library.oito:

            Binary.append('8')

        if X ==  Binario_Library.nove:

            Binary.append('9')

        if X ==  Binario_Library.zero:

            Binary.append('0')


    print('\n',str.join('', Binary))

    Add.clear()

