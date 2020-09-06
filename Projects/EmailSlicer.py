import re

emailId = input("Enter emailId : ")

emailPattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

if emailPattern.search(emailId):
    userName = emailId[:emailId.index("@")]
    domainName = emailId[emailId.index("@") + 1:]
    print("\n\nUsername : " + userName + "\nDomainName : " + domainName)

else:
    print("\n\nEnter correct emailId")
