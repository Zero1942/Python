import xlwt
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('pywt')
worksheet.write(0, 0, '姓名')
new_workbook.save('/Users/wangruiming/Documents/GitHub/DevOps/Python/pywrite.xls')