# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1954125

#Author name - Menuli Thalagala

#Date -16th November 2022




#Integer required , Out of total 

while True:    
    while True:
        def input_data(message, error_msg_1 = 'Integer required', error_msg_2 = 'Out of range'):  #message is the  parameter for Pass ,Defer and Fail 
            while True:
                 try:
                    value = int(input(message))
                 except ValueError:
                    print(error_msg_1)
                    continue
                 if 0<= value <=120 and value%20 == 0:
                    return value
                    break
                 else:
                    print(error_msg_2)
                    continue
        Pass =  input_data('Please enter your credit at pass: ')
        Defer = input_data ('Please enter your credit at defer: ')
        Fail =  input_data('Please enter your credit at fail: ')
        break
                
#Total incorrect       
    if sum ([Pass, Defer, Fail]) != 120:
        print('Total incorect')
        continue
      
    
    
        
    if Pass == 120 and Defer == 0 and Fail == 0:
        print('Progress')
    elif (Pass == 100 and Defer == 20 and Fail == 0)or(Pass == 100 and Defer == 0 and Fail == 20):
        print('Progress(module trailer)')

    elif (Pass == 80):
        if (Defer == 40 and Fail == 0)or(Defer == 20 and Fail == 20)or(Defer == 0 and Fail == 40):
            print('Do not progress-module retriever')
            
    elif Pass == 60:
        if (Defer == 60 and Fail == 0 )or(Defer == 40 and Fail == 20)or(Defer == 20 and Fail == 40) or (Defer == 0 and Fail == 60):
            print('Do not progress-module retriever')
            
    elif Pass == 40:
        if(Defer == 80 and Fail == 0)or(Defer == 60 and Fail == 20)or(Defer == 40 and Fail == 40)or(Defer == 20 and Fail == 60):
            print('Do not progress-module retriever')
            
    if (Pass == 40 and Defer == 0 and Fail == 80)or(Pass == 20 and Defer == 20 and Fail == 80)or(Pass == 20 and Defer == 0 and Fail == 100):          
        print('Exclude')

    elif Pass == 20:
        if (Defer == 100 and Fail == 0)or(Defer == 80 and Fail == 20)or(Defer == 40 and Fail == 60)or(Defer == 60 and Fail == 40):
            print('Do not progress-module retriever')

    elif Pass == 0:
        if (Defer == 120 and Fail == 0)or(Defer == 100 and Fail == 20)or(Defer == 80 and Fail == 40)or(Defer == 60 and Fail == 60):
            print('Do not progress-module retriever')
        elif (Pass == 0 and Defer == 40 and Fail == 80)or(Pass == 0 and Defer == 20 and Fail == 100)or(Pass == 0 and Defer == 0 and Fail == 120):
            print('Exclude')
    break
    
 
