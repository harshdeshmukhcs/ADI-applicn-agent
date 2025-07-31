# Analog Devices GenAI Challenge Submission

This project is a GenAI agent designed to summarize the job descriptions and generate onboarding emails in the tone and structure of a real Analog Devices executive — specifically, Giuseppe Olivadoti, VP of Digital Healthcare.

It was built as a submission for the **Vibe Coder-in-Residence (GenAI Tech EA)** role at Analog Devices.

## ✨ What It Does

- 📄 **Summarizes complex job descriptions** into bullet-point insights tailored for executive readers
- ✉️ **Writes onboarding-style announcement emails** in the voice of VP Giuseppe Olivadoti
- 🧠 Reflects Giuseppe’s communication style using language drawn from real ADI materials

## 🧠 Voice & Tone Modeling

To mimic Giuseppe Olivadoti’s real tone, phrasing, and communication patterns, this project uses prompt engineering based on:

- His **official title** and responsibilities at ADI
- A **transcript of his public speaking** during ADI's Healthcare Tech Day 2023  
  🎥 [Source video](https://ez.analog.com/jp/webinar/c/e/525)  
- Signature phrasing integrated into prompts:
  - “accelerate time to impact”
  - “platforms that reduce complexity”
  - “care that is today reactive and will tomorrow be proactive”
  - “solutions that climb the technology stack”

## ⚙️ How It Works

- `agent.py` loads the job post from `job_post.txt`
- It injects this into custom prompt templates in `prompts/`
- Uses the Together API with **LLaMA 3.1** (`meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`) to:
  - Generate a job summary
  - Generate a VP-style intro email
- Outputs are saved to `example_output/summary.txt` and `intro_email.txt`

## 📂 Folder Structure

analog-devices-agent/
├── agent.py  # Main runner script
├── llama.py  # Together API call logic
├── job_post.txt  # The original Analog Devices job post
├── prompts/
│ ├── summarize_prompt.txt 
│ └── vp_intro_prompt.txt 
├── example_output/
│ ├── summary.txt  # Output for the summarized jog descrip.
│ └── intro_email.txt  # Output of VP intro mail
├── .env 
├── requirements.txt
└── README.md

## ▶️ How to Run

1. Add your Together API key to `.env`:
   ```bash
   TOGETHER_API_KEY=your-key-here

2. Install dependencies:

    pip install -r requirements.txt

3. Run the agent:

    python agent.py


  The generated output will be saved in example_output/.

  ## 🌐 Frontend UI + Hosting

     - This agent is integrated into a full-stack frontend, deployed here:

    ## 🔗 Live Demo: https://edge-ai-agent.vercel.app/

    - Frontend: Built with React + TailwindCSS + ShadCN UI, deployed on Vercel

    - Backend API: The GenAI agent (agent.py) is deployed separately on Railway

    - Uses a clean UI to paste job descriptions and display the generated content live

    - The UI mimics a real Analog Devices internal tool for executive support.


    ## Thank You!
