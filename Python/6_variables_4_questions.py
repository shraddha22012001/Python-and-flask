def num_square(num):
    print(input_num)
    square= num * num

    return square


input_num = 101

if input_num > 100:
    result = num_square(5)


print(result)


'''
Q1. What is the scope of num,square, input_num, result?
Ans-1 : num -> num is a local variable. Whose scope is only inside the function.
square -> square is also a local variable. Whose scope is only inside the function.
input_num -> input_num is a global variable. which can be used inside or outside the function.
result -> num is also a local variable. Whose scope is only inside the if condition.


Q2. What is the lifetime of each variable? When will they be created and destroyed?
Ans-2 : 1->Local variables including function parameters have a life from the start of the execution of 
the function to the end of execution - i.e. the end of the function or the return statement.

2 -> Global variables live from when the module is imported until 
the end of the application - unless the variable is explicitly deleted.


Q3. What would happen if input_num had a value of less than 100?
Ans-3 : if input_num is less than 100 then it will throw an error that 
'result is not defined'. If we declare result out of function like 'result=0'
then the program will be execute and print 0.


Q4. What would be the scope and value of `result` if input_num has a value of less than 100?
Ans-4 : Firstly 'result' is a local variable. The scope of result is valid only inside function. 
And if the input_num value is less than 100 then it'll throw an error that 'result' is not defined.
'''