import csv
from multiprocessing import Pool

def process_file(file_path):
    total_transactions = 0
    total_amount = 0.0

    with open(file_path, mode='r', newline='') as file:
        
        reader = csv.reader(file)
        header = next(reader)
        amount_index = header.index("Amount")
        
        for row in reader:
            total_transactions += 1
            total_amount += float(row[amount_index])
    
    return file_path,total_transactions,total_amount

def main(csv_files):
    
    with Pool(processes=len(csv_files)) as pool:
        results = pool.map(process_file,csv_files)
        
    total_files = len(results)
    total_transcations = sum(result[1] for result in results)
    total_amount = sum(result[2] for result in results)
    
    for file_name, transactions, amount in results:
        print(f"File: {file_name}, Transactions: {transactions}, Total Amount: {amount:.2f}")

    print("\nFinal Summary Report:")
    print(f"Total Files Processed: {total_files}")
    print(f"Total Transactions: {total_transcations}")
    print(f"Total Amount: {total_amount:.2f}")
    
    
    
if __name__ == '__main__':
    csv_files = ['transactions_region1.csv','transactions_region2.csv','transactions_region3.csv']
     
    main(csv_files)