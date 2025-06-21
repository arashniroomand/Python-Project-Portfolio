def HappyNumber(num):
    """
    A happy number is a number defined by the following process:
    starting with any positive integer, replace the number by the sum of 
    the squares of its digits. and repeat the process untill a number quals 
    1 (where it will stay), or it loops endlessly in a cylce which does not include 1.

    :param num: Input number
    :return: Ture if num is happy number, False otherwise
    
    Examples:
    
    """
    list1 = []
    while num!= 1 and num not in list1 :
        list1.append(num)
        num = sum([int(i)**2 for i in str(num)])
        
    
    return num == 1

if __name__ == "__main__":
    assert HappyNumber(44) is True
    
    result = HappyNumber(input("Enter your number: "))

