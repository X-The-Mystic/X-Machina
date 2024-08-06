from distutils.core import setup

setup(
    name="TurtleDoS",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["turtledos=turtledos:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool.",
    author="X the Mystic",
    author_email="</XtM>@cerberusdev.com",
    url="https://github.com/X-The-Mystic/X-Machina",
    keywords=["dos", "http", "slowloris", "turtledos"],
    license="Unlicence",
)
