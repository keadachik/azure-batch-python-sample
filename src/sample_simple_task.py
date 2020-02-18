import sys



def bin_cat(args,output):
    out = open(output, 'ab')

    for file in args:
        print(file)
        frac = open(file, 'rb')
        out.write(frac.read())
        frac.close()
    
    out.close()


if __name__=='__main__':

    output = 'output.txt'

    bin_cat(sys.argv[1:3],output)

    print(sys.version)