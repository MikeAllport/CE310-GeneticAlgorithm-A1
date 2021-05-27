"""
bitToRealHelper.py is a helper class to convert a binary representation to a real numbered representation for the purpose of the assignment. In reality, it would be much simpler to program a GA that uses real values and an interpolation method during crossover.

@author Michael Allport 2021
"""

class BitToReal():
    """BitToReal's purpose it to extract sub bit arrays from a chromosome for its component
    variables. A BitToReal may be instantated with [10, 10, 10] bitLength, and the proceeding
    method GetRealValue would take a chromosome as input and be able to extract the 1st, second,
    or third variable's real value based on 10 bits each, or its bit arrays with GetBitArray.
    
    Extra members have been made to print this bit representation's resolution. Error checking
    has also been enabled so any chromosome input with a BitToReal cannot be of a length less than
    the total of its variables length. It can however be greater than. So a chromosome can have more
    bits than this representation, but the extra bits will just be ignored when calculating real values"""
    def __init__(self,
               bitLengths: list,
               minimum,
               maximum,
                ):
        self._bitLengths = bitLengths
        self._minimum = minimum
        self._maximum = maximum

        

    def GetRealValue(self, chromosome: list, variable):
        """GetRealValue's purpose is to attain the real value of a given variable number from a given chromosome
        chromosome: the array containing bits
        variable: the variable number to get value from, variable 1 being of bit length self._bitLengths[0] 
        """
        self.CheckChromosomeLength(chromosome)
        return self.ConvertBinaryArrToReal(self, self.GetBitArray(chromosome, variable))
    

    def GetBitArray(self, chromosome: list, variable):
        """GetBitArray's purpose is to return a bit array pertaining to the given variable from the given chromosome
        chromosome: the array containing bits
        variable: the variable number of the array to get, variable 1 being of bit length self._bitLengths[0] 
        """
        self.CheckChromosomeLength(chromosome)
        variableBits = chromosome[(sum(self._bitLengths[i-1] for i in range(1, variable))):
                           (sum(self._bitLengths[i-1] for i in range(1, variable+1)))]
        return variableBits
        
  
    @staticmethod
    def ConvertBinaryArrToReal(btr, bitArr):
        """ ConvertBinaryArrToReal's purpose is to convert a given array of bits into its real value"""
        dec = sum(bitArr[i] * 2**i for i in range(len(bitArr)))
        return btr._minimum + ((dec) / (2**len(bitArr) - 1)) * (btr._maximum - btr._minimum)

    
    def GetBinaryRealResolutions(self):
        """GetBinaryRealResolutions purpose is to return the precision of a given binary real representation"""
        return [(self._maximum - self._minimum) / (2**self._bitLengths[i] - 1) for
                i in range(len(self._bitLengths))]
    
    def PrintResolutions(self):
        """PrintResolutions purpose is to attain an array of resolutions, and print them to console"""
        resolutions = self.GetBinaryRealResolutions()
        for i in range(len(resolutions)):
            print(f'Resolution Variable {i}: {resolutions[i]}')
        
    
    def GetBitArrays(self, chromosome):
        """GetBitArrays purpose is to extract each variables bit array from a given chromosome and return them in an array"""
        self.CheckChromosomeLength(chromosome)
        arr = []
        for i in range(1, len(self._bitLengths) +1):
            arr.append(self.GetBitArray(chromosome, i))
        #arr.append(self.GetRealValue(chromosome, i) for i in range(1, len(self._bitLengths) + 1))
        return arr
    

    def CheckChromosomeLength(self, chromosome):
        """CheckChromosomeLength's purpose is to ensure that the chromosomes length is not greater than the sum of 
        the variables lengths, if it is throw an exception"""
        sumLengths = sum(self._bitLengths[i] for i in range(len(self._bitLengths)))
        if (sumLengths > len(chromosome)):
            raise Exception(f'Error, chromosome of length({len(chromosome)}) given when total' +
                           f' variable lengths should be {sumLengths}')
    