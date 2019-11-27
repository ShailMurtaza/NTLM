#python 3
import hashlib,binascii
import os
def title():
    print("                          [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]")
    print("")
    print("                          {                    NT or NTLM hash generator     }")
    print("                          [  Created by Shail                                ]")
    print("")
    print("                          ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
title()    
def gameloop():
        print("")
        print("-----------------------")
        print("")
        s = raw_input("Enter input  ") 
        print (s)

        hash = hashlib.new('md4', s.encode('utf-16le')).digest()
        print ("NT hash::")
        print binascii.hexlify(hash)
        #os.system("pause")
        gameloop()
gameloop()
