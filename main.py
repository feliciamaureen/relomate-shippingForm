import os
from flask import Flask
from flask import render_template

from functions import newQuery
from forms import shipper, receiver, commercialInvoice, dangerousDeclaration

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/shipper", methods=['GET', 'POST'])
def shipperForm():
    form = shipper()
    
    if form.validate_on_submit():
        newQuery(form.shipperName.data, form.shipperMobile.data, form.shipperEmail.data, form.shipperAddress.data, form.shipperAddressSuburb.data, form.shipperAddressState.data, form.shipperAddressPostCode.data, form.shipperAddressCountry.data)

    if newQuery == True:
        return redirect('/receiver')

    return render_template("shipperForm.html", title="Shipping Form", form=form)

@app.route("/receiver", methods=['GET', 'POST'])
def receiverForm():
    form = receiver()
    
    if form.validate_on_submit():
        receiverDetails(form.receiverName.data, form.receiverMobile.data, form.receiverEmail.data, form.receiverAddress.data, form.receiverAddressSuburb.data, form.receiverAddressState.data, form.receiverAddressPostCode.data, form.receiverAddressCountry.data)

    if receiverDetails == True:
        return redirect('/receiver')
    return render_template("receiverForm.html", title=" Receiver Form", form=form)

@app.route("/items", methods=['GET', 'POST'])
def itemForm():
    form = commercialInvoice()
    return render_template("itemForm.html", title="Shipping Form", form=form)

@app.route("/declaration", methods=['GET', 'POST'])
def declatationForm():
    form = dangerousDeclaration()
    return render_template("declaration.html", title="Shipping Form", form=form)

if __name__ == '__main__':
    app.run(debug=True)   