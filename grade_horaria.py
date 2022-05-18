segunda = [[[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], []]]
terca = [[[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], []]]
quarta = [[[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], []]]
quinta = [[[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], []]]
sexta = [[[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], []]]
sabado = [[[], [], [], [], []], [[], [], [], [], [], []], [[], [], [], []]]
dias_da_semana = [segunda, terca, quarta, quinta, sexta, sabado]


def mostra_horario():

    def view_grade(a):
        if len(a) == 0:
            resultado = ' '*8
        else:
            resultado = a[0]
        return resultado

    print('+---------------+----------+----------+----------+----------+----------+----------+')
    print('|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |')
    print('+---------------+----------+----------+----------+----------+----------+----------+')

    # Manha
    for x in range(0, 5):
        len_linha_manha = 0
        if x == 0:
            turno = '08:00 - 08:55'
        if x == 1:
            turno = '08:55 - 09:50'
        if x == 2:
            turno = '10:00 - 10:55'
        if x == 3:
            turno = '10:55 - 11:50'
        if x == 4:
            turno = '12:00 - 12:55'

        len_linha_manha = len(segunda[0][x]) + len(terca[0][x]) + len(
            quarta[0][x]) + len(quinta[0][x]) + len(sexta[0][x]) + len(sexta[0][x])
        if len_linha_manha > 0:
            print(
                f'| {turno} | {view_grade(segunda[0][x])} | {view_grade(terca[0][x])} | {view_grade(quarta[0][x])} | {view_grade(quinta[0][x])} | {view_grade(sexta[0][x])} | {view_grade(sabado[0][x])} |')
            print(
                '+---------------+----------+----------+----------+----------+----------+----------+')
    # Tarde
    for y in range(0, 6):
        len_linha_tarde = 0
        if y == 0:
            turno = '12:55 - 13:50'
        if y == 1:
            turno = '14:00 - 14:55'
        if y == 2:
            turno = '14:55 - 15:50'
        if y == 3:
            turno = '16:00 - 16:55'
        if y == 4:
            turno = '16:55 - 17:50'
        if y == 5:
            turno = '18:00 - 18:55'
        len_linha_tarde = len(segunda[1][y]) + len(terca[1][y]) + len(quarta[1][y]) + len(
            quinta[1][y]) + len(sexta[1][y]) + len(sexta[1][y]) + len(sabado[1][y])

        if len_linha_tarde > 0:
            print(
                f'| {turno} | {view_grade(segunda[1][y])} | {view_grade(terca[1][y])} | {view_grade(quarta[1][y])} | {view_grade(quinta[1][y])} | {view_grade(sexta[1][y])} | {view_grade(sabado[1][y])} |')
            print(
                '+---------------+----------+----------+----------+----------+----------+----------+')
    # Noite
    for z in range(0, 4):
        len_linha_noite = 0
        if z == 0:
            turno = '19:00 - 19:50'
        if z == 1:
            turno = '19:50 - 20:40'
        if z == 2:
            turno = '20:50 - 21:40'
        if z == 3:
            turno = '21:40 - 22:30'

        len_linha_noite = len(segunda[2][z]) + len(terca[2][z]) + len(
            quarta[2][z]) + len(quinta[2][z]) + len(sexta[2][z]) + len(sabado[2][z])
        if len_linha_noite > 0:
            print(
                f'| {turno} | {view_grade(segunda[2][z])} | {view_grade(terca[2][z])} | {view_grade(quarta[2][z])} | {view_grade(quinta[2][z])} | {view_grade(sexta[2][z])} | {view_grade(sabado[2][z])} |')
            print(
                '+---------------+----------+----------+----------+----------+----------+----------+')


