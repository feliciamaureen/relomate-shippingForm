from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, RadioField
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
    q1 = RadioField('q1', choices=[('Yes','yes'),('No','no')])
    q2 = RadioField('q2', choices=[('Yes','yes'),('No','no')])
    q3 = RadioField('q3', choices=[('Yes','yes'),('No','no')])
    q4 = RadioField('q4', choices=[('Yes','yes'),('No','no')])
    q5 = RadioField('q5', choices=[('Yes','yes'),('No','no')])
    q6 = RadioField('q6', choices=[('Yes','yes'),('No','no')])
    q7 = RadioField('q7', choices=[('Yes','yes'),('No','no')])
    q8 = RadioField('q8', choices=[('Yes','yes'),('No','no')])
    q9 = RadioField('q9', choices=[('Yes','yes'),('No','no')])
    q10 = RadioField('q10', choices=[('Yes','yes'),('No','no')])
    q11 = RadioField('q11', choices=[('Yes','yes'),('No','no')])
    q12 = RadioField('q12', choices=[('Yes','yes'),('No','no')])
    q13 = RadioField('q13', choices=[('Yes','yes'),('No','no')])
    q14 = RadioField('q15', choices=[('Yes','yes'),('No','no')])
    q15 = RadioField('q15', choices=[('Yes','yes'),('No','no')])

    #for digital signature 
    shipperNameSign = StringField('Shipper Name', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])

    submit = SubmitField('Submit')

class commercialInvoice(FlaskForm):
    itemName = StringField('Item', validators=[DataRequired()])
    qty = StringField('Qty', validators=[DataRequired()])
    unitVal = StringField('Unit Value', validators=[DataRequired()])
    totalVal = StringField('Total Value', validators=[DataRequired()])
    shopName = StringField('Retail Shop Name', validators=[DataRequired()])
    ABN = StringField('ABN', validators=[DataRequired()])
    
    submit = SubmitField('Add Item')