from init import dbinit
from datetime import date
from validate import Validation

db = dbinit()
validator = Validation()

#extra validation functions
def declarationValidation(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, shipperNameSign, date):
    #all questions need to be false

    #signature crosschecked from sender name 
    if validator.is_alphabetic_with_space(shipperNameSign) == True:
        #if(name is the same as sender name)
        pass
    
    #date correct to system time 
    today = date.today()
    if(date != today):
        print('invalid date')


#firestore functions
def newQuery(shipperName, shipperMobile, shipperEmail, shipperAddress, shipperAddressSuburb, shipperAddressState, shipperAddressPostCode, shipperAddressCountry):
    shipper = {
        u'shipperName': shipperName,
        u'shipperMobile': shipperMobile,
        u'shipperEmail': shipperEmail,
        
        u'shipperAddress': shipperAddress,
        u'shipperAddressSuburb': shipperAddressSuburb,
        u'shipperAddressState': shipperAddressState,
        u'shipperAddressPostCode': shipperAddressPostCode,
        u'shipperAddressCountry': shipperAddressCountry

    }
    if validator.is_alphabetic_with_space(shipperName) == True:
        if validator.is_numeric(shipperMobile) == True: 
           if validator.is_email(shipperEmail) == True:
               if validator.is_alphanumeric_with_space(shipperAddress) == True:
                   if validator.is_alphabetic(shipperAddressSuburb) == True:
                       if validator.is_numeric(shipperAddressPostCode) == True:
                           if validator.is_alphabetic(shipperAddressCountry) == True:
                                #add validation for locations after array function has been added
                                db.collection(u'shippingRequests').add(shipper)
                                print('new query added')
                                return True

    else:
        print('no')


def populateItems():
    #store receiver deets in sender document as subcollection
    pass
    

def addItem():
    #append function
    #store receiver deets in sender document as subcollection
    pass
    

def receiverDetails():
    #receiver not innested format
    receiver = {
        u'receiverName': receiverName,
        u'receiverMobile': receiverMobile,
        u'receiverEmail': receiverEmail,
        
        u'receiverAddress': receiverAddress,
        u'receiverAddressSuburb': receiverAddressSuburb,
        u'receiverAddressState': receiverAddressState,
        u'receiverAddressPostCode': receiverAddressPostCode,
        u'receiverAddressCountry': receiverAddressCountry

    }
    if validator.is_alphabetic_with_space(receiverName) == True:
        if validator.is_numeric(receiverMobile) == True: 
           if validator.is_email(receiverEmail) == True:
               if validator.is_alphanumeric_with_space(receiverAddress) == True:
                   if validator.is_alphabetic(receiverAddressSuburb) == True:
                       if validator.is_numeric(receiverAddressPostCode) == True:
                           if validator.is_alphabetic(receiverAddressCountry) == True:
                                #add validation for locations after array function has been added
                                db.collection(u'shippingRequests').add(receiver)
                                print('receiver to query added added')
                                return True

    else:
        print('no')
    pass
