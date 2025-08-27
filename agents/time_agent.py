"""Time Agent: Gets current time and date information."""
from agent_plugin import AgentPlugin
from rich.prompt import Prompt
from datetime import datetime, timezone
import time

class TimeAgent(AgentPlugin):
    def __init__(self, model, **kwargs):
        super().__init__(model, **kwargs)

    def run_agent_flow(self, context, **kwargs):
        """Run the time agent - provides current time information."""
        self.console.print("[bold green]Time Agent activated![/bold green]")
        
        # Get current time in various formats
        now = datetime.now()
        utc_now = datetime.now(timezone.utc)
        
        self.console.print(f"[cyan]Current Local Time: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}[/cyan]")
        self.console.print(f"[cyan]Current UTC Time: {utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')}[/cyan]")
        self.console.print(f"[cyan]Unix Timestamp: {int(time.time())}[/cyan]")
        self.console.print(f"[cyan]Day of Week: {now.strftime('%A')}[/cyan]")
        self.console.print(f"[cyan]Week Number: {now.isocalendar()[1]}[/cyan]")
        
        # Ask if user wants specific timezone
        want_timezone = Prompt.ask("[bold green]Do you want time for a specific timezone?[/bold green]", choices=["yes", "no"], default="no")
        
        if want_timezone == "yes":
            timezone_name = Prompt.ask("[bold green]Enter timezone (e.g., US/Eastern, Europe/London, Asia/Tokyo)[/bold green]")
            try:
                import zoneinfo
                tz = zoneinfo.ZoneInfo(timezone_name)
                tz_time = datetime.now(tz)
                self.console.print(f"[cyan]Time in {timezone_name}: {tz_time.strftime('%Y-%m-%d %H:%M:%S %Z')}[/cyan]")
            except Exception as e:
                self.console.print(f"[red]Error getting timezone {timezone_name}: {e}[/red]")
                self.console.print("[yellow]Common timezones: US/Eastern, US/Pacific, Europe/London, Europe/Paris, Asia/Tokyo, Asia/Shanghai[/yellow]")
        
        self.console.print("[dim]Time agent completed.[/dim]")
