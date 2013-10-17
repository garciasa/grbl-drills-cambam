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

    depth = '2.0' # depth in mm (NOTE, not negative!)
    clearance = '1.0' # clearance in mm
    travel_speed = '500.0'
    plunge_speed = '200.0'

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
        elif opt in ('-d', '--depth'):
            depth = str(abs(arg))
        elif opt in ('-c', '--clearance'):
            clearance = arg
        elif opt in ('-t', '--travel_speed'):
            travel_speed = arg
        else:
            assert False, "unhandled option"

    
    fin = open(inputfile,'r')
    fout = open (outputfile,'w')

    lastX = ''
    lastY = ''

    for line in fin:
        modified = False
        temp = ""
        commands = string.split(line)
        print commands
        if len(commands) == 3:
            if commands[1].startswith('X'):
                lastX = commands[1]
                print 'lastX is ', lastX
            elif commands[1].startswith('Y'):
                lastY = commands[1]
                print 'lastY is ', lastY
            if commands[2].startswith('X'):
                lastX = commands[2]
                print 'lastX is ', lastX
            elif commands[2].startswith('Y'):
                lastY = commands[2]
                print 'lastY is ', lastY
        elif len(commands) > 3:
            if commands[1].startswith('X'):
                lastX = commands[1]
                print 'lastX is ', lastX
            elif commands[1].startswith('Y'):
                lastY = commands[1]
                print 'lastY is ', lastY
            if commands[2].startswith('X'):
                lastX = commands[2]
                print 'lastX is ', lastX
            elif commands[2].startswith('Y'):
                lastY = commands[2]
                print 'lastY is ', lastY

        if commands[0] == "G81":
            # Start conversion
            if justMark:
                temp = "G1 Z-0.5 F80\n"
            else:
                if len(commands) == 4:
                    temp = 'G1 ' + commands[1] + ' ' + commands[2] + ' F' + travel_speed + '\n'
                    temp += 'G1 ' + 'Z -' + depth + ' ' + 'F' + plunge_speed + '\n'
                    temp += 'G1 ' + 'Z' + clearance + ' ' + 'F' + plunge_speed + '\n'
                elif len(commands) == 3:
                    if commands[1].startswith('X'):
                        temp = 'G1 ' + commands[1] + ' ' + lastY + ' F' + travel_speed + '\n'
                        temp += 'G1 ' + 'Z -' + depth + ' ' + 'F' + plunge_speed + '\n'
                        temp += 'G1 ' + 'Z' + clearance + ' ' + 'F' + plunge_speed + '\n'
                    elif commands[1].startswith('Y'):
                        temp = 'G1 ' + lastX + ' ' + commands[1] + ' F' + travel_speed + '\n'
                        temp += 'G1 ' + 'Z -' + depth + ' ' + 'F' + plunge_speed + '\n'
                        temp += 'G1 ' + 'Z' + clearance + ' ' + 'F' + plunge_speed + '\n'
                # temp = 'G1 ' + lastX + ' ' + lastY + ' F' + travel_speed + '\n'
                # temp += 'G1 ' + 'Z -' + depth + ' ' + 'F150.0\n'
                # temp += 'G1 ' + 'Z' + clearance + ' ' + 'F150.0\n'
            modified = True

        if commands[0] == "G98":
            modified = True

        if commands[0] == "G80":
            temp = "G1 Z1.5\n"
            modified = True



        if modified:
            fout.write(temp)
        else:
            fout.write(line)

    fin.close()
    fout.close()

if __name__ == "__main__":
    main(sys.argv[1:])



