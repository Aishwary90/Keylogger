# The file is closed automatically after the block of code is executed due to the use of the `with` statement.

with open("sample.txt", "w") as ab:
    ab.write("This is a test\n");
# This code opens the same file in write mode and writes "This is a test" to it, overwriting any existing content.


with open("sample.txt", "r") as ab:
    ab.read();
# This code opens the same file in read mode and reads its content.


with open("sample.txt", "a") as ab:
    ab.write("This test is appended in file\n")
# This code opens a file named "log.txt" in append mode and writes "This is a test" to it.
# The file is created if it doesn't exist, and the content is appended if it does.