import streamlit as st
import sys
from pathlib import Path

# Allow imports from src/
ROOT = Path(__file__).parent
sys.path.append(str(ROOT))

from src.agent.generate import tesco_support_agent_context

st.set_page_config(
    page_title="Tesco AI Support Agent",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Tesco AI Customer Support Agent")
st.write(
    "Classifies customer messages, retrieves historical resolutions, "
    "drafts a reply, and decides whether to auto-handle or escalate."
)

st.divider()

message = st.text_area(
    "Customer message",
    placeholder="Example: Your website is not working properly...",
    height=120
)

previous_context = st.text_area(
    "Previous conversation context (optional)",
    placeholder="Paste the previous customer/support message here...",
    height=100
)

if st.button("🤖 Analyze Message", type="primary"):
    if not message.strip():
        st.warning("Please enter a customer message.")
    else:
        result = tesco_support_agent_context(
            message,
            previous_context
        )

        st.subheader("Agent Decision")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Intent", result["intent"])

        with col2:
            st.metric("Decision", result["decision"])

        st.write("**Reason:**", result["reason"])
        st.write(
            "**Historical Resolution Similarity:** "
            f"{result['similarity']:.3f}"
        )

        st.subheader("💬 Draft Reply")

        st.info(result["draft_reply"])
