'''
La progresión está indexada por el símbolo actual de la cinta (0 o 1)
y luego por estado (un tipo de apuntador de instrucción)
para obtener una 'instrucción', comprendiendo:
- Símbolo a escribir en la posición actual de la cinta,
- Acción de la cabeza (-1 = moverse a la izquierda, +1 = moverse a la derecha)
- Siguiente estado (Como un goto).
'''

# arreglo de diccionaries para cada estado
states = [{}, {}, {}, {}]

# states[estado actual][simbolo que lee] = (simbolo que escribe, direccion en que se mueve en la cinta, estado nuevo)
states[0]['Y'] = ('Y', +1, 0)
states[0]['0'] = ('X', +1, 1)
states[0]['1'] = ('X', +1, 2)
states[0]['B'] = ('B', -1, 4)

states[1]['Y'] = ('Y', +1, 1)
states[1]['0'] = ('0', +1, 1)
states[1]['1'] = ('Y', -1, 3)

states[2]['Y'] = ('Y', +1, 2)
states[2]['1'] = ('1', +1, 2)
states[2]['0'] = ('Y', -1, 3)

states[3]['Y'] = ('Y', -1, 3)
states[3]['0'] = ('0', -1, 3)
states[3]['1'] = ('1', -1, 3)
states[3]['X'] = ('X', +1, 0)

head = 0                                    # posicion de la cabeza
state = 0                                   # estado actual
tape = list(input('Enter tape: '))

# Verifica que termine en B la cinta
assert tape[-1] == 'B'

# Verifica que la cinta contega puros 0's y 1's
for i in range(len(tape) - 1):
    assert tape[i] in ['0', '1']

steps = 0
while state != 4:              # mientras que no este en el estado de aceptacion
    steps += 1
    symbol = tape[head]        # lee el simbolo

    print(f'{state}. State {state}')
    if symbol not in states[state]:
        print(' '.join(tape))
        print(' ' * (head * 2) + '^')  # imprime paso
        print("Rejected")
        break
    symbol, direction, state = states[state][symbol]  # obtiene la instruccion
    # escribe el nuevo simbolo en la cinta
    tape[head] = symbol
    print(' '.join(tape))
    print(' ' * (head*2) + '^')  # imprime paso
    head = head + direction

if state == 4:
    print("Accepted")
    print(steps, 'steps')
