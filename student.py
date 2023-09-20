#Defining the student class
class Student:
    def hello(self):
        #Method to say hello
        print("Hey there! I'm so excited to learn stuff.")
        
    def raise_hand(self):
            print("Pick me!")
pass

class ChattyStudent(Student):
    def hello(self):
        #inheritind behavior from parent class
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walikng Dead last night? You didn't?! Oh man, it was crazy!What, you don't want any spoilers? Okay well let me tell you who died...")
    pass
