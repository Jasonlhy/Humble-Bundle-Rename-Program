import os
from hunspell import Hunspell
h = Hunspell()


def spellvalid_path(basename):
    """Find out the most likely spell valid filename with greedy algorithm

        For example:
        - computertheory -> computer-theory
        - linearalgebra -> linear-algebra
        - algebraessentials -> algebra-essentials
    """
    [filename, extension] = os.path.splitext(basename)

    # Compute the largest spell valid substring by looking at the characters
    tokens = []
    i, end = 0, len(filename)
    while i < end:
        # record the greedy information
        nextI = i + 1
        greedy_token = None

        for j in range(i, end):
            token = filename[i:j+1]
            if len(token) != 0 and h.spell(token):
                greedy_token = token
                nextI = j + 1

        if greedy_token != None:
            tokens.append(greedy_token)

        # If we find the spell greedy token, other next token will look after than token
        # Otherwise we increment by 1
        i = nextI

    valid_filename = "-".join(str(x.strip()) for x in tokens)
    return valid_filename + extension


def batch_rename(path, extension=".pdf"):
    """Given the path of the directory, batch rename the file names to be spell valid filename

        For example:
        - C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\computertheory.pdf -> C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\computer-theory.pdf
        - C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\linearalgebra.pdf -> C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\linear-algebra.pdf
        - C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\algebraessentials.pdf -> C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\algebra-essentials.pdf
    """
    filenames = [s for s in os.listdir(path) if s.endswith(extension)]

    # Tuple of (filepath, valid spell filepath)
    batch_filename_tuples = [(s, spellvalid_path(s)) for s in filenames]
    batch_filename_tuples = [
        (os.path.join(path, old),
         os.path.join(path, new))
        for (old, new) in batch_filename_tuples]

    for (old, new) in batch_filename_tuples:
        os.rename(old, new)


# Main program
dir_path = input("Path of the folder: ")
extension = input("Extension you want to rename to: ")

if not os.path.isdir(dir_path):
    print("{0} is not a directory".format(dir_path))
    exit()
if not extension.startswith("."):
    exit()

sure = input(
    "Are you sure to rename the file under directory {dir} with extensions {ext} [Y/y]: ".format(dir=dir_path, ext=extension))
if sure == 'Y' or sure == 'y':
    batch_rename(dir_path)
else:
    print("Operation abort")
