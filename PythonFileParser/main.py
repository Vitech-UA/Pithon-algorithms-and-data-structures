# Перевіримо скільки разів було ввімкнено UART


def getUartEnCount():
    '''
    Рахує к-ть ввімкнень UARTа
    :return: int
    '''
    log = open('sh_logs.txt', 'rt')
    uartEnablesCount = 0

    while True:
        fragment = log.readline()
        line = log.readline()
        if not line:
            break
        if (line.find("UART=1") != -1):
            uartEnablesCount += 1
    log.close()

    return uartEnablesCount


def readFile():
    file = open('sh_logs.txt', 'rt')
    output_data = ''
    readLines_count = 100
    current_line_index = int()
    while True:
        fragment = file.readline()
        line = file.readline()
        if not line:
            break
        current_line_index += 1
        if current_line_index > readLines_count:
            break
        output_data += line
        print("Line {0}:  {1}".format(current_line_index, line))
    file.close()


def getMcpWriteData():
    '''
    Повертає ліст, зі значеннями які записувались в mcp23017
    :return:
    '''
    mcpFinded = int()
    outpudData = list()
    log = open('sh_logs.txt', 'rt')
    while True:
        fragment = log.readline()
        line = log.readline()
        if not line:
            break
        position = line.find("mcp23017_write")
        if (position != -1):
            mcpFinded += 1
            insertLine = line[position + len('mcp23017_write'):]
            outpudData.insert(mcpFinded, insertLine)
    log.close()
    return outpudData


def getVoltageValues():
    '''
    Повертає ліст зі значеннями виміряних напруг живлення МК
    :return:
    '''
    findedCnt = int()
    outpudData = list()
    insertData = list()
    log = open('sh_logs.txt', 'rt', encoding='utf-8', errors='replace')
    searchKey = str()

    while True:
        fragment = log.readline()
        line = log.readline()
        if not line:
            break
        position = line.find(str('Напруга живлення МК, В'))
        if (position != -1):
            findedCnt += 1
            insertLine = line[position + len('Напруга живлення МК, В'):]
            # print(insertLine[1:2])
            if (insertLine[1:2] == "="): # :)
                outpudData.insert(findedCnt, insertLine[2:7])

    print("Finded: {0} voltage measurement".format(findedCnt))
    log.close()
    return outpudData


readFile()

print("Uart turned on {0} times".format(getUartEnCount()))

data = getMcpWriteData()
print(data[1])
print(data[2])
print(data[3])

voltages = getVoltageValues()
for i in range(len(voltages)):
    print(voltages[i])
