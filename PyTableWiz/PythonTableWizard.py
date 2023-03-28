import csv

""" Developer   : Pramu Programming Concept """
""" Description : This program has been created for represent (csv, json etc..) data file as a table. """
""" Date        : Wednesday, 01 March 2023 """


class TableWizard:
    def __init__(self, file_path, dialect_mode="r", limit=100, justify='left', align=None, acc_details=True,
                 view_attr=None,
                 tl="┌", ti="┬", tr="┐", hdl="├", hdi="┼", hdr="┤", bl="└", bi="┴", br="┘", vl="│", hl="─"):

        self.file_path = file_path
        self.dialect_mode = dialect_mode
        self.index_finder = []
        self.header = None
        self.row_count = 0
        self.file_path = file_path
        self.file_name = file_path.split('/')[-1]
        self.limit = limit
        self.justify = justify
        self.align = align  # need in dictionary format
        self.accessories_details = acc_details
        self.view_attributes = view_attr

        # adjustments
        self.top_left = tl
        self.top_interconnection = ti
        self.top_right = tr
        self.heading_left = hdl
        self.heading_interconnection = hdi
        self.heading_right = hdr
        self.bottom_left = bl
        self.bottom_interconnection = bi
        self.bottom_right = br
        self.vertical_line = vl
        self.horizontal_line = hl

        self.temp_data_list = []
        self.data_list = []
        self.col_width = []

        self.dataReader()
        self.column_width()
        self.draw_table()

    def dataReader(self):
        # get file path
        if self.file_path:
            try:
                with open(self.file_path, self.dialect_mode) as f:
                    csvRead = csv.reader(f)

                    if self.view_attributes is None:
                        for row in csvRead:
                            self.data_list.append(row)
                        return self.data_list

                    else:
                        for row in csvRead:
                            self.temp_data_list.append(row)
                            col_index = [self.temp_data_list[0].index(x) for x in self.view_attributes if
                                         x in self.temp_data_list[0]]
                            self.data_list.append(list(row[i] for i in col_index))

                        return self.data_list
            except Exception as e:
                print("[!] ", e)
                exit()
        else:
            print("[?] File Path Not Found !")
            exit()

    # set width of each attribute (Set attributes width with matching maximum value of each row by comparison two rows)
    def column_width(self):
        # all rows respectively
        for row in enumerate(self.data_list):
            # row check under limit
            if row[0] <= self.limit:
                # getting values of each row(array)
                for i in enumerate(row[1]):
                    # find out which one is the maximum value
                    # Check both list has same number of items
                    if len(row[1]) <= len(self.col_width):
                        # Check Already existing items length with new item's length
                        if len(i[1]) > self.col_width[i[0]]:
                            # if new value length higher than the existing one, new value substitute to the index
                            self.col_width[i[0]] = len(i[1])
                        else:
                            # if new value length not higher than the existing one, no need any changes
                            pass
                    else:
                        # 'col_width' array initialization
                        self.col_width.append(len(i[1]))
            else:
                break

        # Send the maximum width of each row
        return self.col_width

    # Horizontal Separators
    def draw_separators(self, start_symbol, Separate_symbol, end_symbol):
        print(start_symbol, end='')
        for cw in self.col_width:
            if self.col_width[-1] == cw:
                print(((self.horizontal_line * (cw + 3)) + self.horizontal_line), end=end_symbol)
            else:
                print(((self.horizontal_line * (cw + 3)) + self.horizontal_line), end=Separate_symbol)
        print()

    # table content(records) fix to the table
    def fixed_length(self, text, length):
        if self.justify == 'left':
            text = (text + " " * length)[:length]
        elif self.justify == 'center':
            text = (" " * ((length // 2) - (len(text) // 2)) + text + " " * length)[:length]
        elif self.justify == 'right':
            text = (" " * (length - (len(text))) + text)[:length]
        return text

    # draw the table with all content
    def draw_table(self):
        # find the column numbers with stick position to Set alignment to particular column(s)
        reset_align = self.justify
        if self.align is None:
            pass
        else:
            try:
                # Set index no. instead of column name to the dictionary
                self.align = {self.header.index(x): y for x, y in self.align.items()}
            except ValueError as ve:
                print(f"[!] ValueError : {ve}\n Please check your 'alignment' argument")
                exit()
            except Exception as e:
                print(f'[!] Error : {e}')

        # top of the table
        self.draw_separators(self.top_left, self.top_interconnection, self.top_right)
        print(f"{self.vertical_line} ", end=" ")

        # self.header of the entity
        for column in enumerate(self.data_list[0]):
            print(self.fixed_length(column[1], self.col_width[column[0]]), end=f"  {self.vertical_line}  ")
        print()
        # table body separation from the self.header
        self.draw_separators(self.heading_left, self.heading_interconnection, self.heading_right)
        # header dropping------------------------------------------------------------------------------------->
        self.header = self.data_list.pop(0)

        # body of the entity
        for row in enumerate(self.data_list):
            # row range limitation
            if self.row_count == self.limit:
                # If already read  no. of record reach to the limit, then no need to read the (data) file further more
                break
            else:
                print(f"{self.vertical_line} ", end=" ")
                for column in enumerate(row[1]):
                    # Set alignment to particular column(s)
                    if self.align is None:
                        pass
                    else:
                        if column[0] in self.align:
                            self.justify = self.align[column[0]]
                        else:
                            self.justify = reset_align

                    # print table with content
                    print(self.fixed_length(column[1], self.col_width[column[0]]), end=f"  {self.vertical_line}  ")
            self.row_count += 1
            print()

        # end of the table
        self.draw_separators(self.bottom_left, self.bottom_interconnection, self.bottom_right)

# if __name__ == '__main__':
#     TableWizard("src/test_4.csv")
