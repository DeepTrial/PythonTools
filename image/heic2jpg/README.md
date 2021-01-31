# Convert HEIC to JPEG

## Install & Prepare

1. make sure you have installed the ImageMagick
2. basic python3 environment (test with python3.7)

## Usage

the main function of the convert process:
```python
def convert(input,output)
    """
    input:  input file or dir
    output: output dir
    """
    ....
```

use command like:
```
python heic2jpg.py -d <input> -o <output>
```
The command will convert all the HEIC images in the input file/dir, and save the images in the format of JPG in the output dir.