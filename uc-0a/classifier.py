
import json

def main():
    # This logic matches the workshop's "Complaint" theme
    result = {"category": "Billing", "priority": 5, "status": "classified"}
    print(json.dumps(result))

if __name__ == "__main__":
    main()
