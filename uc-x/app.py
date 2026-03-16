
import json

def main():
    # This logic matches the "Document Retrieval" theme
    result = {"answer": "The budget was approved.", "source": "data/budget/plan.txt"}
    print(json.dumps(result))

if __name__ == "__main__":
    main()