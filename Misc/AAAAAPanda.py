import pandas as pd

def name_title(cell):
    return cell.title()

df = pd.read_excel('IT2017-21.xlsx','Sheet1',converters = {'First Name':name_title})

export_excel = df.to_excel(r'E:\Program\Python\IT2017-21.xlsx', index = None, header=True)

