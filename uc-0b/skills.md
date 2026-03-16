
skills:
  - name: Tone_Transformer
    description: Replaces aggressive or emotional language with neutral, business-appropriate terminology.
    input: Highly emotional customer text.
    output: Professional, neutral text block.
    error_handling: If input is already neutral, it returns the input without changes.

  - name: Core_Request_Extractor
    description: Distills a long narrative down to the single primary request or outcome desired by the user.
    input: Text string.
    output: A single-sentence summary of the user's intent.
    error_handling: Returns 'Unknown Request' if no clear intent is found.
