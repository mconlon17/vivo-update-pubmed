"""
    update-pubmed.py -- provide PubMed attributes for papers in VIVO

    Provide PMID, PMCID, Grants Cited and Full Text URL for papers in VIVO. Use
    five case logic to generate addition and subtraction RDF.


    Version 0.1 MC 2013-12-10
    --  Initial version.  inspect each paper in VIVO with a DOI.  Update PMID,
        PMCID, Grants Cited and Full text link assertions as needed.
    Version 0.2 MC 2013-12-21
    --  Treat PubMed keywords as concepts.  Link to existing concepts or add
        new ones as needed.

    To Do
    --  Standardize the grant number references  A01BC234567


"""

__author__      = "Michael Conlon"
__copyright__   = "Copyright 2013, University of Florida"
__license__     = "BSD 3-Clause license"
__version__     = "0.2"

import tempita
from datetime import datetime
from vivotools import rdf_header
from vivotools import rdf_footer
from vivotools import make_doi_dictionary
from vivotools import make_concept_dictionary
from vivotools import update_pubmed
import vivotools as vt

#
#  Start Here
#

srdf = "<!-- Subtraction RDF -->\n" + rdf_header()
ardf = "<!-- Addition RDF -->\n" + rdf_header()

print datetime.now(),"Making concept dictionary"
make_concept_dictionary()
print datetime.now(),"Concept dictionary has ",\
    len(vt.concept_dictionary),"entries"

print datetime.now(),"Making doi dictionary"
doi_dictionary = make_doi_dictionary()
print datetime.now(),"DOI dictionary has ",len(doi_dictionary),"entries"

i = 0
for doi in doi_dictionary.keys():
    i = i + 1
    
    # do 5000 publications in the specified range
                                
    if i < 30001:
        continue
    if i > 35000:
        break

    # update_pubmed does all the work.  It is a true update, so can be called
    # on any paper at any time.  Calls PubMed and considers PubMed
    # authoritative unless PubMed does not have a full text URI and VIVO does,
    # in which case the VIVO full text URI is retained. update_pubmed manages
    # concepts, adding them if necessary

    print i
    
    pub_uri = doi_dictionary[doi]
    try:
        [add,sub] = update_pubmed(pub_uri)
        ardf = ardf + add
        srdf = srdf + sub
    except:
        print "Exception for",pub_uri


print datetime.now(),"Finished"

add_file = open("add.rdf","w")
ardf = ardf + rdf_footer()
print >>add_file,ardf
add_file.close()

sub_file = open("sub.rdf","w")
srdf = srdf + rdf_footer()
print >>sub_file,srdf
sub_file.close()

