import random
# Albion is Fem Med. , Wallkill is Med. , Hillbrook is Juvie, Rikers is awaiting trial, Attica is Max.
# Bellevue is hospital prison , Sing Sing is for sexual offenses M, Taconic for sex offenses F
#Bedford Hills is Fem Max.
prisons = ["Rikers","Attica","Sing Sing","Bellevue","Hillbrook","Wallkill",
           "Albion","Bedford Hills","Taconic"]
offenses = ["Capital Murder","Murder","Theft","Assault","Fraud","Kidnapping","Manslaughter","Arson","Drug Poss",
            "Hate Crime","Terrorism","Perjury","Weapon Poss","Sex Assualt","Abuse","Failed to register as Sex Offender",
            "Prostitution","Trafficking","Escape","Forgery","Soliciting","Drug Use","Larceny","Robbery",
            "Bribery","Poss of obscene images","Endagering a child","Money Laundering","Sex Abuse","Promoting Gambling",
            "Poss of a Controlled Substance","Judicial offense","Obsturction","Burglary",
            "False Incident Report","Stalking","Public Lewdness/Exposure","Sex Coersion"]

mental = ["Y","N","N"]
awaiting_trial = ["Y","N","N"]
gender = ["M","F"]
on_registry = ["Y","N","N"]

def svu(rounds):
    score = 0
    print("Help Benson and Stabler put away these people!")
    for i in range(rounds):
        print(f"Prisoner #{i + 1}")
        age = random.randint(12,60)
        sex = random.choice(gender)
        awaiting = random.choice(awaiting_trial)
        mental_issues = random.choice(mental)
        offender = random.choice(on_registry)
        offense = random.choice(offenses)

        print(f"Age: {age}")
        print(f"Gender: {sex}")
        print(f"Offense: {offense}")
        print(f"Needs Trial?: {awaiting}")
        print(f"Mentally Ill?: {mental_issues}")
        print(f"Sex Offender?: {offender}")

        if awaiting == "Y":
            correct_prison = "Rikers"
        elif mental_issues == "Y":
            correct_prison = "Bellevue"
        elif (int(age)) < 18:
            correct_prison = "Hillbrook"
        elif offender == "Y":
            correct_prison = "Sing Sing"

        elif offense in ["Endagering a child","Sex Assualt","Public Lewdness/Exposure","Sex Coersion",
                          "Sex Abuse","Kidnapping","Failed to register as Sex Offender","Poss of obscene images"
                          "Prostitution"] and  sex == "M":
            correct_prison = "Sing Sing"

        elif offense in ["Endagering a child","Sex Assualt","Public Lewdness/Exposure","Sex Coersion",
                          "Sex Abuse","Kidnapping","Failed to register as Sex Offender","Poss of obscene images"
                          "Prostitution"] and  sex == "F":
            correct_prison = "Taconic"

        elif offense in ["Capital Murder","Murder","Hate Crime","Terrorism","Manslaughter","Arson",
                          "Assault","Robbery","Trafficking","Escape"] and sex == "M":
            correct_prison = "Attica" 

        elif offense in ["Capital Murder","Murder","Hate Crime","Terrorism","Manslaughter","Arson",
                          "Assault","Robbery","Trafficking","Escape"] and sex == "F":
            correct_prison = "Bedford Hills"

        elif offense in ["Theft","Fraud","Drug Poss","Perjury","Weapon Poss","Abuse","Forgery",
                         "Soliciting","Drug Use","Larceny","Bribery","Money Laundering","Promoting Gambling",
                         "Poss of a Controlled Substance","Judicial offense","Obsturction","Burglary",
                         "False Incident Report","Stalking"] and sex == "M":
            correct_prison = "Wallkill"

        elif offense in ["Theft","Fraud","Drug Poss","Perjury","Weapon Poss","Abuse","Forgery",
                         "Soliciting","Drug Use","Larceny","Bribery","Money Laundering","Promoting Gambling",
                         "Poss of a Controlled Substance","Judicial offense","Obsturction","Burglary",
                         "False Incident Report","Stalking"] and sex == "F":
            correct_prison = "Albion"

        choice = input("Send prisoner to where?").strip()
        if choice.lower() == correct_prison.lower():
            score += 1
            print("Great!\n")
            
        else:
            print(f"Correct prison was: {correct_prison}")

    print(f"Game over, you got: {score}/{rounds}!")

svu(50)