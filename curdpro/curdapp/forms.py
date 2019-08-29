from django import forms

class InsertForm(forms.Form):
    product_id_f=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.TextInput(
            attrs={ 'placeholder':'Product ID','class':'form-control'}
        )
    )

    product_name_f=forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={'placeholder':'Product Name','class':'form-control'}
        )
    )
    product_color_f=forms.CharField(
        label='Product Color',
        widget=forms.TextInput(
            attrs={'placeholder':'Product Color',
                   'class':'form-control'}
        )
    )
    product_cost_f=forms.IntegerField(
        label='Product Cost',
        widget=forms.NumberInput(
            attrs={'placeholder':'Product Cost',
                   'class':'form-control'}
        )
    )


class UpdateForm(forms.Form):
        product_id_f = forms.IntegerField(label='Enter Product ID',
                                          widget=forms.TextInput(attrs={'placeholder': 'Product ID', 'class': 'form-control'}))
        product_cost_f = forms.IntegerField(
            label='Product Cost',
            widget=forms.NumberInput(
                attrs={'placeholder': 'Product Cost',
                       'class': 'form-control'}
            )

        )


class DeleteForm(forms.Form):
        product_id_f=forms.IntegerField(
            label='Enter Product Id',
            widget=forms.NumberInput(
                attrs={'placeholder':'Product ID','class':'form-control'}
            )
        )