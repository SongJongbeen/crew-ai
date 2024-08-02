from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import GlobalNewsResearchTool, LocalNewsResearchTool

# Uncomment the following line to use an example of a custom tool
# from news_reporter.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class NewsReporterCrew():
	"""NewsReporter crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def global_news_reporter(self) -> Agent:
		return Agent(
			config=self.agents_config['global_news_reporter'],
			tools=[GlobalNewsResearchTool()],
			verbose=True
		)

	@agent
	def local_news_reporter(self) -> Agent:
		return Agent(
			config=self.agents_config['local_news_reporter'],
			tools=[LocalNewsResearchTool()],
			verbose=True
		)
	
	@agent
	def editor(self) -> Agent:
		return Agent(
			config=self.agents_config['editor'],
			verbose=True
		)

	@task
	def global_news_research(self) -> Task:
		return Task(
			config=self.tasks_config['global_news_research'],
			agent=self.global_news_reporter(),
			output_file='global_report.md'
		)
	
	@task
	def local_news_research(self) -> Task:
		return Task(
			config=self.tasks_config['local_news_research'],
			agent=self.local_news_reporter(),
			output_file='korean_report.md'
		)
	
	@task
	def publish_news(self) -> Task:
		return Task(
			config=self.tasks_config['publish_news'],
			agent=self.editor(),
			output_file='final_report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the NewsReporter crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
