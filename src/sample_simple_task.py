import sys

output = "output.txt"

def bin_cat(args):
    out = open(output, 'ab')

    for file in args:
        frac = open(file, 'rb')
        out.write(frac.read())
        frac.close()
    
    out.close()


if __name__=='__main__':

    bin_cat(sys.argv[1:])