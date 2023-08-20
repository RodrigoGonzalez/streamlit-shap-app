"""Build script for Cython files.

This script is called by poetry when building the package. It will compile
Cython files if Cython is installed. Otherwise, it will do nothing.

See #distributing-cython-modules for more information.
https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html

Taken from:
https://stackoverflow.com/questions/63679315/how-to-use-cython-with-poetry

To use add the following to pyproject.toml:

[tool.poetry]
...
build = 'build.py'

[build-system]
requires = ["poetry>=0.12", "cython"]
build-backend = "poetry.masonry.api"

Now, when you do poetry build, nothing happens. But if you install this package
elsewhere, it gets compiled.

You can also build it manually with:

$ cythonize -X language_level=3 -a -i mylibrary/myfile.py
Finally, it seems that you can't publish binary packages to PyPi. The solution
is to limit your build to "sdist":

$ poetry build -f sdist
$ poetry publish
"""
import os

# See if Cython is installed
try:
    from Cython.Build import cythonize
# Do nothing if Cython is not available
except ImportError:
    # Got to provide this function. Otherwise, poetry will fail
    def build(setup_kwargs):
        """Do nothing."""


# Cython is installed. Compile
else:
    from distutils.command.build_ext import build_ext

    # This function will be executed in setup.py:
    def build(setup_kwargs):
        """Build Cython files."""

        # The files you want to compile
        extensions = [
            "src/flake8_custom_import_rules/core/error_messages.py",
            "src/flake8_custom_import_rules/core/import_rules.py",
            "src/flake8_custom_import_rules/core/node_visitor.py",
            "src/flake8_custom_import_rules/core/nodes.py",
            "src/flake8_custom_import_rules/core/restricted_import_visitor.py",
            "src/flake8_custom_import_rules/core/rules_checker.py",
        ]

        # gcc arguments hack: enable optimizations
        os.environ["CFLAGS"] = "-O3"

        # Build
        setup_kwargs.update(
            {
                "ext_modules": cythonize(
                    extensions,
                    language_level=3,
                    compiler_directives={"linetrace": True},
                ),
                "cmdclass": {"build_ext": build_ext},
            }
        )
