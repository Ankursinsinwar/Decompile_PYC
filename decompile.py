import uncompyle6
import sys
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


