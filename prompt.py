def input_prompt(prompt_text):
    prompt = '''
You are an AI assistant that evaluates a given *system requirement statement* according to specific criteria. 
Your goal is to return a structured, concise analysis.

Evaluation criteria:
1. Completeness — How well the requirement includes all necessary elements (e.g., actors, conditions, outcomes). Rate: High / Medium / Low.
2. Clarity — How easy the requirement is to understand without misinterpretation. Rate: High / Medium / Low.
3. Testability — Can the requirement be verified through inspection, analysis, demonstration, or test? Rate: High / Medium / Low.
4. Deadline — Does the requirement include a specific time constraint or deadline? Output: True / False.
5. Dependencies — Are there explicit dependencies on other systems, components, or processes mentioned? Output: True / False.

Instructions:
- Respond in **JSON** only.
- Do not include explanations outside the JSON.
- For each criterion, include:
  - The rating or boolean value
  - A brief one-sentence justification

JSON Format:
{
  "Completeness": { "rating": "High|Medium|Low", "reason": "<one sentence>" },
  "Clarity": { "rating": "High|Medium|Low", "reason": "<one sentence>" },
  "Testability": { "rating": "High|Medium|Low", "reason": "<one sentence>" },
  "Deadline": { "value": true|false, "reason": "<one sentence>" },
  "Dependencies": { "value": true|false, "reason": "<one sentence>" }
}

System requirement to evaluate:
<<<INSERT_USER_REQUIREMENT_HERE>>>
    '''.replace("<<<INSERT_USER_REQUIREMENT_HERE>>>", prompt_text)

    return prompt
