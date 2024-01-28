from django import forms
from . models import RecModel, OutgoingModel

class RecForm(forms.ModelForm):
    class Meta:
        model = RecModel
        fields = ('register_date','sender','ref_number','subject','address_date','remarks','file_to')
    
    def __init__(self, *args, **kwargs):
        super(RecForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # Customize the date field to use DateInput widget
        self.fields['register_date'].widget = forms.SelectDateWidget()



class OutgoingMailsForm(forms.ModelForm):
    class Meta:
        model = OutgoingModel
        fields = '__all__'
        labels ={
            'register_date': 'Date',
            'mail_sender': 'Sender',
            'mail_receiver': 'Receiver',
            'ref_number': 'Ref. Number',
            'subject': 'Subject',
            'collected_by': 'Collected_by',
            'collecting_date': 'Collecting_date'
        }

    def __init__(self, *args, **kwargs):
        super(OutgoingMailsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})