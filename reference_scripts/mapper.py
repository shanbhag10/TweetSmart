#!/usr/bin/python

# The Mapper
import sys
import csv

# Set local variables
def mapperFunc(filename):

    print 'Starting mapper.py'

    iteration = 0

    currentCountry = None
    previousCountry = None
    currentFx = None
    previousFx = None
    percentChange = None
    currentKey = None

    fxMap = []
    first = True
    file_object = open(filename)
    infile = file_object.readlines()

     # skip first line of input file

    for line in infile:

        if first:
            first = False
            continue

        line = line.strip()
        line = line.split(',', 2)

        try:
            # Get data from line
            currentCountry = line[1].rstrip()
            if len(line[2]) == 0:
                continue
            currentFx = float(line[2])

            if currentCountry != previousCountry:
                previousCountry = currentCountry
                previousFx = currentFx
                previousLine = line
                continue

            # If country same as previous, add to map
            elif currentCountry == previousCountry:
                percentChange = ((currentFx - previousFx) / previousFx) * 100.00
                percentChange = percentChange
                # Set the array with tuple keys
            
                fxMap.append((currentCountry,round(percentChange, 4),1))

            # Update Values
            previousCountry = currentCountry
            previousFx = currentFx
            previousLine = line

            #Uncomment if you want to see the output
            if iteration % 50000 == 0:
                print "Current iteration is %d" % iteration
            iteration += 1

        # Handle unexpected errors
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print "currentFx: %.2f previousFx: %.2f" % (currentFx, previousFx)
            print message
            sys.exit(0)

    # Show the returned values
    print fxMap
    return sorted(fxMap)


def reducerFunc(fxMap):
    current_key = None
    current_count = 0
    key = None

    # Import the mapped FX data data
    for line in fxMap:
        key = (line[0],line[1])
        count = float(line[2])

        try:
            count = int(count)
        except ValueError:
            continue

        if current_key == key:
            current_count += count
        else:
            if current_key:
                print '%s\t%s' % (current_key, current_count)
            current_count = count
            current_key = key

    # do not forget to output the last word if needed!
    if current_key == key:
        print '%s\t%s' % (current_key, current_count)

        

if __name__ == "__main__":
    reducerFunc(mapperFunc(sys.argv[1]))

