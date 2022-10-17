from django.shortcuts import render

# Create your views here.
def blog_main(request):
    return render(request, 'blog/index.html', {'msg' : 'HELLO Django'})

def calc_1(request):
    if request.method == 'POST':
        # 계산
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        opr = request.POST['opr']
        result = eval(num1+opr+num2)
        return render(request, 'blog/calc_1_form.html', {'result': f"{num1} {opr} {num2} = {result}"})
    return render(request, 'blog/calc_1_form.html')

def calc_2(request):
    return render(request, 'blog/clac_2_form.html')

def gugudan(request):
    if request.method == 'POST':
        dan = int(request.POST['dan'])
        s = ''

        for i in range(1,10):
            s += f'{dan} * {i} = {dan*i}'

        return render(request, 'blog/gugudan.html', {'result' : s})

    return render(request, 'blog/gugudan.html')