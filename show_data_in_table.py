from PyTableWiz.PythonTableWizard import TableWizard

TableWizard("src/DataFile_2.csv", limit=6, view_attr=['officeCode', 'addressLine1'])

# , DTE=['firstName', 'employeeNumber', 'email']
# , align={'Product Name': 'left', 'Product Code': 'center'}
# , align={'territory': 'left', 'state': 'center', 'city': 'left'}
# , align={'checkNumber': 'left'}
# , align={'country': 'left', 'customerName': 'center'}
# , align={'jobTitle': 'left', 'employeeNumber': 'center'}
# , DTE=['country', 'addressLine1', 'state', 'city', 'territory'],
#             align={'territory': 'left', 'state': 'center', 'city': 'right'}
# , limit=5, DTE=['country', 'addressLine1', 'state', 'city', 'territory'],
#            align={'territory': 'left', 'state': 'center', 'city': 'right'}
