
def  StringValadation(str):
    try:
        int(str)
        return  "valid integer"
    except ValueError:
        try:
            float(str)
            return "valid float"
        except ValueError:
            return "Invalid input"
        
    
print(StringValadation("1"))
print(StringValadation("jfjf"))