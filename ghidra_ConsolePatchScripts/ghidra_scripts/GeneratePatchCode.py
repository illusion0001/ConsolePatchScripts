#Generate codes for console patches.
#Supported platform and formats: PS3 (RPCS3 Game Patches), PS4 (py-patch), Xbox 360 (Xenia Game Patches)
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

        if processor.startswith('PowerPC:BE:64:64-32addr') or ('PowerPC:BE:64:A2-32addr'): # PS3
            print('Platform is PS3.')
            for codeUnit in codeUnits:
                print('- [ be32, 0x{0}, 0x{1} ] # {2}'.format(codeUnit.getAddress(), hexlify(codeUnit.getBytes()), codeUnit.toString()))
        elif processor.startswith('PowerPC:BE:64:VLE-32addr'): # X360
            print('Platform is Xbox 360.')
            for codeUnit in codeUnits:
                print('    [[patch.be32]]\n'
                      '        address = 0x{0}\n'
                      '        value = 0x{1} # {2}'.format(codeUnit.getAddress(), hexlify(codeUnit.getBytes()), codeUnit.toString()))
        elif processor.startswith('x86:LE:64:default'):
            if minAddr.startswith('00400000'):
                # use 0x400000 (disabled aslr) addr for now
                # who knows what the correct one will be
                print('Image Base {} is correct.'.format(minAddr))
                print('Platform is PS4.')
                for codeUnit in codeUnits:
                    print('- [ bytes, 0x{0}, \"{1:<20}\" ] # {2}'.format(codeUnit.getAddress(), hexlify(codeUnit.getBytes()), codeUnit.toString()))
                    # align to left with spaces if less than 20 chars
            else:
                print('Image Base {} is not correct, patch address will be wrong! Make sure it is set to 0x400000.\nExiting script.'.format(minAddr))
                return
        else:
            print('Processor: {} is not supported!\nExiting script.'.format(processor))
            return

gen_patch()
