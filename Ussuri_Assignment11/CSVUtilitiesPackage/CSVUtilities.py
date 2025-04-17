import csv

class CSVUtilities:
    def load_csv_to_dict_list(self, filename):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            return list(csv.DictReader(file))

    def write_dict_list_to_csv(self, data, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            if not data:
                file.write("No data found.\n")
                return

            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()

            for row in data:
                # Ensure Gross Price is always a string formatted to 2 decimals
                if "Gross Price" in row:
                    try:
                        price = float(row["Gross Price"])
                        row["Gross Price"] = "{:.2f}".format(price)
                    except:
                        row["Gross Price"] = "0.00"

                writer.writerow(row)


