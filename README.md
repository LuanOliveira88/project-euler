# Project Euler: Problems and Solutions 


## Introduction

### About Project Euler

[Project Euler](https://projecteuler.net/) is a collection of challenging mathematical and computational problems intended to be solved with computer programs. The project was created by Colin Hughes in 2001 and has since grown to include a wide range of problems, from simple to highly complex. Each problem requires more than just mathematical insights to solve, often necessitating a combination of clever algorithms, efficient programming, and deep understanding of the underlying mathematics.

### Purpose of This Repository

This repository is dedicated to solving and discussing various problems from Project Euler. The goal is to develop and share methods and algorithms that can tackle these problems, which are not only intellectually stimulating but also applicable to real-world scenarios faced by software and systems developers/analysts. By working through these problems, one can improve problem-solving skills, learn new programming techniques, and deepen their understanding of both computer science and mathematics.


## Prerequisites

- Python 3.x
- The necessary packages can be installed using the simple command

```
pip install -r requirements.txt
```

## Setup

Clone the repository to your local machine:

```
git clone https://github.com/LuanOliveira88/project-euler.git
cd project-euler
```

## Usage

You can add a directory structure for a problem using its ID with a simple command:

```
python scripts\main.py <id>
```

For example, to add problem 1 to the project, it is:

```
python scripts\main.py 1 
```

This command will create a folder containing a ``main.py`` file for developing the solution to the problem, a ``main_test.py`` file for tests, and a ``README.md`` file for problem descriptions, such as the statement, algorithms used, or results obtained. The automation script fetches the problem's title and statement.

After running the command for problem 1, your directory structure will look like this:

```
project-euler/
│
├── problems/
│   ├── problem_1/
│   │   ├── main.py
│   │   ├── main_test.py
│   │   └── README.md
│   └── ...
└── scripts/
    ├── __init__.py
    └── main.py
```

## Contact

If you have any questions or suggestions, feel free to contact me at olivrluan@gmail.com or, alternatively, you can open an issue in this repository to discuss any problems or suggestions.

