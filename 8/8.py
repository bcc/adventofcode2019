#!/usr/bin/env python3

import sys, os

if len(sys.argv) < 3:
    print(sys.argv[0], "width", "height")
    exit()

width = int(sys.argv[1])
height = int(sys.argv[2])

for line in sys.stdin:
    pixels = line.rstrip()

    layer = 0
    x = 0
    y = 0
    layers = []
    counts = []

    row = []
    layer = []

    zeroes = 0
    ones = 0
    twos = 0

    # build layers.
    for i in range(0, len(pixels)):
        pixel = int(pixels[i])

        if pixel == 0:
            zeroes += 1
        elif pixel == 1:
            ones += 1
        elif pixel == 2:
            twos += 1

        row.append(pixel)
        x += 1

        # Assemble layer
        if x == width:
            x = 0
            y += 1
            layer.append(row)
            row = []
            
        # Add layer, stats and reset counts
        if y == height:
            y = 0
            layers.append(layer)
            counts.append((zeroes, ones, twos))
            layer = []
            zeroes = 0
            ones = 0
            twos = 0

    # return part 1 answer
    fewest = None
    wanted = 0
    for layer in counts:
        if fewest is None or layer[0] < fewest:
            wanted = layer[1] * layer[2]
            fewest = layer[0]   
    print(wanted)

    # render part 2 answer
    for y in range(0,height):
        row = ""
        for x in range(0, width):
            p = 2
            for l in range(0, len(layers)): 
                if p == 2:
                    p = layers[l][y][x]
            if p == 0:
                row = row + " " 
            else:
                row = row + "*"
        print(row)
            
                