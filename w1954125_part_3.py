# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1954125

#Author name - Menuli Thalagala

#Date -16th November 2022


#count variables are used to count the number of outcomes in each progression 
count_1 = 0    #count-1 for Progress
count_2 = 0    #count-2 for module trailer
count_3 = 0    #count_3 for module retriever 
count_4 = 0    #count_4 for Exclude

#List created for each outcome
Progress =[]
module_trailer =[]
Module_retriever =[]
Exclude =[]

#Integer required , Out of total
while True:
    while True:
        def input_data(message, error_msg_1 = 'Integer required', error_msg_2 = 'Out of range'):
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
        Pass =  input_data('Enter your total PASS credits: ')
        Defer = input_data ('Enter your total DEFER credits: ')
        Fail =  input_data('Enter your total FAIL credits: ')
        break
                
       
#Total incorrect

        
    def sum_credits(Pass_CR, Defer_CR, Fail_CR):        
        return Pass_CR + Defer_CR + Fail_CR
    total = sum_credits(Pass, Defer, Fail)
    if total != 120:
        print('Total incorrect')
        
            
            
                    
       
#Progressive outcomes
            
    while True:
        
        if Pass == 120 and Defer == 0 and Fail == 0:
            print('Progress')
            count_1 += 1
            values_1 =Pass,Defer,Fail   #value_1 contains the marks to get the outcome as Progress,later appended to the Progress list
            Progress.append(values_1)

        elif (Pass == 100 and Defer == 20 and Fail == 0)or(Pass == 100 and Defer == 0 and Fail == 20):
            print('Progress(module trailer)')
            count_2 += 1
            value_2 = Pass, Defer, Fail   #value_2 contains the marks to get the outcome as Module trailer,later appended to the module_trailer  list
            module_trailer.append(value_2)


        elif (Pass == 80):
            if (Defer == 40 and Fail == 0)or(Defer == 20 and Fail == 20)or(Defer == 0 and Fail == 40):
                print('Do not progress-module retriever')
                count_3 += 1
                value_3 = Pass,Defer,Fail  #value_3 contains the marks to get the outcome as Module retriever,later appended to the Module_retriever list 
                Module_retriever.append(value_3)
            
        elif Pass == 60:
            if (Defer == 60 and Fail == 0 )or(Defer == 40 and Fail == 20)or(Defer == 20 and Fail == 40) or (Defer == 0 and Fail == 60):
                print('Do not progress-module retriever')
                count_3 += 1
                value_3 = Pass,Defer,Fail
                Module_retriever.append(value_3)
        
            
        elif Pass == 40:
            if(Defer == 80 and Fail == 0)or(Defer == 60 and Fail == 20)or(Defer == 40 and Fail == 40)or(Defer == 20 and Fail == 60):
                print('Do not progress-module retriever')
                count_3 += 1
                value_3 = Pass,Defer,Fail
                Module_retriever.append(value_3)
                
        if (Pass == 40 and Defer == 0 and Fail == 80)or(Pass == 20 and Defer == 20 and Fail == 80)or(Pass == 20 and Defer == 0 and Fail == 100):
            print('Exclude')
            count_4 += 1
            value_4 = Pass,Defer,Fail    #value_4 contains the marks to get the outcome as Exclude,later appended to the Exclude list
            Exclude.append(value_4)

        elif Pass == 20:
            if (Defer == 100 and Fail == 0)or(Defer == 80 and Fail == 20)or(Defer == 40 and Fail == 60)or(Defer == 60 and Fail == 40):
                print('Do not progress-module retriever')
                count_3 += 1
                value_3 = Pass,Defer,Fail
                Module_retriever.append(value_3)
                

        elif Pass == 0:
            if (Defer == 120 and Fail == 0)or(Defer == 100 and Fail == 20)or(Defer == 80 and Fail == 40)or(Defer == 60 and Fail == 60):
                print('Do not progress-module retriever')
                count_3 += 1
                value_3 = Pass,Defer,Fail
                Module_retriever.append(value_3)
                
            elif (Pass == 0 and Defer == 40 and Fail == 80)or(Pass == 0 and Defer == 20 and Fail == 100)or(Pass == 0 or Defer == 0 and Fail == 120):
                print('Exclude')
                count_4 += 1
                value_4 = Pass,Defer,Fail
                Exclude.append(value_4)
        break

#Predict Progress for multiple times
    
    def predict_progress(question):
        return question
    question =(str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes and or 'q' to quit and view results: ")))
    if question == 'y':
        continue  
    elif question == 'q':
        

        
#Histogram

        print("---------------------------------------------------------------")
        print("Histogram")
        print('Progress',count_1,':','*'*count_1)
        print('Trailer',count_2,':','*'*count_2)
        print('Retriever',count_3,':','*'*count_3)
        print('Exclude',count_4,':','*'*count_4)
        total = count_1 + count_2 + count_3 + count_4
        print(total,'outcomes in total')
            
#Part 2(List extension)

            
    def results(grade_1 = Progress, grade_2 = module_trailer, grade_3 = Module_retriever, grade_4 = Exclude):    
        
        for i in grade_1:
            print('Progress -',i)          
        for i in grade_2:
            print('Progress(module trailer) - ',i)            
        for i in grade_3:
            print('Module retriever -',i)          
        for i in grade_4:
            print('Exclude -',i)        
    results()    
    break
#Part 3
#File Extension

file = open('Progressive.txt', 'w')       #All the outcomes are printed in the file named 'Progressive'
for line in Progress:       #line is the variable name used instead of i
    file.write('Progress - ' + str(line)+'\n')
for line in  module_trailer:
    file.write('Progress(module trailer)- '+ str(line) +'\n')
for line in Module_retriever:
    file.write('Module retriever- '+ str(line) +'\n')
for line in Exclude:
    file.write('Exclude - '+ str(line) +'\n')
file.flush()
file.close()


