from django.db.models import fields
from django.forms import ModelForm, inlineformset_factory

from .models import Question, Option


class QuizQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


OptionFormSet = inlineformset_factory(Question, Option,fields = ('option_text', 'is_correct', 'option_num'), extra=4, max_num=4 )

# class QuizOptionForm(ModelForm):
#     class Meta:
#         model = Option
#         fields = ('option_text', 'is_correct', 'option_num')


