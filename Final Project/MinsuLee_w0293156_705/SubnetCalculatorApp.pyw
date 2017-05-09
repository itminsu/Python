import sys
import csv
import math #to import log

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import SubnetCalculatorUI

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, SubnetCalculatorUI.Ui_Subnet_Calculator):

    classType = ''
    calculatorResults = []
    changeFlag = False

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.actionOpen.triggered.connect(self.load_subnet_calculator)
        self.actionCalculate.triggered.connect(self.calculate)
        self.actionClear.triggered.connect(self.clearAll)
        self.actionSave_As.triggered.connect(self.saveResult)
        self.actionExit.triggered.connect(self.exit_program)

        self.pushButton_calculate.clicked.connect(self.calculate)

    # ADD SLOT FUNCTIONS HERE
################################ load subnet file (subnetResults.txt) ####################################
    def load_subnet_calculator(self):
        try:
            self.LoadCalculatorFromFile("SubnetResults.txt")
            self.DisplayCalculatorResultsFromList()
        except FileNotFoundError as e:
            print(e)

################################ clear all ####################################
    def clearAll(self):
        self.lineEdit_nw_addr.clear()
        self.lineEdit_num_hosts_subnet.clear()
        self.lineEdit_subnet_sz.clear()
        self.lineEdit_decimal_octets.clear()
        self.lineEdit_decimal_addr.clear()
        self.lineEdit_binary_octets.clear()
        self.lineEdit_hex_octets.clear()
        self.lineEdit_nw_class.clear()
        self.lineEdit_numberOf_IP_addr.clear()
        self.lineEdit_subnetmask.clear()
        self.lineEdit_binary_mask.clear()
        self.lineEdit_numberOf_subnets.clear()
        self.list_IP_ranges.clear()

################################ Calculate function ####################################
    def calculate(self):
################################ Inspect the input
        try:
            nw_addr = self.lineEdit_nw_addr.text().strip()
            numberOfHostsPerSubnet = self.lineEdit_num_hosts_subnet.text().strip()

            if nw_addr == '' :
                # Occur the error message
                QMessageBox.information(self,
                                    'Error',
                                    'Enter the network address',
                                    QMessageBox.Ok)
                self.lineEdit_nw_addr.hasFocus()
                return
            elif numberOfHostsPerSubnet == '' :
                # Occur the error message
                QMessageBox.information(self,
                                    'Error',
                                    'Enter the number of hosts per subnet',
                                    QMessageBox.Ok)
                self.lineEdit_nw_addr.hasFocus()
                return
            elif self.validate_nw_addr(nw_addr) == 3: # 3 means network address has 3 dots
                lis = nw_addr.split('.')
                for li in lis:
                    if li.isdigit() == False:
                        QMessageBox.information(self,
                                            'Error',
                                            'Enter a valid network address',
                                            QMessageBox.Ok)
                        self.lineEdit_nw_addr.hasFocus()
                        return
            else:
                QMessageBox.information(self,
                                    'Error',
                                    'Enter a valid network address',
                                    QMessageBox.Ok)
                self.lineEdit_nw_addr.hasFocus()
                return
################################ Calculate
            list_nw_addr_1 = nw_addr.split('.')
            list_nw_addr_2 = nw_addr.split('.')
            list_nw_addr_3 = nw_addr.split('.')
            list_nw_addr_4 = nw_addr.split('.')
            list_nw_addr_5 = nw_addr.split('.')
            list_nw_addr_6 = nw_addr.split('.') # ['0','0','0','0']
# determine class by using first octet
            if 1 <= int(list_nw_addr_1[0]) <= 126:
                self.classType = 'A'
            elif 128 <= int(list_nw_addr_1[0]) <= 191:
                self.classType = 'B'
            elif 192 <= int(list_nw_addr_1[0]) <= 223:
                self.classType = 'C'

            validation = self.validateIPAndNumberOfHosts(list_nw_addr_1, int(numberOfHostsPerSubnet))

            if validation[0] == False:
                QMessageBox.information(self,
                                    'Error',
                                    validation[1],
                                    QMessageBox.Ok)
                self.lineEdit_nw_addr.hasFocus()
                return
            else: # if an user input valid network address and number of hosts per subnet
                self.changeFlag =  True
