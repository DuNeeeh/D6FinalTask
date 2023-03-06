import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import News


# Создаем свой набор фильтров для модели News.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Name',
    )
    date = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Later Then',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )
    # typeofcategory = ChoiceFilter(
    #     field_name='categoryType',
    #     label='Тип поста',
    #     choices=Post.CATEGORIES,
    # )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = News
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'category',
        }
