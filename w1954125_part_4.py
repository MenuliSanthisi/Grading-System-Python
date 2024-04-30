# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1954125

#Author name - Menuli Thalagala

#Date -16th November 2022


#list created for outcomes and marks 
outcomes = []

#marks dictionary stores the id_number and marks
marks = dict()

while True:
    id_number = input('Please enter student ID -')
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
            
    def sum_credits(Pass_CR, Defer_CR, Fail_CR):        
        return Pass_CR + Defer_CR + Fail_CR
    total = sum_credits(Pass, Defer, Fail)
    if total != 120:
        print('Total incorrect')
        continue
    results = Pass, Defer, Fail    #The result variable contains values of Pass,Defer and Fail which are appended to the outcome list
    while True:
        
        if Pass == 120 and Defer == 0 and Fail == 0:
            print('Progress')
            outcomes = str('Progress' + str(results))

        elif (Pass == 100 and Defer == 20 and Fail == 0)or(Pass == 100 and Defer == 0 and Fail == 20):
            print('Progress(module trailer)')
            outcomes = str('Progress(module trailer)' + str(results))


        elif (Pass == 80 and Defer == 40 and Fail == 0)or(Pass == 80 and Defer == 20 and Fail == 20)or(Pass == 80 and Defer == 0 and Fail == 40):
            print('Do not progress-module retriever')
            outcomes = str('Do not progress-module retriever' + str(results))
                
            
        elif (Pass == 60 and Defer == 60 and Fail == 0)or(Pass == 60 and Defer == 40 and Fail == 20)or(Pass == 60 and Defer == 20 and Fail == 40) or (Pass == 60 and Defer == 0 and Fail == 60):
            print('Do not progress-module retriever')
            outcomes = str('Do not progress-module retriever' + str(results))
        
            
        elif (Pass == 40 and Defer == 80 and Fail == 0)or(Pass == 40 and Defer == 60 and Fail == 20)or(Pass == 40 and Defer == 40 and Fail == 40)or(Pass == 40 and Defer == 20 and Fail == 60): 
            print('Do not progress-module retriever')
            outcomes = str('Do not progress-module retriever' + str(results))
               
                
        elif (Pass == 40 and Defer == 0 and Fail == 80)or(Pass == 20 and Defer == 20 and Fail == 80)or(Pass == 20 or Defer == 0 and Fail == 100):
            print('Exclude')
            outcomes = str('Exclude' + str(results))

        elif (Pass == 20 and Defer == 100 and Fail == 0)or(Pass == 20 and Defer == 80 and Fail == 20)or(Pass == 20 and Defer == 40 and Fail == 60)or(Pass == 20 and Defer == 60 and Fail == 40):             
            print('Do not progress-module retriever')
            outcomes = str('Do not progress-module retriever' + str(results))
                

        elif (Pass == 0 and Defer == 120 and Fail == 0)or(Pass == 0 and Defer == 100 and Fail == 20)or(Pass == 0 and Defer == 80 and Fail == 40)or(Pass == 0 and Defer == 60 and Fail == 60):            
            print('Do not progress-module retriever')
            outcomes = str('Do not progress-module retriever' + str(results))
                
        elif (Pass == 0 and Defer == 40 and Fail == 80)or(Pass == 0 and Defer == 20 and Fail == 100)or(Pass == 0 or Defer == 0 and Fail == 120):
                print('Exclude')
                outcomes = str('Exclude' + str(results))
                
        marks[id_number] = outcomes   #marks[id-number] returns the progression of the student which is assigned as outcomes 
        break
     
    def predict_progress(question):
        return question
    question =(str(input("\nWould you like to enter another set of data?\nEnter 'y' for yes and or 'q' to quit and view results: ")))
    if question == 'y':
        continue  
    elif question == 'q':
        break

for key,values in marks.items():        #key is id_number and value is the progression of the student 
    print(f'{key}: {values}',end ='')

               
      
