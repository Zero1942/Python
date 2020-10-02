import xlrd
xlsx = xlrd.open_workbook('/Users/wangruiming/Documents/服务器清单.xlsx')
table = xlsx.sheet_by_index(0)
# table = xlsx.sheet_by_name('APS')
print(table.cell_value(13,0))
print(table.cell(13,0).value)
print(table.row(13)[0].value)