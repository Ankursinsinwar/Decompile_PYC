import chainlit as cl
from chainlit import AskUserMessage, Message, on_chat_start
from decompile import decompile_pyc
import os

@on_chat_start

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
