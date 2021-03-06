from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from login.forms import LoginForm
from django.contrib.auth import views as authviews
from django.core.urlresolvers import reverse
from login import views as loginviews
from administrator import views as adminviews

urlpatterns = [
    url(r'^index/', TemplateView.as_view(template_name='index.html')),
    url(r'^test/', TemplateView.as_view(template_name='test.html')),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^cursus/', adminviews.renderCourses),
    url(r'^logintest/', TemplateView.as_view(template_name='login.html')),
    url(r'^register/', TemplateView.as_view(template_name='register.html')),
    url(r'^admin/', admin.site.urls),
    url(r'purchasecourse/', adminviews.purchaseCourse, name="purchasecourse"),
    url(r'^viewcourse/(?P<lang>\w+)', adminviews.renderViewCourse, name="viewcourse"),
    url(r'', include('login.urls')),
    url(r'^login/$', authviews.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'registerSubmit/', loginviews.create, name="registerSubmit"),
    url(r'passwordSubmit/', loginviews.changePassword, name="passwordSubmit"),
    url(r'pdf/', loginviews.pdfBuilder, name="pdf"),
    url(r'logout/', authviews.logout, name="logout"),
    url(r'addcourse/', adminviews.renderAddCourse),
    url(r'purchases/', adminviews.renderPurchases),
    url(r'administrator/',adminviews.renderAdministrator, name="administrator"),
    url(r'passwordSubmitAdmin/', adminviews.passwordSubmitAdmin, name="passwordSubmitAdmin"),
    url(r'editusers/', adminviews.renderEditUsers, name="editusers"),
    url(r'makestaff/', adminviews.makeUserStaff, name="makestaff"),
    url(r'insertcourse/', adminviews.addCourse, name="insertcourse")
]