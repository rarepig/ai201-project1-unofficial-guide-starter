from query import ask

import gradio as gr

def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""
    
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources

with gr.Blocks(title="WGU CS Course Guide") as demo:
    gr.Markdown("# 🎓 WGU CS Unofficial Course Guide")
    gr.Markdown("Ask questions about WGU Computer Science courses — difficulty, study tips, time estimates, and more.")
    
    inp = gr.Textbox(
        label="Your Question",
        placeholder="e.g. How long does C950 take? What are the hardest courses?",
        lines=2
    )
    btn = gr.Button("Ask", variant="primary")
    
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Sources", lines=3)
    
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch(server_port=None)