import sys
import re

# Definir un arreglo con los estados de no aceptores
Advance = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Definir un arreglo con los estados que reconoce comentarios
Comment = [19,38]

# Definir un arreglo con los estados de aceptor
Accept = [15, 16, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]


# Definir un arreglo con los estados de error
Error = [39,40,41,42] 

Operators = {
    18: '(',
    20: '<',
    21: '<=',
    22: '<>',
    23: '>',
    24: '>=',
    25: ':=',
    26: '+',
    27: '-',
    28: '*',
    29: '/',
    30: '=',
    31: ';',
    32: ',',
    33: "'",
    34: '.',
    35: ')',
    36: '[',
    38: ']'
}

Identifier = {}
Integers = {}
Reals = {}

Keywords = {
    43: 'program',
    44: 'procedure',
    45: 'function',
    46: 'begin',
    47: 'end',
    48: 'var',
    49: 'integer',
    50: 'real',
    51: 'string',
    52: 'array',
    53: 'of',
    54: 'if',
    55: 'then',
    56: 'else',
    57: 'repeat',
    58: 'until',
    59: 'for',
    60: 'to',
    61: 'do',
    62: 'readLn',
    63: 'writeLn'
}

def check_keyword(word):
    for key, value in Keywords.items():
        if value == word:
            return True
    return False


# Función para verificar si el string es un número entero
def is_integer(word):
    try:
        int(word)
        return True
    except ValueError:
        return False


# Función para verificar si el string es un número flotante
def is_float(word):
    try:
        float(word)
        return True
    except ValueError:
        return False




def check_identifier(word):
    return word in Identifier.values()



def error_message(state):
       if state== 39:
              print(f"Simbolo de asignación := mal asignado.\n")
              sys.exit()
       elif state==40 :
              print(f"Comentario de una linea mal asignado.\n")
              sys.exit()
       elif state ==41:
               print(f" Simbolo de comentario de una linea mal asignado.\n")
               sys.exit()
       elif state ==42:
               print(f"Caracter inexistente.")
               sys.exit()

               



