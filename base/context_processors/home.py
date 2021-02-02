from leave.models import Leaves

def leaves(request):
    return {'leaves': Leaves.objects.all()}

