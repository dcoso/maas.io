from canonicalwebteam.django_views import TemplateFinder
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template import loader


class MaasTemplateFinder(TemplateFinder):
    def get_context_data(self, **kwargs):
        """
        Get context data fromt the database for the given page
        """

        # Get any existing context
        context = super(MaasTemplateFinder, self).get_context_data(**kwargs)

        # Add level_* context variables
        clean_path = self.request.path.strip('/')
        for index, path, in enumerate(clean_path.split('/')):
            context["level_" + str(index + 1)] = path

        return context


def custom_404(request):
    t = loader.get_template('error/404.html')
    return HttpResponseNotFound(t.render({'request_path': request.path}))


def custom_500(request):
    t = loader.get_template('error/500.html')
    return HttpResponseServerError(t.render({}))
