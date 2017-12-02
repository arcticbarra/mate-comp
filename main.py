# Turing Machine simulator to add unary numbers (e.g. 11 + 111)
#
# prog is indexed by the current tape symbol (0 or 1) and then by state
# (a kind of instruction pointer) to get an 'instruction' comprising:
#   symbol to write on current tape position,
#   head action (-1 = move left, +1 = move right)
#   next state (like a goto jump).

#       symbol 0    symbol 1

# arreglo de diccionaries para cada estado
states = [{}, {}, {}, {}]

# states[estado actual][simbolo que lee] = (simbolo que escribe, direccion en que se mueve en la cinta, estado nuevo) 
states[0]['X'] = ('X', +1, 0)
states[0]['0'] = ('X', +1, 1)
states[0]['1'] = ('X', +1, 2)
states[0]['B'] = ('B', -1, 4)
states[1]['X'] = ('X', +1, 1)
states[1]['0'] = ('0', +1, 1)
states[1]['1'] = ('X', -1, 3)
states[2]['X'] = ('X', +1, 2)
states[2]['1'] = ('1', +1, 2)
states[2]['0'] = ('X', -1, 3)
states[3]['X'] = ('X', -1, 3)
states[3]['0'] = ('0', -1, 3)
states[3]['1'] = ('1', -1, 3)
states[3]['B'] = ('B', +1, 0)

tape = ['B','1', '1', '0', '1', '1', '0', '0', 'B'] # cinta (se agrega B al principio para simular lista circular)
head = 1                                    # posicion de la cabeza
state = 0                                   # estado actual
print(tape)
while state != 4:                           # mientras que no este en el estado de aceptacion
    symbol = tape[head]                         # lee el simbolo
    if symbol not in states[state]:
        print("Rechazada")
        break
    symbol, dir, state = t = states[state][symbol]  # obtiene la instruccion
    print(' ' * (head * 3 + 1) + '^  ' + str(t))  # imprime paso
    tape[head] = symbol                         # escribe el nuevo simbolo en la cinta
    print(tape)
    head = head + dir

if state == 4:
    print("Exito")
