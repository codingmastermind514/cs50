def main():
    # take user input for filename in the format filename.filetype
    filename = input("File name: ").lower().strip()

    # find the file extension by splitting and grabbing the last element of the list
    ext = filename.split(".")[-1]

    # check extension against several known extensions & print
    match ext:
        case 'gif':
            print('image/gif')
        case 'jpg':
            print('image/jpeg')
        case 'jpeg':
            print('image/jpeg')
        case 'png':
            print('image/png')
        case 'pdf':
            print('application/pdf')
        case 'txt':
            print('text/plain')
        case 'zip':
            print('application/zip')
        case _:
            print('application/octet-stream')

main()
