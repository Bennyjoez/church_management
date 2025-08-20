from django.shortcuts import render

# Create your views here.
def get_members_list(request):
    """
    A simple API endpoint to return a list of members.
    For this initial scaffold, we are returning a hardcoded list.
    """
    members = [
        {'id': 1, 'first_name': 'John', 'last_name': 'Doe'},
        {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith'},
    ]
    return JsonResponse({'members': members})