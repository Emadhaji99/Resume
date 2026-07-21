from bidi.algorithm import get_display
import os
import arabic_reshaper
import csv 
import openpyxl

wb=openpyxl.load_workbook("SAMPEL.xlsx")
Sheet=wb["Sheet1"]
column_A=Sheet["A"]
coloumn_B=Sheet["B"]
Main_List=[]
Expense_List=[]
invest_List=[]
for cell in coloumn_B:
     if ":" in str(cell.value):
          Expense_List.append(str(cell.value))
for cell in column_A:
     if cell.font.size==20:
          Main_List.append(str(cell.value))
print(Main_List)

Main_file = r"C:\project\profession\Technology\Digital Technology\resume\Projects\Automation\Automation finance\Budgeting\expense.csv" 

#Extracting The Data From Main File (Reading)

with open(Main_file, mode="r", newline="", encoding="utf-8-sig") as csvfile: 
    reader = csv.DictReader(csvfile) 
    for row in reader:
        Type_transaction=row['مبلغ گردش بدهکار']
        if eval(Type_transaction)!=0:
            reshaped = arabic_reshaper.reshape(str(f"در تاریخ  {row["تاریخ"]}و ساعت  {row['زمان']}و این تراکنش به مبلغ برداشتی {row['مبلغ گردش بدهکار']} به شرح {row['شرح']}  برای چیه ?"))
            bidi_text = get_display(reshaped)
            Expense_Field=input(bidi_text).upper()


        else:
                reshaped = arabic_reshaper.reshape(str(f"در تاریخ   {row["تاریخ"]}و  ساعت  {row['زمان']}و این تراکنش به مبلغ وازیزی  {row['مبلغ گردش بستانکار']} به شرح  {row['شرح']}  برای چیه ?"))
                bidi_text = get_display(reshaped)
                Income_Field=input(bidi_text).upper()
