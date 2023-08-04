def trees_crediting_level_approach():
    period_emissions=[]
    annual_emissions=[]
    
    def get_reference_period_emissions():
        iteration=0
        print("----------------------------------------------------------------------")
        while iteration < 5:
            period_emission = input("Kindly enter the emission value for year "+ str(iteration+1)+ " : ")
            period_emissions.append(float(period_emission))
            iteration += 1

    def get_annual_emissions():
        iteration = 0
        print("----------------------------------------------------------------------")
        while iteration < 5:
            annual_emission = input("kindly enter the annual emission for year "+ str(iteration+1)+ " : ")
            annual_emissions.append(annual_emission)
            iteration +=1
    
    def get_crediting_level():
        sum_emissions = 0
        for emission in period_emissions:
            sum_emissions = float(emission) + sum_emissions
        crediting_level = (sum_emissions / 5)
        return crediting_level
    
    def get_annual_emission_reductions():
        iteration = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("The Crediting level is : "+ str(get_crediting_level()))
        while iteration < 5:
            annual_emission_reduction = get_crediting_level() - float(annual_emissions[iteration])
            print("_________________________________________________________________________")
            print("The Annual Emmission Reduction for year "+ str(iteration + 1) +" is :    " + str(get_crediting_level() - float(annual_emissions[iteration])))
            iteration += 1
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    get_reference_period_emissions()
    get_annual_emissions()
    get_annual_emission_reductions()       
    
trees_crediting_level_approach()



