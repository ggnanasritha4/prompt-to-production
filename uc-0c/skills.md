
skills:
  - name: Pattern_Match_Extractor
    description: Uses regex to identify specific alphanumeric patterns like Order IDs (ORD-XXXX).
    input: Unstructured text.
    output: String (Order ID).
    error_handling: Returns null if the pattern is not found.

  - name: Financial_Parser
    description: Identifies currency symbols and converts the following digits into a clean float value.
    input: Text containing monetary values.
    output: Float (e.g., 99.99).
    error_handling: Returns 0.0 if no valid price is detected.