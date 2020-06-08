from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import (
    LoginView, LogoutView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import (
    reverse_lazy, reverse
)
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .mixins import OnlyYouMixin
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, TodoUpdateForm, TodoCreateForm,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from .models import Todo

UserModel = get_user_model()


class TopView(TemplateView):
    template_name = 'cms/top.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'cms/login.html'

class Logout(LogoutView):
    pass

class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'cms/signup.html'
    success_url = reverse_lazy('cms:top')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())


class UserUpdate(OnlyYouMixin, UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'cms/user_update.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])


class UserDetail(DetailView):
    model = UserModel
    template_name = 'cms/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class UserList(ListView):
    model = UserModel
    template_name = 'cms/user_list.html'

class UserDelete(OnlyYouMixin, DeleteView):
    model = UserModel
    template_name = 'cms/user_delete.html'
    success_url = reverse_lazy('cms:top')


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo #コレTodoなのでは？←Todoにしたらページ開かなくなった←インポートを忘れてました
    form_class = TodoUpdateForm
    template_name = 'cms/todo_update.html'

    def get_success_url(self):
        return resolve_url('cms:user_detail', pk=self.kwargs['pk'])

class TodoCreate(LoginRequiredMixin,CreateView):
    form_class = TodoCreateForm
    template_name = 'cms/todo_create.html'
    success_url = reverse_lazy('cms:top')

    def form_valid(self, form):
        todo = form.save(commit=False)
        #todo.owners.add(self.request.user)
        todo.save()
        user = self.request.user
        user.todos.add(todo)
        #return HttpResponseRedirect(self.get_success_url()) #エラー出る
        return HttpResponseRedirect(reverse('cms:top')) #エラー出ない


class TodoList(ListView):
    model = Todo
    context_object_name = "todo_list"  # この行で変数名を指定(html内でobject_listを"todo_list"って書けるようになるだけ。)
    template_name = 'cms/todo_list.html'
    #paginate_by = 10   #1ページに表示する個数を制限できる

    def get_queryset(self):
        return Todo.objects.all().annotate(Count('user')).order_by('-user__count')  # ユーザー多い順に表示

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['bar'] = Todo.objects.all().annotate(Count('user')).order_by('-user__count')  # 他のモデルからデータを取得
    #    return context


class TodoAdd(LoginRequiredMixin, TemplateView):
    template_name = 'cms/todo_add.html'
    context_object_name = "todo_list"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # いろいろやる
        # ToDo listで選んだToDoをそのUserのtodosに加えたい。
        todo = Todo.objects.get(**kwargs)
        context["todo"] = todo
        user = self.request.user
        user.todos.add(todo)
        return context


class MyTodoList(ListView):
    model = Todo
    context_object_name = "my_todo_list"  # この行で変数名を指定(html内でobject_listを"todo_list"って書けるようになるだけ。)
    template_name = 'cms/my_todo_list.html'
    #paginate_by = 10   #1ページに表示する個数を制限できる

    def get_queryset(self):
        user = self.request.user
        return user.todos.all()


class TodoMain(LoginRequiredMixin, TemplateView):
    template_name = 'cms/todo_main.html'
    context_object_name = "my_todo_list"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # いろいろやる
        # My ToDo listで選んだToDoをそのUserのmain_todoに加えたい。
        owner = self.request.user
        todo = owner.todos.get(**kwargs)
        context["todo"] = todo
        #owner.main_todo.update_or_create(todo, defaults=None, **kwargs) #この辺とmodelの問題を解決する必要あり
        #main_todo = owner.main_todo
        todo.owner.add(owner)
        return context
