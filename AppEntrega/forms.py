from django import forms

class formSetCliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=100)

class formSetProveedor(forms.Form):
    nombre = forms.CharField(max_length=40)
    RUT = forms.IntegerField()
    email = forms.EmailField(max_length=100)

class formSetArticulo(forms.Form):
    nombre = forms.CharField(max_length=40)
    nro = forms.IntegerField()
    precio = forms.IntegerField()
    vendedor = forms.CharField(max_length=100)

class formSetServicio(forms.Form):
    descripcion = forms.CharField(max_length=100)
    proveedor = forms.CharField(max_length=100)
    precio = forms.IntegerField()