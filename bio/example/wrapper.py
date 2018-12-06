'''
A test wrapper
'''

__author__ = "Anders Goncalves da Silva"
__copyright__ = "Copyright 2018, MDU PHL"
__email__ = "anders.goncalves@unimelb.edu.au"
__license__ = "MIT"


import sh
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

with open(snakemake.output[0], "w") as h:
    sh.cat(snakemake.input[0], _out=h)
