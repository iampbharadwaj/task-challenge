#!/usr/bin/python3
"""
This script is used to calculate the volume, surfa
ce area, sum of the edges of the cuboid.
Script takes side length as the command line argum
ents
"""
import argparse
import sys
import logging
import os
from typing import List, Union


logging.basicConfig(filename="cuboidcalci.log", 
                    format='%(asctime)s %(message)s',
                    level=logging.DEBUG,
                    filemode='w') 

logger = logging.getLogger()

FloatInt = Union[float, int]


def find_surface_area(side_length, side_height, side_width):
    return 2 * ((side_length * side_height) + (side_height * side_width) + (side_width * side_length))


def find_volume(side_length, side_height, side_width):
    return side_length * side_height * side_width


def find_sum_of_edges(side_length, side_height, side_width):
    return 4 * (side_length + side_height + side_width)


def cuboid_app(edge_list):
    output = {}
    try:
        for edge in edge_list:
            if edge <= 0:
                raise ValueError(
                    'Zero or Negative Arguments provided, please provide all 3 positive parameters')
        edge_list = [float(idx) for idx in edge_list]
        length, height, width = edge_list
        surface_area = find_surface_area(length, height, width)
        volume = find_volume(length, height, width)
        sum_of_edges = find_sum_of_edges(length, height, width)
        output['surface_area'] = surface_area
        output['volume'] = volume
        output['sum_of_edges'] = sum_of_edges
        output['error'] = None
    except (argparse.ArgumentError, argparse.ArgumentTypeError, ValueError) as e:
        output['error'] = e
    finally:
        if output['error'] is None:
            print('Surface_area = ', output['surface_area'])
            print('Volume = ', output['volume'])
            print('Sum_of_edges = ', output['sum_of_edges'])
        else:
            print('Error = ', output['error'])
        return output


def parse_args(argv: List[FloatInt]) -> List[FloatInt]:
    parser = argparse.ArgumentParser()
    parser.add_argument('values', nargs=3, type=float, help='Need values')
    args = parser.parse_args(argv[1:])
    values_list = args.values
    return values_list


def run(args: List[FloatInt]) -> None:
    try:
        logger.info(cuboid_app(args))
    except (IOError, SyntaxError) as er:
        logger.error(er)


def main(argv: List[Union[float, int]]) -> None:
    values = parse_args(argv)
    logger.info('Performing calculation with Cuboid Edges:')
    run(values)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
