from datetime import datetime
import os

def Header():
    print('==========================')
    print('Clínicas de Consultas Agíl')
    print('==========================')

def Menu():
    print('[1] CADASTRAR CLIENTE')
    print('[2] MARCAÇÃO DE CONSULTAS')
    print('[3] CANCELAMENTO DE CONSULTAS')
    print('[4] SAIR')

def Exit():
    print('=============')
    print('Volte sempre!')
    print('=============')

def RegisterClient():
    print('[Forneça as informações do Cliente]')
    name = str(input('Nome: ')).strip().lower()
    phone = str(input('Phone: ')).strip()

    if check_existing_phone(phone):
        print(f"\033[31mERRO: Já existe um cliente cadastrado com o telefone {phone}.\033[m")
        return

    with open(f'{name}.txt', 'w') as arq:
        arq.write(f'Nome: {name.capitalize()} \nPhone: {phone}')
    
    print("Paciente cadastrado com sucesso")

def check_existing_phone(phone):
    client_files = return_list_clients()

    for client_file in client_files:
        with open(client_file, 'r') as arq:
            content = arq.read()
            if f'Phone: {phone}' in content:
                return True

    return False

def list_clients():
    client_files = [file for file in os.listdir() if file.endswith('.txt')]

    if not client_files:
        print("Nenhum paciente cadastrado.")
        return None

    print("Lista de Pacientes:")
    for index, file in enumerate(client_files, start=1):
        with open(file, 'r') as arq:
            content = arq.read()
            print(f"{index}. {content}\n")

    return client_files

def return_list_clients():
    client_files = [file for file in os.listdir() if file.endswith('.txt')]

    if not client_files:
        print("Nenhum paciente cadastrado.")
        return None

    return client_files

def schedule_appointment():
    client_files = [file for file in os.listdir() if file.endswith('.txt')]

    if not client_files:
        print("Nenhum paciente cadastrado.")
        return

    print("Lista de Pacientes:")
    for index, file in enumerate(client_files, start=1):
        with open(file, 'r') as arq:
            content = arq.read()
            print(f"{index}. {content}\n")

    try:
        client_index = int(input("Escolha o número do cliente para agendar a consulta: ")) - 1
        selected_client = client_files[client_index]
    except (ValueError, IndexError):
        print("\033[31mERRO! Digite uma opção válida!\033[m")
        return

    day = get_valid_date()
    hour = input("Hora da consulta [ex.:9h]: ")
    specialty = input("Especialidade desejada: ")


    if check_existing_schedule(day, hour):
        print(f"Erro: Já existe um cliente agendado nesse dia e nessa hora!")
        return

    with open(selected_client, 'a') as arq:
        arq.write(f"\nConsulta agendada para dia: {day}, Hora: {hour}, Especialidade: {specialty}.")

    print("Consulta agendada com sucesso.")

def get_valid_date():
    while True:
        day = input("Dia da consulta [dia/mês/ano]: ")
        if is_valid_date(day):
            return day

def check_existing_schedule(day, hour):
    client_files = return_list_clients()

    for client_file in client_files:
        with open(client_file, 'r') as arq:
            content = arq.read()
            if f'Consulta agendada para dia: {day}, Hora: {hour}' in content:
                return True

    return False

def is_valid_date(day):
    try:
        appointment_date = datetime.strptime(day, "%d/%m/%Y")
        current_date = datetime.now()

        if appointment_date < current_date:
            print("Erro: Você está tentando marcar uma consulta para uma data anterior à data atual.")
            return False
        else:
            return True

    except ValueError:
        print("Erro: Formato de data inválido. Use o formato [dia/mês/ano].")
        return False

def cancellation_appointments():
    client_files = list_clients()

    if not client_files:
        return

    try:
        client_index = int(input("Escolha o número do cliente para listar os agendamentos: ")) - 1
        selected_client = client_files[client_index]
    except (ValueError, IndexError):
        print("\033[31mERRO! Digite uma opção válida!\033[m.")
        return

    with open(selected_client, 'r') as arq:
        content = arq.read()
        appointments = [line.strip() for line in content.split('\n') if line.startswith("Consulta")]

        if not appointments:
            print("Nenhum agendamento encontrado.")
            return

        print("\n" * 130)
        print("\nLista de Agendamentos:")
        for index, appointment in enumerate(appointments, start=1):
            print(f"{index}. {appointment}\n")

        try:
            appointment_index = int(input("Escolha o número do agendamento para cancelar: ")) - 1
            selected_appointment = appointments[appointment_index]
        except (ValueError, IndexError):
            print("\033[31mERRO! Digite uma opção válida!\033[m")
            return

        print(f"\nDetalhes do Agendamento escolhido:\n{selected_appointment}")

        cancel = input("Deseja cancelar este agendamento?[S/N]: ").lower()
        if cancel == 's':
            with open(selected_client, 'w') as arq:
                arq.write(content.replace(selected_appointment, ''))

            print("Agendamento cancelado com sucesso.")
        else:
            print("Agendamento não cancelado.")

def clean_terminal():
    print("\n" * 130)