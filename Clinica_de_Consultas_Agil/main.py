import defs

while True:
    defs.Header()
    defs.Menu()

    response = input('ESCOLHA A OPÇÃO: ').strip()

    defs.clean_terminal()
    if response.isnumeric():
        response = int(response)
        if response == 1:
            while True:
                defs.clean_terminal()
                defs.RegisterClient()
                r = str(input('Deseja cadastrar outro cliente?[S/N]: ')).strip().upper()
                if r == 'N':
                    defs.clean_terminal()
                    break
                while r != 'S':
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    r = str(input('Deseja cadastrar outro cliente?[S/N]: ')).strip().upper()
                    if r == 'N':
                        defs.clean_terminal()
                        break
                if r == 'N':
                    break

        if response == 2:
            while True:
                defs.clean_terminal()
                defs.schedule_appointment()
                r = str(input('Deseja marcar outra consulta?[S/N]: ')).strip().upper()
                if r == 'N':
                    defs.clean_terminal()
                    break
                while r != 'S':
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    r = str(input('Deseja marcar outra consulta?[S/N]: ')).strip().upper()
                    if r == 'N':
                        defs.clean_terminal()
                        break
                if r == 'N':
                    break
        
        if response == 3:
            while True:
                defs.clean_terminal()
                defs.cancellation_appointments()
                r = str(input('Deseja cancelar outra consulta?[S/N]: ')).strip().upper()
                if r == 'N':
                    defs.clean_terminal()
                    break
                while r != 'S':
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    r = str(input('Deseja cancelar outra consulta?[S/N]: ')).strip().upper()
                    if r == 'N':
                        defs.clean_terminal()
                        break
                if r == 'N':
                    break

        if response == 4:
            defs.Exit()
            break
    
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')

