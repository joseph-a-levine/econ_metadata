*------------------Header---------------------
* Loading data from JEL codes
* load_econlit.do
* Last edited date: 2020-11-29
* Last edited by: Joseph Levine
*---------------------------------------------




*------------------Outline--------------------
/*
*	Outline
*	Program set-up
*	Part 1: 
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

log using "$temppath\2_practice_$S_DATE.txt", replace text   // Open log file


*----------------------------------------------------------------


clear





import delimited "$datapath\10_14_all.csv"


drop in 1/2


rename v2 	title
rename v3 	author
rename v4 	author_aff
rename v5 	publication
rename v6 	pub_date
rename v7 	JEL_codes
rename v8 	ID_1
rename v9 	pub_type
rename v10 	ID_2
rename v11 	ID_3







clear all
log close

exit
