import argparse     # argparse is a standard python module used for parsing command line argumetns.

"""
NOTE
    use '-' for single letter arguments (-a, -b, -c, ...)
    use '--' for word arguments (--help, --number, ...)
"""
# Initializing a parser object
parser = argparse.ArgumentParser(description="Make an animal sound") 

# adding argument to the parser object
parser.add_argument("--sound", help="sound to make", default="Meow", type=str)
parser.add_argument("-n", help="number of times to make sound", default=1, type=int)


args = parser.parse_args()      # parser parses all arguments mentioned using the add_argument function, returning a argparse.namespace object

# main code logic
for _ in range(args.n):
    print(args.sound) 