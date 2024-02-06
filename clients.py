def main():
    infile = open('clients.txt', 'r')

    i = 1

    for line in infile:
        line = line.rstrip("\n")
        print(f"{i}. {line}")

        i += 1

    infile.close()

    print(f"\nTotal number of customers: {i-1}")

main()