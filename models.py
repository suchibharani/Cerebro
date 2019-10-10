import re
import phonenumbers
from django.db import models
from phonenumbers import carrier
from validate_email import validate_email
from django.core.exceptions import ValidationError


class Please(models.Model):
    emailplus = models.EmailField()
    country = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=100)

    def clean(self):
        clean_number = re.sub("[^0-9&^+]", "", self.phone_number)
        alpha_2 = self.country
        z = phonenumbers.parse(clean_number, "%s" % (alpha_2))
        if not validate_email(self.emailplus, check_mx=True, verify=True):
            raise ValidationError("Invalid email")
        if len(clean_number) > 15 or len(clean_number) < 3:
            raise ValidationError(
                "Number cannot be more than 15 or less than 3")
        if not phonenumbers.is_valid_number(z):
            raise ValidationError(
                "Number not correct format or non-existent")
        if carrier.name_for_number(z, "en") == '':
            raise ValidationError("Please enter a mobile number")
        else:
            return phonenumbers.format_number(
                z, phonenumbers.PhoneNumberFormat.E164)

    def __str__(self):
        return self.emailplus
