import httpx
from fastmcp import FastMCP
import requests

mcp = FastMCP(name = "A simple MCP sever")

#@mcp.tool()
#def task_generator(task_description: str):
#   """
 #   Generate a task based on the provided description.
  #  """
   
    #result = create_task(task_description)
    #return result

#@mcp.tool()
#def add_employee_to_project(employee_id: str, project_id: str):
#    """
#    Add an employee to a project.
#    """
    
#    result = add_employee(employee_id, project_id)
#    return result

@mcp.tool()
def get_project(project_description: str):
    """
    Get projects from the application backend based on the provided description.
    """
    response = requests.get("https://roster-employee-app-nu.vercel.app/generate_project/employees", params={"description": project_description})
    result = response.json()
    return result

app = mcp.http_app(stateless_http=True)