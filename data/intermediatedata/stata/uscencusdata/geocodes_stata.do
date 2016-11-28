
import delimited C:\Users\Kristoffer\Documents\GitHub\uselectdata\data\intermediatedata\csv\uscencusbureau\cleancsv\geocode.csv, delimiter(comma) varnames(1) case(preserve) rowrange(6) clear 

label var sumlvl 		"Summary Level. 10 is nation, 40 is state, 50 is county"
label var statecode 	"Official State Codes (FIPS)"
label var countycode 	"Official County Codes (FIPS)"
label var subcountycode "Official County Subdivision Codes (FIPS)"
label var otherareacode "Official Place Codes (FIPS), other types of areas"
label var citycode		"Offical Consolidtated City Codes (FIPS)"
label var areaname		"Area Name (including legal/statistical area description)"   
	  
	  

