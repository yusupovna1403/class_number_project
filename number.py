class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        if self.value % 2 != 0:
            return True
        else:
            return False
        

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value % 2 == 0:
            return True
        else:
            return False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        count = 0
        for num in range(2,self.value):
            if self.value % num == 0:
                count+=1
        if count == 0:
            return True
        else:
            return False


    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        for num in range(1,self.value+1):
            if self.value % num == 0:
                divisors.append(num)
        return divisors


    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        sum = 0
        while self.value > 0:
            num = self.value % 10
            self.value//=10
            sum+=num
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        num_reverse = 0
        while self.value > 0:
            num = self.value % 10
            num_reverse = num_reverse*10 + num
            self.value//=10
        return num_reverse

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return str(self.value) == str(self.value)[::-1]
        

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        digits = []
        while self.value > 0:
            num = self.value % 10
            digits.append(num)
            self.value//=10
        return digits

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        digits = []
        while self.value > 0:
            num = self.value % 10
            digits.append(num)
            self.value//=10
        max = digits[0]
        i = 1
        for i in digits:
            if i > max:
                max = i
        return max

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        digits = []
        while self.value > 0:
            num = self.value % 10
            digits.append(num)
            self.value//=10
        min = digits[0]
        i = 1
        for i in digits:
            if i < min:
                min = i
        return min

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        sum = 0
        while self.value > 0:
            num = self.value % 10
            self.value//=10
            sum+=num

        return sum/len(self.value)

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        num_len = len(self.value)
        middle = (num_len - 1)//2
        if middle % 2 == 0:
            return str(self.value)[middle]
        else:
            return (str(self.value[middle]) + str(self.value[middle+1]))/2

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.
        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(value = 32145)
print(number.get_number())
print(number.is_odd())
print(number.is_even())
print(number.is_prime())
print(number.get_divisors())
print(number.get_length())
print(number.get_sum())
print(number.get_reverse())
print(number.is_palindrome())
print(number.get_digits())
print(number.get_max())
print(number.get_min())
print(number.get_average())
print(number.get_median())

