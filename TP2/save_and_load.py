def write_object_to_file(d,filename):
    with open(filename,"w") as file:
        file.write(str(d))

def read_object_from_file(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
    return eval(lines[0])