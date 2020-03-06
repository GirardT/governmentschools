#########################################################################################################
#   Program Name : dbprep.py                                                   #
#   Program Description:                                                                                #
#   This program prepares a SQLite table containing data about government school locations and          #
#   student enrolment numbers in NSW.                                                                   #
#   Source: https://data.cese.nsw.gov.au/data/dataset/nsw-public-schools-master-dataset                 #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 01/03/2020            Girard Andrew Tabanag         #
#                                                                                                       #
#########################################################################################################

import os

os.system('python csv_to_sqlite.py -f master_dataset.csv')
