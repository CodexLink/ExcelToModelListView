import openpyxl

wb = openpyxl.load_workbook('E:\A Development That No One Knows\Github\InventoryEditor-Data_List_Simplier_AEMB\TrialError_ExperimentalPrototype\sample.xlsx')
first_sheet = wb.get_sheet_names()[0]
worksheet = wb.get_sheet_by_name(first_sheet)

#here you iterate over the rows in the specific column
for row in range(2,worksheet.max_row+1):  
    for column in "ADEF":  #Here you can add or reduce the columns
        cell_name = "{}{}".format(column, row)
        worksheet[cell_name].value # the value of the specific cell