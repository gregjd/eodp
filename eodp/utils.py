# import re
import os


DATA_FOLDER = './data/'


def get_all_policies_merged():

    return "\n\n".join(get_all_policies(text_only=True))

def get_all_policies(text_only=False):

    file_names = os.listdir(DATA_FOLDER)
    files = []
    for name in file_names:
        with open(DATA_FOLDER + name) as openfile:
            text = openfile.read().decode('utf-8')
            info = {"name": name,
                    "text": text}
            files.append(text if text_only else info)

    return files

