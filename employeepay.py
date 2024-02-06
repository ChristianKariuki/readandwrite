def main():
    import csv

    empdata = open('Employee_data.csv','r')

    csv_file = csv.reader(empdata)

    next(csv_file)
    outfile = open('Employee_pay.csv', 'w')
    writer = csv.writer(outfile)

    writer.writerow(["Full name", "Total Pay"])

    emp_count = 0

    for rec in csv_file:
            
        full_name = rec[1]
        pay = float(rec[3]) * (1 + float(rec[7]))

        writer.writerow([full_name, pay])

        emp_count += 1
main()