################################ Calculate and display information of subnet size, address, subnet mask and list of IP ranges
                self.calculatorResults.clear()

                self.calculatorResults.append(self.lineEdit_nw_addr.text().strip()) # NW addrress
                self.calculatorResults.append(self.lineEdit_num_hosts_subnet.text().strip()) # Number of hosts per subnet

                self.lineEdit_subnet_sz.setText(str(self.CalculateSubnetSize(numberOfHostsPerSubnet)))
                self.calculatorResults.append(str(self.CalculateSubnetSize(numberOfHostsPerSubnet)))

# Display address information
                self.lineEdit_decimal_octets.setText(self.CalculateDecimalOctets(nw_addr))
                dec_addr = str(self.CalculateDecimalAddress(list_nw_addr_1))
                self.lineEdit_decimal_addr.setText(dec_addr)
                bin_addr = self.CalculateBinaryAddress(list_nw_addr_1)
                self.lineEdit_binary_octets.setText(bin_addr)
                hx_addr = self.CalculateHexAddress(list_nw_addr_2)
                self.lineEdit_hex_octets.setText(hx_addr)

                self.calculatorResults.append(self.CalculateDecimalOctets(nw_addr))
                self.calculatorResults.append(dec_addr)
                self.calculatorResults.append(bin_addr)
                self.calculatorResults.append(hx_addr)

# Calculate and display subnet mask information
                self.lineEdit_nw_class.setText(self.CalculateNetworkClass(list_nw_addr_3[0]))
                self.lineEdit_numberOf_IP_addr.setText(str(self.CalculateNumberOfIPAddresses(list_nw_addr_4[0])))
                self.lineEdit_subnetmask.setText(self.CalculateSubnetMask(numberOfHostsPerSubnet))
                self.lineEdit_binary_mask.setText(self.CalculateBinaryMask(numberOfHostsPerSubnet))
                self.lineEdit_numberOf_subnets.setText("{:.0f}".format(self.CalculateNumberOfSubnets(list_nw_addr_5[0], numberOfHostsPerSubnet)))

                self.calculatorResults.append(self.CalculateNetworkClass(list_nw_addr_3[0]))
                self.calculatorResults.append(str(self.CalculateNumberOfIPAddresses(list_nw_addr_4[0])))
                self.calculatorResults.append(self.CalculateSubnetMask(numberOfHostsPerSubnet))
                self.calculatorResults.append(self.CalculateBinaryMask(numberOfHostsPerSubnet))
                self.calculatorResults.append("{:.0f}".format(self.CalculateNumberOfSubnets(list_nw_addr_5[0], numberOfHostsPerSubnet)))

# Make a list of IP Ranges
                self.list_IP_ranges.clear()
                ip_range = self.CalculateSubnetList(list_nw_addr_6, numberOfHostsPerSubnet)
                for i in range(len(ip_range)):
                    self.list_IP_ranges.addItem(ip_range[i])
                    self.calculatorResults.append(ip_range[i])
        except TypeError as e:
            print("TypeError occurred.")
            self.lineEdit_nw_addr.hasFocus()
        except ValueError:
            print("ValueError occurred.")
            QMessageBox.information(self,
                                'Error',
                                'Enter a valid input',
                                QMessageBox.Ok)
            self.lineEdit_nw_addr.hasFocus()
        except Exception as e:
            print(e)
            QMessageBox.information(self,
                                'Error',
                                e,
                                QMessageBox.Ok)
            self.lineEdit_nw_addr.hasFocus()

################################ Save the information to file (subnetResults.txt) ####################################
    def saveResult(self):
        self.save_changes_to_file()

    #ADD HELPER FUNCTIONS HERE
################################ Determine validation of network address ####################################
    def validate_nw_addr(self, nw_addr): # count a number of dots
        try:
            count = 0
            li_nw_addrs = list(nw_addr)
            for li_nw_addr in li_nw_addrs:
                if li_nw_addr == '.':
                    count += 1
            return count
        except Exception as e:
            print(e)
