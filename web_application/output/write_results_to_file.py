# TODO: Test
def write_to_file(result, filename="test.txt"):
    # print(write_to_file)
    f = open(filename, "x")
    f.write(result)
    f.close()

    #open and read the file after the overwriting:
    # f = open("demofile3.txt", "r")
    # print(f.read())
    pass

# write_to_file("test")