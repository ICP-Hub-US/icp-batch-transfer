# Program to send batch transfers to ICP addresses. It reads a csv file with the addresses, amounts and memo.
# It relies on the dfx ledger command, so you need to have dfx installed/updated.

def main():
    
    import csv, sys

    if len(sys.argv) == 2:
        source_file = sys.argv[1]
    else:
         print("Please specify the csv file with addresses to transfer to.")
         sys.exit(0)

    print(f"ICP address to transfer from is {get_account_id()}")
    print(f"Starting balance on the account is {get_account_balance()}\n")

    try:

        with open(source_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination = row['destination']
                amount = row['amount']
                memo = row['memo']
                transfer_icp(destination, amount, memo)

    except FileNotFoundError:
        print ("Source file not found." )
    
    print(f"Ending balance on the account is {get_account_balance()}\n")


def get_account_id():
    import subprocess
    result = subprocess.run('dfx ledger account-id', stdout=subprocess.PIPE, shell=True)
    account_id = result.stdout.decode('utf-8').strip()
    return account_id

def get_account_balance():
    import subprocess
    result = subprocess.run('dfx ledger balance --ic', stdout=subprocess.PIPE, shell=True)
    balance = result.stdout.decode('utf-8').strip()
    return balance

def transfer_icp(destination, amount, memo=1):
    import subprocess
    print(f"Attempting to send {amount} to {destination}")
    result = subprocess.run(f'dfx ledger transfer --ic --memo {memo} --amount {amount} {destination}', stdout=subprocess.PIPE, shell=True)
    print(result.stdout.decode('utf-8'))
    
if __name__ == "__main__": 
	main() 
