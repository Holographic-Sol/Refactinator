#Refactor by Benjamin Jack Cullen

import os
import sys
import fileinput

homeDir = '/home/'

def choice(targetFile, targetString, newString):
    print('\nTarget File: '+targetFile)
    print('Target String: '+targetString)
    print('New String: '+newString)
    choice = input('\nContinue? y/n : ')
    if choice=='y':
        for line in fileinput.input(targetFile, inplace=True):
            print (line.rstrip().replace(targetString, newString)),
        print('Done.')
        main()
    elif choice=='n':
        print('Aborted.')
        main()
    else:
        print('Invalid Option!!\n')

def main():
    print('Specify File to be refactored')
    targetFile = input('File: ')
    print('Searching...')
    for dirName, subdirList, fileList in os.walk(homeDir):
        for fname in fileList:
            fullPath = os.path.join(homeDir, dirName, fname)
            if fullPath == targetFile:
                print('Found: ',fullPath)
                print('\nString to be refactored')
                targetString = input('String: ')
                newString = input('New String: ')
                choice(targetFile, targetString, newString)
    if fullPath != targetFile:
        print('File not found!\n')
        main()
                
q=1
while q==1:
    print('\nWELCOME TO REFACTOR\n')
    print('Caution: Please be extremely careful with this tool.')
    print('For safety reasons this tool only searches for your')
    print('requested file in home directory as apose to from root.\n')
    main()
