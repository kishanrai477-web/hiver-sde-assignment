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
