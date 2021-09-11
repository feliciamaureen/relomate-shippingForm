from init import dbinit
from validate import Validation

db = dbinit()
validator = Validation()

#extra validation functions
def declarationValidation():
    #all questions need to be false
    #signature crosschecked from sender name 
    #date correct to system time 


#firestore functions
def newQuery():
    #atm the collection name is just shippingRequests
    #will group by companies, but ask first if that's needed
    location = {
        u'shipperName': shipperName,
        u'shipperMobile': shipperMobile,
        u'shipperEmail': shipperEmail,
    }
    if validator.is_alphabetic_with_space(shipperName) == True:
        if validator.is_phone_number(shipperMobile) == True: 
           if validator.is_email(shipperEmail) == True:
            #add validation for locations after array function has been added
            db.collection(u'shippingRequests').add(tour)
            print('added')
    else:
        print('no')

def populateItems():
    #store receiver deets in sender document as subcollection
    

def addItem():
    #append function
    #store receiver deets in sender document as subcollection
    

def receiverDetails():
    #store receiver deets in sender document as nested item
