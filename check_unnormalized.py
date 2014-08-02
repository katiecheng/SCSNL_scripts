#-------------------------------------------------------------------------------
# Name:         check_unnormalized
# Purpose:      quickly open, rate, and make notes on unnormalized images
#
# Author:       Katie Cheng
#
# Created:      01/27/2014
# Licence:      Python 2.4.3
#-------------------------------------------------------------------------------
"""
A Python program to quickly open, rate, and make notes on unnormalized images

User defines a subject_list and corresponding session_list of the same length.
Script opens each unnormalized image sequentially.
User inputs ratings and notes.
Script returns a CSV file with columns: subject, session, rating, notes.
"""

def main():

    # Load subject and session txt files
    sub_file = open("/fs/apricot1_share1/MathFUNDamentals/preprocessing/sally/subjects_sessions/fmrisubjectlist.txt","r") # EDIT txt file name if desired
    sess_file = open("/fs/apricot1_share1/MathFUNDamentals/preprocessing/sally/subjects_sessions/mftasks.txt","r") # EDIT txt file name if desired

    # Read txt files and save in list format
    sub_list = sub_file.read().split('\n')
    sess_list = sess_file.read().split('\n')

    # Check sub and sess list length
    if not len(sub_list) == len(sess_list):
        print 'ERROR: subject list and session list are not the same length'

    # Import CSV module and create new CSV file
    import csv
    c = csv.writer(open("unnormalized_notes.csv", "wb")) # EDIT csv file name

    # Open each unnormalized image sequentially
    index = -1
    print

    for subject in sub_list:
        index += 1
        from subprocess import call
        filename = ('/fs/musk1/20'+subject[0:2]+'/'+subject+'/'+'fmri/'+
                    sess_list[index]+'/unnormalized/I.nii.gz')
        call(['fslview',filename])

        # displayed as script runs
        print subject, sess_list[index]
        rating = raw_input('    Rate as "good" or "bad": ') # EDIT rating system
        notes = raw_input('    Unnormalized notes: ')
        print

        # saves user input to scv
        c.writerow([subject, sess_list[index], rating, notes])

if __name__ == '__main__':
    main()
