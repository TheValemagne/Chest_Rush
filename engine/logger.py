global Session_Infos
Session_Infos = None

def log_Operation (operation, op_time) :

    """Function used to store informations of the session"""

    try :

        File = open(Session_Infos[0],"r")

        Data = File.readlines()

    except :

        First_Line = "Builded " + Session_Infos[1] + "\n\n"

        Second_Line = "Build number : " + Session_Infos[2] + "\n\n"

        Third_Line = "LOGS REGISTERED :\n\n"

        Data = [First_Line,Second_Line,Third_Line]

        pass

    Info = op_time + operation + "\n"

    Data.append(Info)

    File = open(Session_Infos[0],"w")

    File.writelines(Data)

    File.close()