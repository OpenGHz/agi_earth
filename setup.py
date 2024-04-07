from setuptools import setup,find_packages

setup(
    name='discover_agisphere',
    version='1.0.0',
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=['numpy'],
    author='OpenGHz',
    author_email='ghz23@mails.tsinghua.edu.cn',
    description='Discover robotics ecosystem.',
    url='https://gitlab.com/OpenGHz/airbot_play_vision_python.git',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8'
)