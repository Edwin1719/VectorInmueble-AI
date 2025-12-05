from typing import List, Optional
from crewai.tools import BaseTool
import os
import subprocess
# No longer importing Firecrawl

class CommandLineTool(BaseTool):
    name: str = "Command Line Tool"
    description: str = (
        "Executes a command in the shell. Crucial for starting necessary servers "
        "or running scripts. Input must be a valid shell command as a single string."
    )

    def _run(self, command: str) -> str:
        """Executes a shell command."""
        try:
            print(f"--- Executing Shell Command: {command} ---")
            
            # Using shell=True is a security risk if the command is from an untrusted source.
            # In this controlled environment, we are replicating known commands.
            # We add a timeout to prevent the process from hanging indefinitely,
            # especially for server commands that are meant to run in the background.
            # The output of server-startup commands might not be the most important part,
            # the fact that they are running is.
            result = subprocess.run(
                command,
                shell=True,
                text=True,
                capture_output=True,
                encoding='utf-8',
                timeout=120 # Add a timeout of 2 minutes
            )
            
            output = f"Command executed.\n"
            if result.stdout:
                output += f"Stdout:\n{result.stdout}\n"
            if result.stderr:
                output += f"Stderr:\n{result.stderr}\n"
            
            return output

        except subprocess.TimeoutExpired:
            return f"Command '{command}' timed out after 120 seconds. This is expected for server commands that run continuously. Assume the server is running and proceed."
        except FileNotFoundError:
            return f"Error: Command not found. Ensure the command and its dependencies (like Node.js/npx) are installed and in the system's PATH."
        except subprocess.CalledProcessError as e:
            return (
                f"Error executing command: `{command}`.\n"
                f"Return code: {e.returncode}\n"
                f"Stdout: {e.stdout}\n"
                f"Stderr: {e.stderr}"
            )
        except Exception as e:
            return f"An unexpected error occurred: {e}"


class FileWriterTool(BaseTool):
    name: str = "File Writer Tool"
    description: str = (
        "Writes given content to a specified file. Useful for saving reports, "
        "analysis, or other text outputs. The tool will create the file if it does not exist."
    )
    
    def _run(self, file_path: str, content: str) -> str:
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return f"Successfully wrote content to {file_path}"
        except Exception as e:
            return f"Error writing to file {file_path}: {e}"

class TavilySearchTool(BaseTool):
    name: str = "Tavily Web Search"
    description: str = (
        "Performs a web search using Tavily. Input should be a search query string. "
        "An optional list of URLs can be provided to search within. "
        "Returns relevant search results and a concise answer."
    )

    def _run(self, search_query: str, urls: Optional[List[str]] = None) -> str:
        """
        Performs a web search using Tavily.
        """
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Error: TAVILY_API_KEY no encontrada. Por favor, configúrala en tu archivo .env."

        try:
            from tavily import TavilyClient
            client = TavilyClient(api_key=api_key)

            if not search_query and not urls:
                return "Error: Se requiere 'search_query' o 'urls' para la búsqueda Tavily."

            response = client.search(
                query=search_query,
                search_depth="advanced",
                include_answer=True,
                urls=urls
            )

            # Format the results
            formatted_results = ""
            if response.get("answer"):
                formatted_results += f"Answer: {response['answer']}\n\n"
            
            if response.get("results"):
                formatted_results += "Relevant Results:\n"
                for i, result in enumerate(response["results"]):
                    formatted_results += f"{i+1}. Title: {result['title']}\n"
                    formatted_results += f"   URL: {result['url']}\n"
                    formatted_results += f"   Snippet: {result['content']}\n\n"
            
            if not formatted_results:
                return "No se encontraron resultados para la consulta."

            return formatted_results

        except Exception as e:
            return f"Ocurrió un error al realizar la búsqueda con Tavily: {e}"
