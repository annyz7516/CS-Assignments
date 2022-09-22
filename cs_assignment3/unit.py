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

# print(read_csv('students.csv'))
#print(len(read_csv('students.csv')))

students = read_csv('students.csv')
#print(students)

# def get_totals(data):
#     total_list = []
#     for pairing in data:
#         total = 0
#         for i in range(1, len(pairing)):
#             total += pairing[i]
#         total_list.append(total)
#     return (total_list)
#
# def top_student_basic(data):
#     total_score_list = get_totals(data)
#     high_score = 0
#     high_score_index = 0
#     for index in range(len(total_score_list)):
#         if total_score_list[index] > high_score:
#             high_score_index = index
#             high_score = total_score_list[index]
#     return data[high_score_index][0]
#
# def top_student_intermediate(data):
#     high_score_ID_list=[]
#     total_list = get_totals(data)
#     for i in range(len(total_list)):
#         if total_list[i] == high_score(data):
#             high_score_ID_list.append(data[i][0])
#     return high_score_ID_list
#
#
# def high_score(data):
#     total_score_list = get_totals(data)
#     high_score = 0
#     for index in range(len(total_score_list)):
#         if total_score_list[index] > high_score:
#             high_score = total_score_list[index]
#     return high_score
#
#
def high_score(data):
    total_score_list = get_totals(data)
    print(total_score_list)
    highest_score = 0
    for index in range(len(total_score_list)):
        if total_score_list[index] > highest_score:
            highest_score = total_score_list[index]
    return highest_score

def higher_practical_data(data):
    higher_data = []
    for i in range(len(data)):
        higher_data.append(data[i][0:3])
        if data[i][-1] <= data[i][-2]:
            higher_data[i].append(data[i][-2])
        else:
            higher_data[i].append(data[i][-1])
    return higher_data

def get_totals(data):
    total_list = []
    new_data = higher_practical_data(data)
    for stud_score_list in new_data:
        total = 0

        for i in range(1, len(stud_score_list)):
            total += stud_score_list[i]
        total_list.append(total)
    return total_list
print(get_totals(students))


def top_student_basic(data):
    total_score_list = get_totals(data)
    high_score = 0
    high_score_index = 0
    for index in range(len(total_score_list)):
        if total_score_list[index] > high_score:
            high_score_index = index
            high_score = total_score_list[index]
    return data[high_score_index][0]
print(top_student_basic(students))

def top_student_intermediate(data):
    high_score_ID_list=[]
    total_list = get_totals(data)
    for i in range(len(total_list)):
        if total_list[i] == high_score(data):
            high_score_ID_list.append(data[i][0])
    return high_score_ID_list
print(top_student_intermediate(students))

# Also, define any other "helper" functions here #

def high_score(data):
    total_score_list = get_totals(data)
    print(total_score_list)
    highest_score = 0
    for index in range(len(total_score_list)):
        if total_score_list[index] > highest_score:
            highest_score = total_score_list[index]
    return highest_score

print(high_score(students))
