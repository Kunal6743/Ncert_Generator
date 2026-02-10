import groq
import os
from dotenv import load_dotenv
load_dotenv()
# ================= CONFIG =================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.1-8b-instant"

client = groq.Groq(api_key=GROQ_API_KEY)

# ================= GEOMETRY CHAPTER DETECTION =================
GEOMETRY_KEYWORDS = [
    "Triangles",
    "Triangle",
    "Circles",
    "Circle",
    "Lines",
    "Angles",
    "Quadrilaterals",
    "Trigonometry",
    "Coordinate Geometry",
    "Constructions",
    "Areas Related to Circles"
]

# ================= PROMPT BUILDER =================
def build_prompt(
    class_no,
    subject,
    chapter_name,
    key_topics,
    easy_q,
    medium_q,
    hard_q
):
    total_q = easy_q + medium_q + hard_q

    # ==========================================================
    # ======================= SCIENCE ==========================
    # ==========================================================
    if subject == "Science":
        return f"""
You are a senior CBSE NCERT Science examiner and textbook solution writer.

Class: {class_no}
Subject: Science
Chapter: {chapter_name}

STRICT NCERT RULES:
- Follow NCERT textbook explanation style ONLY
- Use school-level scientific language
- Use NCERT-preferred terminology
- Do NOT use competitive, advanced or outside knowledge
- Do NOT invent facts or examples
- Key points are for reference, not for copying
- Answers must look like CBSE board model answers

NCERT KEY POINTS (REFERENCE):
{key_topics}

TASK:
Generate EXACTLY {total_q} questions from this chapter.

DIFFICULTY DISTRIBUTION (MANDATORY):
- {easy_q} EASY questions:
  • Definitions, facts, direct concepts
  • Answers: 2–3 lines

- {medium_q} MEDIUM questions:
  • Explanation-based, examples, applications
  • Answers: 4–5 lines

- {hard_q} HARD questions:
  • Why/How, reasoning-based
  • Answers: 6–8 lines
  • Strictly NCERT-based

FORMAT (STRICT):
[Easy]
Q1. ...
Answer: ...

[Medium]
Q...
Answer: ...

[Hard]
Q...
Answer: ...
"""

    # ==========================================================
    # ===================== MATHEMATICS ========================
    # ==========================================================
    else:
        is_geometry = any(
            key.lower() in chapter_name.lower()
            for key in GEOMETRY_KEYWORDS
        )

        geometry_rules = """
IMPORTANT GEOMETRY RULES (VERY STRICT):
- Use ONLY standard NCERT theorems and identities
- Do NOT create or assume new identities
- Proof questions must be based on well-known NCERT theorems ONLY
- Allowed examples:
  • Pythagoras Theorem
  • Basic Proportionality Theorem (Thales)
  • Angle sum property of triangle
  • Similar triangles theorems
  • Circle theorems (tangent, chord, angle)
- Trigonometric proofs ONLY from:
  • sin²A + cos²A = 1
  • 1 + tan²A = sec²A
  • 1 + cot²A = cosec²A
- Geometry proof format MUST be:
  To prove → Construction → Proof → Hence proved
- If a statement is NOT a valid NCERT theorem or identity,
  DO NOT generate a proof from it
"""

        non_geometry_rules = """
IMPORTANT RULES:
- Do NOT force theorem or proof questions
- Focus on numerical problems and algebraic steps
- Use ONLY standard NCERT methods
"""

        return f"""
You are a senior CBSE NCERT Mathematics examiner and solution writer.

Class: {class_no}
Subject: Mathematics
Chapter: {chapter_name}

{"".join(geometry_rules if is_geometry else non_geometry_rules)}

VERY IMPORTANT:
- Follow NCERT marking-scheme style
- Use proper mathematical symbols (=, ⇒, ∴)
- Avoid repetition
- Maintain logical step-by-step flow

NCERT CHAPTER CONTEXT:
{key_topics}

TASK:
Generate EXACTLY {total_q} mathematics questions.

DIFFICULTY DISTRIBUTION (MANDATORY):
- {easy_q} EASY:
  • Direct formula-based or one-step numericals
  • 2–3 steps

- {medium_q} MEDIUM:
  • Multi-step numericals, explanations
  • 4–5 steps

- {hard_q} HARD:
  • Proofs / derivations / theorem-based questions
  • Step-by-step logical solution
  • Geometry chapters MUST include proof questions

FORMAT (STRICT):
[Easy]
Q1. ...
Solution: ...

[Medium]
Q...
Solution: ...

[Hard]
Q...
Solution: ...
"""

# ================= AI CALL =================
def generate_questions(
    class_no,
    subject,
    chapter_name,
    key_topics,
    easy_q,
    medium_q,
    hard_q
):
    prompt = build_prompt(
        class_no,
        subject,
        chapter_name,
        key_topics,
        easy_q,
        medium_q,
        hard_q
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