################################ Save the results to file (SubnetResults.txt) ####################################
    def save_changes_to_file(self):
        try:
            if self.changeFlag ==  True:
                dataFileName = "SubnetResults.txt"
                with open(dataFileName, "w") as myFile:
                    for i in range(len(self.calculatorResults)):
                        if i < len(self.calculatorResults):
                            myFile.write(self.calculatorResults[i] + "\n")
                        else: # Last line
                            myFile.write(self.calculatorResults[i])
                self.changeFlag =  False
                QMessageBox.information(self, 'Saved', 'Changes were saved to the file', QMessageBox.Ok)
            else:
                QMessageBox.information(self, 'Not accepted', 'No Changes were occurred.', QMessageBox.Ok)
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
################################ The function to load caclulate file ####################################
    def LoadCalculatorFromFile(self, dataFileName):
        try:
            self.calculatorResults.clear()
            with open(dataFileName, "r") as myFile:
                fileData = csv.reader(myFile)
                for row in fileData:
                    self.calculatorResults.append(row)
        except Exception as e:
            print(e)
################################ Display the all of results of calculate from list ####################################
    def DisplayCalculatorResultsFromList(self):
        try:
            # Initialize all widgets
            self.clearAll()
            # Display data
            self.lineEdit_nw_addr.setText(self.calculatorResults[0][0]) # NW addrress
            self.lineEdit_num_hosts_subnet.setText(self.calculatorResults[1][0]) # Number of hosts per subnet
            self.lineEdit_subnet_sz.setText(self.calculatorResults[2][0]) # Subnet size
            # Calculate and display address information
            self.lineEdit_decimal_octets.setText(self.calculatorResults[3][0])
            self.lineEdit_decimal_addr.setText(self.calculatorResults[4][0])
            self.lineEdit_binary_octets.setText(self.calculatorResults[5][0])
            self.lineEdit_hex_octets.setText(self.calculatorResults[6][0])
            # Calculate and display netmask information
            self.lineEdit_nw_class.setText(self.calculatorResults[7][0])
            self.lineEdit_numberOf_IP_addr.setText(self.calculatorResults[8][0])
            self.lineEdit_subnetmask.setText(self.calculatorResults[9][0])
            self.lineEdit_binary_mask.setText(self.calculatorResults[10][0])
            self.lineEdit_numberOf_subnets.setText(self.calculatorResults[11][0])
            # Listing IP Ranges
            str_ip_ranges = ''
            iteration = len(self.calculatorResults) - 12 # 20 - 12 = 8 times
            for i in range(iteration):
                str_ip_ranges += self.calculatorResults[i + 12][0] + '|'
            ip_ranges = str_ip_ranges.split('|')
            for ip_range in ip_ranges:
                self.list_IP_ranges.addItem(ip_range)
        except IndexError:
            print("IndexError occurred.")
        except Exception as e:
            print(e)
################################ Set the able ####################################
    def setEditable(self):
        self.lineEdit_subnet_sz.setEnabled(False)
        self.lineEdit_decimal_octets.setEnabled(False)
        self.lineEdit_decimal_addr.setEnabled(False)
        self.lineEdit_binary_octets.setEnabled(False)
        self.lineEdit_hex_octets.setEnabled(False)
        self.lineEdit_nw_class.setEnabled(False)
        self.lineEdit_numberOf_IP_addr.setEnabled(False)
        self.lineEdit_subnetmask.setEnabled(False)
        self.lineEdit_binary_mask.setEnabled(False)
        self.lineEdit_numberOf_subnets.setEnabled(False)
################################ Calculate subnet size ####################################
#Claculate subnet size by using the number of hosts per subnet
    def CalculateSubnetSize(self, numberOfHostsPerSubnet):
        if self.classType == 'C': # Class C
            for n in range(1,8): # The number of hosts in Class C has range 1 (2**1 -1) ~ 254 (2**8 -2)
                if 2**n - 1 <= int(numberOfHostsPerSubnet) <= 2**(n+1) - 2: # 2 means network and broadcast address
                    return 2**(n+1)
                                  # Return 4 if range is located between 1 and 2
                                  # Return 8 if range is located between 3 and 6
                                  # Return 16 if range is located between 7 and 14
                                  # Return 32 if range is located between 15 and 30
        elif self.classType == 'B': # Class B
            for n in range(1,16):
                if 2**n - 1 <= int(numberOfHostsPerSubnet) <= 2**(n+1) - 2:
                    return 2**(n+1)
        elif self.classType == 'A': # Class A
            for n in range(1,24):
                if 2**n - 1 <= int(numberOfHostsPerSubnet) <= 2**(n+1) - 2:
                    return 2**(n+1)
                                  # Return 16,777,216 if range is located between 8,388,607 and 16,777,214
