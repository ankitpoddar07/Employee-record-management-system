from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(
        label="Enter your email",
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
    name = forms.CharField(
        label="Enter your name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
    )
    feedback = forms.CharField(
        label="Your feedback",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your feedback'}),
    )
