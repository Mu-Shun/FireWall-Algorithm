class FireWall:
    def __init__(self, file):
        with open(file) as fw:
            listOfInput = []
            count = 0
            for line in fw:
                listOfInput.append([])
                stack = line.split(',')
                listOfInput[count].append(stack[0][1:])
                listOfInput[count].append(stack[1])
                listOfInput[count].append(stack[2])
                listOfInput[count].append(stack[3][:-2])
                count = count + 1
        self.dic = {}
        for i in range(len(listOfInput)):
            if "-" in listOfInput[i][2]:
                temp = listOfInput[i][2].split('-')
                for j in range(int(temp[0]), int(temp[1])+1):
                    if listOfInput[i][0]+listOfInput[i][1] not in self.dic:
                        self.dic[listOfInput[i][0]+listOfInput[i][1]] = {}
                        self.dic[listOfInput[i][0]+listOfInput[i][1]][j] = listOfInput[i][3]
                    else:
                        self.dic[listOfInput[i][0]+listOfInput[i][1]][j] = listOfInput[i][3]
            else:
                if listOfInput[i][0]+listOfInput[i][1] not in self.dic:
                    self.dic[listOfInput[i][0]+listOfInput[i][1]] = {}
                    self.dic[listOfInput[i][0]+listOfInput[i][1]][int(listOfInput[i][2])] = listOfInput[i][3]
                else:
                    self.dic[listOfInput[i][0]+listOfInput[i][1]][int(listOfInput[i][2])] = listOfInput[i][3]
                    
    def accept_packet(self, direction, protocol, port, IP_address):
        dic = self.dic
        if direction + protocol not in dic or port not in dic[direction + protocol]:
            return False
        elif dic[direction + protocol][port] == IP_address:
            return True
        elif "-" in dic[direction + protocol][port]:
            temp2 = dic[direction + protocol][port].split('-')
            temp2[0] = temp2[0].split('.')
            temp2[1] = temp2[1].split('.')
            IP_address = IP_address.split('.')
            for i in range(len(IP_address)):
                if int(IP_address[i]) - int(temp2[0][i]) == 0:
                    continue
                elif int(IP_address[i]) - int(temp2[0][i]) > 0:
                    for j in range(len(IP_address)):
                        if int(IP_address[j]) - int(temp2[1][j]) == 0:
                            continue
                        elif int(IP_address[j]) - int(temp2[1][j]) < 0:
                            return True
                        else:
                            return False
                    else:
                        return True
                else:
                    return False
            else:
                return True
        else:
            return False