################################ Show validate hosts per subnet ####################################
    def validateHostsPerSubnet(self, classOfNetwork, num_hosts):
        if classOfNetwork == 'A': # Class A has 24 zero that define the number of hosts
            if 1 <= num_hosts <= (2 ** 24) - 2 : #(2 ** 24)16,777,216 - 2
                return [True,'']
            else:
                return [False, 'Invalid The number of host of A class']
        elif classOfNetwork == 'B': # Class B has 16 zero that define the number of hosts
            if 1 <= num_hosts <= (2 ** 16) - 2 : #(2 ** 16)65,536 - 2
                return [True,'']
            else:
                return [False, 'Invalid The number of host of B class']
        elif classOfNetwork == 'C': # Class C has 8 zero that define the number of hosts
            if 1 <= num_hosts <= (2 ** 8) - 2 : #(2 ** 8)256 - 2
                return [True,'']
            else:
                return [False, 'Invalid The number of host of C class']
################################ Show validate ip and number of hosts ####################################
    def validateIPAndNumberOfHosts(self, list_str_nw_addr, num_hosts):
        list_int_nw_addr = [0,0,0,0]
        for i in range(len(list_str_nw_addr)): # str -> int
            list_int_nw_addr[i] = int(list_str_nw_addr[i])
        if list_int_nw_addr[0] == 0 :
            return [False, 'Invalid network address: Enter a valid network address \n Enter the number not first octet 1']
        elif 1 < list_int_nw_addr[0] and list_int_nw_addr[0] > 223: # If 1st octet is not between 1 and 223, it's not valid
            return [False, 'Invalid network address: Enter a valid network address \n Enter the number between 1 and 223.']
        else:
            if list_int_nw_addr[0] == 127: # # If 1st octet is 127, it's not valid (loop back)
                return [False, 'Invalid network address: Enter a valid network address \n Enter the number not first octet 127.']
            else: # If 1st octet is valid, validate the following 3 again.
                if 1 <= list_int_nw_addr[0] <= 126: # class Type = 'A'
                    if list_int_nw_addr[1] != 0 or list_int_nw_addr[2] != 0 or list_int_nw_addr[3] != 0 :
                        return [False, 'Invalid network address: Enter a valid network address \n A class should be XXX.0.0.0']
                    else:
                        return self.validateHostsPerSubnet('A', num_hosts) # Validate # of hosts per subnet (A class)
                elif 128 <= list_int_nw_addr[0] <= 191: # classType = 'B'
                    if list_int_nw_addr[2] != 0 or list_int_nw_addr[3] != 0 :
                        return [False, 'Invalid network address: Enter a valid network address \n B class should be XXX.XXX.0.0']
                    else:
                        return self.validateHostsPerSubnet('B', num_hosts) # Validate # of hosts per subnet  (B class)
                elif 192 <= list_int_nw_addr[0] <= 223: #  classType = 'C'
                    if list_int_nw_addr[3] != 0 :
                        return [False, 'Invalid network address: Enter a valid network address \n C class should be XXX.XXX.XXX.0']
                    else:
                        return self.validateHostsPerSubnet('C', num_hosts) # Validate # of hosts per subnet  (C class)

################################ Retrun ipaddress to decimal octets ####################################
    def CalculateDecimalOctets(self, ipAddress):
        return ipAddress

################################ Calculate decimal address ####################################
#I found law how to get decimal address but, I don't know why it is
    def CalculateDecimalAddress(self, ipAddress):
        list_IP = ipAddress
        return int(list_IP[0]) * (2 ** 24) + int(list_IP[1]) * (2 ** 16) \
               + int(list_IP[2])  * (2 ** 8) + int(list_IP[3]) * (2 ** 0)

################################ make binary ####################################
    def trans(self, x):
        if x == 0: return [0] * 8
        bit = []
        while x:
            bit.append(x % 2)
            x >>= 1
        return self.makeBinary(bit[::-1])

