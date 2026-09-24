# AI FAQ Chatbot (Demo)

[![GitHub stars](https://img.shields.io/github/stars/maticcretic-commits/ai-faq-chatbot?style=social)](https://github.com/maticcretic-commits/ai-faq-chatbot/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/maticcretic-commits/ai-faq-chatbot)](https://github.com/maticcretic-commits/ai-faq-chatbot/commits/main)
[![Cost: Free](https://img.shields.io/badge/cost-%E2%82%B90-brightgreen)](https://github.com/maticcretic-commits/ai-faq-chatbot)


A demo chatbot that answers common customer questions automatically — and hands off to a human when it doesn't know the answer.

## Who is this for?
Small businesses that get the same questions over and over ("What are your hours?", "Do you deliver?", "How do I track my order?").

## How it works
1. Customer types a question
2. The bot matches it against a FAQ knowledge base (`faqs.json`)
3. Confident match → instant answer, 24/7
4. No confident match → polite handoff message + the question gets logged for the owner

## Try it
```bash
python bot.py
```
Type `quit` to exit.

## Tech
Python, no frameworks needed for the demo. The same logic plugs into n8n / Make / Zapier, or upgrades to an LLM (OpenAI) for smarter answers.

## Roadmap
- [ ] Connect to OpenAI for natural-language answers
- [ ] WhatsApp / Telegram integration
- [ ] Log unanswered questions to keep improving the FAQ

*Built while learning automation — feedback welcome!*

## ❤️ Support My Work

> If you find this project useful, please consider supporting my work with a Bitcoin donation:
>
> **₿ `BC1Q6Q75K8ZJXVW7W02LMDPRPY6XX6QK4LZZ2RMVAY`**

## ☕ Support my work
If this project was useful, you can support it with Bitcoin: `bc1q6q75k8zjxvw7w02lmdprpy6xx6qk4lzz2rmvay`
