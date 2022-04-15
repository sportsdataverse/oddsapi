def read_txt(file):
    with open("{}".format(file)) as f:
        lines = f.readlines()
    return lines[0]