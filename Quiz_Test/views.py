from django.shortcuts import redirect, render , HttpResponse
from .models import Category,Detail_Vote,Answer,Correct_Answer

def Home(request):
    template = 'html/home.html'
    context = {'category':Category.objects.all()}
    return render(request,template,context)

def List_quiz(request,pk):
    template = 'html/list_quiz.html'
    context = {'list_quiz':Detail_Vote.objects.filter(category=pk)}
    return render(request,template,context)

def Quiz(request,pk):
    template = 'html/quiz.html'
    data = Detail_Vote.objects.get(pk = pk)
    total = [i for i in range(data.start_qustion,data.end_qustion+1)]
    choices = [i for i in range(1,data.type_choices+1)]
    context = {'range':total,'choices':choices,'pk':data.pk,'time':data.time,'type':'answer'}
    return render(request,template,context)

def Correct_Answers (request,pk):

    template = 'html/set_correct_asnwer.html'
    data = Detail_Vote.objects.get(pk = pk)
    total = [i for i in range(data.start_qustion,data.end_qustion+1)]
    list_quiz = {}
    type_choices = [i for i in range(1,data.type_choices+1)]
    for i in range(data.start_qustion,data.end_qustion+1):
        choices = type_choices.copy()
        try:
            
            choice = Correct_Answer.objects.get(vote = data , number = i)
            answer =choice.answer

            if answer == 0:
                list_quiz[i] = choices

            else:    
                index =  (answer -1) ##index of answer equil :  number of answer - 1 
                choices[index] = 'True' 
                list_quiz[i] = choices
              

        except  :
            list_quiz[i] = choices

    context = {'Answers':list_quiz,'pk':data.pk,'time':data.time,'type':'correct_answer',}
    return render(request,template,context)

def Save_quiz_answer(request):

    if request.method == 'POST':

        pk = request.POST['quiz_pk']
        vote = Detail_Vote.objects.get(pk=pk)

        if 'answer' in request.POST :
            
            for item , answer in request.POST.items():
                item = str(item).replace('questoin-','')
                
                if str(item).isdigit() :
                    item = int(item)
                    
                    try:
                        vote_quiz = Answer.objects.get(vote = vote , number = item ) 
                        vote_quiz.answer = answer
                        vote_quiz.save()
                    except:
                        Answer(vote = vote , number = item , answer = answer ).save() 


        elif 'correct_answer' in request.POST:
            
            for item , answer in request.POST.items():
                item = str(item).replace('questoin-','')
            
                if str(item).isdigit() :
                    item = int(item)
            
                    try:
                        vote_quiz = Correct_Answer.objects.get(vote = vote , number = item ) 
                        vote_quiz.answer = answer
                        vote_quiz.save()
                    except:
                        Correct_Answer(vote = vote , number = item, answer = answer).save() 
    
    return redirect(Home)

def Result_quiz(request,pk):
    data = {}
    template = 'html/result.html'
    vote = Detail_Vote.objects.get(pk=pk)
    total_Correct = 0
    total_worng = 0
    total_none = 0
    
    for i in range(vote.start_qustion,vote.end_qustion+1):
        choices = [None,None,None,None]
        status_answers = False
        
        try:
            answer = Answer.objects.get(vote = vote , number = i)
            answer = answer.answer
            index =  (answer -1) ##index of answer equil :  number of answer - 1 
            choices[index] = 'False' 
            data[i] = choices
            status_answers = True
        except:
            pass
        
        try:
            correct = Correct_Answer.objects.get(vote = vote , number = i)
            answer = correct.answer
            index =  (answer -1) ##index of answer equil :  number of answer - 1 
            if 'False' in choices:
                index_False = choices.index('False')
                # print(index_False , index)
                if index == index_False:
                    choices[index] = 'True/False'      
                else:
                    choices[index] = 'True'      
            else:
                choices[index] = 'True'
            data[i] = choices
            
            status_answers = True
        except:
            pass

        if status_answers == False:
            data[i] = choices
            total_none +=1
            # print(f'FALSE : {i}')
        else:
            if 'True/False' in data[i]:
                total_Correct +=1
            else:
                if 'False' not in data[i] :
                    total_none +=1
                else:
                    total_worng +=1
            

    # for i , n in data.items():
    #     print(i,n)

    # print(f'{total_Correct:} {total_worng:} {total_none:}')

    context = {"data":data,'worng':total_worng,'Correct':total_Correct,'total_none':total_none}
    return render(request,template,context)