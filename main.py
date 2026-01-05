import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

# Initialize Groq LLM
def initialize_llm():
    return ChatGroq(
        groq_api_key="YOUR_API_KEY",
        model_name="llama3-8b-8192"
    )

# Create Streamlit app
def create_app():
    st.title("Story Writing AI Chatbot")
    return initialize_llm()

# Prompt template for story generation
def create_prompt_template():
    return PromptTemplate(
        input_variables=["topic"],
        template="Write a short story about {topic}."
    )

# Get user input
def get_user_input(llm):
    col1, col2 = st.columns(2)
    topic = col1.text_input("Enter a topic for your story:")
    genres = ["nORMAL", "Romance", "Fantasy"]
    selected_genre = col2.selectbox("Choose a genre:", genres)
    story_length = st.slider("Select story length (words):", 100, 8192, 500)
    return topic, selected_genre, story_length

# Generate and display story
def generate_story(llm, prompt_template, topic, selected_genre, story_length):
    if st.button("Generate Story"):
        if topic.strip():
            try:
                prompt = prompt_template.format(topic=f"{topic} ({selected_genre})")
                response = llm.invoke(prompt, max_tokens=story_length)
                st.write(response.content)
            except Exception as e:
                st.error(f"Error generating story: {e}")
        else:
            st.warning("Please enter a topic before generating a story.")

# Saved Stories
def save_story(topic, story):
    saved_stories = []
    a=str(saved_stories.append((topic, story)))
    st.success("Story saved!")
    with open("savetitle.txt","w") as file:
      file.write(savetitle)

# Feedback
def submit_feedback(feedback):
   st.success("Thanks for your feedback")
   with open("feedback.txt","w") as file:
    file.write(feedback)

def main():
    llm = create_app()
    prompt_template = create_prompt_template()
    topic, selected_genre, story_length = get_user_input(llm)
    generate_story(llm, prompt_template, topic, selected_genre, story_length)

    # Saved Stories
    st.markdown("---")
    st.subheader("Saved Stories")
    if st.button("Save Story"):
        save_story(topic, "Generated Story")

    # Feedback
    st.markdown("---")
    st.subheader("Feedback")
    feedback = st.text_input("Provide feedback on the generated story:")
    if st.button("Submit Feedback"):
        submit_feedback(feedback)

if __name__ == "__main__":
    main()