################################ A function to make binary ####################################
    def makeBinary(self, li):
        newli = []
        loop = 8 - len(li)
        for i in range(loop):
            newli.append(0)
        return newli + li

################################ Convert int to str ####################################
    def convertItemIntTOStr(self, list):
        string = ''
        for i in range(len(list)):
            string += str(list[i])
        return string

################################ Create binary address ####################################
    def CalculateBinaryAddress(self, ipAddress):
        list_IP = ipAddress
        for i in range(len(list_IP)):
            list_IP[i] = self.convertItemIntTOStr(self.trans(int(list_IP[i])))
        return ".".join(list_IP)

################################ Convert from decimal to hex ####################################
    def decToHex(self, dec):
        hx_str = hex(dec).split('x')[1].upper()
        if len(list(hx_str)) == 1:
            hx_str = '0' + hx_str
        return hx_str

################################ Create hex address ####################################
    def CalculateHexAddress(self, ipAddress):
        list_IP = ipAddress
        for i in range(len(list_IP)):
            list_IP[i] = self.decToHex(int(list_IP[i]))
        return '.'.join(list_IP)

################################ Define the class of network ####################################
    def CalculateNetworkClass(self, ipAddress):
        ip = int(ipAddress)
        if 1 <= ip <= 126: # 127 is loopback address
            return 'A'
        elif 128 <= ip <= 191:
            return 'B'
        elif 192 <= ip <= 223:
            return 'C'

################################ Calculate the number of available ip address ####################################
    def CalculateNumberOfIPAddresses(self, networkIPAddress):
        ip = int(networkIPAddress)

        if 1 <= ip <= 126:
            return 2 ** 24 # Class A - 16777216 # 127 is loopback address
        elif 128 <= ip <= 191:
            return 2 ** 16 # Class B - 65536
        elif 192 <= ip <= 223:
            return 2 ** 8 # Class C - 256

################################ Calculate subnet mask ####################################
# get the form like '255.255.255.192 or /26'
    def CalculateSubnetMask(self, numberOfHostsPerSubnet):
        try:
            # math.log(64, 2) = 6
            valueOfLog = int(math.log(self.CalculateSubnetSize(numberOfHostsPerSubnet), 2))
            # int(binary, 2)
            str_binary_mask = self.CalculateBinaryMask(numberOfHostsPerSubnet) # ex)'11111111.11111111.11111111.11000000'
            list_binary_mask = str_binary_mask.split(".") # ex)["11111111","11111111","11111111","11000000"]
            for i in range(len(list_binary_mask)): # ex)['255','255','255','192']
                list_binary_mask[i] = str(int(list_binary_mask[i], 2))
            return ".".join(list_binary_mask) + " or /" + str(32 - valueOfLog)# ex) '255.255.255.192 or /26'
        except Exception as e:
            print(e)

################################ Calculate the binary ####################################
    def CalculateBinaryMask(self, numberOfHostsPerSubnet):
        try:
# Log make big number to simple
            valueOfLog = int(math.log(self.CalculateSubnetSize(numberOfHostsPerSubnet), 2))
            if self.classType == 'C':
                return "11111111." * 3 + ("1" * (8-valueOfLog)) + ("0" * valueOfLog)
            # ex) 64  log (64, 2) = 6
            #     11111111.11111111.11111111.xxxxxxxx
            # --> 11111111.11111111.11111111.11000000
            elif self.classType == 'B':
                li_temp = list(("1" * (8*2-valueOfLog)) + ("0" * valueOfLog))
                li_temp[7] = li_temp[7] + '.' # Insert a dot(.)
                return "11111111." * 2 + ''.join(li_temp)
            elif self.classType == 'A':
                li_temp = list(("1" * (8*3-valueOfLog)) + ("0" * valueOfLog))
                li_temp[7] = li_temp[7] + '.' # Insert a 1st dot(.)
                li_temp[15] = li_temp[15] + '.' # Insert a 2nd dot(.)
                return "11111111." * 1 + ''.join(li_temp)
        except Exception as e:
            print(e)

