prompt = """
You are a highly knowledgeable and creative assistant. Your goal is to provide precise, accurate, and engaging articles while adhering to the following guidelines:

1. **Clarity**: Ensure all information is clear, concise, and well-structured.
2. **Relevance**: Address the request directly and avoid unnecessary details.
3. **Depth**: Where applicable, provide a comprehensive response with supporting examples or explanations.

Task: Rewrite the following text for [purpose, e.g., SEO optimization, formal communication, creative storytelling] while ensuring it avoids [specific issues, e.g., plagiarism, redundancy, irrelevant information].

Input Text:
"[Insert text here]"

Output Requirements:
- Length: [Specify desired word count or range]
- Tone: [Specify tone, e.g., formal, friendly, persuasive]
- Style: [Specify style, e.g., conversational, technical, poetic]
- Additional Details: [List any specific instructions, e.g., include a call-to-action, focus on specific keywords]

"""

def article_prompt(text):
    return f"""
You are a highly knowledgeable and creative assistant. Your goal is to provide precise, accurate, and engaging articles while adhering to the following guidelines:

1. **Clarity**: Ensure all information is clear, concise, and well-structured.
2. **Relevance**: Address the request directly and avoid unnecessary details.
3. **Depth**: Where applicable, provide a comprehensive response with supporting examples or explanations.
3. dont return any additional text. just write the article.

Task: Rewrite the following article for SEO optimization while ensuring it avoids plagiarism.

Input article:
"{text}"

""".strip()

def with_two_text(text, text1):

    return f"""
You are a highly knowledgeable and creative assistant. Your goal is to provide precise, accurate, and engaging articles while adhering to the following guidelines:

1. **Clarity**: Ensure all information is clear, concise, and well-structured.
2. **Relevance**: Address the request directly and avoid unnecessary details.
3. **Depth**: Where applicable, provide a comprehensive response with supporting examples or explanations.
3. dont return any additional text. just write the article.

Task: Rewrite the following articles into one article for SEO optimization while ensuring it avoids plagiarism.

Input articles:
"{text}", 
"{text1}"

""".strip()