"""
IMPORTANT:

Expects a CSV formatted with one set of EQSQ responses per row:
PID in first column, followed by item responses ('Definitely Disagree', etc.)

"""

import csv

# collect filenames as user input
print "-------------------------------------------------------------------"
csv_filename = raw_input("Enter the full name of the CSV file containing your EQSQ responses:\n")
print 
new_filename = raw_input("Enter the desired full name of the CSV file for your score output:\n")
print

# create score file
with open(new_filename, 'wb') as score_csv:
    row = "PID,E_raw,E_standard,S_raw,S_standard,D,category\n"
    score_csv.write(row)


# open data file
with open(csv_filename) as eqsq_csv:
    data = csv.reader(eqsq_csv.read().splitlines())

    for row in data:

        # check if scores are valid
        if row.count('') >= 5:
            print "Invalid score: more than 5 answers incomplete"
            continue

        # populate a dictionary with item_label:item_value
        row_dict = {}

        for index, item in zip(range(0,56), row):
            if index == 0:
                row_dict['PID'] = item
            else:
                row_dict[index] = item

        # initialize a new score counter
        eq_score = 0
        sq_score = 0
        
        # iterate over items in dictionary and add up the score
        for item_label in row_dict:

            if item_label in [1, 6, 14, 18, 26, 28, 30, 31, 37, 42, 43, 45, 48, 52]:
                if row_dict[item_label] == 'Slightly Agree':
                    eq_score += 1
                elif row_dict[item_label] == 'Definitely Agree':
                    eq_score += 2

            elif item_label in [2, 4, 7, 9, 13, 17, 20, 23, 33, 36, 40, 53, 55]:
                if row_dict[item_label] == 'Slightly Disagree':
                    eq_score += 1
                elif row_dict[item_label] == 'Definitely Disagree':
                    eq_score += 2

            elif item_label in [5, 8, 10, 12, 19, 21, 24, 25, 29, 34, 35, 38, 39, 41, 44, 46, 49, 50]:
                if row_dict[item_label] == 'Slightly Agree':
                    sq_score += 1
                elif row_dict[item_label] == 'Definitely Agree':
                    sq_score += 2

            elif item_label in [3, 11, 15, 16, 22, 27, 32, 47, 51, 54]:
                if row_dict[item_label] == 'Slightly Disagree':
                    sq_score += 1
                elif row_dict[item_label] == 'Definitely Disagree':
                    sq_score += 2

        # calculate standardized scores
        E = (eq_score - 37.70)/54
        S = (sq_score - 24.11)/56
        D = (S-E)/2

        # determine category
        if D < -0.205:
            category = 'Extreme Type E'
        elif -0.205 <= D and D < -0.050:
            category = 'Type E'
        elif -0.050 <= D and D < 0.037:
            category = 'Type B'
        elif 0.037 <= D and D < 0.260:
            category = 'Type S'
        elif D >= 0.260:
            category = 'Extreme Type S'

        with open(new_filename, 'a') as score_csv:
            row = "%s,%r,%r,%r,%r,%r,%s\n" %(row_dict['PID'], eq_score, E, sq_score, S, D, category)
            score_csv.write(row)

print "Scoring complete."
print "-------------------------------------------------------------------"




