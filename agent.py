# agent.py
from llama import call_llama
from pathlib import Path

# Load input text
job_post = Path("job_post.txt").read_text(encoding="utf-8")
summarize_prompt = Path("prompts/summarize_prompt.txt").read_text(encoding="utf-8").format(job_post=job_post)

# Call LLaMA to summarize
print("📄 Generating summary...")
summary = call_llama(summarize_prompt)
Path("example_output/summary.txt").write_text(summary, encoding="utf-8")

# Call LLaMA to write VP email
vp_prompt = Path("prompts/vp_intro_prompt.txt").read_text(encoding="utf-8").format(summary=summary)
print("✉️  Generating VP-style intro email...")
intro_email = call_llama(vp_prompt)
Path("example_output/intro_email.txt").write_text(intro_email, encoding="utf-8")

print("✅ Done! Check example_output/")
