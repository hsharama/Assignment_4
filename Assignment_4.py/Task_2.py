# Write and Append Data to a File
""" Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

out_ap_1 = input("Enter text to write to the file: ")

with open("output.txt", "w") as fh:
    fh.write(out_ap_1 + "\n")
    print("Data successfully written to output.txt\n")

out_ap_2 = input("Enter additional text to append: ")

with open("output.txt", "a") as fh:
    fh.write(out_ap_2 + "\n")
    print("Data successfully appended.\n")

print("Final content of output.txt :")

with open("output.txt", "r") as fh:
    content = fh.read()
    print(content)

    


