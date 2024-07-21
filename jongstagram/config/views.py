from django.shortcuts import redirect


def index(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    else:
        return redirect("users:login")

def custom_page_not_found(request, exception):
    return redirect("users:login")
