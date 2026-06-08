import os

def create_output_folder():

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
        