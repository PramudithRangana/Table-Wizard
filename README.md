# Table Creating for CSV Data File

- To run this program, it's need to call the class as follows

```python
from PyTableWiz.PythonTableWizard import TableWizard

TableWizard("src/My filepath/to/datafile.csv")
```
- Here take the file path of the data file which you need to create a table.
- You can customize how many rows need to be belongs to the table by using *__limit__*  key word as an argument to provide a limitation. It will get 100 rows by default.

	E.g: 
```python
limit = 100
```

- *justify* key word allow us to change alignments of all column. All column will appear as left justify by default.
- *align* key word allow us to change each column severally.
- You should provide the particular column name as a key and which side to align as value.
- 'align' argument is represented as a dictionary.
	
	E.g: 
```python
align = {'Column 1': 'Side', 'Column 2': 'Side', 'Column 3': 'Side'}
```

- This module has method to customise which column need to be created as a table.
- To do this you can use *DTE* as an argument.
- DTE Stand for: Derived Table Expression.
- this argument get values as a list.

    E.g:

```python
DTE = ['Column 1', 'Column 2', 'Column 3', 'Column 4']
```

- Select specific rows by using 'SelectedRows'.
- 'SelectedRows' argument is represented as a dictionary.

	E.g:
```python
SelectedRows = {'Column 1': ('value 1', 'value 2', 'value 3'), 'Column 2': ('value 1', 'value 2')}

```

- If you not necessary the accessory details about the table creation, you can set it *false*.
- To set it, use the key word *acc_details*. by default, it is True.

- To create the table used the following symbols:

![img.png](img.png)
