from PyTableWiz.PythonTableWizard import TableWizard

TableWizard("src/DataFile_5.csv", limit=25,
            SelectedRows={'employeeNumber': ('1056', '1076', '1102', '1188'),
                          'lastName': ('Murphy', 'Jennings', 'Bow',),
                          'firstName': ('Martin', 'Mami', 'Peter')})
