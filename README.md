# Hiver SDE Assignment

A comprehensive project for data processing, intent classification, retrieval systems, and agent-based evaluation.

## Project Structure

```
hiver-sde-assignment/
├── data/              # Data files and datasets
├── src/               # Source code
│   ├── data/         # Data download and preprocessing
│   ├── intents/      # Intent discovery and classification
│   ├── retrieval/    # Embedding and retrieval systems
│   ├── agent/        # Agent prompts and generation
│   └── evaluation/   # Evaluation metrics and reporting
├── notebooks/        # Jupyter notebooks for exploration
├── evaluation/       # Evaluation results and predictions
└── report/           # Final reports
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
```

## Components

- **Data Processing**: Download and preprocess datasets
- **Intent Discovery**: Discover and classify user intents
- **Retrieval**: Embed and retrieve relevant documents
- **Agent Generation**: Generate responses using LLM agents
- **Evaluation**: Comprehensive evaluation framework
# Hiver SDE Assignment — AI Customer Support Agent

An AI-powered customer support prototype built using the Customer Support on Twitter dataset. The system focuses on **intent classification, historical-resolution retrieval, response drafting, and safe escalation**.

The prototype uses **Tesco** as the selected brand.

> **Evaluation note:** The working sample available for this prototype contains only 93 tweets, resulting in 8 Tesco customer messages. Therefore, the reported metrics are a small pilot evaluation and should not be interpreted as production-level performance. The intended evaluation should use 150–250 independently labelled messages from the full dataset.

---

## 1. Problem Statement

The goal is to build an AI support agent that can:

1. Classify an incoming customer message into a support intent.
2. Retrieve relevant historical Tesco resolutions.
3. Draft a helpful response grounded in those historical resolutions.
4. Decide whether the request can be automatically handled or should be escalated.
5. Provide a reason for the escalation decision.
6. Evaluate the system using automated metrics, baselines, human review, and an LLM-as-a-judge.

---

## 2. System Workflow

