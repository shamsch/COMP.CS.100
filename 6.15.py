"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def longest_substring_in_order(s):
    """
    This function returns the longest  orderd substring
    """
    if s == '':
        return s
    else:
        keep = s[0] # Taking the first char if the string
        result = s[0] # This is the longest string
        length = len(s) # Length of the input string

        for i in range(length - 1): # We shall not go further than the index so length-1
            if s[i] <= s[i + 1]: # Checcking if the next char is greater or equal than the current one (determines alphabatical order basically)
                keep = keep + s[i + 1] # If so we want to add current char with next char since they are in order
                if len(keep) > len(result): # If the result is shorter than keep than store keep in result (stores the longest one, for equals keep the previous ones)
                    result = keep
            else: # If not in order then check the next char
                keep = s[i + 1]

        return result

def main():
    pass

if __name__ == "__main__":
    main()
