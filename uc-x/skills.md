

skills:
  - name: Semantic_Doc_Search
    description: Searches the /data directory for files containing keywords relevant to the user's query.
    input: User search query.
    output: Filename and relevant text snippets.
    error_handling: Returns 'No matching documents' if search fails.

  - name: Citation_Formatter
    description: Appends a source line to the agent's response to provide auditability.
    input: Filename.
    output: String (e.g., 'Source: data/policy.txt').
    error_handling: Returns 'Source: Unknown' if file metadata is missing.