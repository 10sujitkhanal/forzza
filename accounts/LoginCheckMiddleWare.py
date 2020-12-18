from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.is_superuser == True or user.is_staff == True:
                if modulename == "admin.common.views":
                    pass
                elif modulename == "accounts.views" or modulename == "django.views.static" or modulename == "django.contrib.auth":
                    pass
                elif modulename == "notifications.views" or modulename == "django.views.static" or modulename == "django.contrib.auth":
                    pass
                else:
                    return redirect("common:dashboard")
            
            elif user.is_active == True:
                if modulename == "core.views":
                    pass
                elif modulename == "deposit.views" or modulename == "django.views.static":
                    pass
                elif modulename == "withdraw.views" or modulename == "django.views.static":
                    pass
                elif modulename == "accounts.views":
                    pass
                elif modulename == "message.api":
                    pass
                else:
                    return redirect("/")

            else:
                return redirect("accounts:login")
