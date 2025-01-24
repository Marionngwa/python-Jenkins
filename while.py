answered = False

while not answered:
    question = input("Will you like some coffee? Enter 'y' for yes and 'n' for no: ").lower()
    if question == 'y' or question == 'n':  # Corrected logical condition
        answered = True

print("Please proceed to the kiosk.Thank you")

