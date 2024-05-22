from datetime import datetime
from langchain_community.utilities import SQLDatabase
from langchain.agents import Tool 
from dateutil.parser import parse


def format_date(date):
    """
    format_date Function:
    - Function Purpose: Formats the date string to a standard format.
    - Parameters Explained:
      - date: The date string to be formatted.
    - Returns: The formatted date string.
    """
    try:
        return parse(date).strftime('%Y-%m-%d')
    except ValueError as e:
        return f"Error: {e}"

date_format_tool = Tool(
    name="DateFormatTool",
    func=format_date,
    description="Formats the date string to a standard format.",
)

formatted_date = date_format_tool.invoke("8/29/2006")
print(formatted_date)