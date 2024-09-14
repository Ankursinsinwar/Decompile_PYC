import chainlit as cl
from chainlit import AskUserMessage, Message, on_chat_start
from decompile import decompile_pyc
import os

@on_chat_start

# async def main():
#     res = await AskUserMessage(content="What is your name?", timeout=30).send()
#     if res:
#         await Message(
#             content=f"Your name is: {res['output']}.\nChainlit installation is working!\nYou can now start building your own chainlit apps!",
#         ).send()



# async def start():
#     files = None

#     # Wait for the user to upload a file
#     while files == None:
#         files = await cl.AskFileMessage(
#             content="Please upload a text file to begin!", accept=["text/plain"]
#         ).send()

#     text_file = files[0]

#     with open(text_file.path, "r", encoding="utf-8") as f:
#         text = f.read()

#     # Let the user know that the system is ready
#     await cl.Message(
#         content=f"`{text_file.name}` uploaded, it contains {len(text)} characters!"
#     ).send()




# @cl.on_message
# async def start():
#     files = None

#     # Wait for the user to upload a file
#     while files == None:
#         files = await cl.AskFileMessage(
#             content="Please upload a text file to begin!", accept=[".pyc"]
#         ).send() 


#     text_file = files[0].name
#     print(text_file)
#     text = disassemble_pyc(text_file)
#     print(text)

#     # with open(text_file.path, "rb", encoding="utf-8") as f:
#     #     text = f.read()

#     # Display the file content directly
#     await cl.Message(
#         content=f"```\n{text}\n```"
#     ).send()










# async def start():
#     files = None

#     # Wait for the user to upload a file
#     while files == None:
#         files = await cl.AskFileMessage(
#             content="Please upload a .pyc file to begin!", accept=[".pyc"]
#         ).send() 

#     # Get the uploaded file path
#     pyc_file_path = files[0].path

#     # Disassemble the .pyc file
#     disassembled_code = disassemble_pyc(pyc_file_path)

#     # Send the disassembled code as a message
#     await cl.Message(
#         content=f"```\n{disassembled_code}\n```"
#     ).send()










# @cl.on_message

# async def start():
#     files = None

#     # Wait for the user to upload a file
#     while files == None:
#         files = await cl.AskFileMessage(
#             content="Please upload a .pyc file to begin!", accept=[".pyc"]
#         ).send() 

#     # Get the uploaded file path
#     pyc_file_path = files[0].path

#     # Disassemble the .pyc file
#     disassembled_code = decompile_pyc(pyc_file_path)

#     # Send the disassembled code as a message
#     await cl.Message(
#         content=f"```\n{disassembled_code}\n```"
#     ).send()







@cl.on_message

async def start():
    files = None

    # Wait for the user to upload a file
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a .pyc file to begin!", accept=[".pyc"]
        ).send() 

    # Get the uploaded file path
    pyc_file_path = f"__pycache__/{files[0].name}"

    print (pyc_file_path)

    # Decompile the .pyc file
    disassembled_code = decompile_pyc(pyc_file_path)

    # Send the disassembled code as a message
    await cl.Message(
        content=f"```\n{disassembled_code}\n```"
    ).send()





# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()