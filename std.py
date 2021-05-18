
from openpyxl import load_workbook

book = load_workbook('base.xlsx')
sheet = book("baseDados")
print(book.seetnames)
juntacompleta = sheet['E2'].value
print(juntacompleta)