# coding: utf-8
#!/usr/bin/env python

from django import forms


class LoginForm(forms.Form):
    student_id = forms.CharField(label="学号", max_length=15)
    password = forms.CharField(label="密码", max_length=100)
