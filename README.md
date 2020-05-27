# Purpose

I bought some books from [Humble Bundle](https://www.humblebundle.com/) with PDF format, the default filenames are **ALWAYS** in unreadable format.
 
- dimensionalanalysisforunitconversionusingmatlab.pdf
- algebraessentials.pdf
- multivariableandvectorcalculus.pdf


Therefore, the purpose of this program is quite simple, it will rename the unreadable filename into a more human readable format by finding the largest word tokens that can pass the spell check, and combines them into the new filename. For example: 

- computertheory.pdf -> computer-theory.pdf
- linearalgebra.pdf -> linear-algebra.pdf
- algebraessentials.pdf -> algebra-essentials.pdf

## Requirements

- Python 3
- pip install cyhunspell

## Usage

```bash
python rename.py
Path of the folder: C:\\Users\\jason\\Documents\\RenamePDFs\\TestData
Extension you want to rename to: .pdf
Are you sure to rename the file under directory C:\\Users\\jason\\Documents\\RenamePDFs\\TestData with extensions .pdf [Y/y]: Y
```

## Why greedy algorithm?
Because all followings are true

- h.spell("a") => True
- h.spell("algebra") => True
- h.spell("essentials") => True
- h.spell("essential") => True

## Roadmap
- Customize spell dictionary
- Take preference of some term over another (for sample - the secure over these) 
