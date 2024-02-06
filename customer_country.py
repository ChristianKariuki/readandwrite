def main():
    import csv

   
    infile = open('customers.csv', 'r')
    csv_file = csv.reader(infile)

    next(csv_file)
    outfile = open('customer_country.csv', 'w')
    writer = csv.writer(outfile)

    writer.writerow(["Full name", "Country"])

    customer_count = 0

    for rec in csv_file:
            
        full_name = rec[1] + " " + rec[2]
        country = rec[4]

        writer.writerow([full_name, country])

        customer_count += 1
    print("Total number of customers:", customer_count)

main()
