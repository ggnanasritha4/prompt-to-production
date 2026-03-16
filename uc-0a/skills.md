
skills:
  - name: Keyword_Triage
    description: Analyzes input strings for high-priority department keywords like 'refund' or 'login'.
    input: Raw customer complaint string.
    output: Department category (Billing, Tech, Delivery, or General).
    error_handling: Defaults to 'General' if no keywords are identified.

  - name: Sentiment_Assessor
    description: Evaluates the urgency of the text to assign a priority score from 1 to 5.
    input: Raw customer complaint string.
    output: Integer (Priority score).
    error_handling: Returns 3 (Medium) for neutral or ambiguous text.