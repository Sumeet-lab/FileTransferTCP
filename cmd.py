import subprocess

from termcolor import colored

command = ''

def execute(command):
    process = subprocess.Popen( command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output and error
    if (len(error)!=0):
        print(colored("Error:","red"))
        print(colored(error.decode(),"red"))
        return False

    # print("Output:")
    # print(output.decode())
    return True



if __name__ == '__main__':
    execute(command)

