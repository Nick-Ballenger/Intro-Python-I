"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
with open('C:/Users/nicks/Documents/Intro-Python-I/src/foo.txt') as f:
    read_data = f.read()
    print(read_data)
    f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newFile = open('bar.txt', 'w')
newFile.write('Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality...')
newFile.close()