try:
    with open("novooo.txt", "x+") as f:
        f.write("Novi sadrzaj sad \n")
        f.seek(0)
        print(f.readlines())
except FileExistsError:
    print("Vec postoji")