
import unittest

def read_csv(csv_file_name):					        	  		  	 		 	
    '''					        	  		  	 		 	
    Reads the csv file and returns a list of 
    student records
    '''					        	  		  	 		 	
    data = [] 
    with open(csv_file_name, 'r') as f:
        next(f)
        for line in f:
            record = []
            for token in line.strip().split(','):
                if token.isdigit():
                    record.append(int(token))
                else:
                    record.append(token)
            data.append(record)
    return data

class Tester(unittest.TestCase):
    def test_get_totals(self):
        students = read_csv('students.csv')
        expected = [234, 147, 192, 270, 248, 270, 270]
        totals = get_totals(students)
        self.assertListEqual(totals, expected)

    def test_top_student_basic(self):
        students = read_csv('students.csv')
        self.assertEqual(top_student_basic(students), 'S2')

    def test_top_student_intermediate(self):
        students = read_csv('students.csv')
        top_students = top_student_intermediate(students)
        expected = ['S2', 'S8', 'S6']
        self.assertListEqual(top_students, expected)

def example_function(data):					        	  		  	 		 	
    '''					        	  		  	 		 	
    Return a list containing assignment 1 marks,
    in order of occurrence
    '''					        	  		  	 		 	
    result = []
    for item in data:
        # item itself is a list, holding different fields
        # for one student, first field (index 0) is ID, 
        # second field (index 1) is assignment 1 mark
        result.append(item[1])
    return result

# Do not modify anything above this comment

##################################################
#         Define the three functions here        #
def get_totals(data):
    total_list = []
    new_data = higher_practical_data(data)
    for stud_score_list in new_data:
        total = 0
        for i in range(1, len(stud_score_list)):
            total += stud_score_list[i]
        total_list.append(total)
    return total_list

def top_student_basic(data):
    total_score_list = get_totals(data)
    high_score = 0
    high_score_index = 0
    for index in range(len(total_score_list)):
        if total_score_list[index] > high_score:
            high_score_index = index
            high_score = total_score_list[index]
    return data[high_score_index][0]

def top_student_intermediate(data):
    high_score_ID_list=[]
    total_list = get_totals(data)
    for i in range(len(total_list)):
        if total_list[i] == high_score(data):
            high_score_ID_list.append(data[i][0])
    return high_score_ID_list

# Also, define any other "helper" functions here #
def higher_practical_data(data):
    higher_data = []
    for i in range(len(data)):
        higher_data.append(data[i][0:3])
        if data[i][-1] <= data[i][-2]:
            higher_data[i].append(data[i][-2])
        else:
            higher_data[i].append(data[i][-1])
    return higher_data

def high_score(data):
    total_score_list = get_totals(data)
    highest_score = 0
    for index in range(len(total_score_list)):
        if total_score_list[index] > highest_score:
            highest_score = total_score_list[index]
    return highest_score

##################################################

# Do not modify anything below this comment

if __name__ == '__main__':
    records = read_csv('students.csv')
    a1marks = example_function(records)
    print("Assignment 1 marks:",a1marks)
    unittest.main()

