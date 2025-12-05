import os
from dotenv import load_dotenv
load_dotenv()

from agente_inmobiliario.crew import AgenteInmobiliarioCrew

def run():
    """
    Run the AgenteInmobiliario crew.
    """
    # Define the inputs for the crew. These are the variables that will be
    # interpolated into the tasks.
    inputs = {
        'precio_min': "200,000,000",
        'precio_max': "600,000,000",
        'area_min': "80",
        'area_max': "150",
        'sectores': "Cuba, Pinares, Ciudad Jardín, Álamos",
        'estratos': "3, 4, 5"
    }
    
    # Instantiate the crew and kick it off
    crew = AgenteInmobiliarioCrew()
    result = crew.crew().kickoff(inputs=inputs)
    
    print("\n\n########################")
    print("## Here is the result of your crew run:")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run()

