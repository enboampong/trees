def trees_hfld_approach():
    reference_period_deforestation_rates = [ ]
    reference_period_forest_covers = [ ]
    reference_period_emissions = [ ]
    annual_emissions = []
    annual_foregone_removals = []
    hfld_scores = [ ]
    iteration = 0
    
    carbon_stock = input("Kindly enter the Total Carbon Stock in above and below ground tree biomass : ")

    def get_reference_period_deforestation_rates():
        iteration = 0
        while len(reference_period_deforestation_rates) < 5:            
            reference_period_deforestation_rate = input("Kindly enter the reference period deforestation rate percentage value for year "+ str(iteration + 1) +" : ")
            if reference_period_deforestation_rate == '':
                reference_period_deforestation_rate = 0
            reference_period_deforestation_rates.append(reference_period_deforestation_rate)
            iteration += 1

    def get_reference_period_forest_covers(): 
        iteration = 0  
        while len(reference_period_forest_covers) < 5:            
            reference_period_forest_cover = input("Kindly enter the reference period forest cover value for year "+ str(iteration + 1)+" : ")
            if reference_period_forest_cover == '':
                reference_period_forest_cover = 0
            reference_period_forest_covers.append(reference_period_forest_cover)
            iteration += 1

    def get_reference_period_emissions(): 
        iteration = 0   
        while len(reference_period_emissions) < 5:
            reference_period_emission = input("Kindly enter the reference period emission value for year "+ str(iteration + 1)+" : ")
            if reference_period_emission == '':
                reference_period_emission = 0
            reference_period_emissions.append(reference_period_emission)
            iteration += 1

    def get_annual_emissions():
        iteration = 0
        while len(annual_emissions) < 5:
            annual_emission = input("Kindly enter the annual emission value for year "+ str(iteration + 1)+" : ")
            if annual_emission == '':
                annual_emission = 0
            annual_emissions.append(annual_emission)
            iteration += 1

    def get_annual_foregone_removals():
        iteration = 0
        while len(annual_foregone_removals) < 5:
            annual_foregone_removal = input("Kindly enter the annual foregone removal value for year "+ str(iteration + 1)+" : ")
            if annual_foregone_removal == '':
                annual_foregone_removal = 0
            annual_foregone_removals.append(annual_foregone_removal)
            iteration += 1

    get_reference_period_deforestation_rates()
    get_reference_period_forest_covers()
    get_reference_period_emissions()
    get_annual_emissions()
    get_annual_foregone_removals()
#========================================================================================================================================================
    while iteration < 5:
        hfld_score= (((int(reference_period_forest_covers[iteration])*100-50)/100) + (0.5- int(reference_period_deforestation_rates[iteration])*100))
        hfld_scores.append(hfld_score)
        if hfld_score < 0.5:
            threshold = " exceeds the threshold"
        else:
            threshold = " does not exceed the threshold"
        print("The HFLD score for reference year "+ str(iteration + 1) + " is" + str(hfld_score) + ". It "+  threshold)
        iteration += 1
    sum_scores=0
    for score in hfld_scores:
        sum_scores = sum_scores + score
    avg_hfld_score = sum_scores/len(hfld_scores)
    print ("The Average HFLD Score is :"+ str(avg_hfld_score))

#=========================================================================================================================================================
    sum_emissions = 0
    for emission in reference_period_emissions:
        sum_emissions = int(emission) + sum_emissions
    crediting_level = sum_emissions / 5
    hfld_crediting_level = (crediting_level + (avg_hfld_score * (0.0005 * int(carbon_stock))))
    print("The HFLD Crediting level is "+ str(hfld_crediting_level))

#=========================================================================================================================================================

trees_hfld_approach()
