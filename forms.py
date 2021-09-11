from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired

#add parcel service type

class shipper(FlaskForm):
    shipperName = StringField('Full Name', validators=[DataRequired()])
    shipperMobile = StringField('Mobile Number', validators=[DataRequired()])
    shipperEmail = StringField('Email', validators=[DataRequired()])

    shipperAddress = StringField('Address', validators=[DataRequired()])
    shipperAddressSuburb = StringField('Suburb', validators=[DataRequired()])
    shipperAddressState = StringField('State', validators=[DataRequired()])
    shipperAddressPostCode = StringField('Post Code', validators=[DataRequired()])
    shipperAddressCountry = StringField('Country', validators=[DataRequired()])
    
    submit = SubmitField('Confirm Shipper Details')

class receiver(FlaskForm):
    receiverName = StringField('Full Name', validators=[DataRequired()])
    receiverMobile = StringField('Mobile Number', validators=[DataRequired()])
    receiverEmail = StringField('Email', validators=[DataRequired()])

    receiverAddress = StringField('Address', validators=[DataRequired()])
    receiverAddressSuburb = StringField('Suburb', validators=[DataRequired()])
    receiverAddressState = StringField('State', validators=[DataRequired()])
    receiverAddressPostCode = StringField('Post Code', validators=[DataRequired()])
    receiverAddressCountry = StringField('Country', validators=[DataRequired()])
    
    submit = SubmitField('Confirm Receiver Details')

class dangerousDeclaration(FlaskForm):
    #doesnt actually get stored, validated on fx and main 
    #change to the actual questions
    q1 = BooleanField('q1', default=False)
    q2 = BooleanField('q2', default=False)
    q3 = BooleanField('q3', default=False)
    q4 = BooleanField('q4', default=False)
    q5 = BooleanField('q5', default=False)
    q6 = BooleanField('q6', default=False)
    q7 = BooleanField('q7', default=False)
    q8 = BooleanField('q8', default=False)
    q9 = BooleanField('q9', default=False)
    q10 = BooleanField('q10', default=False)
    q11 = BooleanField('q11', default=False)
    q12 = BooleanField('q12', default=False)
    q13 = BooleanField('q13', default=False)
    q14  = BooleanField('q14', default=False)
    q15 = BooleanField('q15', default=False)

    #for digital signature 
    shipperNameSign = StringField('Shipper Name', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])

    submit = SubmitField('Create New Account')

class commercialInvoice(FlaskForm):
    itemName = StringField('Item', validators=[DataRequired()])
    qty = StringField('Qty', validators=[DataRequired()])
    unitVal = StringField('Unit Value', validators=[DataRequired()])
    totalVal = StringField('Total Value', validators=[DataRequired()])
    shopName = StringField('Retail Shop Name', validators=[DataRequired()])
    ABN = StringField('ABN', validators=[DataRequired()])
    
    submit = SubmitField('Add Item')