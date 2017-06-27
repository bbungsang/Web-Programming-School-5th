from django import forms

from .models import SmsInfo

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


class SmsForm(forms.ModelForm):

    class Meta:
        model = SmsInfo
        fields = [
            'to_num',
            'from_num',
            'content',
        ]

    def check_info(self):

        to_num = self.cleaned_data['to_num']
        from_num = self.cleaned_data['from_num']
        content = self.cleaned_data['content']

        api_key = "NCSGLMHSQ2FTVZUA"
        api_secret = "2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F"

        params = dict()
        params['type'] = 'sms'
        params['to'] = to_num
        params['from'] = from_num
        params['text'] = content

        cool = Message(api_key, api_secret)

        try:
            response = cool.send(params)

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)
