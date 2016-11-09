from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection


@login_required(login_url="login/")
def renderAdministrator(request):
    users = User.objects.all()
    return render(request, "administrator.html", {"users": users})


@login_required(login_url="login/")
def renderEditUsers(request):
    users = User.objects.all()
    return render(request, "editusers.html", {"users": users})


def renderAddCourse(request):
    return render(request, "addcourse.html")


def renderCourses(request):
    courses = []
    langs = []

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.execute("SELECT lang FROM courses")
        langs = cursor.fetchall()

    return render(request, "cursus.html", {"courses": courses, "langs": langs})


def renderViewCourse(request, lang="empty"):
    course = []

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM courses WHERE lang = '" + lang + "'")
        course = cursor.fetchall()

    return render(request, "viewcourse.html", {"course": course, "lang": lang})



def makeUserStaff(request):
    post = request.POST.copy()
    del post["csrfmiddlewaretoken"]

    array_keys = list(post.keys())

    for key in array_keys:
        if request.POST[key] is '2':
            with connection.cursor() as cursor:
                cursor.execute("SELECT is_staff FROM auth_user WHERE username = '" + key + "'")
                is_staff = cursor.fetchone()

                if not is_staff[0]:
                    cursor.execute("UPDATE auth_user SET is_staff = 1 WHERE username = '"+ key +"'")

        elif request.POST[key] is '1':
            with connection.cursor() as cursor:
                cursor.execute("SELECT is_staff FROM auth_user WHERE username = '" + key + "'")
                is_staff = cursor.fetchone()

                if is_staff[0]:
                    cursor.execute("UPDATE auth_user SET is_staff = 0 WHERE username = '"+ key +"'")

    # return render(request, "test.html", {"post": array_keys, "fpost": request.POST})
    return redirect("administrator")


def addCourse(request):
    post = request.POST.copy()
    del post["csrfmiddlewaretoken"]

    try:
        title = post["course_title"]
        lang = post["course_lan"]
        price = post["course_price"]
        descr = post["course_description"]
    except NameError:
        print("Post varaibles not defined")

    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO courses VALUES(NULL, '"+title+"','"+lang+"','"+price+"','"+descr+"')")

    return redirect("administrator")


def passwordSubmitAdmin(request):
    if request.method == "POST":
        username = request.POST["username"]
        passwordI = request.POST["passwordI"]
        passwordII = request.POST["passwordII"]
        if passwordI == passwordII:
            u = User.objects.get(username=username)
            u.set_password(passwordI)
            u.save()
            return redirect("home")
        else:
            return redirect("home")
    else:
        return redirect("home")

