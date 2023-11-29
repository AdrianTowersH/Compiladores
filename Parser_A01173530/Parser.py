import sys
import re

# Definir un arreglo con los estados de no aceptores
Advance = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Definir un arreglo con los estados que reconoce comentarios
Comment = [19,38]

# Definir un arreglo con los estados de aceptor
Accept = [15, 16, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]


# Definir un arreglo con los estados de error
Error = [40,41,42,43] 

#Definir diccionario para identificadores
Identifier = {}
#Definir diccionario para numeros enteros
Integers = {}
#Definir diccionario para numeros reales
Reals = {}

# Declarar una lista global
token_list = []

# Definir un diccionario con todos los operadores
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
    37: ']',
    39: ':'
}

Union={
    15:'ID',
    16:'int_number',
    17:'real_number',
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
    37: ']',
    39: ':',
    44: 'program',
    45: 'procedure',
    46: 'function',
    47: 'begin',
    48: 'end',
    49: 'var',
    50: 'integer',
    51: 'real',
    52: 'string',
    53: 'array',
    54: 'of',
    55: 'if',
    56: 'then',
    57: 'else',
    58: 'repeat',
    59: 'until',
    60: 'for',
    61: 'to',
    62: 'do',
    63: 'readLn',
    64: 'writeLn'
}


# Definir un diccionario con todas las palabras claves
Keywords = {
    44: 'program',
    45: 'procedure',
    46: 'function',
    47: 'begin',
    48: 'end',
    49: 'var',
    50: 'integer',
    51: 'real',
    52: 'string',
    53: 'array',
    54: 'of',
    55: 'if',
    56: 'then',
    57: 'else',
    58: 'repeat',
    59: 'until',
    60: 'for',
    61: 'to',
    62: 'do',
    63: 'readLn',
    64: 'writeLn'
}

#Funcion booleana que checa si la palabra esta en el diccionario de palabras reservadas
def check_keyword(word):
    for key, value in Keywords.items():
        if value == word:
            return True
    return False

#Funcion booleana que checa si la palabra esta en el diccionario de  operadores
def check_operators(word):
    for key, value in Operators.items():
        if value == word:
            return True
    return False



#Función para verificar si el string es un número entero
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


# Función para agregar  la sequencia de tokens
def agregar_token(token_id):
    global token_list
    token_list.append(token_id)

def obtener_valor(numero):
    # Verificar si el número está en el diccionario
    if numero in Union:
        return Union[numero]
    else:
        return f"No hay valor asociado al {numero}"

#Funcion que checa que retorna el identificador del diccionario de identificadores
def check_identifier(word):
    return word in Identifier.values()


#Funcion que muestra mensaje de error dependiendo el estado y detiene el programa
def error_message(state):
       """if state== 39:
              print(f"\nSimbolo de asignación := mal asignado.")
              sys.exit()"""
       if state==40 :
              print(f"\nComentario de una linea mal asignado.\n")
              sys.exit()
       elif state ==41:
               print(f"\nSimbolo de comentario de una linea mal asignado.")
               sys.exit()
       elif state ==42:
               print(f"\nCaracter inexistente.")
               sys.exit()
       else :
               print(f"\nComentario de N lineas no terminado")
               sys.exit()

               
#Funcion de tabla de transicion que retorna el estado dependiendo del estado actual y la letra actual
#Aqui ocurre la transicion
def transition_table(state, ch):
        if(state < 7):
            if(state== 0):
                if ch.isspace():
                       state=0
                       return state
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
#Funcion que muestra las tablas final de identificadores, numeros enteros y reales
def show_tables():
    print("\nTabla de identificadores\n")

    for clave_id, valor_id in Identifier.items():
          print(clave_id, ":", valor_id)
    
    print("\nTabla de numeros enteros\n")
    for clave_int, valor_int in Integers.items():
        print(clave_int, ":", valor_int)

    print("\nTabla de numeros reales\n")
    for clave_float, valor_float in Reals.items():
        print(clave_float, ":", valor_float)





#Función que añade la ultima letra a la palabra iterada
def complete_string(state,word):
        if( state== 21):
                word='<='
                return word
        elif(state== 22):
                word='<>'
                return word
        elif(state== 24):
                word='>='
                return word
        elif(state== 25):
                word=':='
                return word
        elif(state== 33):
              word=word+"'" 
              return word     
        
        return word

