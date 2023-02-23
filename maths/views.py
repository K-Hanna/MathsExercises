from django.shortcuts import render

from maths import doStuff, Datas
from maths.forms import MathsForm

outputData = []
inputData = Datas.InputData.__new__(Datas.InputData)


def index(request):
    form = MathsForm(request.POST)
    if 'start' in request.POST:
        if form.is_valid():
            inputData.__init__(int(request.POST.get('amount')),
                               int(request.POST.get('minValue')),
                               int(request.POST.get('maxValue')),
                               request.POST.getlist('operations'))
            examples = doStuff.drawNumbers(inputData)
            doStuff.fillOutput(examples, outputData)
            context = {'input': inputData,
                       'output': outputData,
                       'buttons': [True, False, True]}
            return render(request, 'index.html', context)
        else:
            context = {'form': form,
                       'error': "Wybierz chociaż jedno działanie.",
                       'buttons': [True, True, False]}
            return render(request, 'index.html', context)
    if 'finish' in request.POST:
        answers = request.POST.getlist('answer')
        doStuff.check(outputData, answers)
        score = sum([output.check for output in outputData])
        showFinishButton = True
        if score == len(outputData):
            score = "Brawo!"
            showFinishButton = False
        context = {'input': inputData,
                   'output': outputData,
                   'score': score,
                   'buttons': [showFinishButton, False, True]}
        return render(request, 'index.html', context)
    if 'reset' in request.POST:
        outputData.clear()
        context = {'form': MathsForm(),
                   'buttons': [True, True, False]}
        return render(request, 'index.html', context)
    context = {'form': form}
    return render(request, 'index.html', context)
