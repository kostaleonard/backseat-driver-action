"""An entrypoint for the action."""

import subprocess
import sys

clean_args = []

if sys.argv[1] != "--fail_under=":
    clean_args.append(sys.argv[1])
clean_args += sys.argv[2:]
process = subprocess.run(["backseat-driver"] + clean_args)
exit(process.returncode)
