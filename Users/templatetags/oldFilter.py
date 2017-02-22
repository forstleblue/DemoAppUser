from django import template
import datetime
register = template.Library()

@register.filter(name='oldRange')
def oldRange(value):
	now = datetime.datetime.now()
	old = now.year - value.year
	if old > 13:
		return "allowed"
	else:
		return "blocked"

@register.filter(name='checkBizzFuzz')
def checkBizzFuzz(value):
	reThree = value % 3
	reFour = value % 4
	if reThree == 0 and reFour == 0:
		return "BizzFuzz"		
	elif reFour==0:
		return "Fuzz"
	elif reThree ==0:
		return "Bizz" 
	else:
		return value
			

	