from xlrd import open_workbook


def read_locators(sheet_name):
    wb = open_workbook(r"E:\sony\Frame_work\Data\locators.xls")
    ws = wb.sheet_by_name(sheet_name)
    used_row = ws.nrows
    locators = {}
    for index in range(used_row):
        data = ws.row_values(index)
        locators[data[0]] = (data[1], data[2])
    return locators


def read_header(sheet_name, test_case_name):
    wb = open_workbook()
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    for index in range(used_rows):
        data = ws.row_values(index)
        if data[0] == test_case_name:
            header = ws.row_values(index - 1)
            return ",".join(header[1:])


def read_data(sheet_name, test_case_name):
    wb = open_workbook()
    ws = wb.sheet_by_name(sheet_name)
    used_rows = ws.nrows
    test_data = []
    for index in range(used_rows):
        data = ws.row_values(index)
        if data[0] == test_case_name:
            test_data.append(data[1:])
