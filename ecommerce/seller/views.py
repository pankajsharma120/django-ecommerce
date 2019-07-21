from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from braces import views
from django.core.urlresolvers import reverse_lazy
from .utils import get_current_user
from .models import SellerProfileModel
from .forms import SellerProfileCreateForm,SellerLoginForm
# Create your views here.


class SellerProfileCreateView(views.AnonymousRequiredMixin,
                              views.FormValidMessageMixin,
                              generic.CreateView):

    template_name = 'seller/seller_signup.html'
    model = SellerProfileModel
    form_class = SellerProfileCreateForm
    success_url = reverse_lazy('seller:login')




class SellerLoginView(views.AnonymousRequiredMixin,generic.FormView):
    form_class = SellerLoginForm
    success_url = reverse_lazy('Index')
    template_name = 'seller/seller_login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(SellerLoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You\'ve been logged out. Come back soon!')
    return HttpResponseRedirect(reverse_lazy('Index'))


class DetailAccountView(
        views.LoginRequiredMixin,
        generic.DetailView
):
    model = SellerProfileModel
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'seller/seller_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailAccountView, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        context['username'] = username

        context['user'] = get_current_user(self.request)
        # context['posts'] = get_posts(username)

        if username is not context['user'].username:
            result = Connection.objects.filter(
                follower__username=context['user'].username
            ).filter(
                following__username=username
            )

            context['connected'] = True if result else False

        return context
