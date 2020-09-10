# Author: Xinyi Yang xvy5166@psu.edu
# Collaborator: Yiqian Li yvl5838@psu.edu
# Collaborator: Harsh Ladani hal5240@psu.edu
# Section: 4
# Breakout: 14

def getLetterGrade(grade):
  if (grade >= 93.0):
    return("A")
  elif (grade >= 90.0):
    return("A-")
  elif (grade >= 87.0):
    return("B+")
  elif (grade >= 83.0):
    return("B")
  elif (grade >= 80.0):
    return("B-")
  elif (grade >= 77.0):
    return("C+")
  elif (grade >= 70.0):
    return("C")
  elif (grade >= 60.0):
    return("D")
  else:
    return("F")

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  if (grade >= 93.0):
    print("Your letter grade for CMPSC 131 is A.")
  elif (grade >= 90.0):
    print("Your letter grade for CMPSC 131 is A-.")
  elif (grade >= 87.0):
    print("Your letter grade for CMPSC 131 is B+.")
  elif (grade >= 83.0):
    print("Your letter grade for CMPSC 131 is B.")
  elif (grade >= 80.0):
    print("Your letter grade for CMPSC 131 is B-.")
  elif (grade >= 77.0):
    print("Your letter grade for CMPSC 131 is C+.")
  elif (grade >= 70.0):
    print("Your letter grade for CMPSC 131 is C.")
  elif (grade >= 60.0):
    print("Your letter grade for CMPSC 131 is D.")
  else:
    print("Your letter grade for CMPSC 131 is F.")

  

if __name__ == "__main__":
 run()
  
  
