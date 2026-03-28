""" Main class for character creation """

import argparse
from koikatsu_child_generator.chara import Child

DEBUG = False

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="cmd")
parser_create = subparsers.add_parser("create",
                                      help="create a new child-character from two parents")
parser_create.add_argument("mother",
                           help="path to female parent character")
parser_create.add_argument("father",
                           help="path to male parent character")
parser_create.add_argument("-g",
                           "--gender",
                           choices=["female", "male"],
                           help="specify gender of character to be created")
parser_create.add_argument("-fn",
                           "--filename",
                           default="new_child",
                           help="output filename (don't add file extension)")
parser_create.add_argument("-v",
                           "--verbose",
                           action="store_true",
                           help="show information about some attributes of the new character")
args = parser.parse_args()

if args.cmd == "create":
    if args.verbose:
        DEBUG = True

    child = Child(mother=args.mother, father=args.father, output_name=args.filename, debug=DEBUG)

    if args.gender:
        if args.gender in ("female"):
            child.create()
        elif args.gender in ("male"):
            child.create(False)
    else:
        child.create_random()
