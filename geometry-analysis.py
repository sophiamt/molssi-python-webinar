"""
This module has functions associated with analyzing the geometry of a molecule.
"""

import numpy
import os
import argparse

def calculate_distance(coords1, coords2):
    x_distance = coords1[0]-coords2[0]
    y_distance = coords1[1]-coords2[1]
    z_distance = coords1[2]-coords2[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12

def bond_check(atom_distance,min_length=0,max_length=1.5):
    """
    Check if a distance is a bond based on a minimum and maximum length.
    Inputs: distance, min_length, max_length
    Defaults: min_length=0, max_length=1.5
    Return: True or false
    """
    if atom_distance>min_length and atom_distance<=max_length:
        return True
    else:
        return False
    
parser = argparse.ArgumentParser(description="This script analyzes a user provided xyz file and outputs all the bonds.") 
parser.add_argument("xyz_file", help="The filepath for the xyz file to analyze")
args = parser.parse_args()

if __name__ == "__main__":
    file_location=args.xyz_file
    xyz_file=numpy.genfromtxt(fname=file_location, dtype='unicode', skip_header=2)
    symbols=xyz_file[:,0]
    coordinates=xyz_file[:,1:]
    coordinates=coordinates.astype(numpy.float)
    num_atoms=len(symbols)
    for num1 in range(0,num_atoms):
        for num2 in range(0,num_atoms):
            if num1<num2:
                distance = calculate_distance(coordinates[num1],coordinates[num2])
                if bond_check(distance) is True:
                        print(F'{symbols[num1]} to {symbols[num2]}: {distance:.3f}')