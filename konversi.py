banner = """
  #    #                                                 #####                                        #####                       
 #   #   ####  #    # #    # ###### #####   ####  #    #     #   ##   ##### #    #   ##   #    #    #     # #    # #    # #    # 
 #  #   #    # ##   # #    # #      #    # #      #    #        #  #    #   #    #  #  #  ##   #    #       #    # #    # #    # 
 ###    #    # # #  # #    # #####  #    #  ####  #     #####  #    #   #   #    # #    # # #  #     #####  #    # ###### #    # 
 #  #   #    # #  # # #    # #      #####       # #          # ######   #   #    # ###### #  # #          # #    # #    # #    # 
 #   #  #    # #   ##  #  #  #      #   #  #    # #    #     # #    #   #   #    # #    # #   ##    #     # #    # #    # #    # 
 #    #  ####  #    #   ##   ###### #    #  ####  #     #####  #    #   #    ####  #    # #    #     #####   ####  #    #  ####
  
     ====================================================================
     **                  Instagram : @rakhasidqi                        **
     **                  Github    : RakhaShidqi                        **
     **                  Email     : iniakunpribadi496@gmai.com         **
     ====================================================================
"""
print(banner)

celcius = float(input(" Masukkan Suhu dalam bentuk Celcius : "))
print("Suhu adalah :",celcius, "C")

reamur = (4 / 5) * celcius
print("Suhu reamur adalah :",reamur, "R")

fahrenheit =(9 / 5) * celcius + 32
print("Suhu fahrenheit adalah :",fahrenheit, "F")

kelvin = celcius + 273.15
print("Suhu Kelvin adalah :",kelvin, "K")

# Program Konversi reamur ke satuan lain
print("\nProgram Konversi Temperatur\n")
reamur = float(input(" Masukkan Suhu dalam bentuk reamur : "))
print("Suhu reamur adalah :",reamur, "R")

celcius = (5 / 4) * reamur
print("Suhu celcius adalah :",celcius, "C")

fahrenheit = (9 / 4) * reamur + 32
print("Suhu fahrenheit adalah :",fahrenheit,"F")

kelvin = (5 / 4) * reamur + 273.15
print("Suhu kelvin adalah :",kelvin,"K")

#Program Konversi Fahrenheit ke satuan lain
print("\nProgram Konversi Temperatur\n")
fahrenheit = float(input("Masukkan Suhu dalam bentuk fahrenheit : "))
print("Suhu Fahrenheit adalah :",fahrenheit, "F")

celcius = (5/9) * fahrenheit - 32
print("Suhu celcius adalah :",celcius, "C")

reamur = (4/9) * fahrenheit - 32
print("Suhu reamur adalah :",reamur, "R")

kelvin = (fahrenheit - 32) * 5/9 + 273.15
print("Suhu kelvin adalah :",kelvin,"K")

#Program Konversi Kelvin ke Satuan lain
print("\nProgram Konversi Temperatur\n")
kelvin = float(input("Masukkan Suhu dalam bentuk kelvin : "))
print("Suhu kelvin adalah :",kelvin, "K")

celcius = kelvin - 273.15
print("Suhu celcius adalah :",celcius, "C")

reamur = (4/5) * kelvin - 273.15
print("Suhu reamur adalah :",reamur, "R")

fahrenheit = (kelvin-32) * 9/5 - 273.15
print("Suhu fahrenheit adalah :",fahrenheit, "F")

print("")

