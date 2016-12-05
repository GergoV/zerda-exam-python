# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def write_tentimes(file_name, text):
    if type(file_name) == str and type(text) == str:
        try:
            with open(file_name, 'w') as f: # Not checking if file exists; 'w' creates/truncates in anyway
                f.write(text*10)
            return True
        except Exception:
            return False
    else:
        print('ERROR: Invalid input.')
        return False

write_tentimes('test.txt', 'Yolo!')
