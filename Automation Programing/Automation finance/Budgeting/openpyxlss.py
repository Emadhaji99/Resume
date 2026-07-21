import openpyxl

wb=openpyxl.load_workbook("SAMPEL.xlsx")
Sheet=wb["Sheet1"]
coloumn=Sheet["B"]
Analys_list=["SUM","MAX","Average","total expense"]
for cell in coloumn:
    for item in Analys_list:
        if item in str(cell.value) :
            break 
    else:
        pass

    


    

            

