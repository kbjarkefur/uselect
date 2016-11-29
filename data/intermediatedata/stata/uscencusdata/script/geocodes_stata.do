
import delimited "C:\Users\Kristoffer\Documents\GitHub\uselectdata\data\intermediatedata\csv\uscencusbureau\geocode.csv", clear delimiter(comma) varnames(1) case(preserve)  
				
label var sumlvl 		"Summary Level. 10 is nation, 40 is state, 50 is county"
label var statecode 	"Official State Codes (FIPS)"
label var countycode 	"Official County Codes (FIPS)"
label var subcountycode "Official County Subdivision Codes (FIPS)"
label var otherareacode "Official Place Codes (FIPS), other types of areas"
label var citycode		"Offical Consolidtated City Codes (FIPS)"
label var areaname		"Area Name (including legal/statistical area description)"   
	  

compress	  

save "C:\Users\Kristoffer\Documents\GitHub\uselectdata\data\intermediatedata\stata\uscencusdata\geocodes.dta" , replace


*keep only county
keep if sumlvl == 50 

drop subcountycode otherareacode citycode

gen countyid = statecode*1000 + countycode

rename areaname	countyname 
label var 		countyname		"Name of county (or equivialent)" 

order countyid 
sum countyid, d

drop sumlvl countycode

compress	  

save "C:\Users\Kristoffer\Documents\GitHub\uselectdata\data\intermediatedata\stata\uscencusdata\countycodes.dta" , replace
