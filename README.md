# econ_metadata
This project scrapes and analyzes metadata from EconLit for all papers published in the 2010s. I am motivated to find departments which are especially productive in fields and subfields which match my research interests. Initial results are being used for my Fall 2021 Ph.D. application statements of purpose.

# Overview

JEL codes are awesome. The goal here is to get the JEL codes for every paper published in the 2010s, along with authors, author affiliation, journal name, etc. Plenty of schools says "we're the best for IO or mechanism design or urban or whatever", with this data, we can actually see which departments publish the most in which fields! 

# Data

These data are pulled from the AEA's EconLit database, which I have access to through the University of Maryland up until 2020-12-31. The code to scrape the metadata uses beautifulsoup on PhantomJS to parse for the relevant fields. In total, I collect data from 2010-01-01 to present day. For each journal article, the scraper collects:

* Title
* Authors
* Author affiliations
* Date published
* Publication
* Publication type
* Keywords
* JEL codes
* Ephemera

For the time period, this is more than half a million journal articles. The full list of journals included is available on EconLit.

# Processing

For every article (identified by unique article identifier), we have all of the associated JEL codes and keywords. The JEL codes were stored as a string delimited by semicolons. In order to turn it into a proper edgelist between article and JEL code nodes, it had to be transformed so that each row of the jel column contains exactly one JEL classification code.

This transformed version was panel set, with each row unqiuely identified by a) journal article, b) author/affiliation, and c) JEL code. A similar exercize was performed with the keywords.

## Authors and Author Affiliations

EconLit neither standardizes the names of the authors, nor standardizes the names of the departments. This was resolved with desk research and fuzzy matching in Python. Some arbitrary distinctions remained: for example, EconLit does not distinguish between the University of Paris campuses, so all University of Paris campuses were counted as one institution. Similarly, universities are the top level of affiliation identification. Within universities, department and research center are identified where possible. For individual scholars, we were able to match almost all with their affiliation and work products; some outlying cases included departments or authors with identical names. 

## Publication Weighting

**If you were directed here by my Ph.D. application, please note that those figures on department productivity are not weighted by journal rankings.** 

To weight by influence, I use [IDEAS aggregate journal ranking](https://ideas.repec.org/top/top.journals.all10.html) over the last ten years (same period as my analysis).



