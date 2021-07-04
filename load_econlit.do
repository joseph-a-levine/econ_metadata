*------------------Header---------------------
* Loading data from JEL codes
* load_econlit.do
* Last edited date: 2020-12-30
* Last edited by: Joseph Levine
*---------------------------------------------




*------------------Outline--------------------
/*
*	Outline
*	Program set-up
*	Part 1: Load scraped data
*	Part 2: 
*	Part 3: 
*	Part 4: 
*/
*---------------------------------------------




*-------------------Program set-up-------------------------------

version 15		  // Set version number for backward compatibility
set more off      // Disable partitioned output 
pause on		  // Enables pause, to assist with debugging	
clear all  		  // Start with a clean slate
set linesize 100  // Line size limit to make output/logs more readable
set mem 15m		  // Sets usable memory in the evironment /*\ MUST CHECK FILE SIZE \*/
macro drop _all   // Clear all macros
cap log close     // Close any open log files


/*\ ATTENTION \*/
* Must set file paths below, if you want this to work 

global datapath "~\Dropbox\Research\JEL_codes\Data"     
			// Set datapath
global temppath "~\Dropbox\Research\JEL_codes\Temp"     
			// Set temppath
global resultspath "~\Dropbox\Research\JEL_codes\Results"  
			// Set resultspath



*----------------------------------------------------------------


clear


import delimited "$temppath/JELs_joined_16-19_affs.csv"


gen jel_field = substr(jel, 1,1)
gen jel_subfield = substr(jel, 1,3)

drop if jel == "unclassified"

gen year = real(substr(date,-4,4))

*codebook affiliation
* holy cow, 94k affiliations. not terrible 
replace affiliation = trim(affiliation)
* down to 74k affiliations

* ID for reclink 
gen idmaster=_n

save "$datapath/jel_analysis_16-19", replace 

preserve 
import excel "$temppath/ideas_students_inst_standardized_names.xlsx", sheet("Sheet1") firstrow clear

* ID for reclink
gen idusing=_n

rename name2 affiliation

tempfile ideas_inst
save `ideas_inst',replace
restore

keep if year == 2019

timer on 1
reclink affiliation using `ideas_inst', idm(idmaster) idu(idusing) gen(score)
timer off 1
/*
RESULTS

* This uses the raw ideas name, took about 50 minutes for JUST 2019 papers. *
Observations:  Master N = 383866    C:\Users\jable\AppData\Local\Temp\ST_139a4_000002.tmp N= 550 
  Unique Master Cases: matched = 73404 (exact = 252), unmatched = 310462
* result saved to: "$temppath/reclink_ideas_name_no_std"
================================================================================
* This was using the names_2 variable. Took a very long time for just 2019 papers. Will time going forward
Observations:  Master N = 383866    C:\Users\jable\AppData\Local\Temp\ST_139a4_000002.tmp N= 550 
  Unique Master Cases: matched = 96933 (exact = 4738), unmatched = 286933
 * result saved to: "$temppath/reclink_ideas_name_std1"


*/

e

clear all

exit