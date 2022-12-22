from django_filters import FilterSet, NumberFilter, DateFilter, ModelChoiceFilter, DateTimeFilter,CharFilter, ModelMultipleChoiceFilter
from .models import Post, Author, Category
from django.forms.widgets import SelectDateWidget
from django.forms import DateTimeInput

class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Новость не ранее',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    categoryType = ModelChoiceFilter(
        field_name='categoryType',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='все',
    )

    title_filter = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок содержит',
    )
# class PostFilter(FilterSet):
#     author_choice = ModelChoiceFilter(
#         field_name='author',
#         queryset=Author.objects.all(),
#         label='Автор:')
#
#     dateCreation__gte = DateFilter(
#         field_name='dateCreation',
#         lookup_expr='gte',
#         label='Дата публикации (не ранее):',
#         widget=SelectDateWidget)
#
#     category_choice = ModelMultipleChoiceFilter(
#         field_name='postCategory',
#         queryset=Category.objects.all(),
#         label='Категория:')
#
#     rating__gte = NumberFilter(
#         field_name='rating',
#         lookup_expr='gte',
#         label='Рейтинг (не менее):')
#
#     class Meta:
#         model = Post
#         fields = {
#         }
