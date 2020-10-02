from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Symptoms
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def index_save(request):
    if request.method != "POST":
        return render(request, 'pages/index.html')
    else:
        
        name=request.POST.get('name')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        temperature = request.POST.get('temperature')
        options = request.POST.getlist('options')
        information = request.POST.getlist('information')

        score = 0
        score = int(score)
        if int(temperature) > 37.5 or int(temperature) > 38.3:
            score = 2
                 
        convert_option = [int(i) for i in options] # here convert the list into integer
        sum = 2
        for num in convert_option :  # additon of every element in the list of options
            sum += num
        sum = int(sum)
        
        score = sum + score
        
        # for 2nd checkbox code
        convert_info = [int(j) for j in information]  # here convert the list into integer
        add = 0
        for i in convert_info:   # additon of every element in the list of informations
            add += i
        add = int(add)
        score = add + score
        print(score)

        if score < 5:
            chance_cv = "COVID-19 “Negative”. Merely have chance to get affected by COVID19. Go for isolation and contact doctor and follow advice."
            result = "Negative"
        
        elif (score > 5) or (score == 5):

            chance_cv = "COVID-19 “Positive”. Possible suspected case for COVID-19 affected.Advice patient for isolation and contact doctor and follow advice."
            result = "Positive"

           
            if (score > 5) and (score < 7):
                chance_cv = "COVID-19 “Positive”. Highly chance of COVID-19 affected.Go for isolation and contact doctor immediatelyand follow advice. Contact with: 018778876766, 01678876633, 0186477222"
                result = "Positive"

            elif score > 7:
                chance_cv = "COVID-19 “Positive”.Almost confirmed case of COVID-19 positive.Go for isolation and contact doctor immediately and follow advice. Highly advice patient to be hospitalized. Contact with: 018778876766, 01678876633, 018647722"
                result = "Positive"
        
        try:
            symptomform = Symptoms(name=name, age=age, sex=sex,temperature=temperature,score=score,result=result)
            symptomform.save()
                
            context = {
                'chance_cv': chance_cv,
                'name': name,
                'score': score,
                }

            return render(request, 'pages/result.html', context)
        except:
            return render(request, 'pages/index.html')


def result(request):
    


    return render(request, 'pages/result.html')

def test_list(request):
    all_test = Symptoms.objects.all()
    context = {
        'all_test': all_test,
    }


    return render(request, 'pages/test_list.html', context)