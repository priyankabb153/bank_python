import re
import os
import check_file_present
import no_of_files



class Node:
    def __init__(self, acc_no=None, name=None, age=None, address=None, phone_no=None, balance=None):
        # def __init__(self):
        self.acc_no = acc_no
        self.name = name
        self.age = age
        self.address = address
        self.phone_no = phone_no
        self.balance = balance
        self.next = None


def fetch_name():
    while True:
        name = input("Enter account holders name :")
        name = name.replace(" ", "_")
        if name.replace("_", "").isalpha():
            break
        else:
            print("Enter a valid name")

    return name


def fetch_age():
    while True:
        try:
            age = int(input("Enter the age:"))
            if age > 0:
                break
            else:
                print("Age should be greater than zero")
        except ValueError:
            print(" Enter number for age")
            continue
    return age


def fetch_address():
    while True:
        address = input("Enter the address:")
        address = address.replace(" ", "_")
        if address.replace("_", "").isalpha():
            break
        else:
            print("Enter a valid address")

    return address


def fetch_phone_no():
    while True:
        try:
            phone_no = input("Enter the phone number:")
            pattern = re.compile("(0/91)?[7-9][0-9]{9}")
            match = re.match(pattern, phone_no)
            if match and len(phone_no) == 10:
                break
            else:
                print("Invalid Phone number")
                print("Please enter a valid phone number ")
                continue
        except ValueError:
            print(" Enter number for Phone number ")
            continue
        except TypeError:
            print(" Enter number greater than zero for Phone number ")
            continue
    return phone_no
    
def no_of_lines(filename):
    file = open(filename, "r")
    counter = 0
    lines = file.read()
    count = lines.split("\n")
    for i in count:
        if i:
            counter += 1

    return counter  

class LinkedList:
    def __init__(self):
        self.head = None

    def display_all(self):
        cur = self.head

        if cur is None:
            print("There are no accounts created")
        print("ACC_NO  NAME\t   AGE  ADDRESS \t PHONE_NO \t BALANCE")
        while cur is not None:
            print(str(cur.acc_no) + "\t\t" + cur.name.replace("_"," ") + "   " + str(cur.age) + "   " + cur.address.replace("_", " ") + " \t " + str(
                cur.phone_no) + " \t " +
                  str(cur.balance))
            cur = cur.next

    def create_account(self, acc_num, nme, years, addresses, ph_no, bal):
        new_node = Node(acc_num, nme, years, addresses, ph_no, bal)

        if self.head is None:
            self.head = new_node
            print()
            print("!!!!!!!!!!!!!!!!!!!Account created successfully!!!!!!!!!!!!!!")
            print()
            print("The account number allocated is " + str(acc_num))
            print()
            print("*********************************************************")
            return

        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

        print()
        print("Account created successfully!!!!!!!!!!!!!!")
        print()
        print("The account number allocated is " + str(acc_num))
        print()
        print("*********************************************************")

    def deposit(self, acc_num, amount):
        print("*************DEPOSIT AMOUNT***************")
        first = self.head

        if self.head is None:
            print("NO ACCOUNTS EXITS!!!!!!!!!!")
            return

        if acc_num <= 0 or amount <= 0:
            print("PLEASE ENTER VALID INPUT!!!!!!!!!!")
            return


        while first is not None and (first.acc_no != acc_num):
            first = first.next

        if first is None:
            print("Account number entered does not exist!!!!!!!!!")
            return

        first.balance = first.balance + amount
        print("Amount deposit successful!!!!!!!!")
        print("Current balance is " + str(first.balance))
        print("*********************************************************")
        return

    def withdraw(self, acc_num, amount):
        print("*************DEPOSIT AMOUNT***************")
        first = self.head

        if self.head is None:
            print("NO ACCOUNTS EXITS!!!!!!!!!!")
            return

        if acc_num <= 0 or amount <= 0:
            print("PLEASE ENTER VALID INPUT!!!!!!!!!!")
            return

        while first is not None and first.acc_no != acc_num:
            first = first.next

        if first is None:
            print("Account number entered does not exist!!!!!!!!!")
            return

        if amount <= first.balance:
            first.balance = first.balance - amount
            print("Withdraw of " + str(amount) + " amount from account " + str(first.acc_no) + " successful!!!!!")
            print()
            print()
            print("Remaining balance is " + str(first.balance) + " !!!!!!!!!!!")

        else:
            print("Insufficient funds cancelling transaction!!!!!!!!!!!!")
            print("*********************************************************")

        return

    def get_account_balance(self, acc_num):
        print("*************Get account balance***************")
        cur = self.head

        if self.head is None:
            return -1

        while cur is not None and cur.acc_no != acc_num:
            cur = cur.next

        if cur is None:
            return -1

        if cur.acc_no == acc_num:
            return cur.balance

        return -1

    def read_accounts_from_file(self):

        file_size = os.path.getsize("bank_record")

        if file_size < 5:
            print("The file is empty ")
            print("Create new accounts")
        else:
            list1 = []
            file = open("bank_record", "r")
            for line in file:
                list1.clear()
                for word in line.split():
                    list1.append(word)
    #            print(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
                my_list.create_account(int(list1[0]), list1[1], int(list1[2]), list1[3], int(list1[4]), int(list1[5]))
    #            print(list1)
            print()
            file.close()

    def write_to_file(self):
        file = open("bank_record", "w")
        cur = self.head

        if cur is None:
            print("Print there is nothing to write to file")

        while cur is not None:
            file.write(str(cur.acc_no) + "\t\t" + cur.name + "\t\t" + str(
                cur.age) + "\t\t" + cur.address + "\t\t" + str(
                cur.phone_no) + "\t\t" +
                       str(cur.balance) + "\n")
            cur = cur.next


# global account_number
# account_number = 1
my_list = LinkedList()
my_list.head = None
flag = True
with open("bank_record", "+a") as fp:
    fp.close()

account_number = no_of_lines('bank_record')
if account_number != 0:
    account_number += 1
# print(account_number)
my_list.read_accounts_from_file()
while flag:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. CREATE ACCOUNT ")
    print("2. VIEW ALL ACCOUNTS ")
    print("3. DEPOSIT AMOUNT ")
    print("4. WITHDRAW AMOUNT ")
    print("5. GET ACCOUNT BALANCE ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice = int(input("Enter your Choice "))

    if choice == 1:
        if account_number == 0:
            account_number = 1
            acc_no = 1
        else:
            acc_no = account_number

        name = fetch_name()
        age = fetch_age()
        address = fetch_address()
        phone_no = fetch_phone_no()
        balance = 0
        account_number = account_number + 1
        my_list.create_account(acc_no, name, age, address, phone_no, balance)

    elif choice == 2:
        my_list.display_all()

    elif choice == 3:
        acc = int(input("Enter the account number: "))
        amt = int(input("Enter amount to deposit : "))
        my_list.deposit(acc, amt)

    elif choice == 4:
        acc = int(input("Enter the account number: "))
        amt = int(input("Enter amount to withdraw : "))
        my_list.withdraw(acc, amt)

    elif choice == 5:
        acc = int(input("Enter the account number: "))
        account_balance = my_list.get_account_balance(acc)

        if account_balance == -1:
            print("Account number doesnt exist!!!!")
        else:
            print("Account balance is " + str(account_balance) + "!!!!!!")
    else:
        print("Enter valid choice")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ch = int(input("Enter 0 to exit "))

    if ch == 0:
        flag = False
        my_list.write_to_file()

