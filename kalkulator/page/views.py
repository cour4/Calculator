from django.shortcuts import render
from django.http import HttpResponse
from .form import formacja
global context
context = {}
global z
z = []

def home(request):
	print(request)
	
	return render(request,'templates/home.html')

def but1(request):
	a = "1"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr


	
	
	return render(request,'templates/home.html',context)

def but_plus(request):
	print("+")
	a = "+"
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	

	return render(request,'templates/home.html',context)

def but_minus(request):
	print("-")
	a = "-"
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	

	return render(request,'templates/home.html',context)


def but_multi(request):
	print("*")
	a = "*"
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	

	return render(request,'templates/home.html',context)

def but_t(request):
	print("/")
	a = "/"
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr

	

	return render(request,'templates/home.html',context)
def equale(request):
	try:
		global ans
		ans = ''
		print(z)
		for x in z:
			
			ans += '' + x


		print(ans)
		print(eval(ans))
		ans1 = eval(ans)
		context["ser"] = ans1
		context["ans"] = ans + "="
		return render(request,'templates/home.html',context)
	except:
		context["ser"] = "Impossible to do "
		return render(request,'templates/home.html',context)

def erase(request):
	z.clear()
	context["ser"] = None
	print(z)
	if context["ser"] == None:
		context["ser"] = ""
	return render(request,'templates/home.html')

def but2(request):
	a = "2"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr

	
	
	return render(request,'templates/home.html',context)

def but3(request):
	a = "3"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr

	
	
	return render(request,'templates/home.html',context)

def but4(request):
	a = "4"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr

	
	
	return render(request,'templates/home.html',context)

def but5(request):
	a = "5"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)

def but6(request):
	a = "6"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)

def but7(request):
	a = "7"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)

def but8(request):
	a = "8"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)

def but9(request):
	a = "9"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr

	return render(request,'templates/home.html',context)

def but0(request):
	a = "0"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)
def ONAV(request):
	a = "("	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)
def CNAV(request):
	a = ")"	
	z.append(a)
	context['ans'] = z
	listToStr = ''.join(map(str, z))
	context['ans'] = listToStr
	
	
	return render(request,'templates/home.html',context)
	
	