import os, visa_dict, argparse

# constants
# block size for VISA clearing
visa_block_size = 168

def find_string (v_file, v_str):
    # check incoming file exists
    if not (os.path.exists(v_file)):
        print('File ' + v_file + ' does not exist!')
        exit(1)

    # find string
    src_file = open(v_file, 'rb', visa_block_size)
    curr_str = ""

    src_file.seek(v_str * visa_block_size)
    block = src_file.read(visa_block_size)
    src_file.close()
    return block.decode('cp500')

def print_tcr (str):
    print ('TC' + str[0:2] + ' : ', visa_dict.TC[str[0:2]])    # TC
    key = str[0:2]+'X'+str[3:4]
    if key in visa_dict.TCR:
        tcr = visa_dict.TCR[key]
        for i in tcr:
            st, en, ds = i
            print(ds + ':', str[st-1:st+en-1])
    else:
        print('TCR is not supported yet')
        print(str)

# Incoming parameters
parser = argparse.ArgumentParser(description='VISA BASEII clearing parser')
parser.add_argument("-f", dest='l_src', help="Source file name")
parser.add_argument("-l", type=int, dest='l_string', help="Row number in file")
args = parser.parse_args()

l_src = str(args.l_src)
l_string = int(args.l_string)

curr_str = find_string (l_src, l_string)

print ('Row from file:')
print (curr_str)
print_tcr (curr_str)