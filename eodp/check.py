import re
import utils


def run_all_checks():

    print('Running all checks on all files. This may take a few minutes.')
    for policy in utils.get_all_policies():
        check_duplicates(policy)
        check_multicity(policy)

    return

def check_duplicates(policy):

    if re.search(r"(.{1000})(.+)(\1)", policy['text'], re.DOTALL):
        print(policy['name'] + ' may contain duplicate content.')

    return

def check_multicity(policy):

    return
