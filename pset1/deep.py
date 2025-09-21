def main():
    # taking user input for the answer
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    # if the question is 42 forty two or forty-two case insensitively then yes
    if question == '42' or question == 'forty-two' or question == 'forty two':
        print("Yes")

    # anything else print no
    else:
        print("No")

main()
