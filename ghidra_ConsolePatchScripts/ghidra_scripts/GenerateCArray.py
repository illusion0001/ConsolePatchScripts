#Generate C Array from selected instructions
#Usage:
#Check the tickbox for the script
#Highlight your code
#Press the keybind

#@author illusion0001
#@category Conversion
#@keybinding Alt-Shift-R
#@menupath
#@toolbar

from ghidra.program.model.block import BasicBlockModel
from ghidra.program.model.listing import CodeUnit
from ghidra.program.model.symbol import SymbolTable
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.util import PseudoDisassembler
from ghidra.app.decompiler import DecompInterface
from ghidra.program.flatapi import FlatProgramAPI

api = FlatProgramAPI(currentProgram)
listing = currentProgram.getListing()
pseudoDisassembler = PseudoDisassembler(currentProgram)
monitor = ConsoleTaskMonitor()

def get_instruction_bytes(instruction):
    return [b & 0xFF for b in instruction.getBytes()]

def generate_c_array(addr_set):
    instructions = listing.getInstructions(addr_set, True)
    c_array = []
    
    start_addr = addr_set.getMinAddress()
    
    for instruction in instructions:
        instr_bytes = get_instruction_bytes(instruction)
        instr_comment = instruction.toString()
        instr_address = instruction.getAddress()
        relative_offset = instr_address.subtract(start_addr)
        c_array.append((instr_bytes, instr_comment, instr_address, relative_offset))
        
    return c_array

def format_c_array(c_array, offset):
    max_bytes_length = max(len(", ".join("0x{:02x}".format(byte) for byte in instr_bytes)) for instr_bytes, _, _, _ in c_array)
    
    formatted = "unsigned char bytes_0x{:x}[] = \n".format(offset) + "{\n"
    for instr_bytes, instr_comment, instr_address, relative_offset in c_array:
        bytes_str = "    " + ", ".join("0x{:02x}".format(byte) for byte in instr_bytes) + ","
        comment_str = " // 0x{:x}({:+x}): {}".format(instr_address.getOffset(), relative_offset, instr_comment)
        formatted += bytes_str.ljust(max_bytes_length + len("    {},")) + comment_str + "\n"
    formatted += "};"
    return formatted

def main():
    addr_set = currentSelection
    if addr_set is None or addr_set.isEmpty():
        print("Please highlight a section of code to generate the C array.")
        return
    
    c_array = generate_c_array(addr_set)
    offset = addr_set.getMinAddress().getOffset()  # Get the starting offset of the selection
    formatted_array = format_c_array(c_array, offset)
    
    print(formatted_array)

if __name__ == "__main__":
    main()
