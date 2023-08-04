def trees_hfld_approach():
    reference_period_deforestation_rates = [ ]
    reference_period_forest_covers = [ ]
    reference_period_emissions = [ ]
    annual_emissions = []
    annual_foregone_removals = []
    hfld_scores = [ ]
    percentage_inceases = []
    deduction_values = []
    emission_reductions = []
    iteration = 0
    penalties = []
    total_emission_reductions = []
    
    carbon_stock = input("Kindly enter the Total Carbon Stock in above and below ground tree biomass : ")

    def get_reference_period_deforestation_rates():
        iteration = 0
        print("----------------------------------------------------------------------")
        while len(reference_period_deforestation_rates) < 5:            
            reference_period_deforestation_rate_input = input("Kindly enter the reference period deforestation rate percentage value for year "+ str(iteration + 1) +" : ")
            if reference_period_deforestation_rate_input:
                reference_period_deforestation_rate = (float(reference_period_deforestation_rate_input)/100.00)
            else:
                reference_period_deforestation_rate = 0
            reference_period_deforestation_rates.append(reference_period_deforestation_rate)
            iteration += 1
        
        
    def get_reference_period_forest_covers(): 
        iteration = 0  
        print("----------------------------------------------------------------------")
        while len(reference_period_forest_covers) < 5:            
            reference_period_forest_cover_input = input("Kindly enter the reference period forest cover value for year "+ str(iteration + 1)+" : ")
            if reference_period_forest_cover_input :
                reference_period_forest_cover = (float(reference_period_forest_cover_input)/100.00)
            else:
                reference_period_forest_cover = 0
            reference_period_forest_covers.append(reference_period_forest_cover)
            iteration += 1
        
        
    def get_reference_period_emissions(): 
        iteration = 0   
        print("----------------------------------------------------------------------")
        while len(reference_period_emissions) < 5:
            reference_period_emission = input("Kindly enter the reference period emission value for year "+ str(iteration + 1)+" : ")
            if reference_period_emission == '':
                reference_period_emission = 0
            reference_period_emissions.append(reference_period_emission)
            iteration += 1

    def get_annual_emissions():
        iteration = 0
        print("----------------------------------------------------------------------")
        while len(annual_emissions) < 5:
            annual_emission = input("Kindly enter the annual emission value for year "+ str(iteration + 1)+" : ")
            if annual_emission == '':
                annual_emission = 0
            annual_emissions.append(annual_emission)
            iteration += 1
        

    def get_annual_foregone_removals():
        iteration = 0
        print("----------------------------------------------------------------------")
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
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while iteration < 5:
        hfld_score= (((float(reference_period_forest_covers[iteration])*100.00-50.00)/100.00) + (0.5- float(reference_period_deforestation_rates[iteration])*100.00))
        hfld_scores.append(hfld_score)
        if hfld_score > 0.5:
            threshold = " exceeds the threshold"
        else:
            threshold = " does not exceed the threshold"
        print("The HFLD score for reference year "+ str(iteration + 1) + " is  " + str(hfld_score) + " . It "+  threshold)
        iteration += 1
    sum_scores=0
    for score in hfld_scores:
        sum_scores = sum_scores + score
    avg_hfld_score = sum_scores/len(hfld_scores)
    
    print ("The Average HFLD Score is :"+ str(avg_hfld_score))

#========================================================================================================================================================
    def get_crediting_level():
        sum_emissions = 0
        for emission in reference_period_emissions:
            sum_emissions = float(emission) + sum_emissions
        crediting_level = sum_emissions / 5
        return crediting_level

#=========================================================================================================================================================
    def get_hfld_crediting_level():  
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
        crediting_level =  get_crediting_level()
        hfld_crediting_level = (crediting_level + (avg_hfld_score * (0.0005 * float(carbon_stock))))
        print("The HFLD Crediting level is "+ str(hfld_crediting_level))
        return hfld_crediting_level
    #get_hfld_crediting_level()
    hfld_crediting_lev = get_hfld_crediting_level()
#=========================================================================================================================================================
    def get_percentage_increase():
        iteration = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        crediting_level = get_crediting_level()
        while iteration < 5:
            if hfld_crediting_lev:
                percentage_increase = ((float(annual_emissions[iteration]) - float(crediting_level))/ float(crediting_level))
                print("The Percentage increase for Year " + str(iteration+1) + " is : " + str(percentage_increase*100)+"%")
                percentage_inceases.append(percentage_increase)      
            else :
                percentage_increase = 0  
            iteration += 1
    

#==========================================================================================================================================================
    def get_deduction_value():
        iteration = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while iteration < 5:
            
            if float(percentage_inceases[iteration]) < 0.15 :
                deduction_value = 0
            else:
                if float(percentage_inceases[iteration]) < 0.35 :
                    deduction_value = 0.15
                else: 
                    if float(percentage_inceases[iteration]) < 0.55 :
                        deduction_value = 0.25
                    else:
                        if float(percentage_inceases[iteration]) < 0.75 :
                            deduction_value = 0.35
                        else:
                            deduction_value = 1
            print("The Deduction Value for Year " + str(iteration+1) + " is : " + str(deduction_value*100)+ "%")
            deduction_values.append(deduction_value)
            iteration += 1

    
#  ==========================================================================================================================================================

    def get_emission_reduction():
        iteration = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while iteration < 5:
            emission_reduction = (hfld_crediting_lev - float(annual_emissions[iteration]))
            emission_reductions.append(emission_reduction)
            print("The emission reduction for Year " + str(iteration+1) + " is : " + str(emission_reduction))
            iteration += 1
        
#============================================================================================================================================================            
    
    def get_penalty():
        iteration = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while iteration < 5:
            penalty = ((float(emission_reductions[iteration]) + float(annual_foregone_removals[iteration])) * float(deduction_values[iteration]))
            penalties.append(penalty)
            print("The HFLD Penalty for Year " + str(iteration+1) + " is : " + str(penalty))
            iteration += 1
            
#============================================================================================================================================================            
            
    def get_hfld_total_emission_reduction():
        iteration = 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while iteration < 5:
            total_emission_reduction = ((float(emission_reductions[iteration]) + float(annual_foregone_removals[iteration])) - float(penalties[iteration]))
            total_emission_reductions.append(total_emission_reduction)
            print("The Total HFLD Emissions Reductions for Year " + str(iteration+1) + " is : " + str(total_emission_reduction))
            iteration += 1
     
    get_percentage_increase()
    get_deduction_value()
    get_emission_reduction()  
    get_penalty()
    get_hfld_total_emission_reduction() 
    
trees_hfld_approach()
