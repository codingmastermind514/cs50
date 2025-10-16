from PIL import Image, ImageOps
import sys

# Exclude the first argument and grab cline args
args = sys.argv[1:]

# Too many command-line arguments
if len(args) > 2:
    sys.exit("Too many command-line arguments")

# Too few command-line arguments
if len(args) < 2:
    sys.exit("Too few command-line arguments")

zero = args[0]
one = args[1]

# Not a valid file extension
if not args[0].lower().endswith((".jpg",".jpeg",".png")) or not args[1].lower().endswith((".jpg",".jpeg",".png")):
    sys.exit("Invalid input")

# grab extensions
ext1 = zero.split(".")
ext2 = one.split(".")

# if they aren't the same
if ext1[1] != ext2[1]:
    sys.exit("Input and output have different extensions ")

# Open the file and read the lines 
try:
    # opened me.png as img
    with Image.open(zero) as img:

        # cropped img to be 600x600 and saved it
        img = ImageOps.fit(img,(600,600))
        shirt = Image.open("shirt.png").convert("RGBA")
        img.paste(shirt,mask=shirt)
        img.save(one)

# except
except BaseException:
    sys.exit(f"Could not read {args[0]}") # couldn't read

