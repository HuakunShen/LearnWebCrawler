import csv
import mysql.connector as SQL

with open('items.csv') as csvfile:
    # csv_file = csv.reader(csvfile, delimiter=',')
    # csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
    # print('debug: ', csv_file)
    mydb = SQL.connect(host='localhost', user='root', password='password', database='booksDB')
    cursor = mydb.cursor()
    csv_data = csv.reader(csvfile, delimiter=',')

    row_count = 0
    for row in csv_data:
        if row_count != 0:
            query = ("INSERT IGNORE INTO books_table "
            "(rating, product_type, upc, title) "
            "VALUES (%s, %s, %s, %s)")
            cursor.execute(query, row)
            # print('debug', row)
        row_count += 1

    mydb.commit()
    cursor.close()
    mydb.close()