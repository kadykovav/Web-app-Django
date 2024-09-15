from .utils import menu, profile_menu


def get_context_processors(request):
    return {
        'mainmenu': menu,
        'profile_menu': profile_menu,
    }
