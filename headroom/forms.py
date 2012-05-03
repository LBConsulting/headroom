from wtforms import Form, BooleanField, TextField, validators,\
    SelectMultipleField, widgets

class DemographicsForm(Form):
    birth_month = TextField(u"Please enter your birth month:",
            [validators.Length(min=1,max=12), validators.Required()])
    birth_year = TextField(u"Please enter your birth year:",
            [validators.Length(min=0,max=99), validators.Required()])
    subject_number = TextField(u"Subject number:",
            [validators.Length(min=0,max=99999), validators.Required()])
    experiment_number = TextField(u"Experiment number:",
            [validators.Length(min=0,max=99999), validators.Required()])

## For later...
class MultiCheckboxField(SelectMultipleField):
    """
    Lists of checkboxes
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
