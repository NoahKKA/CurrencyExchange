class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
  
  #add magic methods here
  def __repr__(self):
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
    return f"{self.value:.2f} {self.unit}"
  
  def __str__(self):
    #This method returns the same value as __repr__(self).
    return Currency.__repr__(self)
  
  def __add__(self,other):
    #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
    return Currency(x + self.value, self.unit)
  
  def __iadd__(self, other):
     return Currency.__add__(self, other)
  
  def __radd__(self, other):
     x = self + other
     if self.unit != "USD":
        x.changeTo("USD")
     return x
  
  def __sub__(self, other):
    if type(other) == int or type(other) == float:
        x = (other * Currency.currencies[self.unit])
    else:
        x = (other.value/ Currency.currencies[self.unit] * Currency.currencies[self.unit])
    return Currency(x + self.value, self.unit)
  
  def __isub__(self, other):
     return Currency.__sub__(self, other)
  
  def __rsub__(self, other):
     x = other - self.value
     x = Currency(x, self.unit)
     if self.unit != "USD":
        x.changeTo("USD")
     return x


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 

# 40.65 EUR
# 47.14 USD
# 26.02 EUR
# 30.17 USD
# 20.84 EUR
# 10.03 USD


