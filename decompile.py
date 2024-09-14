import uncompyle6
import sys

# def decompile_pyc(pyc_file, output_file=None):
#     try:
#         # Open the .pyc file
#         with open(pyc_file, 'rb') as f:
#             # Decompile the .pyc file and print or save the output
#             if output_file:
#                 with open(output_file, 'w') as out:
#                     uncompyle6.decompile_file(pyc_file, out)
#                 print(f"Decompiled source code saved to {output_file}")
#                 print("1")
#             else:
#                 uncompyle6.decompile_file(pyc_file, sys.stdout)
#                 print("2")
#     except Exception as e:
#         print(f"Error: {e}")
#         print("3")

# if __name__ == "__main__":
#     # Replace 'example.pyc' with your .pyc file path
#     pyc_file = '__pycache__\example_script.cpython-38.pyc'
#     # Optionally, specify an output file to save the decompiled source code
#     output_file = 'output.py'
    
#     # Decompile and output the code
#     decompile_pyc(pyc_file, output_file)







# import dis
# import marshal
# import types

# def disassemble_pyc(pyc_file):
#     with open(pyc_file, 'rb') as f:
#         code = f.read(16)  # Skip the header (16 bytes for Python 3.7 and later)
#         code_obj = marshal.load(f)
#         print("hii")
#         code = (dis.dis(code_obj))
#         return code

# # if __name__ == "__main__":
# #     # Replace 'your_script.pyc' with the path to your .pyc file
# pyc_file = 'example_script.cpython-312.pyc'
# print(disassemble_pyc(pyc_file))








# import dis
# import marshal

# def disassemble_pyc(pyc_file):
#     output = []
#     with open(pyc_file, 'rb') as f:
#         f.read(16)  # Skip the header (16 bytes for Python 3.7 and later)
#         code_obj = marshal.load(f)
#         disassembled_code = dis.Bytecode(code_obj)
        
#         for instr in disassembled_code:
#             output.append(f"{instr.opname} {instr.argrepr}")
    
#     return "\n".join(output)








# import dis
# import marshal

# def disassemble_pyc(pyc_file):
#     output = []
#     with open(pyc_file, 'rb') as f:
#         f.read(16)  # Skip the header (16 bytes for Python 3.7 and later)
#         code_obj = marshal.load(f)
#         disassembled_code = dis.Bytecode(code_obj)
        
#         for instr in disassembled_code:
#             output.append(f"{instr.offset}\t{instr.opname}\t{instr.argrepr}")
    
#     return "\n".join(output)







# import dis
# import marshal

# def simplify_instruction(instr):
#     """
#     Simplifies the bytecode instruction to resemble Python code.
#     """
#     if instr.opname in ['LOAD_CONST', 'LOAD_FAST', 'STORE_FAST', 'RETURN_VALUE']:
#         return None  # Ignore basic operations for clarity

#     if instr.opname == 'CALL_FUNCTION':
#         return f"# Call a function with {instr.arg} arguments"
    
#     if instr.opname == 'BINARY_ADD':
#         return "# Perform addition"
    
#     # You can add more simplifications based on the operation names
    
#     return f"{instr.opname} {instr.argrepr}"

# def disassemble_pyc(pyc_file):
#     output = []
#     with open(pyc_file, 'rb') as f:
#         f.read(16)  # Skip the header (16 bytes for Python 3.7 and later)
#         code_obj = marshal.load(f)
#         disassembled_code = dis.Bytecode(code_obj)
        
#         for instr in disassembled_code:
#             simplified_instr = simplify_instruction(instr)
#             if simplified_instr:
#                 output.append(simplified_instr)
    
#     return "\n".join(output)








# import uncompyle6
import io

def decompile_pyc(pyc_file):
    try:
        # Create a StringIO object to capture the output
        output = io.StringIO()

        # Decompile the .pyc file and write the output to the StringIO object
        uncompyle6.decompile_file(pyc_file, output)
        
        # Get the content of the output
        decompiled_code = output.getvalue()

        # Close the StringIO object
        output.close()

        return decompiled_code
    except Exception as e:
        return f"Error: {e}"


