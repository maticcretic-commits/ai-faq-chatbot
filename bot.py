"""
AI FAQ Chatbot - demo starter.
Run:  python bot.py
Type 'quit' to exit.

Learning path (TODOs):
  1. Add your own FAQs to faqs.json
  2. Replace keyword matching with OpenAI embeddings for smarter answers
  3. Connect to WhatsApp/Telegram via n8n or Make
"""

import json
import re

with open("faqs.json") as f:
    FAQS = json.load(f)

HANDOFF_MESSAGE = (
    "I don't have a confident answer for that yet. "
    "I've flagged this for the team - someone will reply shortly! "
    "You can also email us at hello@example.com."
)


def find_answer(question: str):
    """Simple keyword matching. Returns (answer, confidence)."""
    words = set(re.findall(r"\w+", question.lower()))
    best, best_score = None, 0
    for item in FAQS:
        score = len(words & set(item["keywords"]))
        if score > best_score:
            best, best_score = item, score
    if best and best_score >= 1:
        return best["answer"], "high"
    return None, "low"


def main():
    print("Bot: Hi! Ask me anything (type 'quit' to exit).")
    while True:
        q = input("You: ").strip()
        if q.lower() in ("quit", "exit"):
            print("Bot: Bye!")
            break
        answer, confidence = find_answer(q)
        if confidence == "high":
            print(f"Bot: {answer}")
        else:
            print(f"Bot: {HANDOFF_MESSAGE}")
            # TODO: send a real alert to the owner (Slack / email webhook)
            print("      [handoff logged -> owner notified]")


if __name__ == "__main__":
    main()
