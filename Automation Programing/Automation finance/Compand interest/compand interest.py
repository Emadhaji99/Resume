try:
    sarmayeh_avalieh=int(input("enter the value to toman :"))
    darsad=float(input("darsad be ashar: "))
    sal=int(input("chand sal bemone ? "))
    darsad_mahane=float(darsad/12)
    soud_khalie=(sarmayeh_avalieh*darsad)+sarmayeh_avalieh
except ValueError:
    print("enter tho the digit ")

for i in range(sal*12):
    soud_mahane=sarmayeh_avalieh*darsad_mahane
    sarmayeh_avalieh+=soud_mahane
    format_sarmayeh_kol="{:,}".format(sarmayeh_avalieh)
    if i==(sal*12)-1:
        farghe_bein_soud_morkab_va_khalie=(sarmayeh_avalieh-soud_khalie)
        print(format_sarmayeh_kol,"soud morkab")
        print("{:,}".format(soud_khalie),"sarmaye gozarie adi")
        print("{:,}".format(farghe_bein_soud_morkab_va_khalie),"mizan tafavot ba soud morkab ")
        break