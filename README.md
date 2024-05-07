
# ICP Batch Transfer
### Author: Pedro Galvan (@pedrogk)

Python program to send batch transfers to ICP addresses. It reads a csv file with the addresses, amounts and memo. It relies on the `dfx ledger` command, so you need to have dfx installed/updated.

Remember that each individual transfer generates a network fee (.0001 ICP). 

Prerrequisites:
* Python 3.5+ installed.
* dfx client installed [installation instructions](https://internetcomputer.org/docs/current/developer-docs/getting-started/install/#installing-dfx). 

Steps:
1. On the command line (with dfx installed) type `dfx ledger account-id`. This will be the emitting account for the transfer. It needs to have enough ICP balance.
2. To check the balance on this account, do `dfx ledger balance --ic`. Note: By adding the --ic argument you are specifying that you are referring to mainnet (and not a local test environment).
3. Transfer ICP to the given account id and check the balance. You can start with a small amount just to test things out.
4. Create a csv file with three columns: destination, amount, memo. Refer to the sample.csv file.
5. Run the script from the command line with `python icp_batch_transfer.py [csv file]`. This asumes that your python 3 executable is `python`. If its not found or gives an error, then try with `python3` instead.

Donations:
If this is useful, feel free to send a tip with a tiny amount of ICP to dc6d85f45907789a2ee9d6f1c1d1b2f53f029b619c1a8f755b9c37853b7a5d1c