def transition_table(state, ch):
        if(state < 7):
            if(state== 0):
                if ch.isspace():
                       state=0
                       return 0
                elif  ch.isalpha(): #inicio estado cero
                        state=1                 #inicio  de estados no aceptores
                        return state
                elif  ch== '_':
                        state=2
                        return state
                elif   ch.isdigit():
                        state=4
                        return state
                elif   ch== '(':
                        state=7
                        return state
                elif    ch== '<':
                        state=10
                        return state
                elif  ch== '>':
                        state=11
                        return state
                elif   ch== ':':
                        state=12
                        return state
                elif  ch== "'":
                        state=13
                        return state
                elif  ch== '{':
                        state=14
                        return state
                elif  ch== '+':   #inicio de estados aceptores
                        state=26
                        return state   
                elif  ch== '-':
                        state=27
                        return state
                elif  ch== '*':
                        state=28
                        return state
                elif  ch== '/':
                        state=29
                        return state
                elif  ch== '=':
                        state=30
                        return state
                elif  ch== ';':
                        state=31
                        return state
                elif  ch== ',':
                        state=32
                        return state
                elif  ch== '.':
                        state=34
                        return state
                elif  ch== ')':
                        state=35
                        return state
                elif  ch== '[':
                        state=36
                        return state
                elif  ch== ']':
                        state=37
                        return state
                elif  ch== '}':  #inicio de estados de error
                        state=41
                        return state
                elif   ch in '!¡@#$%^&|"¿?':
                        state=42
                        return state           #fin del estado cero
                else :
                        return -1
            elif (state==1 ):
                if (ch.isalpha() or ch== '_' or ch.isdigit()): #inicio estado 1 
                        state=1                                                   #inicio estados no aceptores
                        return state
                elif (ch.isspace() or ch in '<>(=:+-*/;,.)[]{' or  ch== "'"): #inicio estados aceptores
                        state=15
                        return state
                else:
                        return -2
                
            elif (state==2 ):
                if (ch.isalpha() or ch.isdigit()): #inicio estado 2  estados no aceptores
                        state=3
                        return state
                else:
                        return -3
            elif (state==3 ):      
                if (ch.isalpha() or ch== '_' or ch.isdigit()):  #inicio estado 3  estados no aceptores
                        state=1
                        return state
                elif (ch.isspace() or ch in '<>(=:+-*/;,.)[]{' or  ch== "'"): #inicio estados aceptores
                        state=15
                        return state
                else:
                        return -4
            elif (state==4 ): 
                if ch.isdigit():  #inicio estado 4  estados no aceptores
                        state=4
                        return state
                if ch== '.':  
                        state=5
                        return state
                elif (ch.isalpha() or  ch.isspace() or ch in '<>(=:+-*/;,)[]{' or  ch== "'"): # estado aceptor
                    state=16
                    return state
                else:
                    return -5
            elif (state==5 ): 
                if ch.isdigit(): #inicio estado 5  estados no aceptores
                    state=6
                    return state
                else:
                        return -6
            elif (state==6 ):   
                if ch.isdigit(): #inicio estado 6  estados no aceptores
                        state=6
                        return state
                elif (ch.isalpha() or  ch.isspace() or ch in '<>(=:+-*/;,.)[]{' or  ch== "'"): # estado aceptor
                        state=17
                        return state
                else:
                        return -7
        elif (state>=7 ):
            if (state==7 ):
                if ch== '*': #inicio estado 7 estado no aceptor
                        state=8
                        return state       
                elif (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-/;,.)[]{' or  ch== "'"): #estado aceptor
                        state=18
                        return state
                else:
                        return -8
            elif (state==8 ):
                if (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-/;,.)[]{' or  ch== "'" or ch in '!¡@#$%^&|"¿?'): #inicio estado 8 estado no aceptor
                        state=8
                        return state
                elif  ch== '*': 
                        state=9
                        return state
                else:
                        return -9
            elif (state==9):    
                if (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-*/;,.[]{' or  ch== "'" or ch in '!¡@#$%^&|"¿?'): #inicio estado 9 estado no aceptor
                        state=8
                        return state
                elif ch== ')': #estado aceptor
                        state=19
                        return state
                else:
                        return -10
            elif (state==10):
                if (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<(:+-*/;,.[]{' or  ch== "'"): #inicio estado 10 estado  aceptor
                        state=20
                        return state
                elif  ch== '=':
                        state=21
                        return state
                elif  ch== '>':
                        state=22
                        return state
                else:
                        return -11
            elif (state==11):      
                if (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(:+-*/;,.)[]{' or  ch== "'"): #inicio estado 11 estado  aceptor
                        state=23
                        return state
                elif  ch== '=':
                        state=24
                        return state
                else:
                        return -12
                
            elif (state==12):           
                if ch== '=': #inicio estado 12 estado  aceptor
                        state=25
                        return state
                elif (ch.isalpha()  or  ch.isspace() or ch in '<>(:+-*/;,.)[]{' or  ch== "'"): # estado  de error
                        state=39
                        return state
                else:
                    return -13
            elif (state==13): 
                if ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-*/;,.)[]{': #inicio estado 12 estado no  aceptor
                    state=13
                    return state
                elif  ch== "'":                 #estado aceptor
                    state=33
                    return state
                else:
                    return -14  
            elif (state==14): 
                if (ch.isalpha() or ch.isdigit() or  ch==' ' or ch in '<>(=:+-*/;,.)[]' or  ch== "'" or ch in '!¡@#$%^&|"¿?'):  #inicio estado 14 estado no aceptor
                        state=14
                        return state
                elif  ch==  '}':           #estado aceptor
                        state=38
                        return state
                elif ( ch== '\r' or ch == '{' or ch =='\n'):  #estado error
                        print(state)
                        state=40
                        return state
                else:
                    return -15

"""
Probar la tabla de transicion 
state = 13
ch ="'"
output = transition_table(state, ch)
print(output)

"""

def show_tables():
    print("Tabla de identificadores\n")

    for clave_id, valor_id in Identifier.items():
          print(clave_id, ":", valor_id)
    
    print("Tabla de numeros enteros\n")
    for clave_int, valor_int in Integers.items():
        print(clave_int, ":", valor_int)

    print("Tabla de numeros reales\n")
    for clave_float, valor_float in Reals.items():
        print(clave_float, ":", valor_float)
      



def find_id(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    # Si el valor no se encuentra en el diccionario, puedes manejarlo como desees, por ejemplo, retornando None.
    return None



def record_token (state,ch,word):
        print(state)
        
        
        if is_integer(word):
             num = int(word)
             if num not in Integers.values():
                # Encontrar el próximo ID disponible
                idi =max(Integers.keys(), default=0) + 1
                Integers[idi] = num
                print("\n<",state,",",idi,">")
             elif num  in Integers.values():
                   idi=find_id(Integers,num)
                   print("\n<",state,",",idi,">")
        
        elif is_float(word):
              num = float(word)
              if num not in Reals.values():
                    idf=len(Reals) + 1
                    Reals[idf] = num
                    print("\n<",state,",",idf,">")
              elif num  in Reals.values():
                    idf=find_id(Reals,num)
                    print("\n<",state,",",idf,">")

        elif not check_keyword(word) :
            if not check_identifier(word):
                new_id = len(Identifier) + 1
                Identifier[new_id] = word
                print("\n<",state,",",new_id,">")
            elif check_identifier(word):
                  new_id=find_id(Identifier,word)
                  print("\n<",state,",",new_id,">")



def scanner():
    with open('archivo.txt') as file:
        while True:
          # leer un archivo
          ch = file.read(1)

          if not ch:
                 break
          
          state =0 #iniciamos el DFA
          word=""

          # Bucle para recorrer la tabla de transición hasta que no esté en ninguno de los arreglos de aceptor y de error
          while state not in Accept and state not in Error:
                 #print(state, ch)
                 state=transition_table(state, ch)
                 if state in Advance:
                        #print(f"está en el arreglo Advance.") 
                        word=word+ch
                        word=re.sub(r'\s', '', word)
                        #print(word)
                        ch= file.read(1)
                        
                 print(state)
                 if( state== 21):
                    word='<='
                 elif(state== 22):
                        word='<>'
                 elif(state== 24):
                        word='>='
                 elif(state== 25):
                        word=':='

          if state in Accept and state not in Comment:  # Verificar si el estado está en el arreglo aceptor 
              #print("Estado ",state,"letra ",ch, "cadena de palabra \n", word)
              record_token(state,ch,word)
              
          elif state in Error: # Verificar si el estado está en el arreglo error
               error_message(state)               
          
          else:
              print(f"El caracter no está en ninguno de los arreglos.")   
          
              
def main():
      scanner()
      show_tables()     

main()       


