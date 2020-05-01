import configparser
import json
import ast
import hashlib

config1 = configparser.ConfigParser()


config2 = configparser.ConfigParser()


def hash(password):
    return hashlib.md5(password.encode()).hexdigest()


def updateConfigFile(fileName, section,key, textdata):
    config = configparser.ConfigParser()
    config.read(fileName)  # Add this line
    cnfFile = open(fileName, "w")
    config.set(section,key,textdata)
    config.write(cnfFile)
    cnfFile.close()

def initiate_section(filename,section_name):
    config = configparser.ConfigParser()
    config[section_name] = {}
    with open(filename, 'a') as configfile:
        config.write(configfile)

def read_file(filename):
    config = configparser.ConfigParser()
    return config.read(filename)

def main(user):
    if user['user type']=='Patient':
        patient_username = username
    else:
        patient_username = input("Please enter a Patient's username : ")
    stop = False
    while not (stop):
        try:
            config1.read('assignment6.ini')
            patient_user = ast.literal_eval(config1['Users'][patient_username])
            if patient_user['privilege level'] == 'patient':
                config1.read('assignment6.ini')
                priviladges = ast.literal_eval(config1['Priviladge Levels'][user['user type']])
                read_options = ''
                option_number = 1
                for i in priviladges['read']:
                    read_options += '(' + str(option_number) + ')View ' + i + '\n'
                    option_number += 1
                write_options = ''
                for i in priviladges['write']:
                    write_options += '(' + str(option_number) + ')Edit ' + i + '\n'
                    option_number += 1
                select_option = input(
                    "What do you want? Please enter the option number\n" + read_options + write_options)
                try:
                    selected_option_number = int(select_option)
                    if 0 < selected_option_number <= len(priviladges['read']):
                        selected_option = priviladges['read'][selected_option_number - 1]
                        if selected_option == 'personal details':
                            config2.read('patient_details.ini')
                            personal_details_list = ast.literal_eval(config2[patient_username]['personal details'])
                            print(personal_details_list)
                        elif selected_option == 'sickness details':
                            config2.read('patient_details.ini')
                            sickness_details_list = ast.literal_eval(config2[patient_username]['sickness details'])
                            print(sickness_details_list)
                        elif selected_option == 'drug prescriptions':
                            config2.read('patient_details.ini')
                            drug_prescriptions_list = ast.literal_eval(config2[patient_username]['drug prescriptions'])
                            print(drug_prescriptions_list)
                        elif selected_option == 'lab test prescriptions':
                            config2.read('patient_details.ini')
                            lab_test_prescriptions_list = ast.literal_eval(config2[patient_username]['lab test prescriptions'])
                            print(lab_test_prescriptions_list)
                        else:
                            print('invalid input')
                    elif len(priviladges['read']) < selected_option_number < option_number:
                        selected_option = priviladges['write'][
                            selected_option_number - len(priviladges['read']) - 1]
                        if selected_option == 'sickness details':
                            sickness_details = input("Enter sickness details:")
                            config2.read('patient_details.ini')
                            sickness_details_list = ast.literal_eval(config2[patient_username]['sickness details'])
                            sickness_details_list += [sickness_details]
                            updateConfigFile("patient_details.ini", patient_username, 'sickness details',
                                             str(sickness_details_list))
                        elif selected_option == 'drug prescriptions':
                            drug_prescriptions = input("Enter drug prescriptions:")
                            config2.read('patient_details.ini')
                            drug_prescriptions_list = ast.literal_eval(config2[patient_username]['drug prescriptions'])
                            drug_prescriptions_list += [drug_prescriptions]
                            updateConfigFile("patient_details.ini", patient_username, 'drug prescriptions',
                                             str(drug_prescriptions_list))
                        elif selected_option == 'lab test prescriptions':
                            lab_test_prescriptions = input("Enter lab test prescriptions:")
                            config2.read('patient_details.ini')
                            lab_test_prescriptions_list = ast.literal_eval(config2[patient_username]['lab test prescriptions'])
                            lab_test_prescriptions_list += [lab_test_prescriptions]
                            updateConfigFile("patient_details.ini", patient_username, 'lab test prescriptions',
                                             str(lab_test_prescriptions_list))
                        else:
                            print('invalid input')
                    else:
                        selected_option = 0
                        print("invalid input")
                    # print(selected_option)
                except:
                    print("invalid input")
            else:
                print("Username that you enterd is not a patient")
                continue

        except:
            print("Patient's username is not valid")
            while True:
                try_again = input("Do you want to try again? (y/n)")
                if try_again == 'y' or try_again == 'Y':
                    break
                elif try_again == 'n' or try_again == 'N':
                    stop = True
                    break
                else:
                    continue


username = input("Enter your Username: ")
password = input("Enter your Password: ")

try:
    config1.read('assignment6.ini')
    user=ast.literal_eval(config1['Users'][username])
    if (hash(password))==(user['password']):
        if user['user type']=='Doctor':
            main(user)
        elif user['user type']=='Pharmacist':
            main(user)
        elif user['user type']=='MLT':
            main(user)
        elif user['user type']=='Nurse':
            stop = False
            while not (stop):
                create_new_patient = input("What do you want? Please enter the option number\n(1)Create a new Patient\n(2)View a Patient's Details\n")
                if create_new_patient=='1':
                    patient_NIC = input("Enter Patient's NIC: ")
                    patient_fullname=input("Enter Patient's full name: ")
                    patient_birthday = input("Enter Patient's Date of Birth: ")
                    patient_phone_number = input("Enter Patient's Phone Number: ")
                    patient_address = input("Enter Patient's address: ")
                    patient = {"NIC":patient_NIC,"fullname":patient_fullname,"birthday":patient_birthday,"phone_number":patient_phone_number,"address":patient_address}
                    while True:
                        create_patient_username = input("Enter username for Patient: ")
                        try:
                            config1.read('assignment6.ini')
                            ast.literal_eval(config1['Users'][create_patient_username])
                            print('username already in use. Try another')
                            continue
                        except:
                            break
                    create_patient_password = hash(input("Enter password for Patient: "))
                    try:
                        updateConfigFile("assignment6.ini","Users",create_patient_username,"{'password': '"+create_patient_password+"', 'user type': 'Patient', 'privilege level': 'patient'}")
                    except:
                        initiate_section("assignment6.ini", "Users")
                        updateConfigFile("assignment6.ini", "Users", create_patient_username,"{'password': '" + create_patient_password + "', 'user type': 'Patient', 'privilege level': 'patient'}")
                    initiate_section("patient_details.ini", create_patient_username)
                    updateConfigFile("patient_details.ini", create_patient_username, "personal details",str(patient))
                    updateConfigFile("patient_details.ini", create_patient_username, "sickness details", "[]")
                    updateConfigFile("patient_details.ini", create_patient_username, "drug prescriptions", "[]")
                    updateConfigFile("patient_details.ini", create_patient_username, "lab test prescriptions", "[]")
                elif create_new_patient=='2':
                    main(user)
        elif user['user type']=='Patient':
            main(user)
        else:
            print("invalid user type")
    else:
        print('Password is Wrong')

except:
    print('Username is wrong')
