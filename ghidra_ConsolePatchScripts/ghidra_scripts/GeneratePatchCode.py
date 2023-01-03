#Generate codes for console patches.
#Supported platform and formats: PS3 (RPCS3 Game Patches), PS4 (py-patch), Xbox 360 (Xenia Game Patches), PSP (PPSSPP and CWCheat), PS Vita
#Note that PS4 must have the address base set to 0x400000, to match disabled ASLR address.
#Usage:
#Check the tickbox for the script
#Highlight your code
#Press the keybind

#@author illusion0001
#@category Conversion
#@keybinding Alt-Shift-Q
#@menupath
#@toolbar

from binascii import hexlify

def swapbytes(int_tuple):
    swapped = int_tuple[::-1]
    return swapped

def getdata(codeUnit):
    address        = str(codeUnit.getAddress())
    value          = (codeUnit.getBytes())
    oprand_comment = (codeUnit.toString())
    return address, value, oprand_comment

# https://blog.finxter.com/how-to-find-the-longest-string-in-a-python-list
def get_max_str(lst):
    return max(lst, key=len)

def gen_patch():
        # https://github.com/lwerdna/ghidra/blob/master/XorMemoryScript.py
        if currentSelection is None or currentSelection.isEmpty():
            print("Use your mouse to highlight data to generation patch. then press Alt-Shift-Q to generate code.")
            return # exit
                   # else
        # https://github.com/HackOvert/GhidraSnippets#print-all-instructions-in-a-select-function
        processor = str(currentProgram.getLanguageID())
        listing   = currentProgram.getListing()
        addrSet   = currentSelection
        minAddr   = str(currentProgram.getMinAddress())
        codeUnits = listing.getCodeUnits(addrSet, True)
        comments = False
        if processor == 'Allegrex:LE:32:default': # PSP
            # print('Platform is PSP ({0}).'.format(processor))
            for codeUnit in codeUnits:
                addr, val, oprand = getdata(codeUnit)
                value = hexlify(swapbytes(val))
                if(comments == False):
                  print('_L 0x{0} 0x{1}'.format(addr.upper(), value.upper())) # CW uses uppercase
                else:
                  print('_L 0x{0} 0x{1} // {2}'.format(addr.upper(), value.upper(), oprand)) # CW uses uppercase
        elif processor == 'ARM:LE:32:v7': # PSP2
            # print('Platform is PS Vita ({0}).'.format(processor))
            for codeUnit in codeUnits:
                addr, val, oprand = getdata(codeUnit)
                bytes = len(val)
                if (bytes == 2):
                  type = 'bytes16'
                elif (bytes == 4):
                  type = 'bytes32'
                if(comments == False):
                  print('- [ {2}, 0x{0}, 0x{1} ]'.format(addr, hexlify(swapbytes(val)), type))
                else:
                  print('- [ {2}, 0x{0}, 0x{1} ] # {3}'.format(addr, hexlify(swapbytes(val)), type, oprand))
        elif processor == 'PowerPC:BE:64:64-32addr' or processor == 'PowerPC:BE:64:A2-32addr': # PS3
            # print('Platform is PS3 ({0}).'.format(processor))
            for codeUnit in codeUnits:
                getdata(codeUnit)
                addr, val, oprand = getdata(codeUnit)
                if(comments == False):
                  print('- [ be32, 0x{0}, 0x{1} ]'.format(addr, hexlify(val)))
                else:
                  print('- [ be32, 0x{0}, 0x{1} ] # {2}'.format(addr, hexlify(val), oprand))
        elif processor == 'PowerPC:BE:64:VLE-32addr': # X360
            # print('Platform is Xbox 360 ({0}).'.format(processor))
            for codeUnit in codeUnits:
                getdata(codeUnit)
                addr, val, oprand = getdata(codeUnit)
                if(comments == False):
                  print('    [[patch.be32]]\n'
                        '        address = 0x{0}\n'
                        '        value = 0x{1}'.format(addr, hexlify(val)))
                else:
                  print('    [[patch.be32]]\n'
                        '        address = 0x{0}\n'
                        '        value = 0x{1} # {2}'.format(addr, hexlify(val)))
        elif processor == 'x86:LE:64:default':
            if minAddr == '00400000':
                patch_list  = []
                oprand_list = []
                for codeUnit in codeUnits:
                    getdata(codeUnit)
                    addr, val, oprand = getdata(codeUnit)
                    patch = '{ \"type\": \"bytes\", \"addr\": \"0x%s\", "value": \"%s\" },' % (addr, hexlify(val)) # thanks aero+kiwi
                    #patch = '- [ bytes, 0x{0}, \"{1}\" ]'.format(addr, hexlify(val)) # thanks aero+kiwi
                    patch_list.append(patch)
                    oprand_list.append(oprand)
                length = (get_max_str(patch_list))
                real_length = (len(length))
                for patch, oprand in zip(patch_list, oprand_list):
                    if(comments == False):
                      print('{0}'.format(patch, oprand))
                    else:
                      new_string = ('{0:<{1}}'.format(patch, real_length))
                      new_string += ('{ \"comment\": \"%s\" },' % (oprand))
                      print(new_string)
            else:
                print('Image Base {} is not correct, patch address will be wrong! Make sure it is set to 0x400000.\nExiting script.'.format(minAddr))
                return
        else:
            print('Processor: {} is not supported!\nExiting script.'.format(processor))
            return

gen_patch()
