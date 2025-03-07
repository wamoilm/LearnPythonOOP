from encapsulation.bad_example.phone import Phone

# create a basic phone
basic_phone = Phone("B1", "TalkTalk", "TalkTalk_OS")

# print the make
print(f"Make of {basic_phone.model} is {basic_phone.make}")

# let's alter the make of the phone
basic_phone.make = "BlaBla"

# print the altered make
print(f"Make of {basic_phone.model} is {basic_phone.make}")

# Note the above is a bad example for the following reasons
# all fields are public
# client script using the class can easily alter the class attribute values
# there is in fact no protection to stop things to go wrong
# in the above example the basic phone which was created by the "TalkTalk" company now suddenly appears to be
# created by "BlaBla" company which is incorrect.
# we will need to address this issue with the OOPs principle called Encapsulation