```text
Customer Message
       |
       v
Conversation Context
       |
       v
Intent Classification
       |
       v
Historical Resolution Retrieval
       |
       v
Confidence / Safety Checks
       |
       +----------------------+
       |                      |
       v                      v
   AUTO_HANDLE             ESCALATE
       |                      |
       v                      v
Draft Response          Human Review
       |
       v
Final Support Response

| Intent                     | Description                                                         |
| -------------------------- | ------------------------------------------------------------------- |
| `age_verification`         | Questions about age restrictions, ID checks, or Think 25 policy     |
| `website_issue`            | Problems using the Tesco website or online services                 |
| `store_navigation`         | Difficulty finding a product, section, or item in a Tesco store     |
| `product_information`      | Questions about products, availability, or product details          |
| `account_or_personal_info` | Requests involving customer account details or personal information |
| `general_support`          | Other Tesco support questions that do not fit the above categories  |

4. Historical Resolution Retrieval

Historical Tesco responses are used as the knowledge source for response generation.

The prototype uses:

TF-IDF vectorization
Unigram and bigram features
Cosine similarity
A minimum similarity threshold of 0.10

If no sufficiently similar historical resolution is found, the system avoids automatic handling and escalates the request.

Trade-off

TF-IDF is lightweight and interpretable, but it can struggle when customers describe the same issue using substantially different wording.

A future version would use semantic embeddings for improved retrieval.
5. Response Generation

The agent generates a fresh support response based on:

Customer intent
Retrieved historical resolution
The customer's current message

The system does not simply copy the historical response. It uses the historical response as grounding evidence and generates a concise support-oriented reply.

6. Auto-Handle vs Escalation

The agent makes a binary decision:

AUTO_HANDLE

or

ESCALATE
Escalation rules

The prototype escalates when:

The request involves account or personal information.
The customer message is too vague to safely resolve automatically.
Historical retrieval confidence is below the similarity threshold.
The message contains potentially sensitive issues such as fraud, refunds, payment problems, legal issues, or complaints.

Each escalation includes a reason, for example:

"No sufficiently similar historical resolution was found."

or:

"The customer message is too vague to safely resolve automatically."

The system intentionally favors safety over maximizing automation coverage.

7. Conversation Context

A key failure was found when evaluating follow-up messages in isolation.

For example:

"Done all that. Still telling me there..."

Without previous context, this message was classified as:

general_support

However, the previous message established that the customer was experiencing a website problem.

After adding conversation context, the same message was classified as:

website_issue
Decision

Recent conversation context is included during intent classification and retrieval.

Trade-off

More context improves understanding of follow-up messages, but excessive history can introduce irrelevant information and increase input size.

8. Evaluation

The current working sample contains 8 Tesco customer messages.

Therefore, these results are a pilot evaluation, not a statistically reliable estimate of production performance.

Results
Metric	Result
Intent accuracy	87.5%
Auto-handle rate	50%
Escalation rate	50%
LLM relevance	1.50 / 3
LLM groundedness	2.25 / 3
LLM helpfulness	1.75 / 3
LLM safety	3.00 / 3
LLM overall score	1.91 / 3
Human overall score	2.88 / 3
Human–LLM overall MAE	0.97
9. Baselines
Majority-class baseline

The majority-class classifier predicts the most common intent for every message.

Result:

Accuracy: 25%

The support agent therefore performs substantially better than this simple baseline on the pilot set.

Logistic Regression baseline

A TF-IDF + Logistic Regression classifier was also tested.

Because the dataset contains only 8 labelled examples, evaluating the model on the same examples used for training produced 100% accuracy, which is not a valid estimate of generalization.

A leave-one-out evaluation produced:

Accuracy: 12.5%

This demonstrates the instability caused by the extremely small dataset.

10. Failure Analysis

The main observed intent-classification failure was:

Tweet	Actual	Predicted	Root Cause
119321	website_issue	general_support	Follow-up message was ambiguous without conversation context
Fix

The classifier was modified to incorporate the previous conversation message.

With context, the same example was correctly classified as:

website_issue

The retrieval system also found a relevant historical website resolution, allowing the message to be auto-handled.

11. LLM-as-a-Judge

An LLM judge was used to evaluate generated support responses on four dimensions:

Relevance
Groundedness
Helpfulness
Safety

Each dimension is scored from 1–3.

The LLM judge produced an overall average of:

1.91 / 3

The human annotator's average was:

2.88 / 3

The difference indicates that the LLM judge was considerably stricter than the human annotator on this pilot.

Human–LLM agreement
Dimension	Cohen's κ
Relevance	0.00
Groundedness	0.00
Helpfulness	-0.08
Safety	N/A

Safety produced N/A because there was no score variation in the pilot data.

Because only 8 examples were evaluated, these agreement statistics are directional and should not be treated as robust estimates.

12. What Is Misleading About My Headline Number?

The headline intent accuracy of 87.5% can appear stronger than it actually is.

The result is based on only 8 Tesco customer messages.

With 8 examples:

1 incorrect prediction = 12.5 percentage points

Therefore, a single additional failure would reduce the reported accuracy from 87.5% to 75%.

The 87.5% figure should therefore be interpreted as a pilot result demonstrating the prototype, rather than evidence of production-level accuracy.

A stronger evaluation requires the intended 150–250 independently labelled messages, ideally with a held-out test set.

13. Key Design Decisions

Important design decisions are documented in decision_log.md.

Some key decisions include:

Selecting Tesco as the prototype brand.
Defining a custom support-intent taxonomy.
Using TF-IDF for lightweight historical retrieval.
Introducing a retrieval confidence threshold.
Escalating vague and sensitive requests.
Adding conversation context for follow-up messages.
Using an LLM judge as a supplementary evaluation method.
Measuring human–LLM agreement rather than treating the LLM judge as ground truth.
14. One-Week Improvement Plan

If given another week, I would:

Day 1

Expand the gold set to 150–250 independently labelled messages using the full dataset.

Day 2

Improve intent classification using more representative examples and semantic/LLM-based classification.

Day 3

Replace TF-IDF retrieval with semantic embeddings and tune the retrieval threshold.

Day 4

Improve response generation and grounding checks.

Day 5

Tune the escalation policy and measure the automation-vs-safety trade-off.

Day 6

Run a proper held-out evaluation, human review, and LLM-as-a-judge comparison.

Day 7

Clean up the implementation, documentation, reproducibility, and final evaluation report.

15. Project Structure
hiver-sde-assignment/
│
├── data/
│   ├── README.md
│   ├── sample.csv
│   └── tesco_conversations.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   ├── agent/
│   ├── data/
│   ├── evaluation/
│   ├── intents/
│   └── retrieval/
│
├── decision_log.md
├── requirements.txt
├── .env.example
└── README.md
16. Running the Project

Install dependencies:

pip install -r requirements.txt

The main experimentation and evaluation workflow is available in:

notebooks/01_data_exploration.ipynb

API keys should be stored securely as environment variables or notebook secrets and should never be committed to GitHub.

17. Limitations

The main limitation is dataset size.

The working sample contains only 93 tweets and produces 8 Tesco customer messages. This is insufficient for a statistically reliable 150–250 message evaluation.

Other limitations include:

Small number of labelled examples.
Rule-based intent classification.
TF-IDF rather than semantic retrieval.
Limited historical resolutions.
Small human evaluation sample.
LLM-judge disagreement with human ratings.

These limitations are intentionally documented rather than hidden.

18. Conclusion

This project demonstrates an end-to-end AI customer-support workflow:

Message
   ↓
Intent Classification
   ↓
Historical Retrieval
   ↓
Safety / Confidence Check
   ↓
Auto-handle or Escalate
   ↓
Grounded Response

The prototype also demonstrates how evaluation findings can drive system improvements, particularly the use of conversation context to resolve ambiguous follow-up messages.

The next major step is to run the same pipeline on the full dataset with a properly constructed 150–250 message gold set.

### Important

After replacing the README, **don't commit yet**.

First show me a screenshot of the edited README before you click **Commit changes**. I'll check it for anything that could hurt your Hiver submission.
