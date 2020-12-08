from quiz.models import attempt
from django import forms


# class QuizForm(forms.Form):
#     def __init__(self, questions, *args, **kwargs):
#         self.questions = questions
#         for question in questions:
#             field_name = "question_%d" % question.pk
#             choices = []
#             for answer in question.option_set().all():
#                 choices.append((answer.pk, answer.answer,))
#             ## May need to pass some initial data, etc:
#             field = forms.ChoiceField(label=question.question, required=True, 
#                                         choices=choices, widget=forms.RadioSelect)
#             super(QuizForm, self).__init__(*args, **kwargs)
#     def save(self):
#         ## Loop back through the question/answer fields and manually
#         ## update the Attempt instance before returning it.
#         for question in self.questions():
#             attempt.Question = question.pk
#             attempt.user = self.user
#             attempt.total_score += self.score


