from openpyxl import load_workbook
book = load_workbook('E:\\A Development That No One Knows\\Github\\InventoryEditor-Data_List_Simplier_AEMB\\sam.xlsx')
sheet = book.active #active means get the first sheet
sheet['A1']= 100
book.save('E:\\A Development That No One Knows\\Github\\InventoryEditor-Data_List_Simplier_AEMB\\sam.xlsx')