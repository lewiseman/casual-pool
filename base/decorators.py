from django.shortcuts import redirect

def reverse(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'human':
			return redirect('attendance')
		
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_function