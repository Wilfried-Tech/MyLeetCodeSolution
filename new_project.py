
import argparse
import sys, os

arg_parser = argparse.ArgumentParser(description="""
    LeetCode Projects Creator \n
    ----------------------------------
""")

arg_parser.add_argument("--name", required=True)

args = arg_parser.parse_args()

base_dir = os.path.abspath(os.path.dirname(__file__))
dir = os.path.join(base_dir, getattr(args, "name").replace('.', '').title().replace(' ', "_"))
template_dir = os.path.join(base_dir, "_template")
try:
    os.mkdir(dir)
except:
    pass

for file in [os.path.join(template_dir, file) for file in os.listdir(template_dir)]:
    if os.path.isfile(file):
        with open(file,'r') as tf:
            with open(os.path.join(dir, os.path.basename(file)), "w") as dest:
                dest.write(tf.read())
print("done")