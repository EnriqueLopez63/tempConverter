def tempMeth():
    cont = True

    while cont == True:
        inue = "q"

        usrTemp = "r"

        usrTempTyp = "q"

        usrName = input('What is your Name? ')

        while usrTempTyp != "c" and usrTempTyp != "f":
            usrTempTyp = input(usrName + ', c or f. ')

        while usrTemp.isdigit() == False:
            usrTemp = input('Okay ' + usrName + ', now what temprature is it? ')

        usrTemp = int(usrTemp)

        if usrTempTyp == 'c':
            usrTemp = (usrTemp * (9/5)) + 32
            print('The temprature in Farenheight is ' + str(usrTemp))
        elif usrTempTyp == 'f':
            usrTemp = (usrTemp - 32 ) * (5/9)
            print('The temprature in Celcius is ' + str(usrTemp))
        
        while inue != "y" and inue != "n":
            inue = input('Would you like to convert another temprature? Only type y or n. ')
            if inue == "y":
                cont = True
            elif inue == 'n':
                cont = False

