# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:09:58 2020

@author: joanq
"""
''


import random
from string import punctuation
from string import digits
import re
import numpy as np
import matplotlib.pyplot as plt

n0 = 0
n1 = 0
n2 = 0


#Here is a code block to ask user choose different options.

#I did not want to just overwrite my oringinal codes.So I choose to create some
#new options.

#This part is used to ask users whether they choose auto-decrypt option
#or extra auto-decrypt option
#Also.Users can just encrypt and decrypt line by line.Or just do normally.


# part4.1. ask uses whether they choose auto-decrypt option.
while n0 <=0 : 
    Q0 = input("Do you want to choose auto-decrypt option?\n")
    Q0 == Q0.lower()
    if Q0 == "yes":
#Extra!!# about part5.3. Ask uses whether to choose improved auto-decrypt option.
        Q4 = input("Do you want to choose Extra auto-decrypt option?\n")
        Q4 = Q4.lower()
        if Q4 =="yes":
            print("Done")
            cioher_mode = "Extra-auto-decrypt"
            n0+=1
            n1+=1
        elif Q4 == "no":
            print("Done.Just use the simpler one.")
            cioher_mode = "auto_decrypt"
            n0 += 1
            n1 += 1
        else:
            print("You input wrong.Just use the simpler one.")
            n0 += 1
            n1 += 1
#part1.1 Ask users to choose a cipher mode.
    elif Q0 == "no":
        cioher_mode = input("Encrypt or decrypt the message? \n\
input [encrypt] or [decrypt] please. \n")
        cioher_mode == cioher_mode.lower()
        if cioher_mode == "encrypt":
#Extra!!# About part5.2. Ask users whether to encrypt message line by line.
            Q2 = input("Do you want to encrypt lines from message with random rotation value individually? \n\
please enter[yes] or [no]. \n")
            Q2 = Q2.lower()
            if Q2 == "yes":
                print("Done.")
                cioher_mode = "extra_encrypt"
                n0 += 1
                n1 += 1
            elif Q2 =="no":
                print("Done.")
                cioher_mode = "encrypt"
                n0 += 1
            else:
                print("You input wrong.Just encrypt normally.")
                cioher_mode = "encrypt"
                n0 += 1
#Extra!!# About part5.2. Ask users whether to decrypt message line by line.
        elif cioher_mode == "decrypt":
            Q3 = input("do you want to decrypt message line by line? \n\
please enter[yes] or [no] \n")
            Q3 = Q3.lower()
            if Q3 == "yes":
                print("Done.")
                cioher_mode = "extra_decrypt"
                n0 += 1
                n1 += 1
            elif Q2 =="no":
                print("Done.")
                cioher_mode = "decrypt"
                n0 += 1
            else:
                print("You input wrong.Just decrypt normally.")
                cioher_mode = "decrypt"
                n0 += 1
        else:
            print("please try again.")
#part1.2. If users do not provide any useful inputs.Program would ask users to enter again.
    else:
        print("Please input again.")
        
        
#Here, it's a code block to ask users whether they want to choose random 
#rotation value.        
            
while n1 <=0 :
    Q1 = input("Do you want to choose a random number?")
    Q1 == Q1.lower()
    if Q1 == "yes":
        rotation_value = random.randint(-26,26)
        n1 += 1
    elif Q1 =="no":
        rotation_value = int(input("Choose a number which repreats the places should shift each character."))
         
        print("Done.")
        n1 += 1
#part1.2. If users do not provide any useful inputs.Program would ask users to enter again.
         
 
            
#About part3.Here, its a codes block to ask users entry mode.
#User can just use manual entry mode.Or read from file by providing the file path.
            
while n2 <=0 :
    entry_mode = input("Please select a message entry mode. [manual entry] or [read from file].\n")
    entry_mode == entry_mode.lower()
    n3 = 0
    while entry_mode == "manual entry":
            message = input("Input the text to be encrypted or decrypted.")
            if len(message) > 0:
                print("Done.")
                n2 += 1
                break
            else:
                print("Please input again.")
    while entry_mode == "read from file":
            file_path = input("Please input a file name(including a file path).")
            try:
                with open(str(file_path),"r+") as file:
                    message = file.readlines()
                    n2+=1
                    break
            except IOError:
                print("ERROR.Please input again.")
 

#1. Here, it's a class codes block about [encrypt] and [decrypt] function.
#2. [encrypt] can encrypt message with the constant rotation value which provided
#   by users.
#3. [decrypt] can decrypt message with the constant rotation value which provided
#   by users.
#!EXTRA#
#4. [extra_encrypt] can encrypt each line in the message with random rotations
#   value.
#!EXTRA#
#5. [extra_decrypt] can decrypt each line in the message with different rotation
#   value

                


            
class Caesar_cipher():
    def __init__(self,rotation_value,message):
        self.rotation_value = rotation_value
        self.message = message
        self.resualt0 = ""
        self.resualt1 = ""
        self.resualt3 = []
        self.split_message = self.message.splitlines()

#part1.3#When the cipher mode chosen is encrypt then your program should encrypt the message
# given by the user using the rotation given by the user.


    def encrypt(self):
            encrypted_message = []
            for i in self.message:
                i = list(i)
                newi = []
                for character in i:
                    if "a" <= character <= "z":
                        newi.append((chr((ord(character) - ord("a") + self.rotation_value) % 26 + ord("a"))))
                    elif "A" <= character <= "Z":
                        newi.append((chr((ord(character) - ord("A") + self.rotation_value) % 26 + ord("A"))))
                    else:
                        newi.append(character)
                encrypted_message.append("".join(newi))
            self.resualt0 = ("".join(encrypted_message)) 
            return(self.resualt0.upper())
        
#!EXTRA# Part5.2 it can encrypt message line by line.

    def extra_encrypt(self):
        encrypted_message = []
        for line in self.split_message:
            rotation_value = random.randint(-26, 26)
            newline = []
            for i in line:
                i = list(i)
                newi = []
                for character in i:
                    if "a" <= character <= "z":
                        newi.append((chr((ord(character) - ord("a") + rotation_value) % 26 + ord("a"))))
                    elif "A" <= character <= "Z":
                        newi.append((chr((ord(character) - ord("A") + rotation_value) % 26 + ord("A"))))
                    else:
                        newi.append(character)
                newline.append("".join(newi))
            encrypted_message.append(newline)
        self.resualt3.append(["".join(i) for i in encrypted_message])
        self.resualt3 = ("\n".join(self.resualt3[0]))
        return(self.resualt3.upper())
        
#Part1.4#When the cipher mode chosen is decrypt your program should decrypt the message given
# by the user using the rotation given by the user.

    def decrypt(self):
            decrypt_message = []
            for i in message:
                i = list(i)
                newi = []
                for character in i:
                    if "a" <=character <= "z":
                        newi.append((chr((ord(character) - ord("a") - self.rotation_value) % 26 + ord("a"))))
                    elif "A" <=character <= "Z":
                        newi.append((chr((ord(character) - ord("A") - self.rotation_value) % 26 + ord("A"))))
                    else:
                        newi.append(character)
                decrypt_message.append("".join(newi))
            self.resualt1 = ("".join(decrypt_message))
            return(self.resualt1.upper())  ###大写
        
#!EXTRA# Part5.2 it can decrypt message line by line.

    def extra_decrypt(self):
        decrypted_message = []
        for line in self.split_message:
            rotation_value = int(input("please enter a rotation value"))
            newline = []
            for i in line:
                i = list(i)
                newi = []
                for character in i:
                    if "a" <= character <= "z":
                        newi.append((chr((ord(character) - ord("a") - rotation_value) % 26 + ord("a"))))
                    elif "A" <= character <= "Z":
                        newi.append((chr((ord(character) - ord("A") - rotation_value) % 26 + ord("A"))))
                    else:
                        newi.append(character)
                newline.append("".join(newi))
            decrypted_message.append(newline)
        self.resualt3.append(["".join(i) for i in decrypted_message])
        self.resualt3 = ("\n".join(self.resualt3[0]))
        return(self.resualt3.upper())
# 1. Here, it is a code block about part2.
#2. it included 6 define part.
#3. couting part can return the 10 most common words.
#   And print_counting can print it with a format.
#4. Unique_words can print the amount of words which only appear onece.
#5. The total_number can print the total number of words from message.
#6. min_max_word_length could print the length of the maximum word length and 
#   the minimum word length from this message.

class analysing_message():
    
    def __init__(self,message):
        self.message = message
        self.counting() ####
        
#part2.1 select only the ten most common words to sort.

    def counting(self):
        global most_common_words
        text = re.sub(r'[{}]+'.format(punctuation+digits),"", message.lower())
        global text_split
        text_split = text.split()
        global Mcount
        Mcount = {}
        for i in text_split:
            if i not in Mcount:
                Mcount[i] = 1
            else:
                Mcount[i] += 1
        most_common_words = sorted(Mcount.items(), key=lambda item: item[1], reverse=True)
        most_common_words = np.array(most_common_words)
        global resault2
        resault2 = (most_common_words[0:10,:])
        return(resault2)
#part2.2 as a format.Example: the : 4

    def print_counting(self):
        for i in resault2:
            print(i[0]," : ",i[1])
#part2.3 print the number of unique words.
        
    def unique_words(self):
        global unique_number
        unique_number = 0
        for k,v in Mcount.items():
            if v == 1:
                unique_number += 1
            else:
                unique_number += 0
        print("the number of unique words: ",unique_number)
        
#part2.3 print the number of the total words.

    def total_number(self):
        global the_total_number
        the_total_number = len(Mcount.keys())
        print("the total number of words: ",the_total_number)
        
#part2.1 print the maximum and minimun word length.
    
    def min_max_word_length(self):
        word_length_list = []
        for i in text_split:
            word_length_list.append(len(i))
        max_word_length = max(word_length_list)
        min_word_length = min(word_length_list)
        print("the minimun word length: ",min_word_length,"/n",
              "the maximum word length: ",max_word_length)
        
# About part 4.Here is a code block about auto_decrypt in part4, which needed user to choose 
# [yes] or [no] some times.

def auto_decrypt():
#part4.2. it reads the words list from the words.txt.

    with open("words.txt","r+") as file:
        count = 0
        words = file.readlines()
        words = [line.strip() for line in words]
        B = None
#part4.3. Iterate all possible rotations.

        for i in range(0,26):
            rotation_value = i
            A = Caesar_cipher(rotation_value, message)
            test_line0 = A.decrypt()
            test_line0 = test_line0.lower()
            test_line0 = test_line0.splitlines()
            test_line0 = test_line0[0]
            test_line1 = test_line0.split()
            for w in test_line1:
                for word in words:
                    if w == word:
                        count += 1
            while count >=1:
                print(test_line0)
                answer = input("Does the first line has been decrypted successully?")
                answer == answer.lower()
                if answer == "yes":
                    print("The rotation value is ",str(i))
                    B = Caesar_cipher(rotation_value, message)
                    print("The decrypted message:\n",B.decrypt())
                    break
                elif answer == "no":
                    print("Countinue to decrypt.")
                    count = 0
            if B is not None:
                break
                
        if B is None:
            print("The automated decryption system is hard to tackle users' demand.Sorry about that.")
                    
            
#!EXTRA# Here, its a extra_auto_decrypt part which used as def().
# 1. it can automatically decrypt message by comparing matched times with the words.txt
#    And the resault with the greatest amount of matched times is the best solution.
# 2.  Wcount means the count of words.
# 3.  It tackles demand from part5.

def extra_auto_decrypt():
    with open("words.txt","r+") as file:
        Wcount = 0
        words = file.readlines()
        words = [line.strip() for line in words]
        B = None
        solutions = {}
        for i in range(0,26):
            Wcount = 0
            rotation_value = i
            A = Caesar_cipher(rotation_value, message)
            test_line0 = A.decrypt()
            test_line0 = test_line0.lower()
            test_line1 = test_line0.split()
            
            for w in test_line1:
                for word in words:
                    if w == word:
                        Wcount += 1
   
            while Wcount >=1:
                B = Caesar_cipher(rotation_value, message)
                text = str(B.decrypt()+"\n")
                solutions[text] = Wcount
                break
                
        solutions = sorted(solutions.items(), key=lambda item: item[1], reverse=True)
        solutions = np.array(solutions)
        resault_list = solutions[:,0]
        count_list = solutions[:,1]
        resault_list = resault_list.tolist()
        count_list = count_list.tolist()
        count_list = list(map(int,count_list))
        maxcount = max(count_list)
        maxlist = []
        for i in count_list:
            x = 0
            if i == maxcount:
                maxlist.append(resault_list[count_list.index(i)])
                x += 1
        while len(maxlist) == 1:
            print("The decrypted solution is:\n" + maxlist[0])
            break
        while len(maxlist) > 1:
            C = None
            for i in maxlist:
                print(i)
                n4 = 0
                while n4 <= 0:
                    answer = input("Is this correct?Input [yes] or [no].\n")
                    if answer == "yes":
                        C = i 
                        print("Done.Thanks for your answers.")
                        break
                    elif answer == "no":
                        print("OK.lets' try forward.")
                        n4 += 1
                    else:
                        print("Please input your answer again.")
            if C is None:
                print("It cant decrypt this message.Sorry about that.")
                break
            break
               
        if B is None:
            print("The automated decryption system is hard to tackle users' demand.Sorry about that.")

#!EXTRA# Here , a bar chart generated by imported matplotlib.pyplot.
#Also, it can output a My-plot.pdf to show the appeared times of the 10 most
#common words.

def bar_chart():
    V = analysing_message(message)
    y = []
    x = []
    for i in V.counting():
        x.append(i[0])
        y.append(int(i[1]))
    plt.bar(x,y)
    plt.xlabel("$Words$", fontsize = 14)
    plt.ylabel("$Statistics$", fontsize = 14)
    plt.title("Simple Plot of $10$ Most Common Words", fontsize = 16)
    plt.savefig("My-Plot.pdf")
    plt.show()

#Here, a code block used as implement part.


if cioher_mode == "encrypt":
    A = Caesar_cipher(rotation_value, message)
    print(A.encrypt())
elif cioher_mode == "decrypt":
    A = Caesar_cipher(rotation_value, message)
    print(A.decrypt())
elif cioher_mode == "auto_decrypt":
    auto_decrypt()
elif cioher_mode =="Extra-auto-decrypt":
    extra_auto_decrypt()
elif cioher_mode == "extra_encrypt":
    rotation_value = 0
    A = Caesar_cipher(rotation_value, message)
    print(A.extra_encrypt())
elif cioher_mode == "extra_decrypt":
    rotation_value = 0
    A = Caesar_cipher(rotation_value, message)
    print(A.extra_decrypt())
