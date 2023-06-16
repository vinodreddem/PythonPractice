class PolicyVer:
    Location ="AZ"

    def __init__(self,partyTDNr,VIN):
        self.party =partyTDNr
        self.vehicle=VIN

    # instance method ,We must have self as an attribute to the function as input.
    def getAgreementId (self,party,vehicle) :
        return "78946523251"

    def storeAgreementId (self,Agr):
        return


p1=PolicyVer("123456789","Afljcsjydi")

print(p1.getAgreementId(p1.party,p1.vehicle))