import random
# Albion is Fem Med. , Wallkill is Med. , Hillbrook is Juvie, Rikers is awaiting trial, all else is Max.
# Bellevue is hospital prison , Edgecombe is Fem Min. , Queensboro is Min.
prisons = ["Rikers","Greenhaven","Attica","Sing Sing","Bellevue","Hillbrook","Wallkill",
           "Albion","Queensboro",""]
offenses = ["Murder","Theft","Assault","Fraud","Kidnapping","Manslaughter","Arson","Drug Poss.",
            "Hate Crime","Terrorism","Perjury","Weapon Poss.","Sex Assualt","Abuse","Failed to register as Sex Offender",
            "Prostitution","Trafficking","Escape","Forgery","Soliciting","Drug Use","Larceny","Robbery",
            "Bribery","Poss of obscene images","Endagering a child","Money Laundering","Sex Abuse","Promoting Gambling",
            "Poss of a Controlled Substance","Judicial offense","Obsturction","ID Theft","Burglary",
            "False Incident Report","Stalking","Public Lewdness/Exposure",]

mental = ["Y","N"]
awaiting_trial = ["Y","N"]
age = random.randint(12,60)
gender = ["M","F"]
on_registry = ["Y","N"]


