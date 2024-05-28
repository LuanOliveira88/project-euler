import sys 
import os 

if len(sys.argv) == 3:
    id = sys.argv[1]
    title = sys.argv[2]
    path_ = f".\\problems\\problem_{id}"    
    if os.path.exists(path=path_):
        print('Não foi possível criar esse diretório, pois já existe')
    else:
        os.mkdir(path=path_)
        with open(file=os.path.join(path_, "main.py"), mode="w") as file:
            file.write("def solution():\n    ...")
        with open(file=os.path.join(path_, "main_test.py"), mode="w") as file:
            file.write("from main import solution\n\n")
            file.write("def test_solution():\n    ...")
        with open(file=os.path.join(path_, "README.md"), mode="w") as file:
            file.write(f"# {id}. {title}")