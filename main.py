import socket
import datetime

port = 1500 # Set the port number / Устанавливаем номер порта
server = "vip{}.hosting.reg.ru" # Set the server address format / Устанавливаем формат адреса сервера
serverRange = range(1, 1+1) # Set the server range / Устанавливаем диапазон серверов


    # Create a list of server addresses and ports / Создаем список адресов серверов и портов
servers = [
    (server.format(i), port) for i in serverRange
]
result = []

currentTime = datetime.datetime.now().strftime("%d.%m.%y %H-%M-%S")

for server in servers:
    # Connect to each server and check the connection status / Подключаемся к каждому серверу и проверяем статус подключения
    print(f"Connecting to {server[0]}:{server[1]}")
    try:
        socket.create_connection(server, timeout=5)
        result.append(f"Connection to {server[0]}:{server[1]} - SUCCESSFUL")
    except socket.error as e:
        result.append(f"Connection to {server[0]}:{server[1]} - FAILED: {str(e)}")

    # Write the connection results to a file / Записываем результаты подключения в файл
with open(f"results_{currentTime}.txt", "w") as file:
    file.write("\n".join(result))
    