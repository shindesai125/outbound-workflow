![LangGraph Prototype](https://img.shields.io/badge/Workflow-LangGraph-blue)

#  Outbound Lead Generation Workflow (LangGraph Prototype)

##  Overview
This project is a modular, JSON‑driven workflow for **outbound lead generation**.  
It demonstrates how multiple agents can be orchestrated step‑by‑step to simulate a real sales pipeline — from prospecting to outreach to feedback analysis.

The workflow is designed for **clarity, modularity, and upgrade‑readiness**: each agent is isolated, easy to extend, and can be swapped with real APIs when needed.

---

##  Workflow Steps
The pipeline is defined in `workflow.json` and executed by `langgraph_builder.py`.

1. **ProspectSearchAgent** → Returns mock leads (company, contact, email).  
2. **DataEnrichmentAgent** → Adds role, technologies, LinkedIn URL (mock enrichment).  
3. **ScoringAgent** → Assigns lead scores based on simple rules.  
4. **OutreachContentAgent** → Uses **OpenAI API** to generate personalized cold emails.  
5. **OutreachExecutorAgent** → Logs emails to `outbox.log` (mock send).  
6. **ResponseTrackerAgent** → Simulates opens/replies for demo purposes.  
7. **FeedbackTrainerAgent** → Analyzes responses and appends recommendations into a **Google Sheet** (real Sheets API integration).

---

##  What’s Implemented
- JSON‑driven workflow execution.  
- Modular agents with clear input/output contracts.  
- **Real OpenAI integration** for outreach content.  
- **Real Google Sheets integration** for feedback logging.  
- Mock prospecting, enrichment, and sending (upgrade‑ready).  
- ReAct‑style logging (`[Thought]`, `[Action]`, `[Observation]`).  
- Basic error handling and logging.

---

##  What’s Mocked / Not Implemented
- **Prospecting APIs (Apollo/Clay)** → Mocked with static leads.  
- **Data Enrichment (Clearbit/PDL)** → Mocked with dummy role/tech info.  
- **Outreach Execution (SendGrid)** → Mocked by logging emails to file.  
- **Response Tracking (Apollo/CRM)** → Simulated with random open/reply flags.  

---

## 🛠 Setup
1. Clone repo and install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create your local secrets file (do NOT commit this repo file):

    - Copy the example and fill in your real keys locally:

       ```powershell
       # from repo root
       copy .\.env.example .\.env
       # then open .env and replace placeholders with your real keys
       notepad .\.env
       ```

    - Example `.env.example` (committed in repo):

       ```ini
       # Copy this file to .env and fill with your real values (do NOT commit .env)
       OPENAI_API_KEY=ADD_YOUR_KEY_HERE
       GOOGLE_SHEETS_ID=ADD_YOUR_SHEET_ID_HERE
       GOOGLE_SA_JSON=service_accounts.json
       ```

    - This repo intentionally ignores `.env` and `service_accounts.json` so your secrets stay local.

3. Create a Google Sheet, share it with your service account email, and copy its ID.

4. Run the workflow:

    ```bash
    python langgraph_builder.py
    ```

Example Output
- OutreachContentAgent generates cold emails like:
   Subject: Quick idea for Acme Inc
   Hi Jane, I’m reaching out to introduce our SaaS solution...

- FeedbackTrainerAgent logs recommendations into Google Sheets:
   Open rate: 50%
   Reply rate: 25%
   Recommendation: Try shorter subject lines and add personalization.

Security notes
- Never commit `.env` or `service_accounts.json` containing real credentials. If you accidentally pushed keys to a remote, rotate/revoke them immediately.
- If you need help purging secrets from git history while preserving commits, I can help with a safe rewrite (git-filter-repo / BFG) — this is more advanced.



Future Improvements
- Replace mocks with real APIs (Apollo, Clearbit, SendGrid).
- Add robust error handling and retries.
- Implement approval loop for feedback before retraining.
- Enhance personalization with company‑specific hooks.

 Key Takeaway
This prototype shows how to design modular, upgrade‑ready AI workflows.
It balances real integrations (OpenAI + Google Sheets) with mocked components, making it both demo‑friendly and extensible.

---



