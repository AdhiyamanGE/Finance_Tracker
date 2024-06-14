from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import Income, Expense, Reminder
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    test_display = Income.objects.filter(author=request.user)
    context = {"test_display": test_display}
    totinc = 0
    for ilt in test_display:
        totinc = totinc + ilt.amt
    test_display2 = Expense.objects.filter(autor=request.user)
    context2 = {"test_display2": test_display2}
    totexp = 0
    for ilt in test_display2:
        totexp = totexp + ilt.amnt
    sev = totinc - totexp
    return render(
        request, "ft_app1/home.html", {"inc": totinc, "exp": totexp, "sav": sev}
    )


@login_required
def link(request):
    return render(request, "ft_app1/link.html")


@login_required
def linkview(request):
    return render(request, "ft_app1/link_view.html")


@login_required
def bar(request):
    return render(request, "ft_app1/navbar.html")


@login_required
def addinc(request):
    if request.method == "POST":
        cat = request.POST.get("description")
        amtt = request.POST.get("amount")
        datee = request.POST.get("date")
        idd = request.user
        income = Income.objects.create(catg=cat, amt=amtt, date=datee, author=idd)
        income.save()
    return render(request, "ft_app1/add_income.html")


@login_required
def viewinc(request):
    inco = {"inci": Income.objects.filter(author=request.user)}
    return render(request, "ft_app1/view_income.html", inco)


@login_required
def viewexp(request):
    epense = {"expi": Expense.objects.filter(autor=request.user)}
    return render(request, "ft_app1/view_expense.html", epense)


@login_required
def viewrem(request):
    remind = {"remi": Reminder.objects.filter(author=request.user)}
    return render(request, "ft_app1/view_reminder.html", remind)


@login_required
def addrem(request):
    if request.method == "POST":
        cat = request.POST.get("Reminder")
        amtt = request.POST.get("amount")
        datee = request.POST.get("date")
        idd = request.user
        remind = Reminder.objects.create(catg=cat, amt=amtt, date=datee, author=idd)
        remind.save()
    return render(request, "ft_app1/add_reminder.html")


@login_required
def addexp(request):
    if request.method == "POST":
        cat = request.POST.get("expense-name")
        amtt = request.POST.get("expense-amount")
        datee = request.POST.get("expense-date")
        idd = request.user
        expense = Expense.objects.create(cag=cat, amnt=amtt, daet=datee, autor=idd)
        expense.save()
    return render(request, "ft_app1/add_expense.html")


@login_required
def uprof(request):
    return render(request, "ft_app1/u_profile.html")


def regiister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "ft_app1/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "ft_app1/profile.html")
