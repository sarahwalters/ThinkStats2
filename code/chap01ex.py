"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG FemResp data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the response frame.

    df: DataFrame
    """
    # Check to be sure this looks reasonable - it does; don't change anything.
    sortedByIndex = df.pregnum.value_counts().sort_index()
    # print(sortedByIndex)


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemResp()
    
    # Do pregnum records in FemResp match record counts by caseid from FemPreg?
    total = 0
    match = 0

    pregdf = nsfg.ReadFemPreg() # the FemPreg dataframe
    pregmap = nsfg.MakePregMap(pregdf) # key = caseid, val = array of records into pregdf
    for caseid,pregRecords in pregmap.iteritems():
    	counted = len(pregRecords) # from FemPreg
    	recorded = df.pregnum[df.caseid == caseid].values[0] # from FemResp
    	total = total + 1
    	if (counted == recorded):
    		match = match + 1

    assert(total==match)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
