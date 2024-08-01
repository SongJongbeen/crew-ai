from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from tools.custom_tool import StockNewsTool, StockPriceTool, IncomeStmtTool, BalanceSheetTool, InsiderTransactionsTool

# Uncomment the following line to use an example of a custom tool
# from business_analyzer.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class BusinessAnalyzerCrew():
	"""BusinessAnalyzer crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# @llm
	# def chatgpt_llm(self):
	# return ChatGroq(temperature=0, model_name="gpt-4o")

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools = [ScrapeWebsiteTool(), StockNewsTool()],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def technical_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_analyst'],
			tools = [StockPriceTool()],
			verbose=True
		)

	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['financial_analyst'],
			tools = [IncomeStmtTool(), BalanceSheetTool(), InsiderTransactionsTool()],
			verbose=True
		)

	@agent
	def hedge_fund_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['hedge_fund_manager'],
			verbose=True
		)

	@task
	def research(self) -> Task:
		return Task(
			config=self.tasks_config['research'],
			agent=self.researcher()
		)
	
	@task
	def technical_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['technical_analysis'],
			agent=self.technical_analyst()
		)

	@task
	def financial_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['financial_analysis'],
			agent=self.financial_analyst()
		)
	
	@task
	def investment_recommendation(self) -> Task:
		return Task(
			config=self.tasks_config['investment_recommendation'],
			agent=self.hedge_fund_manager(),
			context=[self.research(), self.technical_analysis(), self.financial_analysis()],
			output_file='investment_recommendation.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BusinessAnalyzer crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)