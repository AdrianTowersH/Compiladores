import sys

# Definir un arreglo con los estados de no aceptores
Advance = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Definir un arreglo con los estados de aceptor
Accept = [15, 16, 17, 18, 19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]

# Definir un arreglo con los estados de error
Error = [39,40,41,42] 

def error_message(state):
       if state== 39:
              print(f"Simbolo de asignación := mal asignado.")
              sys.exit()
       elif state==40 :
              print(f"Comentario de una linea mal asignado.")
              sys.exit()
       elif state ==41:
               print(f" Simbolo de comentario de una linea mal asignado.")
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
                elif  ch.isdigit() or ch in '!¡@#$%^&|"¿?':
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
                if ch== '.':  #inicio estado 4  estados no aceptores
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
                if (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-/;,.)[]{' or  ch== "'"): #inicio estado 8 estado no aceptor
                        state=8
                        return state
                elif  ch== '*': 
                        state=9
                        return state
                else:
                        return -9
            elif (state==9):    
                if (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-*/;,.[]{' or  ch== "'"): #inicio estado 9 estado no aceptor
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
                if (ch.isalpha() or ch.isdigit() or  ch==' ' or ch in '<>(=:+-*/;,.)[]'):  #inicio estado 14 estado no aceptor
                        state=14
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


       
       

""" 
def transition_table(state, ch):
       if state== 0 and ch.isalpha(): #inicio estado cero
             state=1                 #inicio  de estados no aceptores
             return state
       elif state==0 and ch== '_':
            state=2
            return state
       elif state==0 and ch.isdigit():
            state=4
            return state
       elif state==0 and ch== '(':
            state=7
            return state
       elif state==0 and ch== '<':
            state=10
            return state
       elif state==0 and ch== '>':
            state=11
            return state
       elif state==0 and ch== ':':
            state=12
            return state
       elif state==0 and ch== "'":
            state=13
            return state
       elif state==0 and ch== '{':
            state=14
            return state
       elif state==0 and ch== '+':   #inicio de estados aceptores
            state=26
            return state   
       elif state==0 and ch== '-':
            state=27
            return state
       elif state==0 and ch== '*':
            state=28
            return state
       elif state==0 and ch== '/':
            state=29
            return state
       elif state==0 and ch== '=':
            state=30
            return state
       elif state==0 and ch== ';':
            state=31
            return state
       elif state==0 and ch== ',':
            state=32
            return state
       elif state==0 and ch== '.':
            state=34
            return state
       elif state==0 and ch== ')':
            state=35
            return state
       elif state==0 and ch== '[':
            state=36
            return state
       elif state==0 and ch== ']':
            state=37
            return state
       elif state==0 and ch== '}':  #inicio de estados de error
            state=41
            return state
       elif state==0 and ch in '!¡@#$%^&|"¿?':
            state=42
            return state           #fin del estado cero
       
       elif state==1 and  (ch.isalpha() or ch== '_' or ch.isdigit()): #inicio estado 1 
            state=1                                                   #inicio estados no aceptores
            return state
       elif state==1   and  (ch.isspace() or ch in '<>(=:+-*/;,.)[]{' or  ch== "'"): #inicio estados aceptores
            state=15
            return state
       
       elif state==2 and  (ch.isalpha() or ch.isdigit()): #inicio estado 2  estados no aceptores
            state=3
            return state
       
       elif state==3 and (ch.isalpha() or ch== '_' or ch.isdigit()):  #inicio estado 3  estados no aceptores
            state=1
            return state
       elif state==3   and  (ch.isspace() or ch in '<>(=:+-*/;,.)[]{' or  ch== "'"): #inicio estados aceptores
            state=15
            return state
       
       elif state==4 and ch== '.':  #inicio estado 4  estados no aceptores
            state=5
            return state
       elif state==4 and  (ch.isalpha() or  ch.isspace() or ch in '<>(=:+-*/;,)[]{' or  ch== "'"): # estado aceptor
            state=16
            return state
       
       elif state==5 and ch.isdigit(): #inicio estado 5  estados no aceptores
            state=6
            return state
       
       elif state==6 and ch.isdigit(): #inicio estado 6  estados no aceptores
            state=6
            return state
       elif state==6  and  (ch.isalpha() or  ch.isspace() or ch in '<>(=:+-*/;,.)[]{' or  ch== "'"): # estado aceptor
            state=17
            return state
       
       elif state==7  and  ch== '*': #inicio estado 7 estado no aceptor
            state=8
            return state       
       elif state==7  and  (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-/;,.)[]{' or  ch== "'"): #estado aceptor
            state=18
            return state

       elif state==8  and (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-/;,.)[]{' or  ch== "'"): #inicio estado 8 estado no aceptor
            state=8
            return state
       elif state==8  and  ch== '*': 
            state=9
            return state
       
       elif state==9  and (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-*/;,.[]{' or  ch== "'"): #inicio estado 9 estado no aceptor
            state=8
            return state
       elif state==9  and  ch== ')': #estado aceptor
            state=19
            return state

       elif state==10  and (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<(:+-*/;,.[]{' or  ch== "'"): #inicio estado 10 estado  aceptor
            state=20
            return state
       elif state==10  and  ch== '=':
            state=21
            return state
       elif state==10  and  ch== '>':
            state=22
            return state
       
       elif state==11  and (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(:+-*/;,.)[]{' or  ch== "'"): #inicio estado 11 estado  aceptor
            state=23
            return state
       elif state==11  and  ch== '=':
            state=24
            return state
       
       elif state==12  and  ch== '=': #inicio estado 12 estado  aceptor
            state=25
            return state
       elif state==12  and (ch.isalpha()  or  ch.isspace() or ch in '<>(:+-*/;,.)[]{' or  ch== "'"): # estado  de error
            state=39

       elif state==13  and (ch.isalpha() or ch.isdigit() or  ch.isspace() or ch in '<>(=:+-*/;,.)[]{'): #inicio estado 12 estado no  aceptor
            state=13
       elif state==13  and  ch== "'":                 #estado aceptor
            state=33

       elif state==14  and (ch.isalpha() or ch.isdigit() or  ch==' ' or ch in '<>(=:+-*/;,.)[]'):  #inicio estado 14 estado no aceptor
            state=14
       elif state==14  and  ch==  '}':           #estado aceptor
            state=38
       elif state==14  and ( ch== '\r' or ch == '{' or ch =='\n'):  #estado error
            state=40
"""
"""


              

def scanner():
    try:
         # Abrir el archivo en modo lectura
         with open('archivo.txt', 'r') as file:
                  
          while True:
               # Leer el contenido del archivo
               content = file.read(1)
             
               if not content:
                    break  # Fin del archivo
               #print(ch)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", str(e))
    




scanner()


          state =0 #iniciamos el DFA

               # Bucle para recorrer la tabla de transición hasta que no esté en ninguno de los arreglos de aceptor y de error
               while state not in Accept and state not in Error:
                    
                
                # Verificar si el número está en los arreglos
               if state in Accept:
                    print(f"está en el arreglo Accept.")
               elif state in Error:
                    error_message(state)
               else:
                    print(f"El caracter no está en ninguno de los arreglos.")





        

"""
