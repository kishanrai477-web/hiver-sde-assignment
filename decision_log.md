# Decision Log

Documenting key decisions made during the project.

## Date: 2024

### Architecture Decisions

- **Modular Structure**: Separated concerns into distinct modules (data, intents, retrieval, agent, evaluation)
- **Intent Classification**: Using keyword-based approach initially, with plans for ML-based classification
- **Retrieval System**: Implementing semantic search using embeddings
- **Agent Framework**: Building on LLM-based response generation with escalation logic

### Technical Decisions

- **Language**: Python for all components
- **Framework**: Using sklearn for ML, transformers for NLP
- **Data Format**: JSONL for dataset files
- **Environment Management**: Using .env files for configuration

### Next Steps

- Implement actual embedding generation
- Train intent classifier on labeled data
- Set up LLM integration
- Build comprehensive evaluation pipeline
- ## Decision 11 — Use conversation context for intent classification

**Decision:** Include recent conversation context when classifying customer follow-up messages.

**Why:** A follow-up such as "Done all that. Still telling me there..." is ambiguous when viewed alone, but the previous message identified the issue as a website problem.

**Observed failure:** Tweet 119321 was initially classified as `general_support` instead of `website_issue`.

**Fix:** Added a context-aware classifier that combines the current message with previous conversation context.

**Result:** The same follow-up was correctly classified as `website_issue`.

**Trade-off:** Using more context improves classification but increases input length and can introduce irrelevant information if too much history is included.
