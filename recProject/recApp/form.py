from django import forms
# from . models import RecModel, OutgoingModel
from .models import IncomingMail, OutGoingMail, BaseAttachments

class IncomingMailsForm(forms.ModelForm):
    class Meta:
        model = IncomingMail
        # fields = ('register_date','sender','ref_number','subject','address_date','remarks','file_to')
        fields = ('sender','ref_number','description','address_date','remarks','file')

    def __init__(self, *args, **kwargs):
        super(IncomingMailsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # Customize the date field to use DateInput widget
        # self.fields['register_date'].widget = forms.SelectDateWidget()



class OutgoingMailsForm(forms.ModelForm):
    class Meta:
        model = OutGoingMail
        fields = ('sender','mail_destination','ref_number','description','collected_by','date_of_collection')
        # fields = '__all__'
        # labels ={
            # 'register_date': 'Date',
            # 'mail_sender': 'Sender',
            # 'mail_receiver': 'Receiver',
            # 'ref_number': 'Ref. Number',
            # 'subject': 'Subject',
            # 'collected_by': 'Collected_by',
            # 'collecting_date': 'Collecting_date'
        # }

    def __init__(self, *args, **kwargs):
        super(OutgoingMailsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class FilesForm(forms.ModelForm):
    class Meta:
        model = BaseAttachments
        fields = ('name', 'category', 'ref_number')

    def __init__(self, *args, **kwargs):
        super(FilesForm, self).__init__(*args, **kwargs)
        for fiel_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})