def add_horario():
    count_errors = 0
    horarios = []
    for x in opcao[2:]:
        horarios.append(x)

    for i in horarios:
        for j in i:
            if j.isupper():
                marcador = i.index(j)
                turno = j

                if j == 'M':
                    periodo = 0
                if j == 'T':
                    periodo = 1
                if j == 'N':
                    periodo = 2

        for k in i[0:marcador]:
            for x in i[marcador+1:]:
                x = int(x)
                x = x-1
                if k == '2':
                    if len(segunda[periodo][x]) == 0:
                        segunda[periodo][x].append(opcao[1])

                    else:
                        count_errors = count_errors + 1
                        if count_errors == 1:
                            print(f'!({comando})')
                if k == '3':
                    if len(terca[periodo][x]) == 0:
                        terca[periodo][x].append(opcao[1])

                    else:
                        count_errors = count_errors + 1
                        if count_errors == 1:
                            print(f'!({comando})')
                if k == '4':
                    if len(quarta[periodo][x]) == 0:
                        quarta[periodo][x].append(opcao[1])
                    else:
                        count_errors = count_errors + 1
                        if count_errors == 1:
                            print(f'!({comando})')

                if k == '5':
                    if len(quinta[periodo][x]) == 0:
                        quinta[periodo][x].append(opcao[1])
                    else:
                        count_errors = count_errors + 1
                        if count_errors == 1:
                            print(f'!({comando})')
                if k == '6':
                    if len(sexta[periodo][x]) == 0:
                        sexta[periodo][x].append(opcao[1])
                    else:
                        count_errors = count_errors + 1
                        if count_errors == 1:
                            print(f'!({comando})')

                if k == '7':
                    if len(sabado[periodo][x]) == 0:
                        sabado[periodo][x].append(opcao[1])
                    else:
                        count_errors = count_errors + 1
                        if count_errors == 1:
                            print(f'!({comando})')
                    
    horarios.clear()


def rm_horario():
    count_errors = 0
    horarios = []
    for x in opcao[2:]:
        horarios.append(x)

    for i in horarios:
        for j in i:
            if j.isupper():
                marcador = i.index(j)
                turno = j

                if j == 'M':
                    periodo = 0
                if j == 'T':
                    periodo = 1
                if j == 'N':
                    periodo = 2

        for k in i[0:marcador]:

            for x in i[marcador+1:]:
                x = int(x)
                x = x-1
                if k == '2':
                    if (len(segunda[periodo][x])) == 0:
                        count_errors += 1

                    else:
                        if segunda[periodo][x][0] == opcao[1]:
                            segunda[periodo][x].remove(opcao[1])
                        else:
                            count_errors += 1

                if k == '3':
                    if (len(terca[periodo][x])) == 0:
                        count_errors += 1
                        # if count_errors == 1:
                        #     print(f'!({comando})') 
                    else:
                        if terca[periodo][x][0] == opcao[1]:
                            terca[periodo][x].remove(opcao[1])
                        else:
                            count_errors += 1

                if k == '4':
                    if (len(quarta[periodo][x])) == 0:
                        count_errors += 1
                        # if count_errors == 1:
                        #     print(f'!({comando})') 
                    else:
                        if quarta[periodo][x][0] == opcao[1]:
                            quarta[periodo][x].remove(opcao[1])
                        else:
                            count_errors += 1

                if k == '5':
                    if (len(quinta[periodo][x])) == 0:
                        count_errors += 1
                        # if count_errors == 1:
                        #     print(f'!({comando})') 
                    else:
                        if quinta[periodo][x][0] == opcao[1]:
                            quinta[periodo][x].remove(opcao[1])
                        else:
                            count_errors += 1
                                                                                                
                if k == '6':
                    if (len(sexta[periodo][x])) == 0:
                        count_errors += 1
                        # if count_errors == 1:
                        #     print(f'!({comando})') 
                    else:
                        if sexta[periodo][x][0] == opcao[1]:
                            sexta[periodo][x].remove(opcao[1])
                        else:
                            count_errors += 1

                if k == '7':
                    if (len(sabado[periodo][x])) == 0:
                        count_errors += 1

                    else:
                        if sabado[periodo][x][0] == opcao[1]:
                            sabado[periodo][x].remove(opcao[1])
                        else:
                            count_errors += 1
    horarios.clear()                        
                                                                   
    if count_errors > 0:
        print(f'!({comando})')


while True:
    comando = input()
    opcao = comando.split()

    if comando == 'Hasta la vista, beibe!':
        break
    if opcao[0] == '?':
        mostra_horario()
    if opcao[0] == '+':
        add_horario()
    if opcao[0] == '-':
        rm_horario()
