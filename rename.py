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
    for i in range(0, end):
        large_token = None
        for j in range(i, end):
            token = filename[i:j+1]
            if len(token) != 0 and h.spell(token):
                large_token = (token, (i, j))
        if large_token != None:
            large_tokens.append(large_token)

    # Find out the largest token with no overlap
    # If overlap, take the token from the left
    last_end_inIdx = None
    valid_tokens = []
    for [token, [start_idx, end_inIdx]] in large_tokens:
        if last_end_inIdx:
            # Only append the token if no overlap
            if start_idx > last_end_inIdx:
                valid_tokens.append(token)
                last_end_inIdx = end_inIdx
        else:
            valid_tokens.append(token)
            last_end_inIdx = end_inIdx

    # print(valid_tokens)
    valid_filename = "-".join(str(x.strip()) for x in valid_tokens)
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
batch_rename_pdf("C:\\Users\\jason\\OneDrive\\Humble Bundle\\Dotnet")