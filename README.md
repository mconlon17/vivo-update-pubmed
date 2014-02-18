# Updating PubMed Facts in VIVO
December 10, 2013

## The Opportunity

Papers can come into VIVO by a number of different paths – hand entry, Thomson-Reuters ingest, PubMed, CrossRef and others.  Papers can be identified uniquely by DOI (Document Object Identifer).  PubMed has additional attributes that have high value to people using VIVO.  Specifically:

    1. PubMedID – the ID of the paper as assigned by PubMed.  This is useful for PubMed related searches
    2. PubMedCentral ID – this this the ID of the paper in PubMedCentral, the open access archive of the National Library of Medicine
    3. NIH Manuscript ID – this ID is assigned by the National Library of Medicine to all manuscripts to be processed.
    4. Keywords – these are standard text description of the mesh terms associated with the paper.
    5. Abstract – the public abstract of the paper.
    6. Grants cited in the paper.  Papers often cite funding sources.  PubMed records the NIH grants that were cited in the paper.  A paper may have multiple grants cited. Linking the paper to the grants that funded it provides enormous value to the administrative users of VIVO.
    7. The URL of the full text of the paper.  This provides direct access to the paper itself.  Linking the VIVO entry to the full text of the paper creates extraordinary value for the research user of VIVO.

## Concept Management

Keywords are entered as concepts in VIVO.  A dictionary of existing concepts is constructed at the outset.  As keywords are found in PubMed, they are looked up in VIVO.  If found, the paper is linked to the concept (hasSubjectArea), if not found, the concept is added and then the paper is linked to her new concept.  Concepts are simple skos:Concept entities with uri and label.  Each label is a MESH term label.  A future process can resolved concept labels to actual mesh entities. 

## The Approach

    1.	Make a dictionary of all papers by DOI. Takes about two minutes for 40,000 papers and provides a translation table from DOI to VIVO URI.
    2.	For each paper
	    1.	Query the paper to get the  attributes as they exist in VIVO.
	    1.	Make an Entrez call to get the attributes from PubMed.  Clean the attributes (strip excess punctuation and whitespace)
	    1.	For each attribute
		    1.	If there is no value in VIVO for the attribute, assert the new value
		    1.	If there is a value in VIVO, Determine if the value in VIVO is the same as the VIVO in PubMed (key string match).  If so, do nothing
            1.	If not
	            1.	Drop the existing value
	            1.	Assert the new value
	3.	Print subtraction RDF and addition RDF
	4.	Review the reports and if approved, subtract the subtraction RDF and add the addition RDF.
	5.	The report can be sent to managers and archived as a record of what was done.

## Notes

	1.	The approach assumes the papers are already in VIVO.  Separate processes add papers to VIVO (manual entry of vitaes, spreadsheet uploads, automated mining of PubMed, Thomson-Reuters, SCOPUS, CrossRef).  These are described elsewhere.
	2.	The approach requires two Entrez calls for each paper in VIVO -- one to get the PMID from the DOI, and one to get attributes for the paper from the PMID.  5,000 papers can be run in about 3 hours, generating 250,000 lines of RDF.  
	3.	We would expect that the Update PubMed attribute script is run every month or so. Regardless of the source of the paper ingest to VIVO, any paper with a DOI will have its PubMed values reviewed and updated or added as needed.

## To Do
    1. Some Entrez return sets appear to nest deeper than expected by the code.  See, for example 10.1016/j.jns.2013.06.033.  This paper has keywords, but they are not found by the current code.  
