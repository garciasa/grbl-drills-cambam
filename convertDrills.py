#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import getopt
import string


def  main(argv):

    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv,"hi:o:m",["ifile=","ofile=","justMark"])
    except getopt.GetoptError:
        print 'convertDrills.py -i <inputfile> -o <outputfile> [-m]'
        print '<inputfile> File with cambam gcodes'
        print '<outputfile> Outfile with drills converted'
        print '-m Just mark the hole'
        sys.exit(2)

    justMark = False
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile> [-m]'
            print '<inputfile> File with cambam gcodes'
            print '<outputfile> Outfile with drills converted'
            print '-m Just mark the hole'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-m", "--justMark"):
            justMark = True
        else:
            assert False, "unhandled option"

    
    fin = open(inputfile,'r')
    fout = open (outputfile,'w')

    for line in fin:
        modified = False
        temp = ""
        commands = string.split(line)
        if commands[0] == "G81":
            # Start conversion
            if justMark:
                temp = "G1 Z-0.5 F80\n"
            else:
                temp = "G1 " + commands[3] + " F80\n" 
            modified = True

        if commands[0] == "G98":
            modified = True

        if commands[0] == "G80":
            temp = "G1 Z3.0\n"
            modified = True

        if modified:
            fout.write(temp)
        else:
            fout.write(line)

    fin.close()
    fout.close()

if __name__ == "__main__":
    main(sys.argv[1:])



