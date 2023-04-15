"""An entrypoint for the action."""

import glob
import subprocess
import sys

clean_args = []
if sys.argv[1] != "--fail_under=":
    clean_args.append(sys.argv[1])
expanded_filenames = []
for filenames_with_potential_spaces in sys.argv[2:]:
    for filename in filenames_with_potential_spaces.strip().split(" "):
        filenames = glob.glob(filename, recursive=True)
        expanded_filenames.extend(filenames)
clean_args += expanded_filenames
process = subprocess.run(["backseat-driver"] + clean_args, stdout=sys.stdout, stderr=sys.stderr)
exit(process.returncode)
