
import json

def main():
    # This logic matches the "Tone-Shift Summary" theme
    result = {"summary": "The customer is requesting a billing review regarding a missing discount.", "tone": "Professional"}
    print(json.dumps(result))

if __name__ == "__main__":
    main()