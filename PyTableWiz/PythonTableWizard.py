import csv
from timeit import default_timer as timer

""" Developer   : Pramu Programming Concept """
""" Description : This program has been created for represent (csv, json etc..) data file as a table. """
""" Date        : Thursday, 16 March 2023 """


class TableWizard:
    def __init__(self, file_path, dialect_mode="r", limit=100, justify='left',
                 align=None, acc_details=True, DTE=None,
                 tl="┌", ti="┬", tr="┐", hdl="├", hdi="┼", hdr="┤", bl="└", bi="┴", br="┘", vl="│", hl="─"):

        self.file_path = file_path
        self.dialect_mode = dialect_mode
        self.limit = limit
        self.justify = justify
        self.align = align  # need in dictionary format
        self.accessories_details = acc_details
        self.Derived_table = DTE  # need in list format

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

        self.col_index = None
        self.row_count = 0

        self.temp_data_list = []
        self.data_list = []
        self.col_width = []

        # star time of entire data table creating
        self.start = timer()
        # Read data from (csv, ..) data file and get all
        self.dataReader()
        # set maximum column width according to the content of each column
        self.column_width()
        # call the table creator
        self.draw_table()
        # end time of entire data table creating
        self.stop = timer()

        # call to data Read Time Counting function
        if self.accessories_details:
            self.reading_details()
        else:
            pass

    # get all data
    def dataReader(self):
        # get file path
        if self.file_path:
            try:
                with open(self.file_path, self.dialect_mode) as f:
                    csvRead = csv.reader(f)

                    if self.Derived_table is None:
                        for row in csvRead:
                            # append data for (normal) table creation
                            self.data_list.append(row)
                        return self.data_list

                    else:
                        # Derived Table Expression
                        for row in csvRead:
                            # store table data temporary
                            self.temp_data_list.append(row)
                            # find index number of each column by headers
                            if not self.col_index:
                                # find index number of each column by headers(column name)
                                self.col_index = [self.temp_data_list[0].index(x) for x in self.Derived_table if
                                                  x in self.temp_data_list[0]]
                            # append data for (derived) table creation
                            self.data_list.append(list(row[i] for i in self.col_index))

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
            # Default alignment representation
            pass
        else:
            try:
                # Set index no. instead of column name to the dictionary ---> N.B: self.data_list[0] (header)
                self.align = {self.data_list[0].index(x): y for x, y in self.align.items() if x in self.data_list[0]}
            except ValueError as ve:
                print(f"[!] ValueError : {ve}\n Please check your 'alignment' argument")
                exit()
            except Exception as e:
                print(f'[!] Error : {e}')

        # top of the table
        self.draw_separators(self.top_left, self.top_interconnection, self.top_right)
        print(f"{self.vertical_line} ", end=" ")

        # self.header of the entity ---> N.B: self.data_list[0] (header)
        for column in enumerate(self.data_list[0]):
            print(self.fixed_length(column[1], self.col_width[column[0]]), end=f"  {self.vertical_line}  ")
        print()
        # table body separation from the header
        self.draw_separators(self.heading_left, self.heading_interconnection, self.heading_right)

        # header dropping--------------------------->>
        self.data_list.pop(0)

        # body of the entity -------> N.B: self.data_list[1:] (content)
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

    # Accessory Details
    def reading_details(self):
        print(f"👉 Records    : {self.row_count}") if self.row_count > 1 else print(f"👉 Record     : {self.row_count}")
        print(f"👉 Attributes : {len(self.data_list[0])}") if len(self.data_list[0]) > 1 else \
            print(f"👉 Attribute  : {len(self.data_list[0])}")
        print(f"👉 File Name  : {self.file_path.split('/')[-1]}")

        # Total Time to Effect (Time Consume)
        time_duration = (self.stop - self.start)
        print(f"👉 TTE        : {time_duration:.4f} sec")

# if __name__ == '__main__':
#     TableWizard("src/test_4.csv")
