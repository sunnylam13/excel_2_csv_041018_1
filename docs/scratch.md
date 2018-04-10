# Scratch Notes and Log

## Tuesday, April 10, 2018 10:57 AM

will need `openpyxl` to read Excel files in current working directory

output as CSV

single Excel might have many sheets

create one CSV per *sheet*

filenames of CSV should be `<excel filename>_<sheet title>.csv`

where

`<excel filename>` is filename of the Excel file without file extension

`<sheet title>` is the string from `Worksheet` object's `title` variable

will likely need many nested loops

