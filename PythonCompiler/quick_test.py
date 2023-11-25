from collections import deque
import subprocess
import os


def quick_test(path="./examples/", log_path="./log"):
    # Tries compiling every example in path.
    # Dumps the log outputs to ./log

    error_files = deque()

    with open(log_path, "w") as file:
        file.write("")

    with open(log_path, "a") as file:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            
            process = subprocess.run(['./Corth/build/corth', 'compile-nasm', full_path], capture_output=True)

            output = process.stdout.decode()
            error = process.stderr.decode()

            file.write(f"File: '{full_path}'\n")
            file.write(output)
            file.write(error)

            if process.returncode:
                error_files.append(full_path)

                print(f"File '{full_path}' returned error code '{process.returncode}'")
                print(output)
                print(error)

    print(f"{len(error_files)} files returned error.")

    return len(error_files)
