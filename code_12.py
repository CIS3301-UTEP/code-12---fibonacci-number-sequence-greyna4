def get_fibonacci_number(position):
    if position == 1 or position == 2:
        return 1
    elif position <= 0: 
        print ("End of recursion")
        pass #does not return anything
    else: 
        return ((get_fibonacci_number (position-1 )) + (get_fibonacci_number(position-2) ))



def get_fibonacci_number_sequence(number):
    sequence_list = []
    for i in range(0, number):
        #print (i +1).append
        sequence_list.append(get_fibonacci_number(i + 1))
    
    return sequence_list



if __name__ == "__main__":
    #pass #Remove this line and insert your code to test your Fibonacci function here


#print(get_fibonacci_number(5))

    print(get_fibonacci_number_sequence(10))

#a sequence of numbers that results from the calculation of the precedent numbers (1,1,2,3,5,8,13)
#if n=1 or n=2 return 1
#if n=0 or lower do not return anything
#else
#fibonacci number -1) + (fibonacci number-2)