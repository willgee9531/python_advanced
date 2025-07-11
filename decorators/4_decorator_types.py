""" 
4 types of decorators to use:
    - @property (enable getter, setter and deleter of private attributes)
    - @static_method
"""

# @property when applied to a method acts like a getter and then allows that 
# method to also act as a setter and deleter by calling the @method.setter/deleter
# e.g. for a private attribute add an underscore at the beginning: _name_of_the_attr

class MaleStudent:
    def __init__(self, name):
        self._name = name
        self.GENDER = "Male"

    @property
    def naming(self):
        """ gets the name value """
        return self._name
    
    @naming.setter
    def naming(self, value):
        """ sets the name value """
        self._name = value.capitalize()
    
    @naming.deleter
    def naming(self):
        """ deletes the name value """
        self._name = ""
    

male_student1 = MaleStudent("G.C. Williams")
print(male_student1.naming)

male_student1.naming = "WillGee"
print(male_student1.naming)

del male_student1.naming
print(male_student1.naming)



# 