



def trees_crediting_level_approach():
    iteration = 0
    iteration2 = 0
    crediting_level = 0
    emissions = []
    total_emissions = 0
    number_of_years = len(emissions)
    while number_of_years <= 5:
        emission = input("Kindly enter the emission value for year "+ str(iteration +1) + ": ")
        if emission == '':
            emission = 0
        emissions.append(int(emission))
        iteration +=1
    for emission in emissions:
        total_emissions +=emission
    crediting_level = total_emissions/number_of_years
    print("The Trees Crediting Level for the period of ", number_of_years , " years is" , crediting_level)

    while iteration2 < number_of_years:
        print("The Annual Emmission Reduction for year", (iteration2 + 1) ,"is " , (crediting_level - emissions[iteration2]))
        iteration2 +=1
    return 0

trees_crediting_level_approach()



