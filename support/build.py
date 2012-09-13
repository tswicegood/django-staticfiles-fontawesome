"""
Relocates the files for a given version of Masonry from vendor/masonry
into a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "2.0.0"


def cp(src):
    cmd = [
        "cp -R vendor/FontAwesome/%s fontawesome/static/fontawesome/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./fontawesome/static/fontawesome"], shell=True)
    subprocess.call(
            ["cd vendor/FontAwesome && git checkout %(version)s" %args],
            shell=True)
    [cp(a) for a in ["css", "font", "less", "sass"]]

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
