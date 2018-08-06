from .models import Settings

def show_all(request):
	return {
		'global_settings': {item.name: item.value for item in Settings.objects.all()}
	}