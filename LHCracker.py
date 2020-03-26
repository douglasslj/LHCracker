#!/usr/bin/python

import crypt

print ""
print "Bem vindo ao Linux Hash Cracker"
print ""

fullHash = raw_input("Informe a hash de senha Linux completa: ")
wordlist = raw_input("Informe a Wordlist: ")
    
with open(wordlist, "rU") as infile:
    for line in infile:
        line = line.strip()
        hashGenerated = crypt.crypt(line,fullHash)
        
        if hashGenerated == fullHash:
            print ""
            print " -- Hash quebrada --"
            print ""
            print "Senha:",line
            print ""
            break
        else:
            print "Verificando:",line
        
        

