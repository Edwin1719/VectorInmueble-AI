from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

from agente_inmobiliario.tools.custom_tools import TavilySearchTool
from crewai_tools import SerperDevTool

@CrewBase
class AgenteInmobiliarioCrew():
	"""AgenteInmobiliario crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		self.openai_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

	@agent
	def property_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['property_scraper'],
			tools=[SerperDevTool(), TavilySearchTool()],
			llm=self.openai_llm,
			verbose=True
		)

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			tools=[SerperDevTool()],
			llm=self.openai_llm,
			verbose=True
		)

	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['financial_analyst'],
			tools=[SerperDevTool()],
			llm=self.openai_llm,
			verbose=True
		)

	@agent
	def report_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generator'],
			tools=[],
			llm=self.openai_llm,
			verbose=True
		)

	@task
	def property_scraping_task(self) -> Task:
		return Task(
			config=self.tasks_config['property_scraping_task'],
			agent=self.property_scraper()
		)

	@task
	def market_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_research_task'],
			agent=self.market_researcher()
		)

	@task
	def financial_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['financial_analysis_task'],
			agent=self.financial_analyst(),
			context=[self.property_scraping_task(), self.market_research_task()]
		)

	@task
	def report_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_generation_task'],
			agent=self.report_generator(),
			context=[
				self.property_scraping_task(),
				self.market_research_task(),
				self.financial_analysis_task()
			],
			output_file="reporte_inversion_pereira.md"
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AgenteInmobiliario crew"""
		return Crew(
			agents=self.agents, # Automatically created by CrewBase
			tasks=self.tasks, # Automatically created by CrewBase
			process=Process.sequential,
			verbose=True,
			# memory=True # For enhanced memory management
		)