################################ Calculate the number of subnets ####################################
    def CalculateNumberOfSubnets(self, ipAddress, numberOfHostsPerSubnet):
        ip = int(ipAddress)
        subnet_size = self.CalculateSubnetSize(numberOfHostsPerSubnet)
        if 1 <= ip <= 126: # in class A
            return 2 ** 24 / subnet_size # The avaiable address is devided by sunnet size
                                          # to show number of hosts each address
        elif 128 <= ip <= 191: # in class B
            return 2 ** 16 / subnet_size
        elif 192 <= ip <= 223: # in class C
            return 2 ** 8 / subnet_size # display # of subnets

################################ Calculate List of ip addresses ####################################
    def CalculateSubnetList(self, ipAddress, numberOfHostsPerSubnet): # returns a list of ip addresses
        try:
            # math.log(64, 2) returns 6 (2 ** 6 = 64)
            list_ip_range = []
            subnet_sz = self.CalculateSubnetSize(numberOfHostsPerSubnet)
            valueOfLog = int(math.log(subnet_sz, 2))
 # Class C
            if self.classType == 'C':
                iteration = 2 ** (8 - valueOfLog) # Interate as many the number of subnet mask
                for i in range(iteration):
                    temp_ip = ipAddress[0:3] # ex) ['XXXXXXXX','XXXXXXXX','XXXXXXXX','xxxxxxxx']
                    list_ip_range.append('.'.join(temp_ip) + '.' + str(subnet_sz * i) + ' - ' + '.'.join(temp_ip) + '.' + str(subnet_sz * (i+1) - 1))
                return list_ip_range
                # if the number of subnets is 4
                # XXXXXXXX.XXXXXXXX.XXXXXXXX.0 - 63
                # XXXXXXXX.XXXXXXXX.XXXXXXXX.64 - 127
                # XXXXXXXX.XXXXXXXX.XXXXXXXX.128 - 191
                # XXXXXXXX.XXXXXXXX.XXXXXXXX.192 - 255

 # Class B
            elif self.classType == 'B':
                if 0 < int(numberOfHostsPerSubnet) <= (2 ** 8) - 2: # 1 ~ 254
                    inner_iteration = 2 ** (8 - valueOfLog)
                    for i in range(2 ** 8): # 256 * iteration
                        temp_ip = ipAddress[0:2] # ex) ['XXXXXXXX','XXXXXXXX','xxxxxxxx','xxxxxxxx']
                        temp_ip.append(str(i))
                        # print(temp_ip)
                        for i in range(inner_iteration): # iteration
                            list_ip_range.append('.'.join(temp_ip) + '.' + str(subnet_sz * i) + ' - ' + '.'.join(temp_ip) + '.' + str(subnet_sz * (i+1) - 1))
                    return list_ip_range
                elif (2 ** 8) - 2 < int(numberOfHostsPerSubnet) <= (2 ** 16) - 2: # 255 ~ 65,534
                    iteration = 256 / (2 ** (valueOfLog - 8)) # (Test data:iteration : 8 ( = 256 / 2 ** (13 - 8)))
                    for i in range(int(iteration)):
                        temp_ip = ipAddress[0:2] # ex) ['XXXXXXXX','XXXXXXXX','xxxxxxxx','xxxxxxxx']
                        list_ip_range.append('.'.join(temp_ip) + '.' + str(2 ** (valueOfLog - 8) * i) + '.0' + ' - ' + '.'.join(temp_ip) + '.' + str(2 ** (valueOfLog - 8) * (i+1) - 1) + '.255')
                    return list_ip_range

                # if the number of subnets is 254
                # XXXXXXXX.XXXXXXXX.0.0 - 0.255
                # XXXXXXXX.XXXXXXXX.1.0 - 0.255
                # ~
                # XXXXXXXX.XXXXXXXX.254.0 - 254.255
                # XXXXXXXX.XXXXXXXX.255.0 - 255.255

 # Class A
            elif self.classType == 'A':
                if 0 < int(numberOfHostsPerSubnet) <= (2 ** 8) - 2: # 1 ~ 254
                    inner_iteration = 2 ** (8 - valueOfLog) # inner iteration = 4 times
                    temp_ip = ['']
                    temp_ip[0] = ipAddress[0]
                    for i in range(2 ** 8): # 256 * 256 * iteration
                        if i == 0:          # determine second octet
                            temp_ip.append(str(i)) # ex) ['10','0'] -> ['10','1'] -> ... -> ['10','255']
                        else:
                            del temp_ip[1:3] # ['10','0','255'] -> ['10']
                            temp_ip.append(str(i)) # # ['10','1'] -> ['10','2'] ... ['10','255']
                        for i in range(2 ** 8): # 256 * iteration
                            if i == 0:
                                temp_ip.append(str(i)) # ex) ['10','0','0'] -> ['10','0','1'] -> ... -> ['10','0','255']
                            else:
                                del temp_ip[2] # ['10','0','0'] -> ['10','0']
                                temp_ip.append(str(i)) # # ['10','0'] -> ['10','0','1'] ...
                            for i in range(inner_iteration): # iteration
                                list_ip_range.append('.'.join(temp_ip) + '.' + str(subnet_sz * i) + ' - ' + '.'.join(temp_ip) + '.' + str(subnet_sz * (i+1) - 1))
                                #                                   10.0.0.0 - 10.0.0.63
                                #                                   10.0.0.64 - 10.0.0.127
                                #                                             ....
                                #                                   10.0.0.192 - 10.0.0.255
                                #                                   10.0.1.0 - 10.0.1.63
                    return list_ip_range

                elif (256 ** 1) - 2 < int(numberOfHostsPerSubnet) <= (256 ** 2) - 2: # 255 ~ 65,534 (Test:5000)
                    iteration = 256 / (2 ** (valueOfLog - 8)) # (Test data:iteration : 8 ( = 256 / 2 ** (13 - 8)))
                    for i in range(256): # 256 * 8 times
                        temp_ip = ipAddress[0:1] # ex) ['10']
                        temp_ip.append(str(i)) # ex) ['10','0'] -> ['10','1'] -> ... -> ['10','255']
                        for i in range(int(iteration)): # 8 times
                            list_ip_range.append('.'.join(temp_ip) + '.' + str(2 ** (valueOfLog - 8) * i) + '.0' + ' - ' + '.'.join(temp_ip) + '.' + str(2 ** (valueOfLog - 8) * (i+1) - 1) + '.255')
                            #                                 ex) 10.0.0.0 ~ 10.0.31.255
                            #                                     10.0.32.0 ~ 10.0.63.255
                            #                                              ....
                            #                                     10.0.224.0 ~ 10.0.255.255
                            #                                     10.1.0.0 ~ 10.1.31.255
                            #                                     10.1.32.0 ~ 10.1.63.255
                            #                                              ....
                            #                                     10.1.224.0 ~ 10.1.255.255
                            #                                              ....
                            #                                     10.255.224.0 ~ 10.255.255.255
                    return list_ip_range
                elif (256 ** 2) - 2 < int(numberOfHostsPerSubnet) <= (256 ** 3) - 2: # 65,535 ~ 16,777,214 (Test:300,000)
                    iteration = 256 / (2 ** (valueOfLog - 16)) # (Test data:iteration : 32 ( = 256 / 2 ** (19 - 16)))
                    for i in range(int(iteration)): # 32 times
                        temp_ip = ipAddress[0] # ex) '10'
                        list_ip_range.append(temp_ip + '.' + str(2 ** (valueOfLog - 16) * i) + '.0.0' + ' - ' + temp_ip + '.' + str(2 ** (valueOfLog - 16) * (i+1) - 1) + '.255.255')
                        #                                 ex) 10.0.0.0 - 10.7.225.255
                        #                                     10.8.0.0 - 10.15.225.255
                        #                                             ...
                        #                                     10.248.0.0 - 10.255.225.255
                    return list_ip_range
# Occur error message
        except MemoryError:
            print('Memory error occurred in this program.')
            QMessageBox.information(self,
                                'Error',
                                'Memory error occurred in this program.',
                                QMessageBox.Ok)
            self.lineEdit_nw_addr.hasFocus()
            return
################################ Exit program ####################################
    def exit_program(self):
        QApplication.closeAllWindows()
################################ Event when the program is closed ####################################
    def closeEvent(self, event):
        if self.changeFlag == True:
            msg = "Do you want to save before close program?"
            reply = QMessageBox.question(self, 'Save',
                     msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.save_changes_to_file()
                event.accept()

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
