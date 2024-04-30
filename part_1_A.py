# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: w1954125

#Author name - Menuli Thalagala

#Date -16th November 2022



#Predic progression outcome

Pass = int(input('Please enter your credit at pass: '))
Defer = int(input('Please enter your credit at defer: '))
Fail = int(input('Please enter your credit at fail: '))

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

    if (Pass == 40 and Defer == 0 and Fail == 80)or(Pass == 20 and Defer == 20 and Fail == 80)or(Pass == 20 or Defer == 0 and Fail == 100):
        print('Exclude')

elif Pass == 20:
    if (Defer == 100 and Fail == 0)or(Defer == 80 and Fail == 20)or(Defer == 40 and Fail == 60)or(Defer == 60 and Fail == 40):
        print('Do not progress-module retriever')

elif Pass == 0:
    if (Defer == 120 and Fail == 0)or(Defer == 100 and Fail == 20)or(Defer == 80 and Fail == 40)or(Defer == 60 and Fail == 60):
        print('Do not progress-module retriever')
        
    elif (Pass == 0 and Defer == 40 and Fail == 80)or(Pass == 0 and Defer == 20 and Fail == 100)or(Pass == 0 or Defer == 0 and Fail == 120):
        print('Exclude')
 
