"""
public static void switch_demo(String[] args) {

    int month = 8;
    String monthString;
    switch (month) {
        case 1:  monthString = "January";
                    break;
        case 2:  monthString = "February";
                    break;
        case 3:  monthString = "March";
                    break;
        case 4:  monthString = "April";
                    break;
        case 5:  monthString = "May";
                    break;
        case 6:  monthString = "June";
                    break;
        case 7:  monthString = "July";
                    break;
        case 8:  monthString = "August";
                    break;
        case 9:  monthString = "September";
                    break;
        case 10: monthString = "October";
                    break;
        case 11: monthString = "November";
                    break;
        case 12: monthString = "December";
                    break;
        default: monthString = "Invalid month";
                    break;
    }
    System.out.println(monthString);
}
"""

# The Pythonic way to implement switch statement is to use the powerful dictionary mappings, 
# also known as associative arrays, that provide simple one-to-one key-value mappings.


def switch_Demo (argument):
    
    switcher = {
        
        1 : "Jan",
        2 : "Feb",
        3 : "Mar"
    }
    return switcher.get (argument, "Invalid Month") # Inalid month is for default condition, If we didn't mention this then we will
#get Key value Error.

    #We can map Function names as well to the keys of the dictionary

def four ():
    return "Apr"

def five ():
    return "May"

def six ():
    return "Jun"

def switcher_Demo_Func (argm):
    
    switcher = {
        
        4: four,
        5 : five,
        6 : six,
        
    }

    func = switcher_Demo_Func.get (argm,lambda : "Invalid Month")
    
    return func()
    
class Switcher(object):
    def numbers_to_months(self, argument):
    """Dispatch method"""
    method_name = 'month_' + str(argument)
    # Get the method from 'self'. Default to a lambda.
    method = getattr(self, method_name, lambda: "Invalid month")
    # Call the method as we return it
    return method()

        def month_1(self):
        return "January"

    def month_2(self):
        return "February"

    def month_3(self):
        return "March"
a=Switcher()
a.numbers_to_months(1)
        
        # Based on the passed argument, the in-built getattr() function will retrieve object methods with the particular name.