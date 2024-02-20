from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .eda import DataAnalysis

data_analysis = DataAnalysis()

@login_required(login_url='/accounts/login')
def index(request):
  template = loader.get_template('pages/index.html')
  context = {
    'dashboard_title': data_analysis.get_title(),
  }
  return HttpResponse(template.render(context, request))
  #return render(request, 'pages/index.html')

# dashboard
def dashboard_title(request):
  return data_analysis.get_title()

def dashboard_status_pie_chart(request):
  return data_analysis.get_status_pie_chart()

def dashboard_tenure_pie_chart(request):
  return data_analysis.get_tenure_pie_chart()

def dashboard_land_title_pie_chart(request):
  return data_analysis.get_land_title_pie_chart()

def dashboard_pie_chart_description(request):
  return JsonResponse({
    "status": data_analysis.get_status_pie_chart_description(),
    "tenure": data_analysis.get_tenure_pie_chart_description(),
    "land_title": data_analysis.get_land_title_pie_chart_description()
  })

def dashboard_property_type_bar_chart(request):
  return data_analysis.get_property_type_bar_chart()

def dashboard_state_bar_chart(request):
  return data_analysis.get_state_bar_chart()

def dashboard_city_bar_chart(request):
  return data_analysis.get_city_bar_chart()

def dashboard_bar_chart_description(request):
  return JsonResponse({
    "property_type": data_analysis.get_property_type_bar_chart_description(),
    "state": data_analysis.get_state_bar_chart_description(),
    "city": data_analysis.get_city_bar_chart_description()
  })

def dashboard_price_box_plot(request):
  return data_analysis.get_price_box_plot()

def dashboard_price_hist_plot(request):
  return data_analysis.get_price_hist_plot()

def dashboard_price_plot_description(request):
  return JsonResponse({
    "box": data_analysis.get_price_box_plot_description(),
    "hist": data_analysis.get_price_hist_plot_description()
  })

def dashboard_price_state_box_plot(request):
  return data_analysis.get_price_state_box_plot()

def dashboard_price_land_title_box_plot(request):
  return data_analysis.get_price_land_title_box_plot()

def dashboard_price_tenure_box_plot(request):
  return data_analysis.get_price_tenure_box_plot()

def dashboard_price_category_plot_description(request):
  return JsonResponse({
    "state": data_analysis.get_price_state_box_plot_description(),
    "land_title": data_analysis.get_price_land_title_box_plot_description(),
    "tenure": data_analysis.get_price_tenure_box_plot_description()
  })

def dashboard_price_state_scatter_plot(request):
  return data_analysis.get_price_state_scatter_plot()

def dashboard_price_land_title_scatter_plot(request):
  return data_analysis.get_price_land_title_scatter_plot()

def dashboard_price_tenure_scatter_plot(request):
  return data_analysis.get_price_tenure_scatter_plot()

def dashboard_price_scatter_plot_description(request):
  return JsonResponse({
    "state": data_analysis.get_price_state_scatter_plot_description(),
    "land_title": data_analysis.get_price_land_title_scatter_plot_description(),
    "tenure": data_analysis.get_price_tenure_scatter_plot_description()
  })

@login_required(login_url='/accounts/login')
def word_cloud(request):
  return render(request, 'pages/word-cloud.html')

def typography(request):
  return render(request, 'pages/typography.html')

def color(request):
  return render(request, 'pages/color.html')

def icon_tabler(request):
  return render(request, 'pages/icon-tabler.html')

def sample_page(request):
  return render(request, 'pages/sample-page.html')


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')