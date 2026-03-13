from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
  Please summarize the research paper titled "{paper_input}" with the following specifications:
  Explanation Style: {style_input}
  Explanation Length:{length_input}
  1. Mathematical Details:
     - Include relevant mathematical equations if present in the paper.
     - Explain the mathematical conecepts using simple, intutive code snippets where applicalbe.
  2. Analogies:
           - Use relatbale analogies to simplify complex ideas.

    If certain infromation is not available in the paper, respond with:"Insufficiant information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and lenght.
""",
input_variables=['paper_input', 'style_input', 'length_input'],

)

template.save('template.json')