#Funcion que retora el id de la palabra dependiendo su diccionario
def find_id(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    return None

#Funcion que sirve para definir  la cadena de los estados
def record_table (state,ch,word):
        #print(state)
        if  check_keyword(word) or check_operators(word) : #Valida si esta en el diccionario de palabras claves 
              idk=find_id(Keywords,word)
              print("\n<",idk,">")
              agregar_token(idk)
        
        elif is_integer(word): #Valida si la cadena es un numero entero de ser asi lo guardamos en la tabla de enteros
             num = int(word)
             if num not in Integers.values():
                # Encontrar el próximo ID disponible
                idi =max(Integers.keys(), default=0) + 1 #Incrementamos los IDs
                Integers[idi] = num
                print("\n<",state,",",idi,">")   #Mostramos estado y ID
                agregar_token(state)
             elif num  in Integers.values(): #Si el numero ya existe no incrementamos la cadena
                   idi=find_id(Integers,num)
                   print("\n<",state,",",idi,">")
                   agregar_token(state)
        
        elif is_float(word): #Valida si la cadena es un numero reales de ser asi lo guardamos en la tabla de reales
              num = float(word)
              if num not in Reals.values():
                    idf=len(Reals) + 1 #Incrementamos los IDs
                    Reals[idf] = num
                    print("\n<",state,",",idf,">") #Mostramos estado y ID
                    agregar_token(state)
              elif num  in Reals.values(): #Si el numero ya existe no incrementamos la cadena
                    idf=find_id(Reals,num)
                    print("\n<",state,",",idf,">")
                    agregar_token(state)

        elif not check_keyword(word) and  not check_operators(word): #Valida si la cadena no es una palabra reservada o un simbolo
            if not check_identifier(word):
                new_id = len(Identifier) + 1 #Incrementamos los IDs en el diccionario de identificadoresZ
                Identifier[new_id] = word
                print("\n<",state,",",new_id,">") #Mostramos estado y ID
                agregar_token(state)
            elif check_identifier(word):        #Si la palabra ya existe no incrementamos la cadena
                  new_id=find_id(Identifier,word)
                  print("\n<",state,",",new_id,">")
                  agregar_token(state)
       
        if ch is not None and ch not in [' ', '\n', '\r']:  # Si la letra quee sigue despues de la cadena es un operador lo recuperamos
                state = find_id(Operators, ch)
                if state is not None and ch not in [' ', '\n', '\r']:
                   print("\n<", state, ">")
                   agregar_token(state)


#Funcion que se encarga de mostrar el estado segun su transicion
def record_token (state,ch,word):
      if( state== 20 or state==23 or state== 39):
             print("\n<",state,">")
             agregar_token(state)
        
      if(state==15 or state==16 or state==17): #En dado caso que sea un estado de los aceptores de identificador, numero real o entero
            record_table (state,ch,word) #Hay que recuperar el ultimo caracter
      else:
           if state is not None and ch not in [' ', '\n', '\r']:
              print("\n<",state,">")
              agregar_token(state)



def scanner():
    with open('archivo.txt') as file:
        while True:
          # leer un archivo
          ch = file.read(1)

          if not ch: #Valida si el archivo esta vacio
                 break
          
          state =0 #Iniciamos el DFA
          word="" #Iniciamos la cadena de identificadores con vacio

          # Bucle para recorrer la tabla de transición hasta que no esté en ninguno de los arreglos de aceptor y de error
          while state not in Accept and state not in Error:
                 #print(state, ch)
                 state=transition_table(state, ch)
                 if state in Advance: #Valida si es un estado de avance para seguir leyendo
                        #print(f"está en el arreglo Advance.") 
                        word=word+ch
                        word=re.sub(r'\s', '', word)
                        #print(word)
                        ch = file.read(1)
                        if not ch: #Valida si el archivo esta vacio
                              if(state== 8 or state==9):
                                    error_message(state)
                              
                              break

                 #print(state, ch)
                 word=complete_string(state,word)

          #print("Estado ",state,"letra ",ch)
          if state in Accept and state not in Comment:  # Verificar si el estado está en el arreglo aceptor 
             #print("Estado ",state,"letra ",ch, "cadena de palabra \n", word)
              record_token(state,ch,word)
              
          elif state in Error: # Verificar si el estado está en el arreglo error
               error_message(state)               
          
def match():
        print("ok")

def parser():
    
    agregar_token('$')
    current_token=0
    start(current_token)

    if(token_list[current_token]=='$'):
          print("\nSystax Analisis corrected")
    else:
          print("\nError: Systax Analisis")
          sys.exit()
    
    """
    print("\nSequencia de tokens\n")
    for i in token_list:
        print(i)"""


#1. start → program ID ; vars_block functions_block procedures_block begin statement_list end •
def start(current_token):
      if(obtener_valor(token_list[current_token])=='program'):
            current_token=current_token+1
            if(obtener_valor(token_list[current_token])=='ID'):
                  current_token=current_token+1
                  vars_block(current_token)
                  procedures_block(current_token)
                  if(obtener_valor(token_list[current_token])=='begin'):
                        current_token=current_token+1
                        statement_list(current_token)
                        if(obtener_valor(token_list[current_token])=='end'):
                              current_token=current_token+1
                              if(obtener_valor(token_list[current_token])=='.'):
                                    print("Alles gut mit start")

                        else:
                               print("end")    
                              
                  else:
                     print("No hay ID")


            else:
                   print("Error: No hay ID")             
                  
      else:
            print("Error: No hay program")


#2. vars_block → var ID var_list’ : type_specifier ; var_declaration’ | ε
def vars_block(current_token):
       if(obtener_valor(token_list[current_token])=='var'):
               current_token=current_token+1
               var_listPrime(current_token)
               if(obtener_valor(token_list[current_token])==':'): 
                     current_token=current_token+1
                     type_specifier(current_token)
                     if(obtener_valor(token_list[current_token])==';'): 
                        current_token=current_token+1
                        


               else:
                     print("Error: No hay :")
    
       else:
           print("Error: No hay var")
      

#3. var_declaration’ → var_list : type_specifier ; var_declaration’ | ε
def var_declarationPrime(current_token):
      print("ok")
      
#4. var_list’ → , ID var_list’ | ε
def var_listPrime(current_token):
      print("ok")
      
#5. type_specifier → integer | real | string | array [ NUMBER • • NUMBER ] of basic_type
def type_specifier(current_token):
      print("ok")

#6. basic_type → integer | real | string
def basic_type(current_token):
       if(obtener_valor(token_list[current_token])== 'integer'):
            match('integer')
                   
       elif(obtener_valor(token_list[current_token])=='real'):
             match('real')
       elif(obtener_valor(token_list[current_token])=='string'):
             match('string')
       else:
            print("Error:")

#7. functions_block → functions_block’
def functions_block(current_token):
      print("ok")


#8. functions_block’ → function ID( params ) : type_specifier ; local_declarations begin statement_list end ; functions_block’ | ε
def functions_blockPrime(current_token):
      print("ok")

#9. procedures_block → procedures_block’
def procedures_block(current_token):
      print("ok")
#10. procedures_block’ → procedure ID( params ) ; local_declarations begin statement_list end ; procedures_block’ | ε
def procedures_blockPrime(current_token):
      print("ok")
#11. params → ID var_list’ : type_specifier ; param_list’ | ε
def params(current_token):
      print("ok")
#12. param_list’ → var_list : type_specifier ; param_list’ | ε
def paramsPrime(current_token):
      print("ok")
#13. local_declarations → vars_block | ε
def local_declarations(current_token):
      print("ok")
#14. statement_list → statement ; statement_list’
def statement_list(current_token):
      print("ok")
#15. statement_list’ → statement ; statement_list’ | ε
def statement_listPrime(current_token):
      print("ok")
#16. statement → ID statement′ | begin statement_list end| if ( logic_expression ) then statement   selection_stmt′ | for ID := NUMBER to NUMBER do statement | repeat statement_list until ( logic_expression ) | readln ( ID var_list′ ); | writeln ( output    output_list′) ;
def statement(current_token):
        if( obtener_valor(token_list[current_token])== 'ID'):
            match('ID')
                   
        elif(obtener_valor(token_list[current_token])=='begin'):
             match('if')
        elif(obtener_valor(token_list[current_token])=='for'):
             match('repeat')
        elif(obtener_valor(token_list[current_token])=='readln'):
              match('readln')
        elif(obtener_valor(token_list[current_token])=='writeln'):
             match('writeln')
        else:
            print("Error: Stament")

#17. statement′ → var′ :=  assignment_stmt′ | ( args )
def statementPrime(current_token):
      print("ok")
#18. assignment_stmt’ → arithmetic_expression | STRING
def assignment_stmtPrime(current_token):
      print("ok")
#19. selection_stmt’ → else statement | ε
def selection_stmtPrime(current_token):
      print("ok")
#20. output_list’ → , output output_list’ | ε
def output_listPrime(current_token):
      print("ok")
#21. output → arithmetic_expression | STRING | ε
def output(current_token):
      print("ok")
#22. var′ → [ arithmetic_expression ] | ε
def varPrime(current_token):
      print("ok")
#23. logic_expression → arithmetic_expression relop arithmetic_expression
def logic_expression(current_token):
      print("ok")
#24. relop → <= | < | > | >= | == | !=
def relop(current_token):
       if( current_token == '<='):
            match('<=')
                   
       elif(obtener_valor(token_list[current_token])=='<'):
             match('<')
       elif(obtener_valor(token_list[current_token])=='>'):
             match('>')
       elif(obtener_valor(token_list[current_token])=='>='):
             match('>=')
       elif(obtener_valor(token_list[current_token])=='='):
             match('=')
       elif(obtener_valor(token_list[current_token])=='<>'):
             match('<>')
       else:
            print("Error:")

#25. arithmetic_expression → term   arithmetic_expression’
def arithmetic_expression(current_token):
      print("ok")
#26. arithmetic_expression’ → + term arithmetic_expression’| - term arithmetic_expression’| ε
def arithmetic_expressionPrime(current_token):
        print("ok")
#27. term → factor term’
def term(current_token):
      print("ok")
#28. term’ → * factor   term’ | / factor  term’ | ε
def termPrime(current_token):
      print("ok")
#29. factor → ID factor′ | NUMBER  |  (arithmetic_operator)
def factor(current_token):
      print("ok")
#30. factor′ → ( args ) | var′
def factorPrime(current_token):
      print("ok")
#31. args → arithmetic_expression arg_list’ | ε
def args(current_token):
      print("ok")
#32. arg_list’ → , arithmetic_expression arg_list’ | ε
def  arg_listPrime(current_token):
      print("ok")


            


          
#Funcion main que se encarga de iniciar el scanner y depues mostrar las tablas         
def main():
      scanner()
      show_tables() 
      parser()    

main()       




