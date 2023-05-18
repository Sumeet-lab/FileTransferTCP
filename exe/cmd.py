import subprocess

command = 'ping'

def execute(command):
    process = subprocess.Popen( command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output and error
    if (len(output)!=0):
        print("Output:")
        print(output.decode())

    if (len(error)!=0):
        print("Error:")
        print(error.decode())

if __name__ == '__main__':
    execute(command)

