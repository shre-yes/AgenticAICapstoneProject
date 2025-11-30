from google.adk.agents import LlmAgent,Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search
from google.adk.models.google_llm import Gemini
from google.genai import types

from . import prompt

LLModel = "gemini-2.5-pro"

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

trading_analyst_agent = Agent(
    model=Gemini(model=LLModel, retry_options=retry_config),
    name="trading_analyst_agent",
    instruction=prompt.TA_PROMPT,
    output_key="trade_strategies_output",
)

risk_analysis_agent = Agent(
    model=Gemini(model=LLModel, retry_options=retry_config),
    name="risk_analysis_agent",
    instruction=prompt.RA_PROMPT,
    output_key="final_risk_assessment_output",
)

behavioural_analysis_agent = Agent(
    model=Gemini(model=LLModel, retry_options=retry_config),
    name="behavioural_analysis_agent",
    instruction=prompt.BA_PROMPT,
    output_key="behavioural_analysis_output",
)

execution_planning_agent = Agent(
    model=Gemini(model=LLModel, retry_options=retry_config),
    name="execution_planning_agent",
    instruction=prompt.EA_PROMPT,
    output_key="execution_plan_output",
)

data_analysis_agent = Agent(
    model=Gemini(model=LLModel, retry_options=retry_config),
    name="data_analysis_agent",
    instruction=prompt.DA_PROMPT,
    output_key="market_analysis_output",
    tools=[google_search],
)

advice_orchastrator = LlmAgent(
    name="advice_orchastrator",
    model=Gemini(model=LLModel, retry_options=retry_config),
    description=(
        "guide users through a structured process to receive financial "
        "advice by orchestrating a series of expert subagents. help them "
        "analyze a market ticker, develop trading strategies, define "
        "execution plans, and evaluate the overall risk."
        "Identify the most dominant market emotion (Fear or Greed) and detail the single biggest cognitive bias risk this specific user is currently facing based on their risk profile."
        "Synthesize the findings from all subagents into a final, actionable recommendation that explicitly addresses any misalignment between the proposed plan's risk profile and the user's stated risk attitude, ensuring compliance with suitability standards but only once approved by the user."
    ),
    instruction=prompt.FO_PROMPT,
    output_key="advice_orchastrator_output",
    tools=[
        AgentTool(agent=data_analysis_agent),
        AgentTool(agent=trading_analyst_agent),
        AgentTool(agent=execution_planning_agent),
        AgentTool(agent=behavioural_analysis_agent),
        AgentTool(agent=risk_analysis_agent),
    ],
)

root_agent = advice_orchastrator
