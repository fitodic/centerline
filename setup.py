from setuptools import setup


setup(
    entry_points="""
        [console_scripts]
        create_centerlines=centerline.converters:create_centerlines
    """
)
