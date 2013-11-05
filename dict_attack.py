#!/usr/bin/python
# 
-*- coding: utf-8 -*-

import sys, re, hashlib


hashes = raw_input('\nPlease specify hash value: ')

wordlist = raw_input('\nPlease specify wordlist path: ')

words = open(wordlist, "r")

words = words.readlines()
print "\n",len(words),"words"

for word in words:
    
	hashed = hashlib.md5(word[:-1])
   
	value = hashed.hexdigest()
    
	if hashes == value :
        
	print "Password is:"+word,"\n"

	sys.exit(0)

	elif:
	print "Sorry....Hash not found"\n"
  
	sys.exit(0)
sys.exit(0)
