from django.shortcuts import redirect

def reverse(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'educator':
			return view_func(request, *args, **kwargs)
		
		if group == 'manager_home':
			return view_func(request, *args, **kwargs)

		if group == 'human':
			return redirect('attendance')

	return wrapper_function