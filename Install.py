import subprocess

def install_package(package):
    try:
        subprocess.check_call(['apt', 'install', '-y', package])
        print(f"Package '{package}' installed successfully using apt.")
    except subprocess.CalledProcessError:
        print(f"Failed to install package '{package}' using apt.")

def install_pip_package(package):
    try:
        subprocess.check_call(['pip', 'install', package])
        print(f"Package '{package}' installed successfully using pip.")
    except subprocess.CalledProcessError:
        print(f"Failed to install package '{package}' using pip.")

# Example usage
install_package('git')
install_package('cowsay')
install_package('perl')
install_package('rust')
install_pip_package('requests')
install_pip_package('jsons')
install_pip_package('lolcat')
