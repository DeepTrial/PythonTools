import os, subprocess
import time
import argparse

def convert(input,output):
    if not output:
        print("output path error! please check")

    if os.path.isfile(input):
        filename=input
        if filename.lower().endswith(".heic"):
            subprocess.run(["magick", "%s"%(filename),"%s" % (os.path.join(output, filename[0:-5] + '.jpg'))])
        else:
            print("Input file is not HEIC image")
    elif os.path.isdir(input):
        directory=input
        for filename in os.listdir(directory):
            if filename.lower().endswith(".heic"):
                print('Converting %s...' % os.path.join(directory, filename))
                subprocess.run(["magick", "%s" % os.path.join(directory, filename), "%s" % (os.path.join(output, filename[0:-5] + '.jpg'))])

    else:
        print("input error! the input is not file or dir,please check!")

if __name__ == '__main__':
    # Initial time
    t_init = time.time()

    # Parse arguments
    parser = argparse.ArgumentParser(description='Convert HEIC image files to JPG format using ImageMagic')
    parser.add_argument('-d', '--data',help='Input file/directory.')
    parser.add_argument('-o', '--out',help='Output file/directory. Default: Same as \input directory/file with .jpg extension.',default=None)

    args = parser.parse_args()

    # Convert files from HEIC to JPG
    convert(args.data, args.out)

    # Final time
    t_final = time.time()
    print('Progam finished in {} secs.'.format(t_final - t_init))
