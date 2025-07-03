from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Form for creating and updating Topic instances; includes only the 'text' field for topic name input."""
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} # No label for the text field
        widgets = {'text': forms.TextInput(attrs={'size': 40})}

class EntryForm(forms.ModelForm):
    """A form for creating and updating entries."""
    
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 5})}  # Set both cols and rows for better control