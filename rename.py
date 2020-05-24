import os
import shutil
from hunspell import Hunspell
h = Hunspell()

def spellvalid_path(path: str):
    [filename, extension] = os.path.splitext(os.path.basename(path))

    # Compute the largest spell valid substring start with every character
    # Store the (pattern, (startIdx, endIdx (inclusive)))
    large_tokens = []
    end = len(filename)
    i = 0
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
            large_tokens.append(greedy_token)
        
        # If we find the spell greedy token, other next token will look after than token
        # Otherwise we increment by 1
        i = nextI
        

    print(large_tokens)
    valid_filename = "-".join(str(x.strip()) for x in large_tokens)
    print("valid_filename: " + valid_filename)

    filepath = os.path.join(os.path.dirname(path), valid_filename + extension)
    return filepath

def batch_rename_pdf(path: str):
    filenames = [s for s in os.listdir(path) if s.endswith(".pdf")]
    filenames = [os.path.join(path, s) for s in filenames]

    # Tuple of (filepath, valid spell filepath)
    batch_filename_tuples = [(s, spellvalid_path(s)) for s in filenames]
    for (old, new) in batch_filename_tuples:
        os.rename(old, new)

# batch_rename_pdf("C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths")
# batch_rename_pdf("C:\\Users\\jason\\OneDrive\\Humble Bundle\\Dotnet")

spellvalid_path("C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\computertheory.pdf")
spellvalid_path("C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\linearalgebra.pdf")
spellvalid_path("C:\\Users\\jason\\OneDrive\\Humble Bundle\\Maths\\algebraessentials.pdf")