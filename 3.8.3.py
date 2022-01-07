"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def calculate_dose(weight, time, total_dose_24):
    """
    this function takes weight, last time of paracetemol consumption and dosage in past hour to calculate for new dosage
    """
    x=0
    if time>= 6 and total_dose_24<=4000:
        x=(weight*15)
        if (x+total_dose_24)<=4000:
            return x
        else:
            x=4000-total_dose_24
            return x

    else:
        return x

def main():
    weight= int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total = int(input("The total dose for the last 24 hours (mg): "))
    dosage= calculate_dose(weight,time,total)
    print("The amount of Parasetamol to give to the patient:", dosage)

if __name__ == "__main__":
    main()
