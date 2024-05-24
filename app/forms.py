from django import forms

from app.models import * 


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):#this class is responsibe for defining a model form
    
    class Meta():#this class is resoponsibe for defining the information about the model
        model=Webpage

        fields='__all__'#__all__ is used to take all input element

        fields=['topic_name','name']#it gives only how many fields elements give that many element give

        exclde=['email','url']#except exclude values gives remainders

        labels={'topic_name':'Topic','name':'Name','url':'URL','email':'Email'}#change the names

        help_texts={'topic_name':'should not be integers','name':'only Alphabets'}

        widgets={'url':forms.PasswordInput,'name':forms.Textarea}

class AccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'