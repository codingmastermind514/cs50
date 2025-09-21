# import emoji library
import emoji

# user input
msg = input("Input: ")
# print -- emojized msg and language alias
print(f"Output: {emoji.emojize(msg, language="alias")}")
