try:   
    filename = input("Enter filename: ")
    outfile = open(filename, "w")
    content_ = "This is a test\n"
    outfile.write(content_)
finally:
    outfile.close()