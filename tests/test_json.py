if __name__ == '__main__':
    from argparse import ArgumentParser
    from pathlib import Path
    import json

    parser = ArgumentParser(description="test")
    parser.add_argument('--path', '-p', default="./tests/test.json")
    arguments = parser.parse_args()

    path = Path(arguments.path)

    with open(path, mode='r') as f:
        data = json.load(f)
    
    print(data)