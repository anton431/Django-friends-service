menu = [
        {'title': 'Найти друзей', 'url_name': 'find_friends'},
        {'title': 'Список друзей', 'url_name': 'my_friends'},
        {'title':'Заявки', 'url_name': 'applications'},
        ]

exit = {'exit': 'Войти', 'url_name': 'login'}

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['exit'] = exit
        return context