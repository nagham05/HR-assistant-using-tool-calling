import gradio as gr
from main import chat

def respond(message, history):
    """
    Gradio wrapper around your existing chat() function
    """
    if history is None:
        history = []
    
    reply = chat(message)
    
    # Append user message in the standard dictionary format
    history.append({"role": "user", "content": message})
    # Append assistant reply
    history.append({"role": "assistant", "content": reply})
    
    return history, ""

# Custom CSS ONLY for the page layout and sidebar
custom_css = """
/* Make the container fill the screen height */
.gradio-container {
    max-width: 100% !important;
    height: 100vh !important;
}

/* Sidebar stays custom but stretches */
#sidebar {
    /* A more muted, professional deep blue/gray instead of the bright purple */
    background: linear-gradient(135deg, #2c3e50 0%, #4ca1af 100%); 
    padding: 2rem;
    border-radius: 12px;
    color: white;
    height: 94vh !important;
}

/* Layout for the chat column to take full height */
#chat-column {
    padding-left: 2rem;
    height: 94vh !important;
    display: flex !important;
    flex-direction: column !important;
}

/* Force the chatbot component to grow to the bottom of the page */
#chatbot-container {
    flex-grow: 1 !important;
}

.example-btn {
    width: 100%;
    margin-bottom: 0.75rem;
    text-align: left;
    background: rgba(255, 255, 255, 0.15) !important;
    border: 2px solid rgba(255, 255, 255, 0.3) !important;
    color: white !important;
    padding: 0.75rem 1rem !important;
    border-radius: 8px !important;
    cursor: pointer !important;
}

.button-primary {
    background:  linear-gradient(135deg, #2c3e50 0%, #4ca1af 100%) !important;    
    color: white !important;
    border: none !important;
}
"""

with gr.Blocks(title="HR Assistant") as demo:
    
    with gr.Row():
        # Left Sidebar
        with gr.Column(scale=3, elem_id="sidebar"):
            gr.Markdown("# 🧑‍💼 HR Assistant")
            gr.Markdown("Your intelligent companion for all HR-related queries")
            
            gr.Markdown("### 💡 Try these examples:")
            
            ex1 = gr.Button("👤 Tell me about Omar Habli", elem_classes="example-btn")
            ex2 = gr.Button("🏖️ Check Nagham Habli leave balance", elem_classes="example-btn")
            ex3 = gr.Button("📋 Interview questions for Data Scientist", elem_classes="example-btn")
            ex4 = gr.Button("ℹ️ What does HR do?", elem_classes="example-btn")
        
        # Right Chat Area
        with gr.Column(scale=7, elem_id="chat-column"):
            # Using default Gradio Chatbot styling
            chatbot = gr.Chatbot(
                label="Conversation",
                elem_id="chatbot-container",
                height="80vh" # This ensures it takes up the majority of the page
            )
            
            # Input Row
            with gr.Row(elem_id="input-row"):
                with gr.Column(scale=9):
                    msg = gr.Textbox(
                        label="",
                        placeholder="💬 Type your question here...",
                        show_label=False,
                        elem_id="message-input"
                    )
                with gr.Column(scale=1, min_width=100):
                    send = gr.Button("Send ", elem_classes="button-primary")
            
            clear = gr.Button("🗑️ Clear Chat", size="sm")

    # Event handlers
    ex1.click(lambda: "Tell me about Omar Habli", None, msg)
    ex2.click(lambda: "Check Nagham Habli leave balance", None, msg)
    ex3.click(lambda: "Interview questions for Data Scientist", None, msg)
    ex4.click(lambda: "What does HR do?", None, msg)
    
    msg.submit(respond, inputs=[msg, chatbot], outputs=[chatbot, msg])
    send.click(respond, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear.click(lambda: [], None, chatbot)

# Launch with CSS for layout only
demo.launch(css=custom_css)