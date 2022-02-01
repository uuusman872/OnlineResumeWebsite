from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)
from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "backend/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonial = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        context["testimonials"] = testimonial
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context



class ContactView(generic.FormView):
    template_name = "backend/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Tanks you. We will be in touch soon")
        return super().form_valid(form)



class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "backend/portfolio.html"
    paginate_by  = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name =  "backend/portfolio-detail.html"



class BlogView(generic.ListView):
    model = Blog
    template_name = "backend/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)



class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "backend/blog-detail.html"







