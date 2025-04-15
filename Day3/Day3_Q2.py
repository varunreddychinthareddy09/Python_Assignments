#Q2
def f_lst(data):
    if type(data) is str:
        return [int(num) for num in data.strip('()').split(',')]
    elif type(data) is list:  
        return [f_lst(item) for item in data]

input_data = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

output_data = f_lst(input_data)

print(output_data)