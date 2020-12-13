from django.db.models import fields
from django.forms import ModelForm, inlineformset_factory, Textarea

from .models import Question, Option


class QuizQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'ques_text': Textarea(attrs={'cols': 70, 'rows': 10}),
   }



OptionFormSet = inlineformset_factory(
    Question,
    Option,
    fields = ['option_text', 'is_correct', 'option_num'],
    widgets = {'option_text': Textarea(attrs={'cols': 30, 'rows': 1})},
    extra=4,
    max_num=4 
)

# class QuizOptionForm(ModelForm):
#     class Meta:
#         model = Option
#         fields = ('option_text', 'is_correct', 'option_num')


